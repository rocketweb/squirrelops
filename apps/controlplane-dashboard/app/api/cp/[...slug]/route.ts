import { NextRequest } from "next/server"

// Server-side proxy (BFF) to the control-plane API.
//
// The browser talks only to this same-origin route; the control-plane auth token
// is read here from a SERVER-ONLY env var (no NEXT_PUBLIC prefix) and never ships
// to the client bundle. The upstream host is fixed by configuration, so callers
// cannot redirect this proxy at an arbitrary destination.

export const runtime = "nodejs"
export const dynamic = "force-dynamic"

const PROXY_PREFIX = "/api/cp"

const upstreamBase = (
  process.env.CONTROLPLANE_API_INTERNAL_BASE ??
  process.env.CONTROLPANE_API_INTERNAL_BASE ??
  "http://127.0.0.1:8199"
).replace(/\/+$/, "")

const upstreamToken = (
  process.env.CONTROLPLANE_API_TOKEN ??
  process.env.CONTROLPANE_API_TOKEN ??
  ""
).trim()

// Hop-by-hop and identity headers that must not be forwarded upstream.
const STRIPPED_REQUEST_HEADERS = new Set([
  "host",
  "connection",
  "content-length",
  "authorization",
  "cookie",
  "x-api-key",
])

const buildUpstreamUrl = (request: NextRequest): string => {
  const pathname = request.nextUrl.pathname
  const suffix = pathname.startsWith(PROXY_PREFIX) ? pathname.slice(PROXY_PREFIX.length) : pathname
  const normalized = suffix.startsWith("/") ? suffix : `/${suffix}`
  return `${upstreamBase}${normalized}${request.nextUrl.search}`
}

const proxy = async (request: NextRequest): Promise<Response> => {
  const url = buildUpstreamUrl(request)

  const headers = new Headers()
  request.headers.forEach((value, key) => {
    if (!STRIPPED_REQUEST_HEADERS.has(key.toLowerCase())) {
      headers.set(key, value)
    }
  })
  if (upstreamToken) {
    headers.set("authorization", `Bearer ${upstreamToken}`)
  }

  const method = request.method.toUpperCase()
  const hasBody = method !== "GET" && method !== "HEAD"
  const body = hasBody ? await request.arrayBuffer() : undefined

  let upstream: Response
  try {
    upstream = await fetch(url, {
      method,
      headers,
      body,
      redirect: "manual",
      cache: "no-store",
    })
  } catch {
    return new Response(JSON.stringify({ detail: "control-plane API unreachable" }), {
      status: 502,
      headers: { "content-type": "application/json" },
    })
  }

  const responseHeaders = new Headers()
  const contentType = upstream.headers.get("content-type")
  if (contentType) {
    responseHeaders.set("content-type", contentType)
  }
  const wwwAuth = upstream.headers.get("www-authenticate")
  if (wwwAuth) {
    responseHeaders.set("www-authenticate", wwwAuth)
  }

  return new Response(upstream.body, {
    status: upstream.status,
    headers: responseHeaders,
  })
}

export const GET = proxy
export const POST = proxy
export const PUT = proxy
export const PATCH = proxy
export const DELETE = proxy
export const OPTIONS = proxy
