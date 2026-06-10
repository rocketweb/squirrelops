# SquirrelOps Architecture

## The mental model

Think of SquirrelOps as a traffic cop standing in front of your LLM endpoint. Every request gets classified in milliseconds. Benign traffic continues to your real model untouched. Adversarial traffic gets quietly diverted to a decoy that looks and behaves like the real thing.

The decoy talks to the attacker. We watch the conversation. The attacker thinks they're getting somewhere. We learn what they're trying. The real model never sees them.

## The four layers

SquirrelOps' detection pipeline runs in four layers, in order. Each layer can independently flag a request. Multi-layer signals get correlated to determine routing.

### Layer 1. Deterministic rule-based detection

Fast, rule-based classifier looking for known prompt-injection patterns, jailbreak signatures, encoding tricks (base64, leet, language-switching), and known TTP fingerprints from threat intel feeds.

- Sub-millisecond latency
- Pattern library updated per profile bundle release
- Customer-tunable per tenant
- Zero false positives is partly a property of this layer's conservative tuning

### Layer 2. ML-based classifier

A 700MB DeBERTa-v3 model exported to ONNX for fast inference. Trained to detect semantically novel adversarial intent that rule-based patterns miss.

- ~10-30ms inference latency depending on hardware
- Two-class output: benign or adversarial, with confidence
- Threshold tunable per tenant
- Catches the long tail of novel attacks

The honest detail: Layer 2 ships inside a profile bundle, not in the source repo (the model is large). A bundle built without the model runs Layer 1 only and logs a clear DEGRADED warning. The `CLOWNPEANUTS_REQUIRE_STAGE2` flag makes the runtime fail closed instead of silently dropping to one layer. So when you say "two-layer detection," it's accurate for a production bundle that ships the model. For a customer deployment, confirm the bundle includes Layer 2 or set the require flag.

### Layer 3. Decoy persona model

When a request gets classified as adversarial, the routing layer hands it off to a decoy persona model instead of the real model. The decoy is a smaller model trained to behave like the real one but to leak nothing real.

- Crafted to be plausible enough that an attacker keeps engaging
- Emits no real secrets, no real customer data, no real internal information
- Logged in full so the analyst gets the complete adversarial session

### Layer 4. Cryptographic signing and reproducibility

Every profile bundle (the rules + model + decoy persona configuration for a specific tenant) is signed at build time by the HueyDeweyLouie bundle pipeline (Ed25519 signing, content-addressed canonical hashing). Customers can rebuild any bundle from source and verify it is bit-identical to the deployed artifact.

- Two verification modes: fast (~15 seconds) and full (~15 minutes)
- Customer can independently audit what's running in their environment
- Supply chain integrity guarantee for the bundle they run

Scope note: this guarantee is about profile bundles, which is what a customer deploys and what they care about. The control-plane aggregator itself is not signed or reproducible, and the claim does not depend on it being so. Say "reproducible profile bundles," not "reproducible platform."

## Request flow (end-to-end)

A request from an attacker:

1. Hits the SquirrelOps gateway (deployed in-line in front of the LLM endpoint)
2. Layer 1 rule-based classifier runs first. Pattern match? Flag as adversarial.
3. If layer 1 is clean, layer 2 ML classifier runs. Confidence above threshold? Flag as adversarial.
4. **If benign:** request forwards to the real LLM, response returns, transaction completes. SquirrelOps adds <30ms of latency total.
5. **If adversarial:** request gets routed to the decoy persona model. The decoy engages. The session is captured in full.
6. Captured session passes through the enrichment pipeline. ATT&CK techniques labeled. OWASP LLM Top 10 categories tagged. MITRE ATLAS techniques mapped.
7. STIX 2.1 bundle assembled with indicators (IP, UA, session token), attack patterns (techniques observed), and relationships (this indicator used this technique against this decoy).
8. Bundle emitted via TAXII2. Customer's SIEM, SOAR, or threat intel platform polls and ingests.

## The seven enterprise modules

