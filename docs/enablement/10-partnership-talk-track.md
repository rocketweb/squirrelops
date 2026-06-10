# Partnership Talk Track

Partnership calls are not sales calls. A partner isn't asking "does this work and what does it cost." They're asking "how do you fit with what I already do, and is there a reason for us to work together." Different question, different framing. This doc is how to run those conversations.

The core posture: **SquirrelOps is a source of high-quality threat intelligence about the LLM attack surface. Most security tooling consumes threat intelligence. That makes you a complement to almost everyone and a competitor to almost no one.** Lead with complement, always.

## The mental model: you produce, they consume

SquirrelOps' native output is STIX 2.1 attacker intel over TAXII2: who attacked, what technique, what they were after, mapped to ATT&CK and ATLAS. That output is exactly what SIEMs, SOARs, threat-intel platforms, and investigation tools are built to ingest.

So in any partnership conversation, the frame is: "You're the workbench / the pipeline / the platform. We're a new, high-signal feed for a surface you don't have coverage on yet: the LLM. We make your product better at AI security without you building an AI security product."

## Partner types and what each wants

### SIEM / SOAR platforms (Splunk, Sentinel, Chronicle, QRadar, Elastic, Tines, Torq)

**What they want:** more reasons for customers to stay in their platform; coverage of emerging surfaces; content (detections, dashboards) their customers ask for.

**Your pitch:** "Your customers are deploying LLMs and have no detection content for that surface. We emit standard STIX over TAXII2 that drops into your platform natively. We can co-build a content pack: detections, dashboards, response playbooks for AI attacks, running on your platform, fed by our deception layer."

**The ask:** a documented integration, a joint content pack, a co-marketing motion. Maybe a marketplace listing.

### Threat-intel platforms / investigation tools (OpenCTI, Flowsint, ThreatConnect, Anomali, MISP)

**What they want:** richer, differentiated intel feeds; data their users can pivot on and investigate.

**Your pitch:** "We generate a kind of intel you don't have: live, labeled LLM-attacker behavior with full session capture. Your users get a new entity type to investigate. We've already got the STIX/TAXII2 output, and for tools with an enricher model (like Flowsint), we can expose a SquirrelOps enricher so your users pivot from an attacker fingerprint straight into our capture data."

**The ask:** an enricher or connector, a STIX ingestion path, a joint "decoy capture to graph investigation" story. (This is the Flowsint conversation: SquirrelOps is the sensor, they're the workbench.)

### AI platform / MLOps vendors (model-serving, AI gateways, LLM observability)

**What they want:** a security story for their AI platform without building security themselves.

**Your pitch:** "You run AI infrastructure. Security teams are asking your customers 'how is this protected.' We're the deception-and-detection layer that answers that, sitting in front of the models you serve. You stay focused on the platform; we cover the attack surface."

**The ask:** a reference architecture, a bundled or referral motion, a deployment integration with their gateway.

### Consultancies / MSSPs / incident-response shops

**What they want:** differentiated services to sell; tooling that makes their analysts more effective.

**Your pitch:** "You're advising clients on AI risk. We're the tooling that turns that advice into deployed detection and real intel. White-label the deception layer into your AI security service, or resell."

**The ask:** a partner/reseller motion, training, deal registration.

## The one slide that works in any partnership call

Three boxes, left to right:

1. **The LLM attack surface** (the new, uncovered thing)
2. **SquirrelOps** (deception + capture + STIX/TAXII2 intel)
3. **Your platform** (SIEM / TIP / AI platform / service)

Arrow from 2 to 3. The message: "We turn an uncovered surface into a feed your platform already knows how to use."

## What NOT to do in partnership calls

- **Don't position as a competitor.** Even to a SIEM that has a deception module or a TIP that has some AI coverage, lead with "we extend you on the LLM surface," not "we replace your X." You're too early to win a competitive frame and you don't need to.
- **Don't oversell the installed base.** You're lighthouse phase. A partner who learns you have zero production customers after you implied otherwise is gone. Honest framing: "We're early and selective about partners precisely because we can co-build the integration the right way. You'd be in at the ground floor of a new category."
- **Don't commit to roadmap you can't ship.** A partner integration (an enricher, a content pack, a connector) is real engineering. Scope it as a small, bounded build (the Flowsint enricher was ~3 weeks), not a vague promise.
- **Don't give away the intel for free without thinking.** Your STIX feed is the valuable thing. Co-marketing and reference rights are fair trades early; unlimited free data redistribution is not. Keep the data relationship deliberate.

## The early-stage partnership advantage (turn the weakness into the pitch)

You're small and new. To the right partner, that's the offer, not the apology: "We're early. That means we'll build the integration with you, your way, and you get a differentiated AI security story before your competitors have one. A big vendor would make you wait in line. We'll co-build this in weeks."

Early-to-early partnerships (you + another young company) move fastest and have the most mutual upside. The logos and the joint case study from a first integration are often worth more than the direct revenue in year one. Price that accordingly: be generous on the first few co-builds to get proof points, then tighten.

## Concrete next-step menu for a partnership call

End every partnership conversation with a specific, small next step:
1. "Let's scope a basic integration. I'll send a one-page spec and a sample STIX bundle from our adversarial test suite."
2. "Let's do a joint technical session: your solutions engineer and me, 45 minutes, map the integration points."
3. "Let's draft a joint blog post once the integration works. The narrative writes itself: decoy capture to [your platform] in one workflow."

Small, concrete, low-commitment. Partnerships die from vagueness. Always leave with a dated next action.
