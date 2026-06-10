# Buyer Personas

Five people show up in these deals. Each cares about something different, fears something different, and will push on something different. If you give the CISO pitch to a SOC engineer, you lose the room. This doc is how to tell who you're talking to and what to lead with.

The decision-makers are the CISO, the GRC/AI Governance lead, and sometimes the Head of AppSec. The technical evaluators are the SOC Manager and the Head of AI Platform. Both groups have to be satisfied: the decision-makers say yes, the evaluators say "this won't break anything." A deal dies if either group is unconvinced.

## How to sense which one you're talking to

Listen for the first thing they probe on:
- Talks about risk, board, budget, "the business" → **CISO**
- Talks about frameworks, audits, evidence, "how do we prove" → **GRC / AI Governance**
- Talks about the application, the pipeline, how it integrates → **Head of AppSec**
- Talks about alerts, noise, their SIEM, on-call → **SOC Manager**
- Talks about latency, the model, the deployment, "will this break our app" → **Head of AI Platform**

When in doubt, ask: "So I pitch this right, what's your role in the AI security decision here?" It's a fair question and it tells you everything.

---

## 1. CISO (economic buyer, risk owner)

**Owns:** AI security risk at the executive level. Signs or kills the deal.

**Fears:** A breach on their watch via the new AI surface they greenlit. Looking negligent to the board for deploying AI without controls. Spending on security theater that doesn't reduce real risk.

**Lead with:** The detection-gap story. "Your team has a great Protect layer for AI. Identity, rate limits, guardrails. Now ask them what's in the Detect column for your LLMs. If the answer is 'we'll see it in the logs,' that's forensics, not detection." Then the outcome: labeled attacker behavior, quantified, into the SIEM they already trust.

**They'll push on:** ROI, whether this is a real category or a nice-to-have, references, and whether you're a viable vendor (you're early; be honest about lighthouse phase and turn it into "you'll have our full attention and influence the roadmap").

**Trap to avoid:** Going deep technical. A CISO doesn't want the four-layer pipeline. They want "real risk, reduced, measurably, into your existing stack." Hand the technical depth to their evaluators.

**The line:** "Logs tell you what happened. Deception tells you who did it, with what, and why, while it's still happening."

---

## 2. GRC / Head of AI Governance (compliance owner)

**Owns:** Framework alignment and audit defensibility for AI systems. Increasingly the person who can block an AI deployment until it's "governed."

**Fears:** An audit finding. The EU AI Act, ISO 42001, or NIST AI RMF gap that has no evidence behind it. Being the person who signed off on an AI system with no detection story.

**Lead with:** The honest framing from `03-framework-alignment.md`. "AI Deception isn't its own framework. It slots into the Detect and Respond functions of whatever you already run." Then map 2-3 of their specific controls (NIST CSF DE.CM, AI RMF Measure, CIS Control 13) and offer the quantified evidence: 66 of 67 attack turns, zero false positives, published against a defined campaign.

**They'll push on:** What you DON'T have. SOC 2, FedRAMP, ISO certification. Answer straight: you support their program with evidence; you're not certified against those yet; you can produce a control-mapping package as an engagement. Honesty here is the entire sale with this persona.

**Trap to avoid:** Claiming compliance you don't have. This persona's whole job is catching that. One overclaim and you're done. Use the "what NOT to claim" discipline from `02` and `03` religiously.

**The line:** "The AI RMF asks for quantified, evidenced risk metrics. We publish ours. Most AI security can't show you a number."

---

## 3. Head of AppSec (technical champion, often the door-opener)

**Owns:** The technical security of the application, including the LLM integration. Often the person who first found you and brought you in.

**Fears:** Adding a tool that creates more work than it saves. A component in the request path that becomes an incident. Something that doesn't actually integrate and becomes shelfware.

**Lead with:** Architecture and fit. The four-layer pipeline, the ~30ms latency, the STIX/TAXII2 output into their existing stack, the reproducible bundles they can audit. This persona respects precision and is turned off by marketing.

**They'll push on:** Latency, failure modes, what happens when the classifier is wrong, the stage-2 model question, false positive handling, deployment topology. Have `01-architecture.md` and `06-deployment-integration.md` cold.

**Trap to avoid:** Bluffing on a technical detail. If you don't know, say "I don't know that exactly, let me get you the precise answer." This persona forgives "let me confirm" and never forgives a confident wrong answer.

**The line:** "Standard STIX over standard TAXII2. No new dashboard, no translation layer. Your existing playbooks start working against attacks on your AI."

---

## 4. SOC Manager (operational evaluator)

**Owns:** Day-to-day detection and response. Lives in the SIEM. Manages on-call.

**Fears:** More noise. Another alert source that cries wolf and burns out the team. A feed that doesn't map to their workflow.

**Lead with:** Signal quality. Zero false positives on benign traffic. Every alert is a real adversarial session with attribution, not a probabilistic guess. It lands in the SIEM they already run, enriched with ATT&CK so it fits their existing playbooks.

**They'll push on:** Alert volume, false-positive rate in practice, how it fits their triage flow, whether it adds on-call burden. The zero-FP story is your strongest card here; pair it with per-tenant tuning.

**Trap to avoid:** Overselling automation. Don't imply it runs their SOC. It feeds their SOC high-quality signal. That's the win they want.

**The line:** "Deception has a structural advantage on false positives. A legitimate user never talks to a decoy. If something's in the decoy, it's hostile. That's why the FP number is what it is."

---

## 5. Head of AI Platform / AI Engineering (the gatekeeper who can veto)

**Owns:** The LLM deployment itself. The pipeline, the models, the serving infrastructure.

**Fears:** Anything in the request path that adds latency, breaks under load, or complicates their deployment. Security bolting something onto their system that they then have to babysit.

**Lead with:** Minimal footprint. ~30ms, loads once, benign traffic passes through untouched, three deployment topologies so it fits how they already run. The real model never even sees adversarial traffic, so their system stays clean.

**They'll push on:** Latency (again), throughput, what happens at scale, failure behavior (does it fail open or closed), how it affects their SLOs.

**Trap to avoid:** Treating them as a rubber stamp. This persona can quietly kill a deal by telling the CISO "it'll add latency and risk to our serving path." Win them early by respecting that the LLM is their system and you're a careful guest in it.

**The line:** "Your model is your system. We sit in front of it, add about 30ms to clean traffic, and route the attackers away before they ever reach it. We're a guest, not a tenant."

---

## Multi-stakeholder calls

You'll often face several at once. The move:
1. Open with the CISO-level frame (the detection gap) so the room agrees on the problem.
2. Then explicitly hand each evaluator their piece: "On integration, here's what your AppSec and platform teams will care about. On evidence, here's what governance needs."
3. Name the room. "Sounds like we've got security leadership, governance, and platform here. Let me make sure each of you gets what you need."

That signals you understand enterprise buying and you're not just pitching one slide to everyone. It also surfaces the silent veto (usually the AI Platform lead) before it kills the deal offline.
