from __future__ import annotations

import copy
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import tempfile
import threading
import time
from typing import Any

import yaml

from .config import ControlPlaneSettings


GIT_COMMAND_TIMEOUT_SECONDS = 10
ORCHESTRATION_SUMMARY_TTL_SECONDS = 3.0

_state_lock = threading.RLock()
_action_registry_lock = threading.Lock()
_workspace_action_locks: dict[str, threading.Lock] = {}
_active_workspace_actions: dict[str, str] = {}
_summary_cache_lock = threading.Lock()
_summary_cache: dict[tuple[str, str, str], tuple[float, dict[str, Any]]] = {}


class ActionAlreadyRunningError(RuntimeError):
    def __init__(self, *, requested_action: str, running_action: str) -> None:
        self.requested_action = requested_action
        self.running_action = running_action
        super().__init__(
            f"cannot start {requested_action}: orchestration action {running_action} is already running"
        )


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    raw = path.read_text(encoding="utf-8")
    payload = yaml.safe_load(raw)
    if not isinstance(payload, dict):
        return {}
    return payload


def _git_output(path: Path, *args: str) -> str:
    command = ["git", "-C", str(path), *args]
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=GIT_COMMAND_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"git command timed out after {GIT_COMMAND_TIMEOUT_SECONDS}s: {' '.join(args)}") from exc
    if completed.returncode != 0:
        raise RuntimeError((completed.stderr or completed.stdout or "git command failed").strip())
    return (completed.stdout or "").strip()


def repo_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"present": False, "path": str(path), "git": False}
    if not (path / ".git").exists():
        return {"present": True, "path": str(path), "git": False}

    try:
        branch = _git_output(path, "rev-parse", "--abbrev-ref", "HEAD")
        commit = _git_output(path, "rev-parse", "HEAD")
        committed_at = _git_output(path, "show", "-s", "--format=%cI", "HEAD")
        dirty = bool(_git_output(path, "status", "--porcelain"))
        return {
            "present": True,
            "path": str(path),
            "git": True,
            "branch": branch,
            "commit": commit,
            "committed_at": committed_at,
            "dirty": dirty,
        }
    except Exception as exc:
        return {
            "present": True,
            "path": str(path),
            "git": True,
            "error": str(exc),
        }


def _empty_action_state() -> dict[str, Any]:
    return {"bootstrap": None, "smoke": None, "update": None}


