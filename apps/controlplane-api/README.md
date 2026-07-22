# Control Plane API

`apps/controlplane-api` is the aggregator API for the multi-product operator dashboard.

It exposes:

- `/overview/summary`: cross-repo health for ClownPeanuts, PingTing, and orchestration state.
- `/sentry/summary`: PingTing status snapshot (`?refresh=true` forces CLI refresh).
- `/sentry/findings`: recent PingTing findings from SQLite (`limit`, `severity`, and inclusion flags).
- `/sentry/runs`: recent PingTing agent run history from SQLite (`limit`, `agent`, `status`).
- `/orchestration/summary`: managed repo and workflow status from SquirrelOps.
- `/orchestration/actions/bootstrap`: executes `scripts/bootstrap_repos.sh` against workspace repos.
- `/orchestration/actions/smoke`: executes `harness/smoke.sh` against workspace repos.
- `/orchestration/actions/update`: executes `scripts/update_repos.sh` against workspace repos.
- `/deception/{path}`: HTTP proxy path to the ClownPeanuts API.
- `/deception/ws/events`: websocket relay for ClownPeanuts event stream.
- `/deception/ws/theater/live`: websocket relay for ClownPeanuts theater stream.

## Run locally

```bash
cd apps/controlplane-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

The API listens on `http://127.0.0.1:8199` by default.

Container image build (from repository root):

```bash
docker buildx build \
  --build-context pingting=../pingting \
  -f apps/controlplane-api/Dockerfile \
  -t squirrelops-controlplane-api \
  --load \
  .
```

The PingTing build context supplies its pinned runtime requirements. For normal local operation, prefer `docker compose -f docker-compose.controlplane.yml up --build`; compose wires this context automatically from `SQUIRRELOPS_WORKSPACE`.

The container starts as root only long enough to map `appuser` to the numeric UID/GID owning the mounted PingTing checkout, then uses `gosu` to run the API unprivileged. It fails startup if the checkout is root-owned or the mapped user cannot read PingTing config/status and write the `data/` and `logs/` directories required by the CLI fallback.

## Environment variables

- `CONTROLPLANE_WORKSPACE_ROOT` (default: parent directory containing this repository)
- `CONTROLPLANE_PROJECTS_CONFIG` (default: `config/projects.yaml`)
- `CLOWNPEANUTS_API_BASE` (default: `http://127.0.0.1:8099`)
- `CLOWNPEANUTS_API_TOKEN` (optional)
- `CLOWNPEANUTS_WS_EVENTS_URL` (default: `ws://127.0.0.1:8099/ws/events`)
- `CLOWNPEANUTS_WS_THEATER_URL` (default: `ws://127.0.0.1:8099/ws/theater/live`)
- `CLOWNPEANUTS_WS_TOKEN` (optional, defaults to `CLOWNPEANUTS_API_TOKEN` when set)
- `PINGTING_REPO_PATH` (default: `$CONTROLPLANE_WORKSPACE_ROOT/pingting`)
- `PINGTING_STATUS_PATH` (default: `$PINGTING_REPO_PATH/data/status.json`)
- `PINGTING_CONFIG_PATH` (default: `$PINGTING_REPO_PATH/config/pingting.yaml`)
- `PINGTING_PYTHON_BIN` (optional explicit Python executable; compose pins `/usr/local/bin/python` so host virtualenvs are never selected inside Linux)
- `PINGTING_STATUS_MAX_AGE_SECONDS` (default: `120`)
- `PINGTING_STATUS_TIMEOUT_SECONDS` (default: `20`)
- `CONTROLPLANE_API_AUTH_TOKEN` (shared API token; when unset the API fails closed and returns 503)
- `CONTROLPLANE_API_AUTH_DISABLED` (set to `1` to intentionally run without auth, trusted local use only)
- `CONTROLPLANE_CORS_ALLOW_ORIGINS` (comma-separated origins)
- `CONTROLPLANE_ACTION_TIMEOUT_SECONDS` (default: `900`)
- `CONTROLPLANE_ACTION_STATE_PATH` (default: `data/controlplane/actions-state.json`)
- `CONTROLPLANE_BOOTSTRAP_SCRIPT_PATH` (default: `scripts/bootstrap_repos.sh`)
- `CONTROLPLANE_SMOKE_SCRIPT_PATH` (default: `harness/smoke.sh`)
- `CONTROLPLANE_UPDATE_SCRIPT_PATH` (default: `scripts/update_repos.sh`)

> The control-plane variables were previously misspelled `CONTROLPANE_*` (missing
> the second "L"). Those legacy names still work as deprecated aliases, but the
> canonical `CONTROLPLANE_*` spelling above takes precedence and should be used.

Browser WebSocket clients authenticate with two subprotocols:
`cp-events-v1` and `cp-auth.<base64url-token>`. Query-string tokens are rejected
so secrets do not persist in access logs. Server-side clients may continue to use
`Authorization: Bearer` or `X-API-Key` headers. The relay sends the ClownPeanuts
token upstream only in an `Authorization` header.
