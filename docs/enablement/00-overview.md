# SquirrelOps Overview

## The one-line pitch

SquirrelOps is a deception security platform for AI. It sits in front of customer-facing LLMs, captures attacker behavior in real time, and emits structured threat intelligence as STIX 2.1 over TAXII2.

## The 30-second version

Most LLM security tries to keep attackers out. Identity, rate limits, content filters, guardrails. That's the Protect layer.

SquirrelOps is the Detect and Respond layer. When someone tries to jailbreak your LLM or prompt-inject your agent, we route them into a high-fidelity decoy and capture what they tried, what tooling they used, and what they were after. The real model stays clean. Your security team gets labeled attacker behavior straight to their SIEM.

Numbers from the v1.0.4 release: 98.5% threat capture, zero false positives, under two minutes to detection.

## What it actually does

SquirrelOps consists of two things working together:

1. **A real-time detection and routing layer.** Sits in front of your LLM endpoints. Classifies incoming traffic as benign or adversarial. Adversarial traffic gets routed to a decoy model. Benign traffic flows to the real model untouched.

2. **A threat intelligence pipeline.** When adversarial traffic hits the decoy, we capture the full session, label the techniques used (mapped to OWASP LLM Top 10 and MITRE ATLAS), and emit STIX 2.1 bundles via TAXII2 to whatever the customer's SIEM, SOAR, or threat intel platform consumes.

The deception layer wins because it doesn't try to block attackers. It engages them, observes them, and feeds the data back to defenders. Attackers reveal their hand without realizing they're talking to a decoy.

## Why this matters now

Every enterprise is deploying customer-facing LLMs. Customer support agents. Sales copilots. Internal RAG systems. Coding assistants. The LLM attack surface is now a real attack surface.

The existing AI security market is dominated by API filters and content moderation tools. These look like WAFs for AI. They reject bad inputs. But they don't tell you who's attacking you, what they're trying, or whether the attack succeeded. They produce alerts, not intelligence.

SquirrelOps produces intelligence. That's the difference.

## Who buys it

Five buyer personas, in rough order of decision-making weight:

1. **CISO.** Owns AI security risk at the executive level. Wants quantified defense, not a security theater story.
2. **Head of AppSec.** Owns the technical implementation. Wants to know how it integrates and what it costs to operate.
3. **GRC / Head of AI Governance.** Owns framework alignment. Wants NIST CSF, NIST AI RMF, ISO 42001 mappings. Wants evidence-based reporting for audits.
4. **SOC Manager.** Owns day-to-day operations. Wants signal-over-noise alerts and clean SIEM integration.
5. **Head of AI Platform / Head of AI Engineering.** Owns the LLM deployment. Wants something that doesn't break their pipeline or add unacceptable latency.

The first three are decision-makers. The last two are technical evaluators. Both need to be happy for a deal to close.

## What it isn't

SquirrelOps is not:

- A WAF for AI. Lakera, Lasso, Cloudflare AI Firewall do that.
- A model alignment or red-teaming tool. Robust Intelligence and HiddenLayer overlap there.
- A general-purpose network deception platform. TrapX, Illusive, Acalvio do that for traditional infrastructure.
- An LLM observability platform. Datadog, Arize, Helicone do that.

SquirrelOps is specifically deception for the LLM attack surface. The Venn diagram intersection of network deception and AI security. A new category.

## Top-line proof points

For deeper provenance on each number, see `02-numbers-and-proof.md`.

- **98.5% threat capture** (66 of 67 attack turns) in the v1.0.4 internal adversarial campaign. Say "of attack turns," never "of the 87-turn campaign." See `02-numbers-and-proof.md` for why the denominator matters.
- **Zero false positives** on benign traffic
- **Under 2 minutes** to detection from first malicious request
- **815 tests** pass on the v1.0.5 release branch (over 1,000 across the full suite). The adversarial campaign spans 6 technique families across 7 attacker profiles. Do not say "80+ techniques."
- **Bit-identical reproducible builds.** Customers can rebuild any profile bundle from source and verify it matches the signed artifact
- **STIX 2.1 over TAXII2** native output. Drops into Splunk, Sentinel, Chronicle, OpenCTI, Elastic without translation

## Current product status (as of v1.0.4, May 2026)

- 7 enterprise modules in the platform (see `05-modules.md`)
- AI Deception module (the v1.0.4 headline) ships the LLM-specific capability
- Pre-customer / lighthouse phase
- Pricing model in `04-pricing.md`
- Public marketing site at squirrelops.io
- Source-available core (SquirrelOps orchestration, ClownPeanuts runtime, PingTing monitoring, macOS app) under PolyForm Noncommercial
- Enterprise modules private

## Founder

Matt MacDougall. Built SquirrelOps as part of Rocket Web. Active in cybersecurity tooling for years before pivoting deception toward the AI attack surface specifically.
