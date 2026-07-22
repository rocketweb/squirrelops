from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
from threading import Event
from typing import Any

import pytest

from controlplane_api import orchestration


def test_action_guard_blocks_overlapping_workspace_actions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    script_path = tmp_path / "scripts" / "smoke.sh"
    script_path.parent.mkdir()
    script_path.write_text("#!/usr/bin/env bash\n", encoding="utf-8")
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    state_path = tmp_path / "state.json"
    started = Event()
    release = Event()

    def fake_run(*_args: Any, **_kwargs: Any) -> subprocess.CompletedProcess[str]:
        started.set()
        assert release.wait(timeout=2)
        return subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")

    monkeypatch.setattr(orchestration.subprocess, "run", fake_run)
    kwargs = {
        "action_name": "smoke",
        "script_path": script_path,
        "base_dir": workspace,
        "timeout_seconds": 2,
        "state_path": state_path,
    }

    with ThreadPoolExecutor(max_workers=2) as executor:
        first = executor.submit(orchestration.run_action, **kwargs)
        assert started.wait(timeout=1)
        with pytest.raises(orchestration.ActionAlreadyRunningError) as exc:
            orchestration.run_action(**(kwargs | {"action_name": "update"}))
        assert exc.value.running_action == "smoke"
        release.set()
        assert first.result(timeout=2)["ok"] is True

    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["smoke"]["output"] == "ok"


def test_git_commands_have_a_timeout(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, Any] = {}

    def fake_run(*_args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        captured.update(kwargs)
        return subprocess.CompletedProcess(args=[], returncode=0, stdout="main\n", stderr="")

    monkeypatch.setattr(orchestration.subprocess, "run", fake_run)
    assert orchestration._git_output(tmp_path, "status") == "main"
    assert captured["timeout"] == orchestration.GIT_COMMAND_TIMEOUT_SECONDS


def test_summary_cache_is_short_lived_and_returns_defensive_copies(
    settings_factory: Any,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = 0

    def fake_projects(_settings: Any) -> list[dict[str, Any]]:
        nonlocal calls
        calls += 1
        return [{"name": "pingting", "status": {"present": True, "dirty": False}}]

    monkeypatch.setattr(orchestration, "build_projects_summary", fake_projects)
    orchestration.clear_orchestration_summary_cache()
    settings = settings_factory()
    first = orchestration.build_orchestration_summary(settings)
    first["projects"].clear()
    second = orchestration.build_orchestration_summary(settings)

    assert calls == 1
    assert second["projects"][0]["name"] == "pingting"


def test_trim_output_preserves_the_error_tail() -> None:
    output = orchestration._trim_output("start-" + ("x" * 20) + "-failure", "", limit_chars=12)
    assert output.endswith("xxxx-failure")
    assert output.startswith("... (truncated")
