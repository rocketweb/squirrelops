from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
API_ROOT = REPO_ROOT / "apps" / "controlplane-api"
for import_path in (REPO_ROOT, API_ROOT):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from controlplane_api.config import ControlPlaneSettings


@pytest.fixture
def settings_factory(tmp_path: Path):
    projects_path = tmp_path / "projects.yaml"
    projects_path.write_text("projects: []\n", encoding="utf-8")

    defaults: dict[str, Any] = {
        "repo_root": REPO_ROOT,
        "workspace_root": tmp_path / "workspace",
        "projects_config_path": projects_path,
        "clownpeanuts_api_base": "http://127.0.0.1:8099",
        "clownpeanuts_api_token": "",
        "clownpeanuts_ws_events_url": "ws://127.0.0.1:8099/ws/events",
        "clownpeanuts_ws_theater_url": "ws://127.0.0.1:8099/ws/theater/live",
        "clownpeanuts_ws_token": "",
        "pingting_repo_path": tmp_path / "pingting",
        "pingting_status_path": tmp_path / "pingting" / "data" / "status.json",
        "pingting_config_path": tmp_path / "pingting" / "config" / "pingting.yaml",
        "pingting_python_bin": None,
        "pingting_status_max_age_seconds": 120,
        "pingting_command_timeout_seconds": 2,
        "orchestration_state_path": tmp_path / "actions-state.json",
        "orchestration_action_timeout_seconds": 2,
        "bootstrap_script_path": tmp_path / "bootstrap.sh",
        "smoke_script_path": tmp_path / "smoke.sh",
        "update_script_path": tmp_path / "update.sh",
        "cors_allow_origins": [],
        "api_auth_token": "control-plane-test-token-0123456789",
        "api_auth_disabled": False,
    }

    def factory(**overrides: Any) -> ControlPlaneSettings:
        return ControlPlaneSettings(**(defaults | overrides))

    return factory
