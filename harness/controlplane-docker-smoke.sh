#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd -P)"
COMPOSE_FILE="${REPO_ROOT}/docker-compose.controlplane.yml"
PROJECT_NAME="squirrelops-controlplane-docker-smoke"
WORKSPACE_ROOT="${SQUIRRELOPS_WORKSPACE:-$(cd "${REPO_ROOT}/.." && pwd -P)}"
UID_PROBE_VOLUME="${PROJECT_NAME}-uid-probe"

cleanup() {
  docker compose --project-name "${PROJECT_NAME}" -f "${COMPOSE_FILE}" down --remove-orphans >/dev/null 2>&1 || true
  docker volume rm "${UID_PROBE_VOLUME}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

export SQUIRRELOPS_WORKSPACE="${WORKSPACE_ROOT}"
export CONTROLPLANE_API_AUTH_DISABLED=1

docker compose --project-name "${PROJECT_NAME}" -f "${COMPOSE_FILE}" build controlplane-api
IMAGE_ID="${PROJECT_NAME}-controlplane-api:latest"
if ! docker image inspect "${IMAGE_ID}" >/dev/null 2>&1; then
  echo "control-plane API image was not built" >&2
  exit 1
fi

docker compose --project-name "${PROJECT_NAME}" -f "${COMPOSE_FILE}" run --rm --no-deps -T controlplane-api \
  python - <<'PY'
from fastapi.testclient import TestClient
from main import app

response = TestClient(app).get("/sentry/summary?refresh=true")
response.raise_for_status()
payload = response.json()
assert payload["ok"] is True, payload.get("errors")
assert payload["source"] == "cli", payload["source"]
assert payload["stale"] is False, payload["stale"]
assert payload["errors"] == [], payload["errors"]
PY

docker volume create "${UID_PROBE_VOLUME}" >/dev/null
docker run --rm --user root --entrypoint sh \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" -c \
  'mkdir -p /workspace/pingting/config /workspace/pingting/data /workspace/pingting/logs && touch /workspace/pingting/config/pingting.yaml && chown -R 1234:1235 /workspace/pingting'

RUNTIME_UID="$(docker run --rm \
  -e PINGTING_REPO_PATH=/workspace/pingting \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" id -u)"
if [[ "${RUNTIME_UID}" != "1234" ]]; then
  echo "control-plane API ran as uid ${RUNTIME_UID}; expected mounted repo uid 1234" >&2
  exit 1
fi

docker run --rm --user root --entrypoint chown \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" -R 100:2345 /workspace/pingting

RUNTIME_GID="$(docker run --rm \
  -e PINGTING_REPO_PATH=/workspace/pingting \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" id -g)"
if [[ "${RUNTIME_GID}" != "2345" ]]; then
  echo "control-plane API ran as gid ${RUNTIME_GID}; expected mounted repo gid 2345" >&2
  exit 1
fi

docker run --rm --user root --entrypoint sh \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" -c \
  'chown 4321:4321 /workspace/pingting/config/pingting.yaml && chmod 600 /workspace/pingting/config/pingting.yaml'

set +e
docker run --rm \
  -e PINGTING_REPO_PATH=/workspace/pingting \
  -v "${UID_PROBE_VOLUME}:/workspace/pingting" \
  "${IMAGE_ID}" id >/dev/null 2>&1
UNREADABLE_CONFIG_EXIT="$?"
set -e
if [[ "${UNREADABLE_CONFIG_EXIT}" != "78" ]]; then
  echo "control-plane API accepted unreadable PingTing config; expected exit 78" >&2
  exit 1
fi

echo "Control-plane Docker smoke passed."
