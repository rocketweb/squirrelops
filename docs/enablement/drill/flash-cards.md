# Flash Cards

Active recall is what builds live-call fluency. Passive reading and Notebook LM listening prime you; retrieval practice encodes it. This deck is the retrieval engine. Use it daily.

The cards live in `flash-cards.tsv` (94 cards). That file is the single source of truth, formatted for direct import into Anki or any SRS tool. Don't maintain a second copy of the cards in prose; edit the TSV.

## Import into Anki (5 minutes, once)

1. Install Anki (free desktop app, ankiweb.net) and the mobile app if you want to drill on the go.
2. File → Import → choose `flash-cards.tsv`.
3. The file carries its own header directives (`#separator:tab`, `#columns:Front Back`, `#tags:squirrelops-enablement`), so Anki auto-detects tab separation and the two fields. Confirm Field 1 = Front, Field 2 = Back.
4. Pick or create a deck ("SquirrelOps Prep"). Import.
5. Done. 94 cards, tagged `squirrelops-enablement`.

When you update the corpus, edit the TSV and re-import (Anki updates existing cards by content, adds new ones).

## What's in the deck (94 cards)

Roughly grouped:
- Positioning and the pitch
- Numbers and proof (the 98.5% denominator trap especially)
- Architecture and the detection pipeline
- The seven modules (with the honest ADLibs/PripyatSprings lines)
- Competitive landscape and the EchoLeak proof point
- Framework mappings
- Pricing and tiers
- Deployment and integration
- Objections and the pressure reflexes
- Buyer personas
- Partnership posture

## How to drill (the part that matters)

**Daily, 10 minutes.** Anki schedules the cards. Do the day's review. Answer each card OUT LOUD before flipping it. Speaking the answer is the rep that transfers to a live call. Reading it silently does not.

**Grade honestly.** If you hesitated or hedged, mark it "Again" or "Hard." The whole value of spaced repetition is that it resurfaces the ones you're shaky on. Gaming your own grades wastes the tool.

**The numbers cards are non-negotiable.** The 98.5%-denominator card, the "what NOT to claim" cards, the latency card. These are the ones a sharp buyer tests and the ones where a fumble costs credibility. Over-learn them.

**Two passes for objection cards.** First pass: can you give the core answer? Second pass: can you give it in two sentences without rambling? Live, the brevity is half the battle.

## The confidence checkpoint

You're ready for a live call when you can do this, recorded on your phone, without notes:

1. The 30-second pitch, clean, in one take.
2. The 98.5% denominator explanation, volunteering the 76%.
3. Three objections answered in under 20 seconds each: "why not Lakera," "you have no customers," "98.5% of what."
4. Name your top three honest limits without flinching (pre-customer, not certified, two modules are foundations).

Record it. Listen back. If you stumble, that's the card to drill tomorrow. When all four are smooth, you're ready. That's the bar, not "I read the docs."

## Why this beats listening alone

Notebook LM's audio overview is a warm-up. It's you listening to two AI hosts talk. A live call is you generating language under pressure while someone pushes back. The flashcard drill is the closest thing to that pressure you can practice solo: a prompt, a beat, your answer out loud, a pass/fail. Do the audio for priming. Do the cards for fluency. Do the mock dialogues (in `mock-dialogues/`) for the flow between them.
