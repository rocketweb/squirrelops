# Personas Card

Full depth in `09-buyer-personas.md`. Glance version.

## Sense who you're talking to (first thing they probe)

| They talk about | They are | Lead with |
|---|---|---|
| Risk, board, budget, "the business" | **CISO** | The detection-gap story |
| Frameworks, audits, "how do we prove" | **GRC / AI Gov** | Honest framework mapping + evidence |
| The app, the pipeline, integration | **AppSec** | Architecture, latency, STIX fit |
| Alerts, noise, their SIEM, on-call | **SOC Manager** | Signal quality, zero FP |
| Latency, the model, "will this break it" | **AI Platform** | Minimal footprint, ~30ms, guest not tenant |

When unsure: "So I pitch this right, what's your role in the AI security decision?"

## Each one's fear → your lead line

- **CISO** fears a breach on the AI they greenlit → "Logs tell you what happened. Deception tells you who, with what, why, live."
- **GRC** fears an audit finding → "We slot into Detect/Respond of what you already run. And we publish a number."
- **AppSec** fears shelfware / a path incident → "Standard STIX over TAXII2. No new dashboard. ~30ms."
- **SOC** fears more noise → "A legit user never talks to a decoy. Anything in it is hostile. That's the FP story."
- **AI Platform** fears latency/risk in their serving path → "Your model is your system. We're a careful guest in front of it."

## The two groups

- **Decision-makers:** CISO, GRC, sometimes AppSec.
- **Evaluators (can veto):** SOC Manager, AI Platform.
- Both must be satisfied. The AI Platform lead is the silent veto. Win them early.

## Multi-stakeholder move

Open with the CISO frame (agree on the problem), then hand each evaluator their piece by name. "Security leadership, governance, platform: let me make sure each of you gets what you need."
