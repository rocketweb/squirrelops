# Mock Dialogue: Curious CISO

A friendly, exploratory first call. The CISO is interested but not yet sold. This models opening with the problem, staying at altitude, and landing a pilot. M is Matt, B is the buyer.

---

**B:** So a colleague forwarded me your post. We're rolling out a couple of customer-facing AI assistants this quarter. Tell me what you do.

**M:** Sure. Quick question first so I aim this right: as you roll those out, what's your team's plan for detecting when someone attacks them?

**B:** Honestly? We've got guardrails on the input. Beyond that, I'm not sure we have one.

**M:** That's the gap we fill, and it's the common one. Most teams have a good Protect layer for AI. Guardrails, rate limits, filters. The Detect column is usually empty. If someone jailbreaks your assistant or prompt-injects your agent, would you know?

**B:** Probably after the fact, in the logs.

**M:** Right. That's forensics, not detection. What we do is sit in front of your assistant, and when a request looks adversarial, we route it into a decoy instead of your real model. The attacker thinks they're getting somewhere. We capture what they tried, what tooling they used, what they were after, and we send that to your SIEM as labeled threat intel. Your real model never sees them.

**B:** So it's a honeypot for the LLM.

**M:** Exactly that. Same proven idea as network honeypots, which your team probably already trusts, applied to the AI surface that just became critical. The difference from a guardrail is we don't try to block the attacker. We let them in, to a decoy, and learn from them.

**B:** What's the catch? This sounds early.

**M:** It is. We're pre-customer, in what I'd call lighthouse phase. I'll be straight with you about that the whole way. The upside for you is you'd get our full attention, real influence on the roadmap, and lighthouse pricing in exchange for being a reference. The honest downside is we don't have a wall of logos yet.

**B:** I appreciate the candor. Does it slow the assistant down?

**M:** About 30 milliseconds on clean traffic. Your model takes hundreds of milliseconds to respond, so users won't feel it. And clean traffic just passes straight through.

**B:** What kind of results do you have?

**M:** On our internal adversarial campaign, we captured 66 of 67 attack turns, so 98.5%, with zero false positives on the benign traffic in that run. I'll be precise: that's against a defined test campaign, not production, because we don't have production numbers yet. We can walk your team through the methodology under NDA.

**B:** That's a strong number. Okay. What would a next step look like?

**M:** A pilot. Four to six weeks, one of your assistants, scoped to your actual use cases. We deploy the decoy, wire the detection into one SIEM, and your team runs adversarial traffic against it and judges the results. It's a fixed fee, and it credits fully toward year one if you move forward.

**B:** Let me get our AppSec lead on the next call. They'll have harder questions than me.

**M:** Perfect, that's exactly who should pressure-test it. Send me a couple of times and I'll come ready for the technical depth.

---

## What to notice

- M opened with a **question**, not a pitch. It surfaced the gap in the buyer's own words ("I'm not sure we have one"). Now the problem is theirs, not Matt's.
- M **stayed at altitude.** No four-layer pipeline, no DeBERTa. A CISO doesn't want it. M handed the depth to the AppSec lead at the end.
- M **volunteered the limits** (pre-customer, defined-test-not-production) before being asked. That candor is what earned "I appreciate the candor."
- M **named the number precisely** (66 of 67 attack turns) and immediately scoped it (not production). No overclaim.
- M **closed on a concrete next step** (pilot, and bring AppSec). Every good call ends with a dated, specific action.
