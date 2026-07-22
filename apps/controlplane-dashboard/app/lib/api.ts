// REST calls go through the same-origin BFF at /api/cp/*, which injects the
// control-plane auth token server-side (see app/api/cp/[...slug]/route.ts).
// No API token is shipped to the browser for REST traffic.
const API_BASE = "/api/cp/deception"

// WebSockets cannot be proxied by `next start`, so they connect directly to the
// control-plane API. Browser clients carry the opt-in token in a WebSocket
// subprotocol so it never appears in URLs or access logs. The token is still
// client-visible, so leave NEXT_PUBLIC_CONTROLPLANE_WS_TOKEN unset to keep all
// secrets off the client and use REST polling through the BFF instead.
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
const WS_BASE_PROTOCOL = "cp-events-v1"
const WS_AUTH_PROTOCOL_PREFIX = "cp-auth."

const cpFetch = (url: string, init?: RequestInit): Promise<Response> => fetch(url, init)

const encodeWebSocketToken = (token: string): string => {
  const bytes = new TextEncoder().encode(token)
  let binary = ""
  for (const byte of bytes) {
    binary += String.fromCharCode(byte)
  }
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "")
}

const webSocketProtocols = (): string[] => {
  const protocols = [WS_BASE_PROTOCOL]
  if (WS_AUTH_TOKEN) {
    protocols.push(`${WS_AUTH_PROTOCOL_PREFIX}${encodeWebSocketToken(WS_AUTH_TOKEN)}`)
  }
  return protocols
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

export { API_BASE, WS_BASE, WS_THEATER_BASE, cpFetch, webSocketProtocols, withQueryParams }
