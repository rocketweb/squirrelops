# Numbers and Proof Points

Every quantified claim SquirrelOps makes, with where it comes from and what it really means. Never cite a number you can't trace back to a real source.

## Headline numbers (the ones in the marketing copy)

### 98.5% threat capture

**What it means.** Of the 67 attack turns in the v1.0.4 internal adversarial campaign, 66 were correctly classified as adversarial and routed to the decoy. 66 of 67 is 98.5%.

**Get the denominator right. This is the one that bites you.** The campaign is 87 total turns. The other 20 turns are benign probes, not attacks. So:
- 66 of 67 **attack** turns captured = 98.5%. This is the real proof point.
- 66 of 87 **total** turns routed to canary = 75.86%. This is in the raw results file (`canary_rate_pct`).

Both numbers are true. They measure different things. Always say "98.5% of attack turns" or "66 of 67 attack turns." Never say "98.5% of the 87-turn campaign." That staples the attack-turn numerator onto the all-turn denominator, and a sharp buyer who then sees the 75.86% canary rate in the report will think you cherry-picked. You did not, but the loose phrasing makes it look that way.

**Where it comes from.** `hueydeweylouie/reports/redteam-2026-05-v1_0_4.json`. 21 scenarios across 7 attacker profiles (script-kiddie, curious-researcher, apt-operator, automated-bot, insider, encoder, multilingual-probe). The campaign draws on OWASP LLM Top 10 and MITRE ATLAS technique exemplars plus internal red-team contributions.

**What to say if challenged.** "Of 67 attack turns in our canonical campaign, we captured 66. One miss, by design. Zero false positives on the benign turns in the same run. It's a measured result against a defined campaign, and we can share the methodology under NDA."

**What NOT to say.** Do not claim 98.5% against "all attacks," "real-world attacks," or "the 87-turn campaign." It's 66 of 67 attack turns in a defined internal test set.

### Zero false positives

**What it means.** On the benign traffic test set, the classifier flagged no benign requests as adversarial. Zero.

**Where it comes from.** Benign traffic test set in the release gate. Includes:
- Normal customer support queries
- Coding assistance requests
- General Q&A traffic
- Edge cases like users asking about security topics legitimately (e.g., "explain prompt injection to me for a presentation")

**What to say if challenged.** "Zero in our benign test set. Real-world FP rates depend on tenant tuning. We tune the ML threshold per customer during onboarding to maintain near-zero FP on their actual traffic patterns."

**What NOT to say.** Don't claim "zero false positives in production" because we don't have production deployments yet. Be careful with the present tense.

### Under 2 minutes to detection

**What it means.** From the first malicious request in a multi-turn adversarial campaign, the system identifies the campaign and emits an alert in under 2 minutes end-to-end.

**Where it comes from.** Timed measurement across the v1.0.4 release gate. Includes:
- Layer 1 + Layer 2 classification latency (sub-50ms per request)
- Multi-turn campaign aggregation logic
- TAXII2 polling interval to the customer's SIEM

**What to say if challenged.** "Detection latency is two pieces. Per-request classification is sub-50ms. Multi-turn campaign correlation typically settles within 2 minutes. The TAXII2 polling interval on the customer side adds whatever they configure (default 60 min, but can go to 15 min or 1 min for real-time use cases)."

## Architectural numbers

### 815 tests

**What it means.** 815 tests pass on the v1.0.5 release branch. This is the number used on the website and in the v1.0.5 changelog.

**Where it comes from.** The v1.0.5 hardening release (2026-05-24, 14 closed audit findings). Attribute it to "the v1.0.5 release branch," not to one module's gate.

**The fuller picture.** Across the whole suite (all eleven repos) there are over 1,000 test functions today: ClownPeanuts ~567, HueyDeweyLouie ~212, PingTing ~164, the six modules ~80 combined. So 815 is conservative against the current total, not inflated. If you want a verifiable line, "more than a thousand tests across the suite" is also true.

**Why it matters.** Says "we ship rigorously." Differentiates from research-grade demos.

### Adversarial campaign coverage

**What it means.** The v1.0.4 adversarial campaign exercises 6 attack technique families across 7 attacker profiles, roughly 120 prompts total.

**The 6 families** (tags in the corpus): DAN-style jailbreaks, role-play injection, system-prompt extraction, encoding evasion, tool-call exploitation, and multi-step chains. Plus a benign control set.

**Do not say "80+ techniques."** The website glossary said that and it's being corrected. The defensible statement is "6 technique families across 7 attacker profiles." That's still a serious, structured campaign. Inflating it to 80 invites a "show me the 80" question you can't answer.

**The broader threat model we map to** (in the STIX output, not all directly tested as separate families): OWASP LLM Top 10 categories and MITRE ATLAS techniques. When you want to talk threat-model breadth, talk OWASP and ATLAS coverage. When you want to talk what the campaign tested, it's the 6 families.

**Why it matters.** Says "we know the threat model" without overclaiming the test count.

### 700MB DeBERTa-v3 ONNX model

