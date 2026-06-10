# FAQ

A catch-all of quick answers, in plain language, for fast reference and for Notebook LM to drill you on. When a question doesn't fit neatly into the other docs, it's here. Each answer is short on purpose. Depth lives in the doc cross-referenced.

## What is it, in one sentence?

A deception security platform for AI. It sits in front of your customer-facing LLM, routes attackers into a decoy, and sends labeled threat intelligence to your SIEM. (`00-overview.md`)

## What problem does it solve?

Enterprises are deploying customer-facing LLMs and have no way to detect when someone attacks them. Guardrails try to block attacks. SquirrelOps detects the ones that get through and tells you who, what, and how. (`00-overview.md`, `07-competitive-landscape.md`)

## How does it actually work?

Two layers of detection (deterministic rules, then an ML classifier) classify every prompt. Adversarial traffic gets routed to a decoy LLM. The real model never sees the attacker. The captured session is enriched with ATT&CK and OWASP LLM labels and emitted as STIX 2.1 over TAXII2. (`01-architecture.md`)

## What are the numbers?

98.5%, meaning 66 of 67 attack turns captured in the internal adversarial campaign. Zero false positives on benign traffic. Under 2 minutes to detection. Always say "of attack turns," never "of the 87-turn campaign." (`02-numbers-and-proof.md`)

## Is it a real product or a demo?

The AI Deception module and the ClownPeanuts runtime are real, tested (1,000+ tests across the suite), and functional. We're pre-customer, in lighthouse phase. Two of the seven modules (ADLibs, PripyatSprings) are real foundations narrower than their names imply. Be precise about that. (`05-modules.md`)

## Who's it for?

Enterprises running customer-facing LLMs. The buyers are CISOs, AppSec leads, GRC/AI-governance, SOC managers, and AI platform owners. (`09-buyer-personas.md`)

## How is it different from Lakera / a guardrail?

Guardrails are a wall that blocks prompts and assumes the block holds. We're the trapdoor behind the wall that catches the attacker who got through. Complementary, run both. (`07-competitive-landscape.md`)

## Who else does LLM deception?

No commercial product we've found. It's been academic research until now. We're defining the category. (Don't make public "first/only" claims until IP counsel reviews patent 12423441.) (`07-competitive-landscape.md`)

## Will it slow down our model?

About 30ms on clean traffic, below the noise floor of LLM response times. The model takes hundreds of ms. (`06-deployment-integration.md`)

## How does it integrate with our SIEM?

Standard STIX 2.1 over TAXII2. Anything that speaks TAXII2 ingests it. OpenCTI is integrated and documented. For Splunk or Sentinel you point their TAXII2 collector at our feed. No proprietary format. (`06-deployment-integration.md`)

## How does it deploy?

Three options: in-line gateway, sidecar, or peered VPC. Container-based. AWS, Azure, GCP, on-prem, or hybrid. Air-gap supported at the top tier. (`06-deployment-integration.md`)

## What does it cost?

Pilot $50-75K (4-6 weeks, credits toward year one). Mission $150-250K/yr + implementation. Constellation $400K-$1M+/yr for multi-environment, multi-BU. (`04-pricing.md`)

## How fast can we be live?

Pilot in 4-6 weeks against one endpoint. Production in 6-8 weeks. Enterprise white-glove in 8-12. (`06-deployment-integration.md`)

## Are you compliant with [framework]?

We slot into the Detect and Respond functions of frameworks you already run (NIST CSF, AI RMF, CIS Control 13, OWASP LLM Top 10, MITRE ATLAS). We are NOT certified against SOC 2, FedRAMP, or ISO yet; we support your program with evidence and can produce a control-mapping package. (`03-framework-alignment.md`)

## Does it see our real user data?

The decoy is not connected to your real systems, so it leaks nothing real. Benign traffic passes to your model; we classify but the deception path only engages attackers. Deploy in-region or in a VPC you control for residency. (`08-objections-and-answers.md`)

## What if the attacker realizes it's a decoy?

By then they've revealed technique, tooling, and intent. That's the win. GhostCrew also populates decoys with realistic activity so they don't look empty. (`08-objections-and-answers.md`)

## Why trust an early vendor with security?

Because of what deploys, not who we are. Every bundle is signed and bit-identically reproducible: you verify exactly what runs, no trust required. Runtime is source-available, output is standard STIX, so you're never locked into a black box. (`08-objections-and-answers.md`)

## What's the decoy model?

A LoRA-adapted small open-weight model, trained to engage attackers convincingly without leaking real secrets. It's the "persona" in each profile bundle. (`01-architecture.md`, `05-modules.md`)

## What's a "profile bundle"?

The signed, reproducible artifact that ships a tenant's detection rules, ML model, and decoy persona to production. Customers can rebuild it from source and verify it's bit-identical to what's deployed. (`01-architecture.md`, `02-numbers-and-proof.md`)

## Can we customize it?

Yes. Per-tenant rule tuning, industry-specific rule packs, custom decoy personas, custom SIEM bridges. That's where the higher tiers and a la carte add-ons live. (`04-pricing.md`)

## What's the company behind it?

SquirrelOps, built within Rocket Web by Matt MacDougall. The suite is eleven repositories: a core runtime, seven deception modules, monitoring, and a consumer home product (which is separate and noncommercial). (`05-modules.md`)

## What's the catch / what should I be honest about?

Pre-customer. Not yet certified. Two modules are foundations, not finished features. The ML layer ships in the bundle (confirm it's included per deployment). The intel feed needs auth turned on before exposure. Stating these plainly is what makes the rest believable. (`02-numbers-and-proof.md`, `08-objections-and-answers.md`)

## What do I do if I get asked something not in here?

"Good question, I don't want to guess. What I can tell you is [closest thing you know]. I'll get you the precise answer by [day]." Then follow up. Never invent. (`08-objections-and-answers.md`)
