from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


def _env_raw(name: str) -> str | None:
    """Read an env var, preferring the canonical name.

    The control-plane variables were historically misspelled "CONTROLPANE_"
    (missing the second "L"). The correct "CONTROLPLANE_" spelling is now
    canonical; the misspelled name is still honored as a deprecated alias so
    "fixing the typo" can never silently change behavior (for example, leaving
    authentication unconfigured).
    """
    value = os.getenv(name)
    if value is not None:
        return value
    if name.startswith("CONTROLPLANE_"):
        legacy = "CONTROLPANE_" + name[len("CONTROLPLANE_"):]
        legacy_value = os.getenv(legacy)
        if legacy_value is not None:
            return legacy_value
    return None


def _env_str(name: str, default: str) -> str:
    value = _env_raw(name)
    return value if value is not None else default


def _parse_int_env(name: str, default: int) -> int:
    raw = _env_raw(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _parse_bool_env(name: str, default: bool = False) -> bool:
    raw = _env_raw(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _parse_origins(raw: str) -> list[str]:
    items = [item.strip() for item in raw.split(",")]
    return [item for item in items if item]


@dataclass(frozen=True)
class ControlPlaneSettings:
    repo_root: Path
    workspace_root: Path
    projects_config_path: Path
    clownpeanuts_api_base: str
    clownpeanuts_api_token: str
    clownpeanuts_ws_events_url: str
    clownpeanuts_ws_theater_url: str
    clownpeanuts_ws_token: str
    pingting_repo_path: Path
    pingting_status_path: Path
    pingting_config_path: Path
    pingting_python_bin: str | None
    pingting_status_max_age_seconds: int
    pingting_command_timeout_seconds: int
    orchestration_state_path: Path
    orchestration_action_timeout_seconds: int
    bootstrap_script_path: Path
    smoke_script_path: Path
    update_script_path: Path
    cors_allow_origins: list[str]
    api_auth_token: str
    api_auth_disabled: bool


def load_settings() -> ControlPlaneSettings:
    repo_root = Path(__file__).resolve().parents[3]
    workspace_root = Path(os.getenv("CONTROLPLANE_WORKSPACE_ROOT", "/Users/matt/code")).expanduser()
    pingting_repo = Path(os.getenv("PINGTING_REPO_PATH", str(workspace_root / "pingting"))).expanduser()

    return ControlPlaneSettings(
        repo_root=repo_root,
        workspace_root=workspace_root,
        projects_config_path=Path(
            os.getenv("CONTROLPLANE_PROJECTS_CONFIG", str(repo_root / "config" / "projects.yaml"))
        ).expanduser(),
        clownpeanuts_api_base=os.getenv("CLOWNPEANUTS_API_BASE", "http://127.0.0.1:8099").strip(),
        clownpeanuts_api_token=os.getenv("CLOWNPEANUTS_API_TOKEN", "").strip(),
        clownpeanuts_ws_events_url=os.getenv(
            "CLOWNPEANUTS_WS_EVENTS_URL",
            "ws://127.0.0.1:8099/ws/events",
        ).strip(),
        clownpeanuts_ws_theater_url=os.getenv(
            "CLOWNPEANUTS_WS_THEATER_URL",
            "ws://127.0.0.1:8099/ws/theater/live",
        ).strip(),
        clownpeanuts_ws_token=(
            os.getenv("CLOWNPEANUTS_WS_TOKEN", "").strip()
            or os.getenv("CLOWNPEANUTS_API_TOKEN", "").strip()
        ),
        pingting_repo_path=pingting_repo,
        pingting_status_path=Path(
            os.getenv("PINGTING_STATUS_PATH", str(pingting_repo / "data" / "status.json"))
        ).expanduser(),
        pingting_config_path=Path(
            os.getenv("PINGTING_CONFIG_PATH", str(pingting_repo / "config" / "pingting.yaml"))
        ).expanduser(),
        pingting_python_bin=(os.getenv("PINGTING_PYTHON_BIN") or "").strip() or None,
        pingting_status_max_age_seconds=_parse_int_env("PINGTING_STATUS_MAX_AGE_SECONDS", 120),
        pingting_command_timeout_seconds=_parse_int_env("PINGTING_STATUS_TIMEOUT_SECONDS", 20),
        orchestration_state_path=Path(
            _env_str(
                "CONTROLPLANE_ACTION_STATE_PATH",
                str(repo_root / "data" / "controlplane" / "actions-state.json"),
            )
        ).expanduser(),
        orchestration_action_timeout_seconds=_parse_int_env("CONTROLPLANE_ACTION_TIMEOUT_SECONDS", 900),
        bootstrap_script_path=Path(
            _env_str("CONTROLPLANE_BOOTSTRAP_SCRIPT_PATH", str(repo_root / "scripts" / "bootstrap_repos.sh"))
        ).expanduser(),
        smoke_script_path=Path(
            _env_str("CONTROLPLANE_SMOKE_SCRIPT_PATH", str(repo_root / "harness" / "smoke.sh"))
        ).expanduser(),
        update_script_path=Path(
            _env_str("CONTROLPLANE_UPDATE_SCRIPT_PATH", str(repo_root / "scripts" / "update_repos.sh"))
        ).expanduser(),
        cors_allow_origins=_parse_origins(
            _env_str(
                "CONTROLPLANE_CORS_ALLOW_ORIGINS",
                "http://127.0.0.1:4317,http://localhost:4317,http://127.0.0.1:3001,http://localhost:3001,http://127.0.0.1:3000,http://localhost:3000",
            )
        ),
        api_auth_token=_env_str("CONTROLPLANE_API_AUTH_TOKEN", "").strip(),
        api_auth_disabled=_parse_bool_env("CONTROLPLANE_API_AUTH_DISABLED", default=False),
    )
