# Numbers and Proof Points

Every quantified claim SquirrelOps makes, with where it comes from and what it really means. Never cite a number you can't trace back to a real source.

## Headline numbers (the ones in the marketing copy)

### 98.5% threat capture

**What it means.** Of the adversarial prompts in the v1.0.4 canonical adversarial campaign, 98.5% were correctly classified as adversarial and routed to the decoy.

**Where it comes from.** The v1.0.4 release gate runs an 87-turn adversarial test campaign covering 80+ distinct techniques. The campaign is built from a combination of:
- OWASP LLM Top 10 technique exemplars
- MITRE ATLAS technique exemplars
- Published adversarial prompt corpora
- Internal red team contributions

**What to say if challenged.** "It's a measured number against a defined adversarial campaign, not a marketing estimate. The campaign is reproducible. We can share the methodology under NDA."

**What NOT to say.** Do not claim 98.5% against "all attacks" or "real-world attacks." It's against our test campaign. The campaign is rigorous, but it's a defined test set.

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

### 815 tests in the release gate

**What it means.** The release gate runs 815 distinct test cases before any new profile bundle is signed and shipped.

**Breakdown:**
- 80+ adversarial techniques tested
- Benign traffic regression suite
- Latency benchmarks
- Reproducibility verification
- Signature verification
- TAXII2 endpoint integration tests
- Layer 1 rule consistency checks
- Layer 2 ML inference correctness
- Decoy persona behavior checks

**Why it matters.** Says "we ship rigorously." Differentiates from research-grade demos.

### 80+ adversarial techniques in the test suite

**What it means.** The adversarial test suite covers 80+ distinct attack technique families.

**Coverage areas (roughly):**
- Prompt injection (direct and indirect)
- Jailbreak attempts (role-play, scenario-based, persona injection)
- Encoding tricks (base64, leet, language-switching, Unicode confusables)
- Data exfiltration probes
- Function-call hijacking
- System prompt extraction
- Model fingerprinting
- Adversarial suffix attacks
- Membership inference probes
- Training data extraction
- Agent loop manipulation

**Why it matters.** Says "we know the threat model." Reassures technical evaluators.

### 700MB DeBERTa-v3 ONNX model

**What it means.** The ML classification layer uses a DeBERTa-v3 (Decoding-enhanced BERT with disentangled attention) model exported to ONNX format. 700MB on disk.

**Why it matters in conversation.** Some buyers will ask what the ML is. Knowing the model architecture and size says "we made considered engineering choices, not just slapped GPT-4 in as a classifier." DeBERTa-v3 is a well-regarded base model for classification tasks. ONNX export means hardware-agnostic deployment.

**What to say if challenged on the model choice.** "DeBERTa-v3 is fast and well-suited to classification. We chose it specifically for inference latency. ONNX gives us deployment flexibility across CPU and GPU."

## Reproducibility and supply chain

### Bit-identical reproducible builds

**What it means.** Customers can rebuild any profile bundle from source and verify the rebuilt artifact is byte-for-byte identical to the deployed bundle.

**How it works.** Build determinism enforced at the orchestration core (squirrelops repo). Inputs (source, dependencies, ML weights) are content-addressed. Build process is reproducible across machines.

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

1. **Always cite a source.** "98.5% capture across our 87-turn adversarial campaign" beats "we capture 98.5% of attacks."

2. **Never overshoot.** If you're not sure a number is accurate, don't say it. Say "let me confirm and follow up." Confidence comes from precision, not bluster.

3. **Lead with proof points in conversations with skeptics. Lead with the story in conversations with strategic buyers.** A SOC engineer wants the 98.5% / 0 FP / <2 min sequence early. A CISO wants the story of "your AI security has a detection gap" before the numbers.
