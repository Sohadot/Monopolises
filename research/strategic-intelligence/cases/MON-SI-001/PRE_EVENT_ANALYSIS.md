# MON-SI-001 — NVIDIA Advanced AI Compute Supply-Chain Exposure (pre-event reconstruction)

**Case type:** retrospective calibration case, pre-gate exploratory prototype (MON-SI-G0 is PROPOSED, not opened)
**Information cutoff:** 2026-05-12T23:59:00Z
**Register:** [`register.pre-event.json`](register.pre-event.json) (13 admitted sources, 7 excluded, 21 claims)
**Market data:** [`event-study-pre-event.json`](event-study-pre-event.json) (price rows after 2026-05-12 removed before computation)
**Status:** analysis complete; not reviewed by a second reviewer; not published

## 0. Research question

> Could a disciplined analyst, using only information public before 13 May 2026, have identified economically material risks involving NVIDIA's China-related demand, Southeast Asian intermediaries, export restrictions and supply-chain exposure?

**System boundary (dated):** NVIDIA-originated advanced data-center compute (ECCN 3A090.a / 4A090.a class) and the commercial channels through which it reaches end demand, February 2025 – 12 May 2026, with attention to China-linked demand reached outside China-headquartered customers.

<!-- hindsight-disclosure:start -->
## 1. Hindsight contamination disclosure

