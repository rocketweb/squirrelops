# Competitive Landscape

The single most important fact in this doc: **nobody is selling what you're building.** As of mid-2026, there is no funded startup and no major vendor productizing a decoy LLM that you route a suspected attacker into. You are defining a category, not fighting for share in one. That changes how you compete. You're not out-featuring a rival; you're teaching a market that a new category exists and that the alternatives don't cover it.

This doc gives you the map, the acquisitions (the space consolidated hard in 2024-2025, so don't rely on old mental models), and the one positioning line that works.

## The headline: the LLM-deception category is uncontested

When buyers or partners ask "who else does this," here is the honest, researched answer:

- **Decoy-LLM routing as a product:** effectively nobody. It exists as academic research and proofs of concept (Palisade Research's "LLM Agent Honeypot," arXiv 2410.13919, is the canonical reference), not as a productized enterprise offering.
- **What gets confused with it:** vendors who use an LLM to make a classic network honeypot more convincing (Acalvio does this, plus open-source projects like beelzebub). In those, the LLM is the puppet faking a compromised server. In yours, the LLM is the asset you defend. Opposite roles.

**A caution to hold.** There is a granted US patent (12423441) on "generative LLM for cybersecurity deception and honeypots." That is an IP freedom-to-operate flag, not a competitor. Do not make public "first" or "only" claims about the category until counsel has read that patent's claims. In conversation you can say "there's no commercial product doing this that we've found," which is true and defensible. Avoid "we're the only company that can legally do this" until IP is cleared.

## The guardrail / filter crowd (consolidated, well-funded, and not your category)

These are the names a buyer will reach for first because they're the loud part of "AI security." They all do the same thing: inspect a prompt and block it at the door. They assume the filter holds.

| Name | What it does | Owner (status) |
|---|---|---|
| Lakera | AI-native runtime guardrails + red teaming | Check Point (~$300M, agreed Sep 2025) |
| Prompt Security | Runtime GenAI/agent security, DLP | SentinelOne (~$250M, agreed Aug 2025) |
| Protect AI | AI supply-chain + runtime security | Palo Alto Networks (closed Jul 2025) |
| Lasso Security | End-to-end LLM/GenAI security | Independent (~$6M seed firmly sourced) |
| Cloudflare Firewall for AI | Inline prompt firewall at the edge | Cloudflare (native) |
| Microsoft Prompt Shields | Jailbreak/injection classifier in Azure | Microsoft (native) |
| NVIDIA NeMo Guardrails | OSS programmable guardrail toolkit | NVIDIA (open source) |
| Guardrails AI | OSS input/output validators | Independent (open source) |

**How you differ, in one line:** guardrails are a wall; SquirrelOps is the trapdoor behind the wall. They try to keep attackers out. You let them in (to a decoy) and study them. The two are complementary, not exclusive: a customer can run Lakera AND SquirrelOps. Frame it that way. "Keep your guardrail. We're what catches the attacker the guardrail misses, and tells you how they got past it."

**The killer supporting fact:** EchoLeak (CVE-2025-32711), disclosed June 2025 by Aim Security, was the first real-world zero-click prompt injection in a production LLM (Microsoft 365 Copilot, CVSS 9.3). It exfiltrated data from a single email and defeated Microsoft's own injection classifier. That's the proof that filters fail and you need a fallback that catches what slips through. This is your best single slide.

## AI red-team and posture vendors (complementary, not competitive)

| Name | What it does | Owner (status) |
|---|---|---|
| HiddenLayer | ML detection & response, model scanning, attack simulation | Independent (~$56M raised) |
| Robust Intelligence | Automated AI red-teaming / validation | Cisco (closed Sep 2024) |
| Protect AI | Model scanning, AI-BOM, red teaming | Palo Alto (closed Jul 2025) |

These test your model for weaknesses before deployment. You catch the attacker after deployment. When a buyer says "we already use HiddenLayer," the answer is "good, that hardens your model. We're the runtime detection layer for when someone attacks it in production. Different job, same goal." Never position against these; position alongside.

## Network deception incumbents (your lineage, none in the LLM layer)

| Name | What it does | Owner (status) | AI move? |
|---|---|---|---|
| Acalvio ShadowPlex | Enterprise deception, decoys, honeytokens | Independent | Closest mover: uses LLMs to *generate* decoys. No decoy-LLM asset. |
| TrapX | Deception tech | Commvault (2022) | Folded into data resilience |
| Illusive Networks | Deception + ITDR | Proofpoint (Dec 2022) | Absorbed, brand dormant |
| Thinkst Canary | Honeypots + canarytokens | Independent | Token model only |
| CounterCraft | High-interaction digital-twin deception | Independent | Twins of infra, not LLMs |

**The lineage story is your credibility.** Deception is a proven, Gartner-recognized enterprise category that has existed for a decade. Nobody has translated it to the LLM layer. You're not inventing a weird new idea; you're taking a trusted security pattern (honeypots, deception, attribution) and applying it to the surface that just became critical. That framing makes you credible to a security buyer who already believes in deception for the network.

**Acalvio is the one to watch.** They're the closest mover and the one a sharp buyer might raise. The distinction to draw cleanly: "Acalvio makes honeypots with AI. We make a honeypot that is an AI. They use an LLM to generate a fake server. We deploy a decoy LLM to catch attacks on your real LLM." Crisp, true, memorable.

## Market facts you can cite (cleanly sourced)

Use these. They're attributable, unlike a lot of the AI-security stat noise.

- **Your real TAM:** the agentic-AI security segment is projected $1.65B (2026) growing to $13.5B (2032), ~42% CAGR (MarketsandMarkets, May 2026). Cite the agentic number, not the broad "AI in cybersecurity" $25-44B figure; the agentic one is closer to what you actually sell.
- **The gap:** 47% of organizations have no AI-specific security controls; 83% lack automated controls to keep sensitive data out of public AI tools (Kiteworks, 2025 survey). Only ~6% report an advanced AI security strategy.
- **The incident:** EchoLeak (CVE-2025-32711), June 2025, zero-click prompt injection in M365 Copilot that beat Microsoft's own classifier.

**Do NOT cite** the "prompt injection up 340% YoY" or "88% of enterprises had an AI-agent incident" figures floating around. They trace to vendor blogs, not primary research, and a sophisticated buyer will know. Stick to the three above.

## The positioning statement

When you need one sentence that captures the whole competitive story:

> "Everyone else is building a taller wall around your LLM. We build the room on the other side of it. When an attacker slips past your guardrails, we route them into a decoy model that wastes their time, captures their playbook, and tells you exactly how they got in."

## How to handle the three competitive questions you'll actually get

**"How are you different from Lakera / a guardrail?"** "They block prompts at the door and assume the block holds. EchoLeak showed those blocks fail. We're the layer that catches the attacker who got past the filter, in a decoy, with full capture. Run both. We're the detection to their prevention."

**"Isn't this just a honeypot?"** "Same proven idea, new surface. Honeypots for networks are a decade-old, trusted category. Nobody had built one for the LLM attack surface. We did. And ours doesn't just sit there: it engages the attacker with a decoy model and emits labeled threat intel to your SIEM."

**"Who else does LLM deception?"** "No commercial product we've found. It's been academic research until now. That's the opportunity and the risk: we're early in a category the big guardrail vendors will eventually notice. Getting in now means you shape it with us." (Honest, doesn't overclaim, turns 'you're early' into 'get in early.')
