# Control Plane Dashboard

The dashboard is a local operator interface for SquirrelOps. Its same-origin
`/api/cp/*` backend-for-frontend injects `CONTROLPLANE_API_TOKEN`, which grants
access to orchestration actions and the authenticated ClownPeanuts proxy.

## Network trust boundary

The default scripts and Docker Compose file bind the dashboard to
`127.0.0.1:4317`. Keep that loopback-only boundary unless another authentication
layer is configured. Do not expose the dashboard server directly to an untrusted
network: anyone who can call its BFF can otherwise use the server-side control-plane
token.

For a remote deployment, put an authenticating reverse proxy in front of the
dashboard and set `CONTROLPLANE_DASHBOARD_AUTH_TOKEN` on the dashboard server. The
BFF will then reject requests unless either:

- the `squirrelops_dashboard_token` cookie matches the configured token; or
- the `X-Controlplane-Dashboard-Token` request header matches it.

The cookie name can be changed with `CONTROLPLANE_DASHBOARD_AUTH_COOKIE`. Have the
authentication proxy issue the cookie with `HttpOnly`, `Secure`, and
`SameSite=Strict`; do not expose the shared secret to client-side JavaScript.

## Environment variables

- `CONTROLPLANE_API_INTERNAL_BASE`: server-side control-plane API URL.
- `CONTROLPLANE_API_TOKEN`: server-only bearer token injected by the BFF.
- `CONTROLPLANE_DASHBOARD_AUTH_TOKEN`: optional BFF authentication token required
  for non-loopback deployments.
- `CONTROLPLANE_DASHBOARD_AUTH_COOKIE`: optional cookie name override.
- `NEXT_PUBLIC_CONTROLPLANE_WS`: direct control-plane WebSocket origin.
- `NEXT_PUBLIC_CONTROLPLANE_WS_TOKEN`: optional, client-visible WebSocket token.
  It is sent in a `cp-auth.<base64url>` WebSocket subprotocol, never in the URL.

If the public WebSocket token is unset, the dashboard falls back to REST polling
through the BFF.
