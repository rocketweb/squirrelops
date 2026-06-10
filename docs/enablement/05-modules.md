# The Modules

SquirrelOps is a platform, not a single product. There is a core that runs everything, and seven deception modules that each cover a different part of the attack surface. This doc is so you can talk about any of them on a call without bluffing, and so you know exactly where the honest line is on each one.

The headline module (AI Deception) is real and deep. Some of the others are mature, a couple are foundations with real code but a narrower reach than the name implies. You need to know which is which, because a technical buyer will probe, and "let me be precise about what that one does today" beats getting caught overstating.

## The core (what runs underneath)

**ClownPeanuts** is the engine. This is the substance of the product: seven service emulators (SSH, HTTP, Redis, MySQL, Postgres, MongoDB, Memcached), a stateful "rabbit hole" engine with credential cascades and lateral-movement artifacts, the detection trap layer, and the STIX 2.1 / TAXII2 server that emits intel. When you talk about "the runtime" or "the decoys," this is it. It is the largest and most complete piece by far.

**SquirrelOps** (the orchestration layer) is a control plane that ties the runtime, monitoring, and dashboard together. Be precise: it is an aggregator and control surface, not a heavyweight brain. It bootstraps the pieces, relays events, and serves the combined dashboard. Don't oversell it as the intelligence of the system. The intelligence is in ClownPeanuts and the AI module.

**PingTing** is the local-first network monitoring toolkit: device discovery, baseline learning, drift detection, breach exposure checks, multi-channel alerting. It is the monitoring half of the home product and a real, hardened tool in its own right.

## The seven modules

### 1. HueyDeweyLouie (AI Deception): the headline, fully real

The v1.0.4 module and the reason most of these conversations are happening. Trains a LoRA decoy persona, ships a two-layer detection pipeline (deterministic rules + DeBERTa-v3 ONNX classifier), and emits signed, reproducible profile bundles that ClownPeanuts runs. This is where the 98.5% (66 of 67 attack turns) and zero-false-positive numbers come from. Deep, tested, and the strongest thing you sell. Everything in `01-architecture.md` and `02-numbers-and-proof.md` is about this module.

**Maturity: production-grade.** Talk about it freely, within the numbers discipline from `02`.

### 2. FunHouseForge (decoy lifecycle orchestrator): real

Stands up, activates, drifts, and tears down deception environments. In practice it is the hub the other modules hang off: it provisions the decoys and chains the supporting modules together. If a buyer asks "how do decoys get deployed and managed," this is the answer.

**Maturity: real.** Manifest-driven, working deploy/activate/reconcile workflows.

### 3. GhostCrew (synthetic activity generator): real

Makes decoys look alive. Generates realistic-looking activity against the decoys (SSH sessions, HTTP requests, DB queries) on scene-based or ambient schedules so an attacker can't tell a decoy from production by watching traffic. A real and underrated differentiator: empty honeypots are obvious; populated ones aren't.

**Maturity: real.** Concrete scene profiles (recon, harvest, lateral, persistence).

### 4. WitchBait (credential canary system): real

Plants trackable fake credentials and watches for use. Registers, rotates, and exports canary credentials (CSV/JSON/NDJSON) and records when one trips. Conceptually similar to Thinkst Canarytokens, scoped into the SquirrelOps deception fabric.

**Maturity: real.** Deterministic per-service plan generation, trip telemetry.

### 5. ADLibs (Active Directory deception): real code, narrower than the name

Seeds fake users, service accounts, and groups to detect adversary enumeration of Active Directory. Here is the honest line you must hold: **today it fabricates and tracks AD-shaped decoy objects and ingests the resulting events; it does not yet perform a live LDAP bind into a customer's production AD.** It generates the deception objects and the detection logic around them. Live AD integration is a connector that sits on top.

**Maturity: foundation.** On a call: "ADLibs generates Active Directory deception objects and the detection around them. Wiring them into your live directory is part of deployment scoping." Do not say "it seeds users directly into your production AD" as if that's a turnkey feature today.

### 6. PripyatSprings (data artifact fingerprinting): real code, narrower than the name

Fingerprints exported artifacts and tracks callbacks when they're opened outside the environment, plus applies toxicity-level transforms. The honest line: **it maintains the fingerprint registry and the callback-tracking pipeline; it does not yet generate the beaconing documents (the docx/pdf with embedded web-bugs) itself.** It tracks and transforms; the artifact-with-beacon generation is the piece that layers on.

**Maturity: foundation.** On a call: "PripyatSprings fingerprints exported artifacts and tracks when they phone home from outside your environment." Don't imply it auto-generates booby-trapped Office docs today.

### 7. DirtyLaundry (adversary behavioral profiling): real

Classifies an intruder's skill level and produces adaptive defense recommendations. Uses five weighted behavioral metrics (typing cadence, command vocabulary, tool signatures, temporal pattern, credential reuse) to score a session and bucket the actor from script-kiddie to APT, then exports the profile (native + STIX). This is the "we don't just catch them, we tell you who they are" story.

**Maturity: real.** Weighted scoring, four skill tiers, STIX export.

## How to talk about the module set

**The honest framing that wins:** "Seven deception modules across the attack surface, unified by one runtime and one intel pipeline. The AI Deception module is the deepest and the newest. The others extend the same deception-and-attribution model to credentials, Active Directory, data artifacts, and attacker profiling."

**When a buyer wants depth on a specific module:** lead with what it really does today. For ADLibs and PripyatSprings, name the foundation-vs-turnkey line yourself before they find it. Volunteering the limit builds more trust than a buyer extracting it.

**Don't list all seven as equally mature.** If you rattle off seven modules as if each were a finished product, a sharp evaluator will pick the weakest and test it, and you'll look like you don't know your own product. You do. The set is: one deep headline module, four solid supporting modules, two real foundations. That's a perfectly good story told straight.

**What's bundled in which tier** is a pricing question, covered in `04-pricing.md`. Roughly: the AI Deception module anchors the product; the supporting modules are where Constellation-tier custom rule packs and per-business-unit work live.
