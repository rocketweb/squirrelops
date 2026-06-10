# Competitive Battlecard

Full picture in `07-competitive-landscape.md`. This is the glance version.

## The headline

No commercial LLM-deception product exists. You define the category. (Don't say "first/only" publicly until counsel checks patent 12423441. Say "no commercial product we've found.")

## The frame

Guardrails are a wall. We're the trapdoor behind it. Complementary. Run both.

## Who they'll name → your one line

| They say | You say |
|---|---|
| Lakera | "API filter, now Check Point. Blocks at the door. We catch what gets through." |
| Prompt Security | "Filter, now SentinelOne. Same wall, no trapdoor." |
| Protect AI | "Model scanning, now Palo Alto. Pre-deploy posture, not runtime capture." |
| HiddenLayer | "Red-teams your model. Complementary. They harden, we catch." |
| Robust Intelligence | "Validation, now Cisco. Tests the model, doesn't trap the attacker." |
| Acalvio | "Closest. They make a honeypot WITH AI. We make a honeypot that IS an AI." |
| Thinkst Canary | "Network canaries. We do it for the LLM surface, with engagement and intel." |
| "Build it ourselves" | "12-18 months: 2-layer pipeline, decoy model, signed bundles, 800-test gate, STIX pipeline. What's that worth, and your exposure while you build?" |

## The proof point

EchoLeak (CVE-2025-32711, June 2025). Zero-click prompt injection in M365 Copilot. Beat Microsoft's own classifier. Filters fail. You need a fallback.

## Market facts (clean sources only)

- Agentic AI security: $1.65B (2026) → $13.5B (2032), 42% CAGR (MarketsandMarkets).
- 47% of orgs have no AI-specific security controls (Kiteworks 2025).
- DO NOT cite "340% YoY" or "88% had an incident." Vendor-blog noise.

## The closer line

"Everyone's building a taller wall around your LLM. We build the room on the other side. When an attacker slips past, we route them into a decoy that wastes their time, captures their playbook, and tells you how they got in."
