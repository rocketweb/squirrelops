// REST calls go through the same-origin BFF at /api/cp/*, which injects the
// control-plane auth token server-side (see app/api/cp/[...slug]/route.ts).
// No API token is shipped to the browser for REST traffic.
const API_BASE = "/api/cp/deception"

// WebSockets cannot be proxied by `next start`, so they connect directly to the
// control-plane API. A browser WebSocket cannot send headers, so when the API
// requires auth the token must travel as a query parameter and is therefore
// visible to the client. This is opt-in: leave NEXT_PUBLIC_CONTROLPLANE_WS_TOKEN
// unset to keep all secrets off the client (the dashboard transparently falls
// back to REST polling through the BFF), or set it to the API token to enable
// the live WebSocket stream and accept that it is client-visible.
const CONTROLPLANE_WS_BASE =
  process.env.NEXT_PUBLIC_CONTROLPLANE_WS ??
  process.env.NEXT_PUBLIC_CONTROLPANE_WS ??
  "ws://127.0.0.1:8199"
const WS_BASE =
  process.env.NEXT_PUBLIC_DECEPTION_WS ??
  `${CONTROLPLANE_WS_BASE}/deception/ws/events`
const WS_THEATER_BASE =
  process.env.NEXT_PUBLIC_DECEPTION_WS_THEATER ??
  `${CONTROLPLANE_WS_BASE}/deception/ws/theater/live`
const WS_AUTH_TOKEN = (
  process.env.NEXT_PUBLIC_CONTROLPLANE_WS_TOKEN ??
  process.env.NEXT_PUBLIC_CONTROLPANE_WS_TOKEN ??
  ""
).trim()

const cpFetch = (url: string, init?: RequestInit): Promise<Response> => fetch(url, init)

const withApiTokenQuery = (url: string): string => {
  if (!WS_AUTH_TOKEN) {
    return url
  }
  try {
    const parsed = new URL(url)
    if (!parsed.searchParams.has("token")) {
      parsed.searchParams.set("token", WS_AUTH_TOKEN)
    }
    return parsed.toString()
  } catch {
    return url
  }
}

const withQueryParams = (url: string, params: Record<string, string>): string => {
  try {
    const parsed = new URL(url)
    for (const [key, value] of Object.entries(params)) {
      parsed.searchParams.set(key, value)
    }
    return parsed.toString()
  } catch {
    return url
  }
}

export { API_BASE, WS_BASE, WS_THEATER_BASE, cpFetch, withApiTokenQuery, withQueryParams }
