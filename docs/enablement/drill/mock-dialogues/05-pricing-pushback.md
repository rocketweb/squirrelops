# Mock Dialogue: Pricing Pushback

Getting to a number and holding it. The buyer likes the product and now wants to compress the price. This models discovery-before-quoting, anchoring, and the "compared to what" move. M is Matt, B is the buyer (a VP Security with budget).

---

**B:** We like it. What does it cost?

**M:** Before I quote you a number that's probably wrong, let me ask three things so it's actually right. How many LLM endpoints are in scope, roughly what query volume, and is this a single environment or multi-region?

**B:** Two assistants to start, call it five million queries a month, single AWS region.

**M:** That puts you squarely in our Mission tier. That's $150K to $250K a year for the platform, plus a one-time implementation of $50K to $100K that covers the deployment, the threat modeling, the SIEM integration, and getting your team to where they own it. Where you land in the range depends on the integration specifics.

**B:** That's a lot more than Lakera quoted us.

**M:** It is. And it's a fair thing to raise, so let me be direct about why. Lakera is priced like an API filter because that's what it is, you pay for prompts inspected. We're a deception platform that produces threat intelligence, full attacker capture into your SIEM. Different category, different value. The honest comparison isn't a filter, it's enterprise deception like Acalvio, and we're priced in that neighborhood. You can also run both: keep Lakera as your filter, we're the detection layer behind it.

**B:** Still. Can you come down?

**M:** Here's how I think about that. I'll move on the implementation fee and on year one, because getting you live and successful is what matters. I won't discount the platform list, because that sets your renewal price and I'm not going to start our relationship by teaching you the real number is lower. What I can offer that's real: we're early, and for our first handful of customers there's a lighthouse arrangement, 30 to 50 percent, in exchange for a case study, a reference, and letting us co-market the win.

**B:** What's the catch on the lighthouse deal?

**M:** You're a reference. You take a couple of reference calls, you let us name you, you give us a case study. That's the trade. If you're not comfortable being public, that's fine, but then it's standard pricing. The discount buys your story, not just your logo.

**B:** And if I want to de-risk before committing to an annual number?

**M:** That's what the pilot is for. $50K to $75K, four to six weeks, one assistant. Your team runs adversarial traffic and judges the results. And the full pilot fee credits toward year one if you move forward, so you're not paying twice. It's the lowest-risk way in.

**B:** Okay. Send me the Mission numbers in writing and the pilot option, and I'll take it to my budget owner.

**M:** I'll send both today, with the lighthouse terms spelled out so your budget owner sees the real path, not just list.

---

## What to notice

- M **refused to quote before discovery.** Three quick questions turned a guess into a defensible range. Never quote cold.
- M **anchored on the tier range** and bundled implementation visibly ("covers the deployment, threat modeling, SIEM integration"), framing it as value, not a tax.
- The **"compared to what" move** on the Lakera objection: M reframed the category (filter vs deception), gave the right comparison (Acalvio), and offered "run both" so it's not either/or.
- M **held the platform price and gave on the right levers** (implementation, year one, lighthouse). This is the discipline from `04-pricing.md`: discount services and year one, protect the renewal list price.
- M made the **lighthouse discount a real trade** ("buys your story, not just your logo"), not a desperate price cut.
- Closed by routing the **pilot as the de-risk path** and committing to send real terms, including the lighthouse path, so the budget owner sees the true number.
