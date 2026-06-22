// REST calls go through the same-origin BFF at /api/cp/*, which injects the
// control-plane auth token server-side (see app/api/cp/[...slug]/route.ts).
// No control-plane token is exposed to the browser.
const controlplaneFetch = (path: string, init?: RequestInit): Promise<Response> => {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`
  return fetch(`/api/cp${normalizedPath}`, init)
}

export { controlplaneFetch }
