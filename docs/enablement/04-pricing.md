# Pricing

Three-tier model. Lighthouse phase. Founder-led sales. Customizations expected per deployment. This is the working pricing playbook. Update as the business scales.

## The shape

Annual platform license + one-time implementation + optional services. Customization lives inside the tier scope, not as a surprise services tail.

## Tier 1. Pilot ($50K to $75K fixed-fee)

The "let us prove it" engagement. Designed to convert, not to be profitable on its own.

**Scope:**
- 4 to 6 weeks
- Single customer-facing LLM
- One profile bundle scoped to their use cases
- Detection feed wired to one SIEM
- Methodology to evaluate results
- 100% of pilot fee credits toward year 1 on conversion

**Delivery cost (~$51K COGS):**

| Role | Hours | Rate | Cost |
|---|---|---|---|
| Founder / Solutions Engineer | 45 | $400 | $18,000 |
| Lead Engineer (Detection + Deployment) | 155 | $175 | $27,125 |
| Threat Researcher (1099) | 28 | $225 | $6,300 |
| **Total** | ~228 | | **~$51,425** |

The Customer Success / coordination role (~17 to 20 hours) is hidden inside the founder's hours today.

**Throughput:**
- 1 senior engineer dedicated to lead-engineer role: ~5 to 6 pilots/year
- 2 senior engineers: ~10 to 12 pilots/year
- The lead-engineer role is the constraint, not pilot price

**Floor pricing rule:** A $50K pilot is break-even at COGS. A $75K pilot is ~33% margin. Below $50K only happens for lighthouse logos with signed reference + case study + co-marketing agreement up front.

## Tier 2. Mission ($150K to $250K annual + $50K to $100K one-time)

Production deployment. Mid-market, single business unit, 1 to 3 LLM endpoints, up to ~10M queries/month.

**Annual platform license includes:**
- Platform license for protected endpoints
- 1 to 2 SIEM/SOAR connectors (Splunk, Sentinel, Chronicle, Elastic)
- Monthly threat intel bundle updates
- Quarterly tuning cycle
- 24/5 support
- <2 min detection SLA

**One-time implementation includes:**
- Discovery and threat modeling
- Profile bundle scoping for their stack
- Deployment integration into gateway or LB
- SIEM connector configuration
- Production readiness review
- Runbook + escalation paths
- Security team enablement (2 sessions)

Typical timeline: 6 to 8 weeks from kickoff to "we own this."

## Tier 3. Constellation ($400K to $1M+ annual all-in)

Multi-model, multi-environment, multi-BU. 100M+ queries/month committed envelope. Air-gapped or VPC-peered deployment. SSO/SCIM, BYO-key, custom retention, custom STIX schemas.

**Includes everything in Mission, plus:**
- Custom rule packs per business unit or vertical (financial, healthcare, gov)
- Multiple SIEM/SOAR connectors
- Custom decoy persona tuned to brand voice
- Dedicated TAM and shared Slack
- Quarterly red-team validation
- 24/7 support
- White-glove implementation (8 to 12 weeks)

This is where the customization premium lives. Starting price gets you the dedicated TAM, the air-gap capability, and BU-specific rule packs. The customization drivers below move it from there.

## Customization drivers (10 levers)

Ten questions to ask in discovery to size the deal:

1. How many LLM endpoints are in scope? (1, 3, 10, 50?)
2. What's the query volume? Monthly average and peak. Drives the platform envelope.
3. What's the deployment topology? Single VPC. Multi-region. Hybrid. On-prem. Air-gapped.
4. Which clouds? AWS, Azure, GCP, on-prem, or mix. Affects connectors and IaC delivery.
5. How many SIEM/SOAR integrations? Standard bundled. Custom adapters priced separately.
6. Industry-specific rule packs? Financial, healthcare, gov/defense. Each is custom engineering plus maintenance.
7. Data residency or sovereignty constraints? EU only. FedRAMP-equivalent. Sovereign cloud.
8. What SLA do they want? Default <2 min. Sub-30 second is a Tier 3 premium.
9. Downstream system bridges? PagerDuty, Opsgenie, Jira, ServiceNow, custom webhooks.
10. Co-managed SOC or embedded analyst? Big lever. Adds $200K to $400K/yr.

## A la carte add-ons