SquirrelOps is a platform, not a monolith. The platform has seven modules working together. The headline v1.0.4 module is HueyDeweyLouie (AI Deception), but the others provide deception across the rest of the attack surface.

Full details in `05-modules.md`. Names:

1. **HueyDeweyLouie** (AI Deception, v1.0.4 module). The LLM-specific layer described above.
2. **FunHouseForge.** Decoy lifecycle orchestrator. Stand-up, activation, teardown of decoys.
3. **GhostCrew.** Synthetic activity generator. Makes decoys indistinguishable from production by running scripted normal-looking activity against them.
4. **WitchBait.** Credential canary system. Plants trackable fake credentials and monitors for usage.
5. **ADLibs.** Active Directory deception. Seeds fake users, service accounts, groups into AD.
6. **PripyatSprings.** Data artifact fingerprinting. Tracks callbacks when exported files are opened outside the customer environment.
7. **DirtyLaundry.** Adversary behavioral profiling. Classifies intruder skill level. Produces adaptive defense recommendations.

Underneath those: the SquirrelOps orchestration core (manages bundle build, signing, release gate), the ClownPeanuts deception runtime (hosts the decoys, serves the TAXII2 API), and PingTing (network monitoring, baseline learning, alerting).

## Deployment topology

Three deployment models supported:

1. **In-line gateway.** SquirrelOps sits between the customer's API gateway and their LLM provider. Cleanest deployment. Adds <30ms of latency.

2. **Sidecar.** SquirrelOps runs as a sidecar to the customer's existing LLM proxy or API gateway. Useful when they have existing routing logic they don't want to replace.

3. **VPC-peered.** SquirrelOps deploys in a separate VPC, peered with the customer's. Useful for sovereignty or air-gap requirements.

All three modes produce identical STIX output. The deployment choice is a customer-environment fit decision, not a capability decision.

## Output: STIX 2.1 over TAXII2

The product's native output is the standard threat intelligence format used across the industry.

- **Collections endpoint:** `/taxii2/api/collections` lists available collections (e.g., LLM-attacks, prompt-injection-campaigns)
- **Objects endpoint:** `/taxii2/api/collections/{collection}/objects` returns the STIX bundles
- **Polling interval:** customer-configurable (default 60 minutes, can go to 15 minutes or less for real-time use cases)
- **Object types emitted:** indicators, observables, attack patterns, relationships

Customer's downstream system (OpenCTI, Splunk Enterprise Security, Microsoft Sentinel, Google Chronicle, IBM QRadar, Elastic Security, Recorded Future, ThreatConnect) polls the TAXII2 endpoint on its schedule and ingests the bundles natively.

## Why this architecture wins

A few specific reasons the architecture matters in sales and partnership conversations:

**No retraining required to update detection.** Profile bundles update independently of the ML model. New rules ship in ~10 minutes without touching the ML classifier. Customer doesn't experience model drift from defense updates.

**Per-tenant tuning.** The threshold on the ML classifier and the rule pattern library are tunable per tenant. A high-security financial customer gets tighter tuning than a marketing demo bot.

**Reproducible, signed bundles.** Every bundle the customer is running can be rebuilt from source and verified bit-identical. Supply chain attack vectors close.

**TAXII2 is the standard.** We don't ask customers to learn a new format or buy a new dashboard. We emit standard STIX 2.1 over standard TAXII2. Their existing tools work.

**The decoy doesn't lie about being a decoy.** It's not pretending to be the real model in a way that creates legal or ethical concern. It engages with the attacker in a way that captures useful intel without making false claims to the attacker.

## What to say when the architecture comes up

The deepest technical question in most sales calls is "how does it work?" The answer in 90 seconds:

"Two layers of detection. Deterministic rule-based first, ML-based second. Adversarial traffic gets routed to a decoy persona model. Real model never sees the attacker. Captured session gets enriched with MITRE ATT&CK and OWASP LLM Top 10 labels, then emitted as STIX 2.1 over TAXII2 to whatever SIEM you're running. Adds about 30ms to benign traffic. Profile bundles are signed and bit-identically reproducible so you can audit what's running."

That's the whole product, technically. Everything else is detail.
