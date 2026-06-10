# Objections and Answers

This is the doc that wins or loses deals. Knowing the product gets you in the room. Handling the hard question under pressure is what closes. Read this one most. Drill it out loud until the answers are reflexes, not recitations.

Every answer below is built on the corrected numbers (`02-numbers-and-proof.md`) and the real competitive picture (`07-competitive-landscape.md`). None of it requires you to bluff. That's the point: you can hold every one of these positions honestly.

## How to handle an objection under pressure (read first)

The objection itself is rarely the hard part. The hard part is the social moment: a skeptical person pushing on you, live, and the urge to over-talk, get defensive, or invent an answer. Three rules:

1. **Pause. Then answer in two sentences, then stop.** The instinct under pressure is to keep talking until you've buried the objection. It reads as nervous. Answer crisply and let silence sit. The confident move is the short answer followed by quiet.

2. **Agree with the true part first.** Most objections contain a real point. "You're right that we're early." "You're right that a guardrail catches a lot." Concede it, then pivot. Fighting the true part makes you look like you're not listening. Conceding it makes the pivot land.

3. **When you don't know, say so, then bridge to what you do know.** "I don't know that exact number off the top of my head. What I do know is X. I'll get you the precise figure by tomorrow." This never loses a deal. A confident wrong answer can lose it permanently, especially with the AppSec and GRC personas whose whole job is catching that.

Now the objections.

## Credibility and numbers

**"98.5% sounds made up. 98.5% of what?"**
This is the one to nail, because the honest answer is your strongest. "Of 67 attack turns in our internal adversarial campaign, we captured 66. That's 98.5%. The full campaign is 87 turns including benign probes, and the raw canary rate across all 87 is about 76%. I'm giving you the attack-turn number because that's the meaningful one: of the turns that were actually attacks, we caught all but one. Zero false positives on the benign turns. I'll share the methodology under NDA." Volunteering the 76% before they find it is what makes you credible. You're the vendor who shows both numbers.

**"How do we know your numbers are real? Every vendor claims 99%."**
"Fair. Two things. One, it's a measured result against a defined, reproducible campaign, not a marketing estimate, and we'll walk your team through the methodology. Two, watch what we DON'T claim: we don't say 98.5% against real-world traffic, we don't claim production deployments we don't have, and we tell you the ML layer ships in the bundle and can be configured. A vendor inflating numbers doesn't volunteer its own limits."

**"You don't have any customers."**
Agree first. "You're right, we're pre-customer. We're in lighthouse phase." Then turn it: "That means two things for you. You get our full attention and you shape the roadmap, and you get lighthouse pricing in exchange for being a reference. A year from now this costs more and you're one of fifty. Right now you're one of five." Never apologize for being early. Price it as access.

## Competitive

**"Why not just use Lakera / a guardrail?"**
"Keep your guardrail. We're not a replacement for it. Guardrails block prompts at the door and assume the block holds. EchoLeak, the zero-click injection that beat Microsoft's own classifier in 2025, is the proof they don't always hold. We're the layer that catches the attacker who got past the filter, routes them into a decoy, and tells you how they got in. Prevention and detection. Run both."

**"Isn't this just a honeypot?"**
"Same proven idea, new surface. Network honeypots have been a trusted enterprise category for a decade. Nobody had built one for the LLM attack surface. And ours doesn't just sit there. It engages the attacker with a decoy model and emits labeled threat intel to your SIEM. It's deception plus attribution, for AI."

**"What about Acalvio? They do AI deception."**
"Close, and worth distinguishing. Acalvio uses an LLM to generate a convincing fake server. We deploy a decoy LLM to catch attacks on your real LLM. They make a honeypot with AI. We make a honeypot that is an AI. Different problem."

**"Who else does this? If it's a real need, someone bigger is doing it."**
"No commercial product we've found. It's been academic research until now. That's both the opportunity and the honest risk: we're early in a category the big guardrail vendors will eventually move into. Getting in now means you help shape it instead of buying whatever they bolt on in two years."

## Technical

**"Will this add latency or break our model?"**
"About 30 milliseconds on clean traffic. Your model takes hundreds of milliseconds to respond, so users won't perceive it. And the real model never even sees adversarial traffic, we route that away before it arrives, so your serving path actually stays cleaner."

**"What's your real false-positive rate in production?"**
Be honest about scope. "Zero on our benign test set. We don't have production numbers yet because we're pre-customer, I won't pretend otherwise. But deception has a structural FP advantage: a legitimate user never talks to a decoy, so anything in the decoy is hostile by construction. We also tune the ML threshold per tenant during onboarding to hold near-zero on your actual traffic."