| Item | Price |
|---|---|
| Custom rule pack development (per pack) | $25K to $50K |
| Red team validation engagement (quarterly) | $30K to $75K |
| Embedded analyst (1 FTE-equivalent) | $200K to $400K/yr |
| Additional decoy persona | $15K to $30K |
| Air-gapped deployment uplift | $50K to $150K one-time + 25 to 50% on annual |
| FedRAMP-style control mapping doc | $25K |
| Custom SIEM/SOAR connector (per system) | $20K to $50K |
| Compliance evidence package (SOC2, ISO 27001 mapping) | $30K to $60K |

## Commercial terms

- Annual commit. Quarterly invoicing for ACVs over $250K.
- Multi-year discounts: 10% on 2-year, 18% on 3-year.
- Pilot fee credits 100% toward year 1 on conversion.
- Auto-renew with 60-day opt-out.
- Standard MSA. Custom MSAs accepted with markup or one-time legal fee.
- First 5 enterprise customers: 30 to 50% discount available in exchange for case study, reference rights, co-marketing.

## Anchoring strategy

**Anchor high.** Quote list. Let enterprise procurement discount you down. Founders consistently undercharge in early enterprise sales by 40 to 60%. The number on the slide should make you slightly uncomfortable.

**The pilot is your weapon.** A well-scoped $50K to $75K pilot converts 50 to 70% of the time when the customer's security team is engaged in the design. Two concurrent pilots is a healthy pipeline indicator.

**Don't price per query.** Creates buyer anxiety. Use platform + envelope. Renegotiate at renewal if volume grew.

**Implementation is a feature, not a tax.** Bundle it visibly into the tier price. "Production deployment is $200K and includes X, Y, Z" beats "platform is $150K plus $50K services."

**Don't compete on price with the AI security commodity vendors.** Lakera and Lasso are $75K to $150K because they're API filters. SquirrelOps is a deception platform with threat intel output. Price like deception (TrapX, Illusive, Acalvio), not API filtering.

**Discount lever, not price lever.** When negotiating, give discount on services or year 1, not on platform list. Protect the renewal price.

## The pricing conversation

When a buyer asks "what does this cost?", the structure is:

1. **Ask discovery first.** Don't quote until you know the 10 customization drivers above. Even a rough answer to 3-4 of them helps.

2. **Frame the tiers.** "We have a pilot tier, a mid-market production tier, and an enterprise tier. The pilot is fixed-fee. The other two are platform-plus-implementation, with the implementation work scoped to your environment."

3. **Direct the buyer to a tier.** Based on what you heard in discovery. "Sounds like you're a fit for our Mission tier."

4. **Give a range, not a point.** "Mission is $150 to $250K annual, plus $50 to $100K implementation. Where you land in that range depends on [the specific drivers you identified]."

5. **Offer the pilot path.** "If you'd rather de-risk it, we can start with a pilot. $50 to $75K. Six weeks. Full credit toward year 1 if you convert."

6. **Don't apologize for the price.** A pause after the number is fine. Let the buyer talk first.

## What to say when a buyer pushes back on price

| Pushback | Response |
|---|---|
| "That's expensive." | "Compared to what?" Then let them anchor before you respond. |
| "Lakera is $75K." | "Lakera is an API filter. We're a deception platform with threat intel output. Different category. Different pricing." |
| "We don't have budget this year." | "When does your fiscal cycle open?" Then build the pipeline for that quarter. |
| "Can we do a smaller pilot?" | "The pilot is already sized for a single LLM endpoint and a six-week timeline. Going smaller compromises the proof-of-value. What's driving the smaller scope?" |
| "We can build this ourselves." | "Maybe. The 800-test release gate, the 87-turn campaign, the reproducible-build infrastructure, the TAXII2 pipeline. That's where most of the engineering went. You can build it in 12-18 months. We did. What's the cost of that?" |

## Open questions to refine the model

These four answers sharpen the numbers materially:

1. Bench reality. Is there a second engineer today, or is the founder the lead engineer? Changes throughput and COGS allocation.
2. Profile bundle automation maturity. Manual rule engineering vs YAML-driven bundle generation determines if the 30 to 40 hour rule engineering line is real or half.
3. SIEM connector status. Pre-built Splunk + Sentinel connectors save 8 to 12 hours per pilot. Custom every time is expensive.
4. Customer environment integration. Self-serve Terraform modules vs. hands-on cloud work is the biggest unlock for the deployment-engineer role.
