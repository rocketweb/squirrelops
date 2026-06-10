# Mock Dialogue: Partnership Call (SIEM / Threat-Intel Vendor)

Not a sales call. The partner asks "how do you fit with us," not "does it work and what's it cost." This models the complement-not-compete posture and turning "you're early" into the offer. M is Matt, B is the partner's BD/solutions lead.

---

**B:** We run a threat-intel platform. Our users do graph-based investigations. Someone flagged you as a possible feed. What's the fit?

**M:** Clean one, I think. Here's the frame: you're the workbench, we're a sensor. We generate a kind of intel you don't have today, live LLM-attacker behavior with full session capture, attacker fingerprints, techniques, intent. Your users get a new entity type to investigate. We already emit standard STIX 2.1 over TAXII2, so the ingestion path mostly exists.

**B:** A lot of feeds claim to be differentiated. What's actually new here?

**M:** Most threat intel is about networks and endpoints. Nobody's feeding you intel about the LLM attack surface, because almost nobody's instrumented it. Your customers are all deploying AI assistants right now and have zero coverage on that surface in your tool. We're the feed that lights it up. That's the differentiation: not better network intel, a whole surface you don't cover yet.

**B:** How would the integration actually work?

**M:** Two shapes. The simple one: you point your TAXII2 collector at our feed and ingest the STIX. The richer one, if your tool has an enricher or connector model, we expose a SquirrelOps enricher so your users pivot from an attacker fingerprint straight into our capture data, in their graph. We scoped a version of that with another tool recently at about three weeks of engineering.

**B:** You're pretty small. Why would we prioritize building with you over a bigger name?

**M:** That's exactly the offer, not the apology. A big vendor makes you wait in line and build to their spec. We'll co-build this with you, your way, in weeks, and you get a differentiated AI security story before your competitors have one. Early-to-early moves fast. The logos and the joint case study are worth more to both of us right now than the contract value.

**B:** What do you want out of it?

**M:** A documented integration, and a joint story we both market. A blog post that writes itself: decoy capture to investigation in your tool, one workflow. I'm not looking to give the intel away wholesale, the feed is the valuable thing, but co-marketing and a reference are a fair trade to prove the integration.

**B:** What would you need from us to start?

**M:** Honestly, a 45-minute technical session, your solutions engineer and me, to map the integration points. I'll come with a one-page spec and a sample STIX bundle from our adversarial test suite so it's concrete, not hand-wavy.

**B:** That's a low-enough lift. Let me set it up.

**M:** Perfect. One thing I'll be upfront about: we're pre-customer, lighthouse phase. I'd rather you hear that from me than discover it. For a partner it's actually a feature, you help shape the integration. But I won't imply an installed base we don't have.

**B:** Noted, and appreciated. I'll get the technical session on the calendar.

---

## What to notice

- M framed it as **complement, never competitor**, even though the partner is a threat-intel tool with some adjacent coverage. "You're the workbench, we're the sensor."
- M answered **"what's actually new"** with the surface argument, not feature bragging. The differentiation is coverage of a surface, not "better than your X."
- M turned **"you're small"** into the pitch ("that's the offer, not the apology") and gave a concrete proof of feasibility (the ~3-week enricher).
- M **protected the data relationship** ("not looking to give the intel away wholesale") while being generous on co-marketing. Early partnerships trade reference rights, not the crown jewels.
- M **volunteered the pre-customer status** even in a partnership context, and reframed it as a partner benefit without overclaiming.
- Closed on the **smallest possible next step** (45-min technical session + a concrete artifact). Partnerships die from vagueness; M left with a dated, bounded action.
