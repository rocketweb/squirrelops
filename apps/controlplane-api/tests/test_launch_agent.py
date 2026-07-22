from __future__ import annotations

import os
from pathlib import Path
import plistlib
import stat
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_launch_agent_plist_escapes_values_and_provisions_auth(tmp_path: Path) -> None:
    home = tmp_path / "home & operator"
    unusual_path = f"/usr/bin:/bin:{tmp_path}/tools&<helpers"
    environment = os.environ | {
        "HOME": str(home),
        "PATH": unusual_path,
        "PYTHON_BIN": sys.executable,
        "NPM_BIN": "/usr/bin/true",
        "NODE_BIN": "/usr/bin/true",
        "CONTROLPLANE_LAUNCHD_DRY_RUN": "1",
    }
    environment.pop("CONTROLPLANE_API_AUTH_TOKEN", None)
    environment.pop("CONTROLPANE_API_AUTH_TOKEN", None)

    subprocess.run(
        ["/bin/bash", str(REPO_ROOT / "scripts" / "controlplane" / "install_launch_agent.sh")],
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )

    plist_path = home / "Library" / "LaunchAgents" / "com.squirrelops.controlplane.plist"
    with plist_path.open("rb") as handle:
        payload = plistlib.load(handle)

    variables = payload["EnvironmentVariables"]
    assert variables["PATH"].endswith(unusual_path)
    assert len(variables["CONTROLPLANE_API_AUTH_TOKEN"]) >= 32
    assert variables["CONTROLPLANE_API_TOKEN"] == variables["CONTROLPLANE_API_AUTH_TOKEN"]
    assert stat.S_IMODE(plist_path.stat().st_mode) == 0o600
