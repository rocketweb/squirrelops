# Mock Dialogue: GRC / AI Governance

This is the Matthew B. conversation made real. The compliance owner. Honesty is the entire sale here, especially about what you DON'T have. M is Matt, B is the buyer.

---

**B:** I lead AI governance. My concern is the gap between how fast we're deploying AI and the frameworks that should govern it. Where does your AI Deception layer fit?

**M:** Straight answer: it isn't its own framework, and I'd be suspicious of anyone who told you it was. It slots into the Detect and Respond functions of whatever you already run. It contributes evidence to your program; it doesn't replace it.

**B:** Okay, that's a better start than most. Be specific. We map to NIST CSF and we're building toward the AI RMF.

**M:** Then two concrete hooks. NIST CSF, we map to DE.CM and DE.AE on the Detect side, continuous monitoring of the LLM attack surface and anomaly analysis with attribution, and RS.AN and RS.CO on Respond, because the captured intel flows as STIX into your existing response workflow. For the AI RMF, the Measure and Manage functions: the framework asks for quantified, evidenced risk metrics on AI systems, and that's exactly why we publish ours.

**B:** What metrics?

**M:** 66 of 67 attack turns captured in our internal adversarial campaign, zero false positives on the benign turns. Most AI security can't hand you a number like that. The AI RMF practically demands one.

**B:** Here's the one that matters to me. Are you SOC 2? ISO 42001? Anything I can put in front of an auditor?

**M:** No, and I won't dress it up. We're not SOC 2 audited, not ISO certified, not FedRAMP authorized. What we can do is produce a control-mapping evidence package for your specific framework as an engagement, and the product itself generates audit-relevant artifacts: every profile bundle is cryptographically signed and reproducible, so you can prove exactly what was running. But if you need a certified platform today, I'm not going to pretend we're it.

**B:** I'll be honest, that candor is rarer than it should be. Most vendors fudge this.

**M:** Fudging it with you specifically would be suicidal. Catching that is your whole job. And if we overclaim once, you stop believing the true things too.

**B:** There's also CIS, some of our controls map there.

**M:** Then you've already got my favorite one. CIS Controls version 8, Control 13, Network Monitoring and Defense, explicitly calls for deploying deception technology. It's been in the framework for years. Until now that meant network honeypots, and there was nothing for the LLM surface. We're the answer to a control your framework already asks for, just for AI.

**B:** That's a useful framing for my internal case. What about the EU AI Act? We have EU users.

**M:** For high-risk systems under the Act, we contribute specifically to Article 15, the cybersecurity requirement, with adversarial-testing evidence and STIX-formatted incident records. I'd flag that "EU AI Act compliance" is your obligation as the deployer, not something I can certify for you. We're evidence into your case, not a compliance stamp.

**B:** Understood, and correctly stated. Can you send me a control-mapping draft against NIST CSF and AI RMF? I want to socialize it internally.

**M:** Yes. I'll send a draft mapping against both, clearly marked as draft, this week. And I'll flag in it the controls where we contribute evidence versus the ones that are your obligation, so it's honest on its face.

---

## What to notice

- M led with the **honest framing** ("it isn't its own framework") and won the room in one sentence. GRC buyers are braced for overclaim; disarming that immediately is the whole move.
- M mapped **specific controls to specific capabilities**, not vague "we align with NIST." Specificity is credibility with this persona.
- The **"are you certified" moment is the entire call.** M said no, plainly, listed exactly what's missing, and offered the real alternative (evidence package, signed artifacts). That straight "no" sells harder than a fudge.
- M made the **CIS Control 13** point land as the buyer's internal ammunition ("useful framing for my internal case"). Giving the champion a tool to sell upward is gold.
- M was **precise about the EU AI Act limit** (deployer obligation, not a vendor cert). Even when the buyer offered an opening, M didn't overreach.
- Closed with a **dated, honestly-labeled deliverable.** Note "clearly marked as draft" and "flag obligation vs evidence." The honesty is structural, not just verbal.
