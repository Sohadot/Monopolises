# MON-SI-001 — Post-event validation (preliminary)

**Written after** `PRE_EVENT_ANALYSIS.md` and `register.pre-event.json` were completed. Nothing below has been fed back into the pre-event files.
**Register:** [`register.post-event.json`](register.post-event.json) · **Market data:** [`event-study-post-event.json`](event-study-post-event.json)
**Validation horizon:** 13 May 2026 – 15 Nov 2026 (about six months; the 12-month risk-condition windows are still open)
**Status:** preliminary. Not counted toward MON-SI-G0 criterion P5, because the case is retrospective and the outcome was known in advance.

## 1. What could be checked against what

| Comparator requested | What was actually available | Evidence class |
|---|---|---|
| Culper Research report, 13 May 2026 | Original PDF **not retrieved** (HTTP 403). Content known only through two secondary summaries | S2 |
| Later Singapore government statements | Singapore Police Force statement, 30 Oct 2026 | S0 |
| Later Malaysian regulatory disclosures | **No primary disclosure located**; one paywalled headline (13 Nov 2026) | unresolved |
| Later U.S. enforcement actions | **No new primary charging document located** naming the channel; secondary reports of a criminal investigation | unresolved |
| Later NVIDIA disclosures | 10-Q Q1 and Q2 FY2027; 8-K of 12 Nov 2026 | S0 |
| Stock-market performance | NVDA vs SMH and SPY: event study and buy-and-hold | S1 |

## 2. Classification of pre-event findings and risk conditions

Allowed classes: *Independently anticipated* · *Partially corroborated later* · *Unresolved* · *Contradicted* · *Not discoverable with the pre-event evidence*.

| Pre-event item | Later evidence | Classification | Note |
|---|---|---|---|
| F1 — geographic disclosures do not reveal end use | NVIDIA adds that it lacks "physical control of our products after sale" and relies on customers' compliance programs (SI1-V-01) | **Partially corroborated later** | Corroborates the observability gap, not any diversion volume |
| F2 — Singapore billing line is not by itself a China signal | Nothing primary contradicts it; per secondary summaries, the short report's headline estimate did not rest on Singapore billing | **Unresolved** | No later primary data on Singapore-billed end use |
| F3 — indirect channels could carry China-linked demand; magnitude unknown | Short-seller estimate of >20% of FY2026 compute revenue (S2, disputed); no primary corroboration of any magnitude | **Unresolved** | The pre-event analysis declined to size this; that refusal still stands |
| F4 — Southeast Asian route tightening exposes indirect demand | Paywalled report of a Malaysian customs check; no primary text | **Unresolved** | — |
| F5 — a named Singapore intermediary under public allegation (S2 lead) | SPF: "Investigations into Megaspeed are ongoing" (SI1-V-03) | **Partially corroborated later** | Corroborates that an investigation exists, **not** an unlawful final destination or any wrongdoing |
| F6 — diversion signals had not visibly moved the price before the cutoff | Immediate reaction to the report was **positive** (CAR[0,+1] +4.6% vs SMH, t = 2.2) | **Partially corroborated later** | Consistent with the market not treating the report's content as new on day 0–1; it does not show the risk was priced |
| RC1 — government statement on a named intermediary within 12 months | SI1-V-03 (30 Oct 2026) | **Independently anticipated** (hindsight caveat) | Derived from pre-cutoff primary evidence without the report; the research question itself was outcome-informed |
| RC2 — NVIDIA changes diversion or end-use disclosure within 12 months | SI1-V-01 (20 May 2026) | **Independently anticipated** (hindsight caveat) | Same caveat. Seven days after the report, so the trigger cannot be identified |
| RC3 — new Southeast Asian permit or licence measure within 12 months | None found (window open to 12 May 2027) | **Unresolved** | — |
| Short-report claims on intermediary financing, upstream server supply and executive relationships (S2) | Not corroborated by any primary source located | **Not discoverable with the pre-event evidence** | They rest on registry and trade data and interviews that this prototype did not access; their truth is also **unresolved** |
| Short-report claim that ">20% of compute revenue was China-driven" | No primary corroboration | **Not discoverable with the pre-event evidence** | It rests on market-share estimates and price assumptions, not on filings |
| Hypothesis "the report caused the subsequent share-price decline" | Positive day 0–1 abnormal return; later decline confounded | **Contradicted** for the immediate window; **Unresolved** for longer horizons | See §3 |

**Validation, not verdict:** none of the above establishes that any party broke any law. Supply-chain relationships corroborated later are not proof of an unlawful final destination.

## 3. Market performance (descriptive, no causal attribution)

Base: close of 12 May 2026 (day −1). Day 0 is 13 May 2026; the report was announced around 18:04 UTC (14:04 New York), during the session. Market model estimated over 4 Nov 2025 – 28 Apr 2026 (120 sessions).

| Window | NVDA | vs SMH model (CAR, t) | vs SPY model (CAR, t) |
|---|---|---|---|
| [0,0] | +2.29% | +0.8% (0.58) | +1.3% (0.78) |
| [0,+1] | +6.78% cumulative | **+4.6% (2.22)** | +4.2% (1.84) |
| [0,+5] | — | +1.8% (0.51) | +0.8% (0.20) |
| [0,+10] | — | −6.5% (−1.35) | −6.6% (−1.22) |

| Buy-and-hold from 12 May close to | NVDA | SMH | SPY | NVDA − SMH | NVDA − SPY |
|---|---|---|---|---|---|
| 27 May 2026 | −3.7% | +6.1% | +1.7% | −9.8 pp | −5.4 pp |
| 12 Jun 2026 | −7.0% | +10.5% | +0.5% | −17.4 pp | −7.4 pp |
| 12 Aug 2026 | +1.6% | +4.2% | +4.9% | −2.6 pp | −3.3 pp |
| 13 Nov 2026 | −26.1% | −13.3% | +2.7% | −12.8 pp | −28.8 pp |

**Confounders known to the researcher inside these windows:** Q1 FY2027 results after the close on day +5 (SI1-PST-006); an $11.9bn acquisition agreement, 2 Sep 2026 (SI1-PST-005); the CEO resignation, 11–12 Nov 2026 (SI1-PST-003); sector-wide moves (SMH −13.3% to 13 Nov). Note that SMH contains NVDA.

**Reading:** NVDA underperformed both benchmarks over six months. A directional "NVDA falls after the report" outcome is observed **but not explained**: the immediate reaction ran the other way, relative performance had recovered to −2.6 pp vs SMH by mid-August, and most of the later gap opened in October–November alongside events the pre-event analysis did not, and could not, anticipate. A correct direction is not evidence for the report's causal account.

## 4. Lessons for the method (calibration, not performance)

1. **Primary filings carried the mechanism but not the magnitude.** The decisive quantities in the short report came from data this prototype treats as proprietary or unverified: trade records, registries and third-party share estimates. A future gate case must decide in advance whether registry access is in scope.
2. **The disclosure-basis change (Q3 FY2026) was a real, primary-sourced observability signal.** It deserves a standing rule: changes to segment or geographic attribution bases are logged as research leads.
3. **Legislative letters are an early, dated, primary record of allegations.** They are useful for timestamping S2 leads, never as findings.
4. **Price reaction and research correctness came apart.** Day 0–1 returns were positive. Market data should stay descriptive in this discipline and must never be a success criterion.

## 5. What this case does not show

- That MON-SI methods predict anything: the case is retrospective and its question was outcome-informed.
- That NVIDIA, Megaspeed or any other party acted unlawfully.
- That the short report's figures are right or wrong.
- That any share-price change was caused by the report, the investigation or any disclosure.
