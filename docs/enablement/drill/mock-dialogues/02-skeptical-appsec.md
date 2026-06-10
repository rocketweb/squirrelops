# Mock Dialogue: Skeptical AppSec Engineer

The technical evaluator. Respects precision, allergic to marketing, will test the architecture. This models technical honesty, including a deliberate "I don't know, I'll follow up" moment. M is Matt, B is the buyer.

---

**B:** Walk me through the detection. What's actually deciding what's an attack?

**M:** Two layers. First a deterministic rule layer, regex and known-pattern matching, sub-millisecond. Then an ML classifier, a DeBERTa-v3 model exported to ONNX, around 10 to 30 milliseconds. The two scores combine by max, so either one firing routes the request to the decoy.

**B:** Max, not average? Why?

**M:** Because a high ML score with no rule match would get diluted below threshold if we averaged. Max means a confident signal from either layer is enough. Rules catch deterministic markers, the ML catches semantic paraphrases the rules miss. We don't want to wash either one out.

**B:** Where does the ML model live? 700MB is not nothing.

**M:** It ships inside the profile bundle, not in the source tree. And I want to be precise here, because it matters: if a bundle is built without the model, the runtime degrades to the rule layer only. We added a flag, you can set it to make the runtime fail closed and refuse to start rather than silently run one layer. So for your deployment we'd confirm the bundle includes the ML layer, or you set the flag.

**B:** Most vendors wouldn't tell me that.

**M:** Most vendors get caught by an engineer like you six weeks in. I'd rather you know now.

**B:** What happens when the classifier is wrong? False positive on a real user.

**M:** Two things. Deception has a structural advantage there: a legitimate user never gets routed to the decoy unless we misclassify, and we tune the threshold per tenant during onboarding to hold the false-positive rate near zero on your actual traffic. On our benign test set it was zero. I won't quote you a production number because we don't have production yet.

**B:** And if you false-positive anyway, the user hits the decoy and gets a wrong answer?

**M:** Correct, that's the failure mode. A misclassified benign user would get a decoy response instead of your model. That's why the threshold tuning and the conservative rule layer matter, and why we measure FP obsessively. It's the thing we'd watch most closely during your pilot.

**B:** What's the latency at p99, not average? Average numbers hide tails.

**M:** Fair, and here's where I'll be honest: I have the average figure, about 30ms added on benign traffic, but I don't have the p99 tail number in front of me and I don't want to make one up. Let me get you the p99 from our benchmarks and send it tomorrow. What hardware profile should I assume for your environment so the number's actually relevant?

**B:** GPU inference, T4-class.

**M:** Got it. I'll send p99 on T4 by tomorrow.

**B:** Okay. The output format, what do we actually ingest?

**M:** Standard STIX 2.1 over TAXII2. Indicators, attack-patterns, relationships, ATT&CK and ATLAS enriched. Your SIEM polls our TAXII2 endpoint. If you're on OpenCTI we've got a documented integration; on Splunk or Sentinel you point their TAXII2 collector at our feed. No proprietary format, no new dashboard.

**B:** That's clean. Send me the p99 and a sample STIX bundle and I'll take it to my team.

**M:** Done. Both by tomorrow.

---

## What to notice

- M answered the **max-vs-average** question with the real engineering reason. Precision earns this persona's respect; vagueness loses it.
- M **volunteered the stage-2 degradation honestly** and turned a product limitation into a trust signal ("most vendors get caught six weeks in").
- M **owned the failure mode** plainly when pushed ("correct, that's the failure mode"). Didn't dodge. Engineers trust people who can say what breaks.
- The **p99 moment is the model.** M didn't have the number, didn't invent one, deferred with a specific commitment AND asked a clarifying question to make the follow-up actually useful. That exchange builds more trust than a guessed number ever could.
- M **closed on two concrete deliverables** with a deadline. Watch that the follow-up actually happens; that email is the trust.