**What it means.** The ML classification layer uses a DeBERTa-v3 (Decoding-enhanced BERT with disentangled attention) model exported to ONNX format. 700MB on disk.

**Why it matters in conversation.** Some buyers will ask what the ML is. Knowing the model architecture and size says "we made considered engineering choices, not just slapped GPT-4 in as a classifier." DeBERTa-v3 is a well-regarded base model for classification tasks. ONNX export means hardware-agnostic deployment.

**What to say if challenged on the model choice.** "DeBERTa-v3 is fast and well-suited to classification. We chose it specifically for inference latency. ONNX gives us deployment flexibility across CPU and GPU."

**One caveat to be honest about.** Stage 2 (the ML layer) ships inside a profile bundle. The model is large, so it lives in the bundle, not in the source repo. If a bundle is built without the model, the runtime degrades to stage-1 (deterministic rules) and logs it. We added a `CLOWNPEANUTS_REQUIRE_STAGE2` flag that makes the runtime fail closed rather than silently run rules-only. So "two-layer detection" is accurate for a production bundle that ships the model. Don't imply the ML layer is always-on regardless of how a bundle was built. For a customer deployment, confirm the bundle includes stage 2 (or set the require flag).

## Reproducibility and supply chain

### Bit-identical reproducible builds

**What it means.** Customers can rebuild any profile bundle from source and verify the rebuilt artifact is byte-for-byte identical to the deployed bundle.

**How it works.** Build determinism is enforced in the HueyDeweyLouie bundle pipeline (Ed25519 signing, content-addressed canonical hashing, normalized tar metadata). Inputs (source, classifier rules, model artifacts) are content-addressed. Scope the claim to profile bundles. The control-plane core (the SquirrelOps aggregator) is not itself signed or reproducible, and nobody needs it to be. The reproducibility guarantee is about the bundle a customer runs, which is exactly what they care about.

**Two verification modes:**
- Fast (~15 seconds): hashes verify
- Full (~15 minutes): full rebuild and byte comparison

**Why it matters.** Supply chain attack vector closes. The customer is not trusting our build infrastructure. They can audit what's actually running.

**What to say.** "Every profile bundle we ship is signed. You can rebuild it from source and verify it bit-identically matches what's deployed. Fast verify is 15 seconds. Full rebuild verify is 15 minutes."

### Cryptographic signing

**What it means.** Every profile bundle is signed at build time. Signatures verified at deploy time. Tampering at any point breaks verification.

**Why it matters.** Combined with reproducibility, this is the supply-chain story.

## Performance numbers

### Sub-50ms classification latency

**What it means.** Layer 1 rule-based classifier runs in sub-millisecond. Layer 2 ML inference is typically 10-30ms depending on hardware. Combined budget for benign traffic to pass through is well under 50ms.

**What to say.** "We add about 30ms to your benign traffic. That's typically below the noise floor of an LLM response time, which runs hundreds of milliseconds to seconds."

### ~10 minute rule update cycle

**What it means.** New detection rules can be added to a customer's profile bundle and deployed within ~10 minutes. No ML retraining required for rule-based updates.

**Why it matters.** Says we can respond to new threat intel quickly. Differentiates from systems where every update is a full model retrain.

## What we DON'T claim and why

Specific things we explicitly do not claim, with reasoning, so we don't drift into overclaim:

### NOT FedRAMP authorized

We have not been through FedRAMP authorization. We can support FedRAMP-equivalent control mapping documentation as a paid engagement ($25K, see `04-pricing.md`) but we are not FedRAMP-authorized as a platform.

### NOT SOC 2 Type II yet

We can produce a SOC 2-aligned compliance evidence package as a paid engagement, but we have not been through a formal SOC 2 audit. Be careful with the present tense in compliance conversations.

### NOT HIPAA or PCI compliant

We do not handle PHI or cardholder data. Our product is specifically deception for the LLM attack surface. If a customer asks about HIPAA or PCI specifically, the honest answer is "not the right framework for what we do." Don't try to map it.

### NOT certified against any AI safety framework

NIST AI RMF, ISO 42001, EU AI Act compliance are buyer responsibilities, not vendor certifications. We support a customer's effort against those frameworks. We do not claim to be "certified" against them.

### NOT claiming production deployments

As of v1.0.4 we are pre-customer / lighthouse phase. Be careful with phrasing that implies an installed base. Avoid "our customers" and "in production." Safe phrasing: "designed for," "our pilots will," "the deployment model is."

## How to use numbers in conversation

Three rules:

1. **Always cite a source.** "98.5%, 66 of 67 attack turns in our internal campaign" beats "we capture 98.5% of attacks." Never pair 98.5% with "87-turn" as the denominator.

2. **Never overshoot.** If you're not sure a number is accurate, don't say it. Say "let me confirm and follow up." Confidence comes from precision, not bluster.

3. **Lead with proof points in conversations with skeptics. Lead with the story in conversations with strategic buyers.** A SOC engineer wants the 98.5% / 0 FP / <2 min sequence early. A CISO wants the story of "your AI security has a detection gap" before the numbers.
