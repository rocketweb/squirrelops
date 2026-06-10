# Framework Card

Full mappings and the "what NOT to claim" in `03-framework-alignment.md`. Glance version.

## The framing (say this first, every time)

"AI Deception isn't its own framework. It slots into the Detect and Respond functions of whatever you already run."

## The mappings (pick 2-3 per buyer)

| Framework | Control | We do |
|---|---|---|
| NIST CSF 2.0 | DE.CM, DE.AE | Continuous LLM-surface monitoring, anomaly analysis w/ attribution |
| NIST CSF 2.0 | RS.AN, RS.CO | Enriched captures, STIX into the SIEM |
| NIST AI RMF | Measure, Manage | Quantified metrics (66/67, 0 FP), incident output |
| CIS Controls v8 | Control 13 | Deception technology (explicitly named in the control) |
| CIS Controls v8 | Control 8 | Audit log mgmt via TAXII2 feed |
| OWASP LLM Top 10 | LLM01, LLM06, etc. | Captured + categorized at the decoy |
| MITRE ATLAS | AI-specific TTPs | Mapped in STIX output |

## CIS Control 13 is your gift

"CIS Controls v8, Control 13 explicitly calls for deception technology. Until now that meant network honeypots. Nothing for the LLM surface. We're that. The framework asked. Now there's an answer."

## What you do NOT have (say it straight)

- NOT SOC 2 certified (can produce a control-mapping package)
- NOT FedRAMP authorized
- NOT ISO 27001 / 42001 certified
- These are buyer obligations we SUPPORT with evidence, not vendor certifications.

## The discipline

GRC buyers catch overclaims for a living. Map specific controls to specific capabilities. Offer the evidence. Name your limits before they ask. Honesty IS the sale with this persona.
