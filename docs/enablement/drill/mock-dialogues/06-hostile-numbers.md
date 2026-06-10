# Mock Dialogue: The Hostile Skeptic

The hardest call. A sharp, slightly adversarial evaluator who's decided your numbers are marketing and wants to catch you. This is the one that tests whether the corrected-numbers discipline actually holds under pressure. If you can run this, you can run anything. M is Matt, B is the buyer (a principal security engineer who has seen every vendor pitch).

---

**B:** 98.5% capture. Come on. Every security vendor I've ever met claims 99-point-something. Where's that number really from?

**M:** Fair skepticism, and you're right that the number alone is meaningless. So let me give you the denominator, which is the part vendors hide. Our adversarial campaign is 87 turns total. 67 of those are actual attack turns; the other 20 are benign probes. We captured 66 of the 67 attack turns. That's the 98.5%. If you instead divide by all 87 turns, the raw canary rate is about 76%. Both numbers are real. I lead with the attack-turn one because it answers the question that matters, of the turns that were attacks, how many did we catch.

**B:** So you're cherry-picking the favorable denominator.

**M:** I'd call it the meaningful denominator, and I just handed you the unfavorable one unprompted, which is the opposite of cherry-picking. The 76% includes benign traffic we correctly let through. Counting "didn't trap a benign probe" as a miss would be the dishonest framing. But you have both numbers now. Judge it however you want.

**B:** Hm. Okay, that's actually a reasonable answer. What about "zero false positives." Nobody has zero.

**M:** On our benign test set, zero. I'm not going to tell you zero in production, because we don't have production yet, and anyone who quotes you a production FP rate without customers is making it up. The reason the test number is zero is structural: a legitimate user never gets routed to the decoy unless we misclassify them, and the rule layer is tuned conservatively. In your pilot, FP is the single thing I'd watch hardest, and I'd want your team watching it too.

**B:** And the "80-plus techniques" I saw somewhere?

**M:** That was on our site and it was overstated. We corrected it. The real number is 6 technique families across 7 attacker profiles, roughly 120 prompts. I'd rather tell you we fixed an overclaim than defend one. If you saw "80+," that's stale.

**B:** You're volunteering a lot of things that make you look worse.

**M:** Because the alternative is you finding them after you've signed, and then you don't trust anything I told you. I'd rather you trust the true claims, which means being the one to surface the limits. We're early, we're not certified, two of our seven modules are foundations rather than finished features, and the ML detection ships in the bundle so it has to be configured right. None of that is hidden. All of it is in our own internal docs.

**B:** Most people in your seat would be arguing with me right now.

**M:** Arguing would mean I think you're wrong to push. You're not. You're doing your job, and the fact that you're pushing this hard tells me you're actually evaluating it, not brushing it off. The vendors who claim 99.9% and zero everything are the ones you should worry about.

**B:** Alright. I came in expecting to bounce you. Send me the campaign methodology and I'll have my red team look at it.

**M:** That's the right next step, and exactly what I'd want. I'll send the methodology under NDA, and if your red team wants to attack a bundle directly during a pilot, that's the best possible validation. I'd rather your team break it than take my word.

---

## What to notice

- M **never got defensive.** Every push got "fair," "reasonable," or "you're doing your job." Agreeing with the legitimacy of the challenge defuses the hostility.
- The **98.5% answer is the whole drill.** M gave the favorable number, then immediately handed over the unfavorable 76% and explained the framing. Volunteering the worse number is what flips "cherry-picking" into trust.
- M **owned the "80+" overclaim** as a corrected mistake, not a thing to defend. "We fixed an overclaim" beats spinning it.
- M **stacked the limits voluntarily** (early, uncertified, two foundation modules, ML-config) and named WHY (so the true claims stay believable). This is counterintuitive and it works.
- M **reframed the hostility as a buying signal** ("you're actually evaluating it") sincerely, not as a trick.
- Closed by **inviting the red team to attack a bundle.** The confident move against a skeptic is to hand them the weapon: "I'd rather your team break it than take my word."

## Why drill this one most

This is the call that separates "knows the product" from "can sell it." If the 98.5% denominator answer is a reflex, if volunteering the 76% feels natural, if you can stack your own limits without flinching, you've internalized the corrected-numbers discipline from `02-numbers-and-proof.md`. Record yourself doing this one. It's the bar.
