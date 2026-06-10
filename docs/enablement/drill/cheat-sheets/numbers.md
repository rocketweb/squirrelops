# Numbers Card

Every number, the exact phrasing, and the trap. Full provenance in `02-numbers-and-proof.md`.

| Number | Say it as | Never say | Source |
|---|---|---|---|
| 98.5% | "66 of 67 attack turns" | "98.5% of the 87-turn campaign" / "of all attacks" | redteam-2026-05-v1_0_4.json |
| 0 FP | "Zero on benign traffic in our test set" | "zero in production" (no prod yet) | benign control set |
| <2 min | "Under 2 minutes to detection" | a hard SLA you can't back | release gate timing |
| ~30ms | "About 30ms on clean traffic, below the noise floor" | "no latency" | layer latency budget |
| 815 tests | "815 on the v1.0.5 release branch" | "815 in the AI module gate" | v1.0.5 |
| 1,000+ tests | "Over a thousand across the suite" | a precise total you didn't verify | suite count |
| 6 families / 7 profiles | "6 technique families across 7 attacker profiles" | "80+ techniques" | attack corpus |
| 700MB DeBERTa-v3 | "700MB DeBERTa-v3, ONNX, ships in the bundle" | "always-on ML regardless of bundle" | stage2 |

## The 98.5% explanation (memorize this)

87 total turns. 67 are attacks, 20 are benign. We caught 66 of 67 attacks = 98.5%. Raw canary rate across all 87 = 75.86%. Both true. The attack-turn number is the meaningful one. **Volunteer the 76% before they find it.**

## Latency breakdown

- Layer 1 (rules): sub-millisecond
- Layer 2 (ML): 10-30ms
- Total benign: ~30ms
- Model load: ~1-2s once, not per request

## What NOT to claim (ever)

Production FP rates. SOC 2 / FedRAMP / ISO certification. "80+ techniques." Whole-platform reproducibility (it's the bundle). Always-on ML (confirm per bundle, or set CLOWNPEANUTS_REQUIRE_STAGE2).