- The researcher began this case **knowing** that a short-seller report (Culper Research, 13 May 2026) alleged undisclosed China-linked demand routed through Southeast Asian intermediaries, and knowing the research question was framed around that allegation. The *choice of question* is therefore outcome-informed.
- One admitted source (SI1-SRC-013, the Senator's October 2025 letter naming a Singapore intermediary) was found through a search whose results included post-event coverage. Its pre-cutoff availability is proven by its own date and PDF metadata, but a blind analyst might not have prioritised it. It is flagged `hindsight_flag: true` and is used only as an S2 lead.
- The Culper report was not read for this reconstruction and is not a source here. Post-event facts appear only in `POST_EVENT_VALIDATION.md`.
- **Consequence:** whatever this reconstruction "gets right" is evidence that the facts were *available*, not that this method would have *found and weighted* them prospectively.
<!-- hindsight-disclosure:end -->

## 2. Summary of findings

| # | Finding | Class | Status at cutoff |
|---|---|---|---|
| F1 | NVIDIA's geographic revenue disclosures never showed where chips were used; the basis moved from billing location to customer HQ in Q3 FY2026, removing the Singapore line | S0 | Known; disclosed by the company |
| F2 | The Singapore billing channel was large (18–22% of revenue) but NVIDIA and Singapore both stated it was mostly invoicing for non-Singapore shipments, and NVIDIA stated >99% of controlled compute billed there was ordered by U.S.-based customers | S0 | Known; partly answers the "Singapore = China" hypothesis in the negative |
| F3 | Three channels could carry China-linked end demand while being booked outside "China": U.S.- or Taiwan-HQ direct customers' downstream resale, Southeast Asian intermediaries, and cloud access to chips deployed outside China. The mechanism is documented; the **magnitude is not** | S0 mechanism / unquantified | Underappreciated *candidate* risk |
| F4 | Southeast Asian transit regimes were tightening (BIS May 2025; Malaysia July 2025), so any demand that depended on those routes was exposed to regulatory interruption | S0 | Known regulatory trend; exposure size unknown |
| F5 | A specific Singapore intermediary had been publicly named, with relayed sizing of about 2% of Data Center sales, by October 2025 | S2 (lead) | Public allegation; unverified |
| F6 | The direct China data-center loss was fully disclosed and the company's guidance assumed zero China DC compute; no pre-cutoff evidence shows the market treating diversion news as material | S0 / S1 | Known risk, apparently priced or ignored |

**Bottom line:** a disciplined analyst **could** have identified a credible, specific, *unquantified* risk condition: part of NVIDIA's non-China-attributed Data Center revenue might depend on China-linked end demand reached through intermediaries or cloud access, and that dependence was exposed to tightening enforcement and reputational shocks. The analyst **could not**, from primary evidence, size that dependence, attribute it to particular customers, establish unlawful conduct by anyone, or predict a share-price move.

## 3. A — Market structure (bounded)

- NVIDIA's FY2026 revenue was $215.9bn, of which Data Center was $193.7bn (compute $162.4bn, networking $31.4bn) (SI1-C-14). Two direct customers took 22% and 14% of revenue (SI1-C-13). This is concentration on the **demand side**, not a measure of market power.
- Substitution in China: NVIDIA states that it was "effectively foreclosed" from China's data-center compute market and that its absence "helped our competitors build larger developer and customer ecosystems" (SI1-C-09). The Chinese government had "encouraged customers to purchase from our China-based competitors" (10-K FY2026 Item 1A). For **legitimate China demand**, domestic substitutes are the lawful outlet; for demand that specifically wants NVIDIA performance, the incentive to obtain it **indirectly** remains.
- **Ontology note (no classification made):** a U.S. licence requirement governing admission of a product class to a destination market is structurally similar to the source-origin admission rule recorded under `access_gatekeeping` in MON-G1-S6. That is an *ontology lead only*. MON-SI-001 assigns no layer, and MON-G1-S3 (CUDA, `no_evidenced_control_layer`) is untouched.

## 4. B — Supply chain: keeping the distinctions apart

| Dimension | What the pre-cutoff evidence shows | Source |
|---|---|---|
| **Billing location** | Singapore: $23.7bn (18%) FY2025; $9.0bn (20%) Q1 and $10.2bn (22%) Q2 FY2026 | SI1-C-01, C-03 |
| **Physical shipment** | Under 2% of FY2025 revenue shipped to Singapore (NVIDIA); under 1% physically delivered (Singapore MTI) | SI1-C-01, C-15 |
| **Ordering party** | >99% of *controlled* compute billed to Singapore was ordered by U.S.-based customers (Q1–Q2 FY2026) | SI1-C-03 |
| **Customer HQ** | From Q3 FY2026: U.S. $149.6bn, Taiwan $42.3bn, China $19.7bn, Other $4.3bn (FY2026) | SI1-C-04, C-06 |
| **End customer** | Disclosed only for Taiwan-HQ customers: 76% of their DC revenue attributed to U.S./Europe end customers (FY2026) | SI1-C-06 |
| **Warehousing** | A "substantial portion" of products warehoused in and distributed from Hong Kong | SI1-C-11 |
| **Cloud vs ownership** | U.S. licence conditions already regulate offering large GPU clusters "as a service"; Malaysia's permit regime covers physical export, transshipment and transit, not remote use | SI1-C-12, C-17 |
| **Ownership / financing of intermediaries** | **Not established**: registries not accessed | SI1-SRC-017 (excluded) |

Three inferences follow (S1, bounded):

1. **The Singapore line was not, by itself, a China signal.** Taking NVIDIA's ordering-party statement at face value, almost all controlled compute billed to Singapore was ordered by U.S.-based customers. A thesis of "Singapore billing = China diversion" is **unsupported** on primary evidence.
2. **Neither billing nor HQ geography bounds China-linked end demand.** Revenue booked to a U.S.- or Taiwan-HQ OEM, distributor or system integrator is "U.S." or "Taiwan" revenue regardless of where the server is installed or who rents it. The DOJ's November 2025 case alleges this exact pattern at small scale: a U.S.-based supplier, a U.S. shell company, and routing through Malaysia and Thailand to the PRC (SI1-C-18).
3. **The residual windows are measurable only as loose upper bounds.** Taiwan-HQ DC revenue attributed to end customers outside the U.S./Europe was at most about $10.2bn in FY2026, and that figure is overstated because non-DC revenue is in the base (SI1-C-07). "Other" HQ revenue was $4.3bn. Neither is China-specific.

## 5. C — Economic interests (hypotheses, not allegations)

| Party | Plausible interest under the observed regime | Evidence status |
|---|---|---|
| NVIDIA | Maximise lawful sales; avoid compliance failures and reputational "diversion" reports, which it lists as a risk factor | S0 (SI1-C-11) |
| U.S./Taiwan-HQ OEMs and distributors | Volume; the resale-compliance burden rests on them | Inferred from the direct/indirect customer structure |
| Southeast Asian data-centre operators and brokers | Arbitrage between controlled demand and lawful capacity, both physical resale and compute rental; exposed to local permit regimes | Mechanism S0 (SI1-C-12, C-17, C-18); specific actors S2 |
| China-based AI developers | Access to frontier NVIDIA performance while domestic substitutes mature | Inferred; 10-K describes state encouragement of domestic purchasing |
| Chinese domestic chip suppliers | Benefit from foreclosure and from any tightening of indirect routes | S0 framing in NVIDIA's own risk factors |
| U.S. and Southeast Asian governments | Enforcement credibility versus investment attraction; Singapore states it does not enforce foreign unilateral controls but acts on fraud | S0 (SI1-C-15, C-16, C-17) |

## 6. D — Financial exposure

- **Already-realised China loss (known):** a $4.5bn H20 charge; about $60m of licensed H20 revenue; zero H200 revenue at FY2026 filing; China-HQ revenue down from $13.6bn in H1 FY2026 to about $3.0bn per quarter in H2 (SI1-C-08, C-09). Q1 FY2027 guidance assumed no China DC compute (SI1-C-10). Gross margin was 71.1% in FY2026, with the H20 charge as a stated drag (SI1-C-14).
- **Mechanical sensitivity (not a forecast, no probability attached):** each 1% of FY2026 Data Center revenue is about $1.94bn; 2% ≈ $3.9bn; 5% ≈ $9.7bn; 10% ≈ $19.4bn. If an indirect channel of a given size were interrupted, this is the revenue scale at stake before any reallocation of supply to other customers. Supply-constrained periods could absorb an interruption through reallocation; that offset is not measurable from filings.
- **Inventory and commitment risk:** the H20 precedent shows that abrupt regulatory change converts product-specific demand into inventory and purchase-commitment charges (SI1-C-09). Any channel interruption tied to a product class would carry the same mechanism.
- **Concentration interaction:** with two direct customers at 36% combined, exposure depends on which customers' downstream channels are involved. That is not disclosed, so it is unknowable here.

## 7. E — Market expectations

| Category | Content |
|---|---|
| **Known risks** (disclosed and plausibly in expectations) | China DC foreclosure; H20/H200 licensing; Chinese government discouragement; diversion reports as a reputational risk; Hong Kong warehousing; AI Diffusion replacement-rule uncertainty |
| **Underappreciated candidate risk** | Dependence of non-China-attributed revenue on China-linked end demand via intermediaries or cloud access, plus its exposure to Southeast Asian and U.S. enforcement. This is "underappreciated" only as a hypothesis: no consensus data was available to test it |
| **Potential catalysts** (classes, not dates) | A government statement naming an intermediary; a charging document naming a channel tied to NVIDIA products; a permit or licence change in Malaysia, Thailand or Singapore; a change in NVIDIA's geographic or customer disclosures |
| **Uncertain / unavailable** | Intermediary ownership and financing (registries not accessed); shipment-level trade data (proprietary); sell-side consensus (proprietary); the 2% sizing (S2) |

**What prices show (SI1-C-21).** Across six earlier public signals, two-session abnormal returns were insignificant in four windows (three negative, one positive). They were significantly negative in two: 14–15 Oct 2025, after the Senator's Megaspeed letter, about −5.3% against both models; and 26–27 Feb 2026, around the FY2026 results, −5.3% vs SMH and −7.4% vs SPY. Both windows are confounded or unattributed. This prototype did not screen the October window for other same-day news, and the February window is an earnings release. **Conclusion:** price data neither confirms nor refutes that the market had priced the indirect-channel risk.

## 8. What could not be inferred (negative findings)

- The **size** of China-linked demand inside U.S.-, Taiwan- or Other-HQ revenue. No primary source bounds it tightly; the analysis declines to estimate it.
- Whether NVIDIA or any named intermediary acted **unlawfully**. No pre-cutoff charging document names NVIDIA or Megaspeed.
- The **ownership or financing** of any intermediary.
- Whether the Q3 FY2026 disclosure-basis change had any purpose other than the one stated.
- Any **share-price direction or magnitude**.

## 9. Pre-registered expectations (written before the validation file)

Had this been a prospective case, the risk conditions registered at the cutoff would have been:

- **RC1** — within 12 months, a government of Singapore, Malaysia or the U.S. issues a primary statement or charging document concerning a named intermediary that purchased NVIDIA products.
- **RC2** — within 12 months, NVIDIA changes or adds disclosure on diversion, end-use, or customer-channel compliance.
- **RC3** — within 12 months, a Southeast Asian jurisdiction adds a new permit or licence measure covering AI accelerators or compute services.
- **Not registered:** any revenue-share figure, any price direction, any legal outcome.

These are recorded here for transparency, but because the outcome was known in advance they **do not count** toward MON-SI-G0 criterion P5.

<!-- errata-pointer -->
---

**Post-freeze errata (2026-11-15).** The text above is preserved as frozen at commit `5b3b756`. Dated corrections SI1-E-01 to SI1-E-04 are recorded in `register.pre-event.json` → `addenda.errata`, and the availability review is in `addenda.availability_review`. No interpretation above is changed by them.
