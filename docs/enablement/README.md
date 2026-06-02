# SquirrelOps Enablement

Source corpus for partnership and sales conversations. Optimized for Notebook LM ingestion.

## Purpose

Build Matt's command of SquirrelOps to the point where partnership calls and sales conversations can happen unscripted, on the spot, without notes. The docs in this directory are the source material. Notebook LM is the drill harness.

Two consumer modes:

1. **Read directly.** When prepping for a specific conversation, pull the relevant doc and skim. Each is structured for fast scan.
2. **Feed to Notebook LM.** Sync this directory to Google Drive, point a Notebook LM workspace at it, and generate audio overviews, study guides, FAQs, and Q&A drills. See `NOTEBOOK-LM-GUIDE.md`.

## Contents

| File | What's in it | When to read |
|---|---|---|
| `00-overview.md` | Top-level product pitch, hooks, headline numbers | First doc for any new conversation |
| `01-architecture.md` | How SquirrelOps works under the hood | Technical conversations with engineers, SOC managers |
| `02-numbers-and-proof.md` | Every quantified claim with provenance | Any conversation where you cite numbers |
| `03-framework-alignment.md` | NIST CSF, AI RMF, CIS, OWASP, ATLAS mapping | GRC, compliance, AI governance buyers |
| `04-pricing.md` | Three-tier model and customization drivers | Commercial conversations |
| `05-modules.md` | The 7 enterprise modules + core platform | Phase 2 |
| `06-deployment-integration.md` | SIEM connectors, cloud topology, deployment models | Phase 2 |
| `07-competitive-landscape.md` | How we differ from Lakera, HiddenLayer, TrapX, etc. | Phase 2 |
| `08-objections-and-answers.md` | Top 20 buyer objections with rehearsed answers | Phase 2 |
| `09-buyer-personas.md` | CISO, AppSec, GRC, SOC, AI lead profiles | Phase 2 |
| `10-partnership-talk-track.md` | Framing SquirrelOps' role in a larger stack | Phase 2 |
| `11-faq.md` | Catch-all FAQ for everything not covered elsewhere | Phase 2 |
| `NOTEBOOK-LM-GUIDE.md` | How to set up sales-prep and partnership-prep notebooks | Reference |
| `drill/` | Cheat sheets, flash cards, mock dialogues | Phase 3 |

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