**"What if the attacker realizes it's a decoy?"**
"Two answers. One, by the time they suspect it, they've already revealed technique, tooling, and intent, which is the whole point. We got the intel. Two, GhostCrew populates decoys with realistic activity so they don't look empty, which is the usual tell. We designed against exactly this."

**"Can't an attacker just avoid the decoy?"**
"To avoid it they'd have to know which requests get routed and why, which is our classifier logic, not exposed to them. From their side it's an LLM endpoint that sometimes behaves like a vulnerable target. The routing is invisible. And if they probe carefully enough to map it, that probing is itself captured signal."

**"Does it see our real user prompts? What about privacy?"**
"Benign traffic passes through to your model; we classify it but the deception path only engages adversarial traffic. The decoy emits no real data because it's not connected to your real systems. For data residency, we deploy in-region or in a VPC you control. Specifics depend on your topology, and I'll get your team the exact data-flow diagram."

**"The ML detection layer, is it always on?"**
Honest answer, it's a strength when handled right. "The ML layer ships inside the profile bundle. For a production bundle that includes it, two-layer detection is always on. We added a flag that makes the runtime refuse to start if it's supposed to have the ML layer and can't load it, so it fails loudly instead of silently dropping to rules-only. For your deployment we confirm the bundle includes it. I'd rather tell you how that works than pretend it's magic."

## Commercial

**"This is expensive."**
"Compared to what?" Let them anchor, then respond. Usually they're comparing to a guardrail. "Lakera is priced like an API filter because that's what it is. We're a deception platform that produces threat intelligence. Different category, different value. The closer comparison is enterprise deception like Acalvio, and we're priced in that neighborhood." See `04-pricing.md` for the full pushback playbook.

**"We could build this ourselves."**
"Maybe. Here's what you'd be building: a two-layer detection pipeline, a trained decoy model, a reproducible signed-bundle system, an 800-plus-test release gate, and a STIX/TAXII2 intel pipeline. We did it over a year. You could in twelve to eighteen months. What's that engineering time worth, and what's the exposure while you build it?"

**"We don't have budget this year."**
"When does your fiscal year open?" Then build the pipeline for that cycle. Don't discount to force a deal into the wrong quarter. Offer the pilot as a smaller entry: "If it's a budget-size question, the pilot is a fraction of a full deployment and credits fully toward year one."

## Compliance and vendor risk

**"Are you SOC 2 / FedRAMP / ISO certified?"**
Straight answer, every time. "Not yet. We're pre-certification and I won't pretend otherwise. We can produce a control-mapping evidence package for your framework as part of an engagement, and we support your audit. If you need a FedRAMP-authorized platform today, we're not that, and I'd rather tell you now than waste your procurement cycle." Honesty with the GRC persona is the entire sale. See `03-framework-alignment.md`.

**"Why should we trust our security to an early-stage vendor?"**
"Because of what we deploy, not who we are. Every profile bundle is signed and bit-identically reproducible. You can rebuild it from source and verify exactly what's running, no trust in us required for the artifact. The real model stays untouched. We're a careful guest in front of your system, and you can audit the guest."

**"What happens to us if you go under?"**
"Fair question for any early vendor. The runtime and core are source-available, so you're not locked into a black box that disappears. The intel output is standard STIX/TAXII2, not a proprietary format you'd have to rip out. We're built so that betting on us early isn't betting your security on our survival."

**"How deep is ADLibs / the AD deception, really?"**
Hold the honest line from `05-modules.md`. "Today ADLibs generates Active Directory deception objects and the detection logic around them. Wiring those into your live directory is part of deployment scoping, not a turnkey switch yet. I'd rather you know exactly what's built than find out later. The AI Deception module is the deep, finished one; ADLibs is a solid foundation we extend per deployment."

## The objections you should welcome

When a buyer pushes hard on numbers, limits, or "who else does this," that's an engaged buyer, not a hostile one. The tire-kickers ask nothing. Treat hard questions as buying signals and answer them with the calm of someone who has nothing to hide, because, if you stay inside these answers, you don't.

## The "I genuinely don't know" script

You will get asked something not in any doc. The move, memorized:

"That's a good question and I don't want to guess at it. What I can tell you is [closest relevant thing you do know]. Let me get you the precise answer and follow up by [specific day]."

Then actually follow up. The follow-up email with the right answer is often a stronger trust signal than knowing it live would have been. Not knowing is fine. Inventing is fatal. Deferring with a dated commitment is professional.
