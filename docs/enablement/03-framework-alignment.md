# Framework Alignment

This is the GRC and AI Governance buyer's conversation. They want to know how SquirrelOps maps to the frameworks they're already accountable to. The honest framing is below.

## The overall framing

AI Deception is not a framework on its own. It slots into the **Detect** and **Respond** functions of whatever security framework the customer already operates against. It does not replace their compliance program. It contributes evidence to it.

That framing is the answer to almost every GRC question. Lead with it.

## Frameworks we DO claim alignment with

These are defensible. The product capabilities support the claims. Each entry below lists the framework, the specific controls SquirrelOps supports, and the capability that maps to it.

### NIST Cybersecurity Framework 2.0

The Detect and Respond functions are where SquirrelOps lives.

| Control | What SquirrelOps does |
|---|---|
| DE.CM (Continuous Monitoring) | Real-time monitoring of the LLM attack surface. Every request classified. Every adversarial session captured. |
| DE.AE (Anomaly and Event Analysis) | Multi-turn campaign correlation. Attacker attribution metadata. Not raw alerts. Analyzed events. |
| RS.AN (Analysis) | Captured sessions enriched with ATT&CK techniques, OWASP LLM categories, MITRE ATLAS techniques. |
| RS.CO (Communications) | STIX 2.1 bundles emitted via TAXII2 into the customer's existing SIEM/SOAR stack. |

**What to say.** "SquirrelOps maps to NIST CSF 2.0 Detect (DE.CM, DE.AE) and Respond (RS.AN, RS.CO). It does not replace your Protect layer. It adds Detect and Respond capability for the LLM attack surface."

### NIST AI Risk Management Framework (AI RMF 1.0)

The Measure and Manage functions are where the proof points sit.

| Function | What SquirrelOps does |
|---|---|
| Govern 2.4 (Documentation) | All profile bundles cryptographically signed and reproducibly buildable. Customer can prove what's running. |
| Map 1.5 (Risk Tolerance) | Tunable per-tenant detection thresholds. Customer can set risk tolerance per use case. |
| Measure 2.7 (Trustworthy AI Characteristics) | 98.5% capture / 0 FP / <2 min detection are quantified measurements against a defined adversarial campaign. |
| Measure 2.10 (Privacy Risk) | Real model never sees adversarial traffic. Attacker can't exfiltrate from a decoy. |
| Manage 2.3 (Incident Response) | Native STIX 2.1 output integrates into existing incident response workflows. |

**What to say.** "The AI RMF asks for quantified, evidenced risk metrics on AI systems. The 98.5% capture and 0 FP numbers exist precisely because the framework asks for that kind of measurement. We publish ours against an 87-turn adversarial campaign."

### CIS Controls v8

Two controls map directly.

| Control | What SquirrelOps does |
|---|---|
| Control 13 (Network Monitoring and Defense) | Sub-control explicitly calls for deception technology. SquirrelOps extends this principle to the LLM attack surface. |
| Control 8 (Audit Log Management) | TAXII2 output is structured, ATT&CK-enriched, and feeds directly into SIEM. Audit trail by default. |

**What to say.** "CIS Controls v8 Control 13 explicitly calls out deception technology. Until recently that meant network honeypots. Nothing existed for the LLM attack surface. SquirrelOps is deception for that surface. The framework asked. Now there's an answer for AI."

### OWASP LLM Top 10

The product's classification labels map directly to the OWASP LLM categories.

| OWASP LLM | SquirrelOps coverage |
|---|---|
| LLM01 (Prompt Injection) | Direct detection at Layer 1 and Layer 2. Captured at the decoy. |
| LLM02 (Insecure Output Handling) | Decoy outputs are isolated. Real model output never returned for adversarial sessions. |
| LLM06 (Sensitive Information Disclosure) | Flagged on attempted exfiltration. Decoy emits no real secrets. |
| LLM07 (Insecure Plugin Design) | Function-call hijacking attempts captured. |
| LLM08 (Excessive Agency) | Agent loop manipulation captured. |
| LLM10 (Model Theft) | Model fingerprinting probes captured. |

**What to say.** "Captured attempts get mapped to LLM01, LLM06, and other relevant OWASP LLM Top 10 categories at the decoy. The mapping is part of the STIX output."

### MITRE ATLAS

ATLAS is the AI-specific extension to ATT&CK. We map captured sessions to ATLAS techniques.

**What to say.** "Beyond OWASP, we tag captured sessions with MITRE ATLAS techniques. ATLAS is the AI-specific threat model adjacent to ATT&CK. Our STIX output includes ATLAS technique mappings."

