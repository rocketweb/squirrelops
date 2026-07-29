# Security Policy

## Reporting a vulnerability

Please do not open a public issue for security reports.

Report privately using GitHub's private vulnerability reporting on this repository's **Security** tab. That routes the report directly to the maintainers and keeps the details confidential until a fix is available.

We aim to acknowledge a report within 5 business days.

## Scope

SquirrelOps runs a control plane that manages local runtimes and workspaces. The areas we most want reports about:

- Authentication or authorization bypass in the control-plane API or its WebSocket relay
- Escape from the managed workspace boundary, including path traversal and container escape
- Server-side request forgery or command injection reachable from control-plane input
- Leakage of API tokens, environment values, or configuration into client bundles, logs, or responses
- Privilege escalation between the dashboard, the API, and the managed runtimes

## Supported versions

This project is pre-1.0 and under active development. Security fixes land on `main`. There are no supported tagged releases yet, so please test against current `main` before reporting.

## Deployment note

The control plane is intended to bind to loopback and sit behind operator-controlled network boundaries. It is not hardened for direct exposure to untrusted networks. Reports that depend on deliberately publishing it to the internet without authentication will be treated as configuration guidance rather than vulnerabilities.

## Disclosure

We follow coordinated disclosure. Once a fix has shipped we publish a GitHub Security Advisory describing the issue and the affected commit range. Please allow reasonable time for a fix before disclosing publicly.
