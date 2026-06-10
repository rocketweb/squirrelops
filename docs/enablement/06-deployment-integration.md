# Deployment and Integration

This is the doc that keeps you out of trouble on a technical call. When an AppSec lead, a SOC manager, or a partner's solutions engineer asks "how does this actually deploy in our stack, and how fast," you need real answers, not hand-waving. Here they are, grounded in how the product actually works.

## The one-paragraph version

SquirrelOps sits in front of your customer-facing LLM endpoints, classifies every request, routes adversarial traffic to a decoy, and emits the captured intel as STIX 2.1 over a standard TAXII2 feed that your SIEM, SOAR, or threat-intel platform polls. Benign traffic passes through to your real model with about 30ms of added latency. Nothing about the output is proprietary: it's standard STIX over standard TAXII2, so your existing tooling ingests it without a translation layer.

## Deployment topologies

Three supported models. The choice is about fitting the customer's environment, not about capability. All three produce identical intel output.

### 1. In-line gateway (cleanest)

SquirrelOps sits between the customer's API gateway and their LLM provider. Every prompt flows through it. This is the simplest mental model and the lowest-friction deployment. Adds ~30ms to benign requests.

Use when: the customer controls their own gateway/proxy layer and is comfortable putting a component in the request path.

### 2. Sidecar

SquirrelOps runs alongside the customer's existing LLM proxy or gateway rather than replacing it. Useful when they have routing logic they don't want to disturb.

Use when: the customer has an established proxy (their own, or a vendor's) and wants deception added without re-architecting the path.

### 3. VPC-peered / isolated

SquirrelOps deploys in its own VPC, peered with the customer's. The runtime and intel pipeline live in a network boundary the customer controls.

Use when: sovereignty, data-residency, or air-gap requirements rule out an in-path component in the main environment. This is the Constellation-tier deployment shape.

## The intel output: STIX 2.1 over TAXII2

This is the integration backbone and the most defensible part of the technical story. It is real and implemented in ClownPeanuts.

**The endpoints** (TAXII 2.1 compliant):
- `/taxii2/`: discovery
- `/taxii2/api/`: API root (declares `taxii-2.1`)
- `/taxii2/api/collections`: lists the intel collection (`clownpeanuts-intel`)
- `/taxii2/api/collections/{id}/objects`: the STIX objects, paginated

**What's in the bundles:** STIX 2.1 indicators (attacker IPs, user agents, session tokens), attack-patterns (techniques observed), and relationships (this indicator used this technique against this decoy). ATT&CK and ATLAS enrichment is applied.

**How the customer consumes it:** their downstream platform polls the TAXII2 endpoint on its own schedule (configurable, default 60 minutes, can drop to 15 or near-real-time). No push, no custom agent, no webhook to build. Standard pull.

## SIEM and threat-intel platform integration

The pattern is the same for every target: point the platform's TAXII2 collector at the SquirrelOps feed.

**Verified / documented:** OpenCTI. There's a documented integration where OpenCTI's TAXII2 connector polls the ClownPeanuts feed and ingests indicators, observables, attack-patterns, and relationships, alongside a MITRE ATT&CK connector. When a buyer uses OpenCTI, this is a known-good path you can speak to concretely.

**Standard TAXII2 consumers** (the customer configures their side):
- Splunk Enterprise Security (TAXII2 input)
- Microsoft Sentinel (threat-intel TAXII2 data connector)
- Google Chronicle / SecOps
- IBM QRadar
- Elastic Security
- Recorded Future, ThreatConnect, Anomali, and other TIPs

Be precise on a call: "We emit standard STIX 2.1 over TAXII2. Anything that speaks TAXII2 ingests it. OpenCTI we've integrated and documented directly. For Splunk or Sentinel, you point their TAXII2 collector at our feed." That's honest. Don't claim a pre-built, one-click connector for every SIEM. The standard-format story is strong enough without inventing turnkey connectors that don't exist yet.

**Custom / non-TAXII targets** (PagerDuty, Opsgenie, Jira, ServiceNow, in-house SOAR): these are bridges built during implementation. Priced as connectors in `04-pricing.md`. Don't promise them as included.

## Latency and footprint

- Layer 1 (deterministic rules): sub-millisecond.
- Layer 2 (ML classifier): ~10-30ms per request depending on hardware.
- Total added latency on benign traffic: about 30ms, which is below the noise floor of typical LLM response times (hundreds of ms to seconds).
- The 700MB ML model loads once at pack-load time (~1-2s), not per request.

When asked "will this slow down our model?": "About 30 milliseconds on clean traffic. Your model takes hundreds of milliseconds to respond. Users won't perceive it."

## Cloud and environment support

- Runs on AWS, Azure, GCP, on-prem, or hybrid.
- Container-based; deployable via the customer's orchestration (the control plane ships a docker-compose; production deployments are scoped per environment).
- Air-gapped deployment is supported and is a Constellation-tier uplift (priced separately, see `04-pricing.md`).
- The reproducible, signed profile bundles mean the customer can verify exactly what's running in any environment, which is the answer to "how do we know what you deployed in our cloud."

## What the customer provides (deployment prerequisites)

Know this list. It's what a serious buyer wants to hear because it tells them the integration is real and bounded:

1. A place to run the component (in-path gateway, sidecar, or peered VPC).
2. Access to route their LLM endpoint traffic through it.
3. A TAXII2-capable SIEM/TIP, or a target for a custom bridge.
4. The use cases and model(s) in scope, so the profile bundle gets tuned to them.
5. A security-team point of contact for the threat-model and tuning sessions.

## Honest limits to state plainly

- **No universal one-click SIEM connector.** Standard TAXII2 + a documented OpenCTI path. Everything else is "point your collector at our feed" or a scoped bridge.
- **Stage-2 ML ships in the bundle.** Confirm a deployment's bundle includes it (or set `CLOWNPEANUTS_REQUIRE_STAGE2` to fail closed) so "two-layer detection" is true for that install. See `01-architecture.md`.
- **Auth must be turned on before exposure.** The runtime can serve its intel feed unauthenticated for local use; a real deployment enables auth and tokens. (We added a loud startup warning when it's off.) Don't describe the feed as secure-by-default; describe it as secured during deployment.

## The deployment timeline to quote

- Pilot: profile bundle scoped and deployed against a single endpoint in 4-6 weeks.
- Mission (production): 6-8 weeks from kickoff to the customer owning it.
- Constellation: 8-12 weeks white-glove, multi-environment.

These match the pricing tiers in `04-pricing.md`. When a partner or buyer asks "how fast can we be live," anchor on those, then narrow once you know their topology and SIEM.
