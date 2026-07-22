#!/usr/bin/env bash
set -euo pipefail

LABEL="${CONTROLPLANE_LAUNCHD_LABEL:-${CONTROLPANE_LAUNCHD_LABEL:-com.squirrelops.controlplane}}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd -P)"
START_SCRIPT="${SCRIPT_DIR}/start_dev.sh"
PLIST_DIR="${HOME}/Library/LaunchAgents"
PLIST_PATH="${PLIST_DIR}/${LABEL}.plist"
UID_VALUE="$(id -u)"

API_PORT="${CONTROLPLANE_API_PORT:-${CONTROLPANE_API_PORT:-8199}}"
DASHBOARD_PORT="${CONTROLPLANE_DASHBOARD_PORT:-${CONTROLPANE_DASHBOARD_PORT:-4317}}"
PYTHON_BIN_VALUE="${PYTHON_BIN:-$(command -v python3 || true)}"
NPM_BIN_VALUE="${NPM_BIN:-$(command -v npm || true)}"
NODE_BIN_VALUE="${NODE_BIN:-$(command -v node || true)}"

if [[ ! "${LABEL}" =~ ^[A-Za-z0-9][A-Za-z0-9.-]*$ ]]; then
  echo "ERROR: launchd label may contain only letters, numbers, dots, and hyphens." >&2
  exit 1
fi

for port in "${API_PORT}" "${DASHBOARD_PORT}"; do
  if [[ ! "${port}" =~ ^[0-9]+$ ]] || ((10#${port} < 1 || 10#${port} > 65535)); then
    echo "ERROR: invalid control-plane port: ${port}" >&2
    exit 1
  fi
done

if [[ -z "${PYTHON_BIN_VALUE}" ]]; then
  echo "ERROR: python3 not found; set PYTHON_BIN before installing launch agent." >&2
  exit 1
fi

if [[ -z "${NPM_BIN_VALUE}" ]]; then
  echo "ERROR: npm not found; set NPM_BIN before installing launch agent." >&2
  exit 1
fi

if [[ -z "${NODE_BIN_VALUE}" ]]; then
  echo "ERROR: node not found; set NODE_BIN before installing launch agent." >&2
  exit 1
fi

API_AUTH_TOKEN="${CONTROLPLANE_API_AUTH_TOKEN:-${CONTROLPANE_API_AUTH_TOKEN:-}}"
GENERATED_API_AUTH_TOKEN=0
if [[ -z "${API_AUTH_TOKEN}" ]]; then
  API_AUTH_TOKEN="$("${PYTHON_BIN_VALUE}" -c 'import secrets; print(secrets.token_urlsafe(32))')"
  GENERATED_API_AUTH_TOKEN=1
fi

PATH_VALUE="${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
PATH_VALUE="$(dirname "${PYTHON_BIN_VALUE}"):${PATH_VALUE}"
PATH_VALUE="$(dirname "${NPM_BIN_VALUE}"):${PATH_VALUE}"
PATH_VALUE="$(dirname "${NODE_BIN_VALUE}"):${PATH_VALUE}"

umask 077
mkdir -p "${PLIST_DIR}"

"${PYTHON_BIN_VALUE}" - \
  "${PLIST_PATH}" \
  "${LABEL}" \
  "${START_SCRIPT}" \
  "${REPO_ROOT}" \
  "${API_PORT}" \
  "${DASHBOARD_PORT}" \
  "${PYTHON_BIN_VALUE}" \
  "${NPM_BIN_VALUE}" \
  "${NODE_BIN_VALUE}" \
  "${PATH_VALUE}" \
  "${API_AUTH_TOKEN}" <<'PY'
from pathlib import Path
import plistlib
import sys

(
    plist_path,
    label,
    start_script,
    repo_root,
    api_port,
    dashboard_port,
    python_bin,
    npm_bin,
    node_bin,
    path_value,
    api_auth_token,
) = sys.argv[1:]

payload = {
    "Label": label,
    "ProgramArguments": [start_script],
    "WorkingDirectory": repo_root,
    "EnvironmentVariables": {
        "CONTROLPLANE_API_PORT": api_port,
        "CONTROLPLANE_DASHBOARD_PORT": dashboard_port,
        "CONTROLPLANE_API_AUTH_TOKEN": api_auth_token,
        "CONTROLPLANE_API_TOKEN": api_auth_token,
        "PYTHON_BIN": python_bin,
        "NPM_BIN": npm_bin,
        "NODE_BIN": node_bin,
        "PATH": path_value,
    },
    "RunAtLoad": True,
    "KeepAlive": True,
    "StandardOutPath": "/tmp/squirrelops-controlplane.launchd.log",
    "StandardErrorPath": "/tmp/squirrelops-controlplane.launchd.err.log",
}

with Path(plist_path).open("wb") as handle:
    plistlib.dump(payload, handle, fmt=plistlib.FMT_XML, sort_keys=False)
PY

chmod 600 "${PLIST_PATH}"

if [[ "${CONTROLPLANE_LAUNCHD_DRY_RUN:-0}" == "1" ]]; then
  echo "Wrote launch agent plist (dry run): ${PLIST_PATH}"
  exit 0
fi

launchctl bootout "gui/${UID_VALUE}/${LABEL}" >/dev/null 2>&1 || true
launchctl bootstrap "gui/${UID_VALUE}" "${PLIST_PATH}"
launchctl enable "gui/${UID_VALUE}/${LABEL}"
launchctl kickstart -k "gui/${UID_VALUE}/${LABEL}"

echo "Installed launch agent: ${LABEL}"
echo "Plist: ${PLIST_PATH}"
if [[ "${GENERATED_API_AUTH_TOKEN}" == "1" ]]; then
  echo "Generated a control-plane API token and stored it in the mode-600 plist."
fi
echo "Dashboard: http://127.0.0.1:${DASHBOARD_PORT}"
echo "API: http://127.0.0.1:${API_PORT}"