def _load_action_state_unlocked(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return _empty_action_state()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return _empty_action_state()
    if not isinstance(payload, dict):
        return _empty_action_state()
    return {
        "bootstrap": payload.get("bootstrap"),
        "smoke": payload.get("smoke"),
        "update": payload.get("update"),
    }


def _load_action_state(path: Path) -> dict[str, Any]:
    with _state_lock:
        return _load_action_state_unlocked(path)


def _save_action_state_unlocked(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as temporary:
            temporary.write(json.dumps(state, indent=2))
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def _record_action_result(path: Path, *, action_name: str, result: dict[str, Any]) -> None:
    with _state_lock:
        state = _load_action_state_unlocked(path)
        state[action_name] = result
        _save_action_state_unlocked(path, state)


def clear_orchestration_summary_cache() -> None:
    with _summary_cache_lock:
        _summary_cache.clear()


def _trim_output(stdout: str, stderr: str, *, limit_chars: int = 12000) -> str:
    combined = "\n".join(part for part in (stdout.strip(), stderr.strip()) if part)
    if len(combined) <= limit_chars:
        return combined
    return f"... (truncated; showing last {limit_chars} characters)\n{combined[-limit_chars:]}"


def run_action(
    *,
    action_name: str,
    script_path: Path,
    base_dir: Path,
    timeout_seconds: int,
    state_path: Path,
) -> dict[str, Any]:
    workspace_key = str(base_dir.resolve())
    with _action_registry_lock:
        action_lock = _workspace_action_locks.setdefault(workspace_key, threading.Lock())
        if not action_lock.acquire(blocking=False):
            raise ActionAlreadyRunningError(
                requested_action=action_name,
                running_action=_active_workspace_actions.get(workspace_key, "unknown"),
            )
        _active_workspace_actions[workspace_key] = action_name

    started_at = _now_iso()
    command = ["bash", str(script_path), str(base_dir)]
    try:
        if not script_path.is_file():
            result = {
                "action": action_name,
                "ok": False,
                "started_at": started_at,
                "finished_at": _now_iso(),
                "exit_code": 127,
                "command": command,
                "output": f"missing script: {script_path}",
            }
        else:
            try:
                completed = subprocess.run(
                    command,
                    cwd=str(script_path.parent.parent),
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds,
                    check=False,
                )
                result = {
                    "action": action_name,
                    "ok": completed.returncode == 0,
                    "started_at": started_at,
                    "finished_at": _now_iso(),
                    "exit_code": completed.returncode,
                    "command": command,
                    "output": _trim_output(completed.stdout, completed.stderr),
                }
            except subprocess.TimeoutExpired as exc:
                result = {
                    "action": action_name,
                    "ok": False,
                    "started_at": started_at,
                    "finished_at": _now_iso(),
                    "exit_code": 124,
                    "command": command,
                    "output": f"action timed out after {timeout_seconds}s: {exc}",
                }

        _record_action_result(state_path, action_name=action_name, result=result)
        clear_orchestration_summary_cache()
        return result
    finally:
        with _action_registry_lock:
            _active_workspace_actions.pop(workspace_key, None)
            action_lock.release()


def build_projects_summary(settings: ControlPlaneSettings) -> list[dict[str, Any]]:
    projects_payload = _load_yaml(settings.projects_config_path)
    raw_projects = projects_payload.get("projects")
    if not isinstance(raw_projects, list):
        return []

    output: list[dict[str, Any]] = []
    for entry in raw_projects:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or "").strip()
        if not name:
            continue

        local_path_raw = entry.get("local_path")
        if isinstance(local_path_raw, str) and local_path_raw.strip():
            local_path = Path(local_path_raw).expanduser()
        else:
            local_path = settings.workspace_root / name

        output.append(
            {
                "name": name,
                "role": str(entry.get("role") or ""),
                "repo": str(entry.get("repo") or ""),
                "verification_key": str(entry.get("verification_key") or ""),
                "dashboard": entry.get("dashboard") if isinstance(entry.get("dashboard"), dict) else {},
                "capabilities": entry.get("capabilities") if isinstance(entry.get("capabilities"), dict) else {},
                "local_path": str(local_path),
                "status": repo_status(local_path),
            }
        )

    return output


def build_orchestration_summary(settings: ControlPlaneSettings) -> dict[str, Any]:
    cache_key = (
        str(settings.workspace_root),
        str(settings.projects_config_path),
        str(settings.orchestration_state_path),
    )
    now = time.monotonic()
    with _summary_cache_lock:
        cached = _summary_cache.get(cache_key)
        if cached is not None and cached[0] > now:
            return copy.deepcopy(cached[1])

    projects = build_projects_summary(settings)
    dirty_repos = [project["name"] for project in projects if bool(project.get("status", {}).get("dirty"))]
    missing_repos = [project["name"] for project in projects if not bool(project.get("status", {}).get("present"))]
    action_state = _load_action_state(settings.orchestration_state_path)

    summary = {
        "generated_at": _now_iso(),
        "projects": projects,
        "project_count": len(projects),
        "dirty_repo_count": len(dirty_repos),
        "dirty_repos": dirty_repos,
        "missing_repo_count": len(missing_repos),
        "missing_repos": missing_repos,
        "last_actions": action_state,
        "commands": {
            "bootstrap": ["bash", str(settings.bootstrap_script_path), str(settings.workspace_root)],
            "smoke": ["bash", str(settings.smoke_script_path), str(settings.workspace_root)],
            "update": ["bash", str(settings.update_script_path), str(settings.workspace_root)],
        },
    }
    with _summary_cache_lock:
        _summary_cache[cache_key] = (now + ORCHESTRATION_SUMMARY_TTL_SECONDS, copy.deepcopy(summary))
    return summary