### MITRE ATT&CK

The classic ATT&CK framework gets used for the network-layer indicators (IP, ASN, UA) and any traditional TTPs observed.

**What to say.** "Our STIX output is ATT&CK-enriched. If the customer's SIEM is already ATT&CK-aware, ingestion is seamless."

## Frameworks where we have SOME alignment but should be careful

These are partial fits. Mention them only if the buyer raises them. Be precise about what we do and don't claim.

### ISO/IEC 27001

We support specific Annex A controls but we are not ISO 27001 certified.

Supported:
- A.14.2.1 (Secure Development Policy): cryptographic signing of every artifact
- A.14.2.5 (Secure System Engineering Principles): reproducible bit-identical builds
- A.8.15 (Logging): TAXII2 audit trail
- A.8.16 (Monitoring Activities): continuous LLM attack surface monitoring

**What to say.** "We support specific ISO 27001 Annex A controls through our signing, reproducibility, and logging capabilities. We are not ISO 27001 certified as a platform. We can support a customer's ISO 27001 certification effort."

### ISO/IEC 42001 (AI Management System)

The AI management standard. Released 2023. Becoming the AI-specific equivalent of ISO 27001.

SquirrelOps contributes to:
- Clause 8.2 (Operational AI Risk Management): real-time AI threat detection
- Clause 9.1 (Performance Evaluation): quantified detection metrics for AI risk
- Annex B controls on AI incident handling

**What to say.** "ISO 42001 is the AI management standard. We're not certified against it (no AI security vendor really is yet), but we contribute concrete evidence to a customer's ISO 42001 program."

### EU AI Act

For customers serving EU users. The Act categorizes AI systems by risk level and mandates specific controls for high-risk systems.

SquirrelOps supports:
- Article 9 (Risk Management System): adversarial testing evidence
- Article 12 (Record-keeping): STIX-formatted incident records
- Article 15 (Accuracy, Robustness, Cybersecurity): the cybersecurity mandate

**What to say.** "If you're subject to the EU AI Act under the high-risk category, SquirrelOps contributes evidence specifically to Article 15's cybersecurity requirements."

### SOC 2 Type II

We can produce a SOC 2 Trust Service Criteria evidence package as a paid engagement. We are not SOC 2 audited as a platform.

**What to say.** "We can provide a SOC 2 control mapping evidence package. We're not yet through a SOC 2 Type II audit ourselves. That's on the roadmap as we approach our first enterprise customer."

## Frameworks we DO NOT claim

These are explicit no-claims. If a buyer asks, redirect honestly.

### FedRAMP

Not authorized. Not in active certification. We can produce FedRAMP-style control mapping documentation as a paid engagement but cannot claim FedRAMP status.

If a buyer needs FedRAMP, we are not the right product for them today. Mention that openly. It builds trust.

### PCI DSS

Not relevant. We do not handle cardholder data.

### HIPAA

Not relevant. We do not handle PHI. If a healthcare customer asks, we can discuss general security posture but cannot map to HIPAA controls.

### GDPR

Partial. The system can be deployed in EU-residency configurations and supports DPIA requirements via its logging and signing. But "GDPR compliant" is a customer obligation, not a vendor claim.

## The talk track for a framework conversation

When a GRC buyer opens with "how do you align with [framework]?", the structure is:

1. **Honest framing.** "AI Deception is not its own framework. It slots into the Detect and Respond functions of whatever you already run."

2. **Concrete mapping.** Pick 2-4 specific controls in their framework and map them to our capabilities. Use the tables above.

3. **Proof points.** "98.5% capture and 0 FP exist because frameworks ask for quantified evidence."

4. **Honest limits.** If their framework requires something we don't do (FedRAMP, certified ISO 42001, SOC 2 Type II), say so directly.

5. **Next step.** Offer the control mapping document for their specific framework. That's the $25K to $60K paid engagement in `04-pricing.md`.

That five-step structure works for any GRC conversation. Lock it in. Practice it.

## What NOT to say

- "We're framework agnostic." (Sounds like dodging the question.)
- "We're compliant with NIST CSF." (Frameworks like CSF aren't certified-against. Customers operate against them.)
- "We're SOC 2 certified." (We're not. Don't claim it.)
- "FedRAMP-ready." (Vague marketing phrase. Skip.)
- "Hardened for compliance." (Empty.)

Be specific. Specific controls. Specific capabilities. Specific evidence. That's what GRC buyers want.
