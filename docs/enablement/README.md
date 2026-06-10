# SquirrelOps Enablement

Source corpus for partnership and sales conversations. Optimized for Notebook LM ingestion.

## Purpose

Build Matt's command of SquirrelOps to the point where partnership calls and sales conversations can happen unscripted, on the spot, without notes. The docs in this directory are the source material. Notebook LM primes you; the `drill/` layer builds the live-call fluency.

Three consumer modes:

1. **Read directly.** When prepping for a specific conversation, pull the relevant doc and skim. Each is structured for fast scan.
2. **Feed to Notebook LM.** Sync this directory to Google Drive, point a Notebook LM workspace at it, and generate audio overviews, study guides, FAQs, and Q&A drills. See `NOTEBOOK-LM-GUIDE.md`. This is passive priming.
3. **Drill with `drill/`.** The active-recall layer: a 94-card Anki deck, glance-able cheat sheets, and six mock call transcripts, with a daily/weekly practice protocol and recorded confidence checkpoints. This is where reading turns into fluency. Start with `drill/README.md`.

## Contents

| File | What's in it | When to read |
|---|---|---|
| `00-overview.md` | Top-level product pitch, hooks, headline numbers | First doc for any new conversation |
| `01-architecture.md` | How SquirrelOps works under the hood | Technical conversations with engineers, SOC managers |
| `02-numbers-and-proof.md` | Every quantified claim with provenance | Any conversation where you cite numbers |
| `03-framework-alignment.md` | NIST CSF, AI RMF, CIS, OWASP, ATLAS mapping | GRC, compliance, AI governance buyers |
| `04-pricing.md` | Three-tier model and customization drivers | Commercial conversations |
| `05-modules.md` | The 7 enterprise modules + core, with honest maturity per module | Technical and product-depth conversations |
| `06-deployment-integration.md` | Topologies, SIEM/TAXII2 integration, latency, prerequisites | Partnership and technical-evaluator calls |
| `07-competitive-landscape.md` | The category is uncontested; how we sit vs guardrails and deception incumbents | "Who else does this," competitive questions |
| `08-objections-and-answers.md` | The hard questions with answers and pressure-handling. Read this most. | Drilling before any live call |
| `09-buyer-personas.md` | CISO, AppSec, GRC, SOC, AI Platform: fears, what to lead with, how to sense which one | Pre-call prep for a known audience |
| `10-partnership-talk-track.md` | Complement-not-compete framing for SIEM/TIP/AI-platform partners | Partnership conversations |
| `11-faq.md` | Catch-all quick answers, cross-referenced to the deep docs | Fast reference and Notebook LM drilling |
| `NOTEBOOK-LM-GUIDE.md` | How to set up sales-prep and partnership-prep notebooks | Reference |
| `drill/` | Cheat sheets, 94-card Anki deck, six mock call dialogues, and the daily/weekly drill protocol | Daily practice for live-call fluency |

## Style and audience

Written for two audiences:

1. **Matt (you).** Direct, concise, no fluff. Every section answers a question you'd actually face in a conversation.
2. **Notebook LM.** Self-contained docs that can be ingested independently. Cross-references use file names (e.g., "see `02-numbers-and-proof.md`") so the AI can resolve them.

Voice rules:
- No em-dashes
- Short declarative sentences
- Fragments where they hit harder
- No soft closers, no throat-clearing, no hedging
- Specific numbers and verbs, not abstractions

## Maintenance

Update these docs whenever the product version changes, pricing shifts, or a real partnership/sales conversation surfaces a question we should have anticipated. The corpus is the source of truth. Marketing site, decks, and AI-generated audio overviews all derive from here.
