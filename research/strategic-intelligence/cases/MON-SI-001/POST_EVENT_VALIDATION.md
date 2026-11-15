# MON-SI-001 — Post-event validation (preliminary)

**Written after** `PRE_EVENT_ANALYSIS.md` and `register.pre-event.json` were frozen at commit `5b3b756` (hashes in [`FREEZE_MANIFEST.json`](FREEZE_MANIFEST.json)). Nothing below feeds back into the pre-event files. Corrections to those files appear only as dated errata (`register.pre-event.json` → `addenda.errata`).
**Register:** [`register.post-event.json`](register.post-event.json) · **Market data:** [`event-study-post-event.json`](event-study-post-event.json)
**Validation horizon:** 13 May 2026 – 15 Nov 2026 (about six months; the 12-month risk-condition windows remain open)
**Prospective credit:** **none.** MON-SI-001 is retrospective, its research question was framed with the outcome known, and it is permanently excluded from MON-SI-G0 criterion P5.

## 1. What could be checked against what

| Comparator | What was actually examined | Evidence class |
|---|---|---|
| Culper Research report, 13 May 2026 | **Not directly examined.** The PDF and every culperresearch.com page returned HTTP 403 to direct retrieval and to the fetch tool (two passes, 2026-11-15). Content is known only through search-index excerpts (SI1-PST-016) and secondary summaries (SI1-PST-009, -010) | S2 |
| Singapore government | MHA press release, 12 Nov 2026 (SI1-PST-013); SPF statement, 30 Oct 2026 (SI1-PST-004); MHA transcript, 3 Mar 2025, located post hoc (SI1-PST-015) | S0 |
| Malaysian regulator | MITI statement, 13 Nov 2026 (SI1-PST-014) | S0 |
| U.S. enforcement | No new U.S. charging document located. Singapore's account of a BIS post-shipment check (SI1-V-08) and of limited U.S. assistance (SI1-V-10) | S0 (as Singapore's statements) |
| NVIDIA disclosures | 10-Q Q1 and Q2 FY2027; 8-Ks of 20 May, 3 Sep and 12 Nov 2026 | S0 |
| Market performance | NVDA vs SMH and SPY | S1 |

Neither the MHA (12 Nov 2026) nor the MITI (13 Nov 2026) statement mentions **NVIDIA** or **China**. The only primary government text linking the Singapore server case to NVIDIA is the March 2025 remark that the servers "may contain Nvidia chips … the highest I can put it at" (SI1-V-13).

## 2. Classification

**Evidentiary status:** *Confirmed* (official statement or documented procedural fact) · *Partially corroborated* (mechanism supported, full allegation not established) · *Unresolved* (direct evidence missing) · *Contradicted* (credible evidence establishes the contrary) · *Not established* (allegation that cannot be raised to a finding).
**Retrospective relation:** *Retrospectively consistent — no prospective credit* · *Not discoverable with the pre-event evidence* · *Not applicable*. No item in this case is, or can become, a prospective prediction.

| Item | Later evidence | Evidentiary status | Retrospective relation |
|---|---|---|---|
| F1 — geographic disclosures do not reveal end use | NVIDIA: no "physical control of our products after sale" (SI1-V-01). MITI: chip imports into Malaysia need no permit; re-exports are under check (SI1-V-12) | **Partially corroborated** | Retrospectively consistent — no prospective credit |
| F2 — the Singapore billing line is not by itself a China signal | MHA: servers transited Singapore to Malaysia "without entering the Singapore market" (SI1-V-07). This concerns physical transit by Singapore companies, not NVIDIA's billing line. No later data on Singapore-billed end use | **Unresolved** | Not applicable |
| F3a — mechanism: China-linked demand could be served via Southeast Asian intermediaries outside China-HQ revenue | Servers bought by Singapore companies went to Malaysia while their onward destination is investigated (SI1-V-07); a Malaysian data-centre tenant imports its own servers and AI chips (SI1-V-12). Neither statement names NVIDIA content or a China end use | **Partially corroborated** | Retrospectively consistent — no prospective credit |
| F3b — magnitude of that demand | None of the new sources gives quantities, values or NVIDIA revenue attribution | **Unresolved** | Not applicable |
| F4 — tightening Southeast Asian controls expose route-dependent demand | MITI confirms the July 2025 permit regime and that it "is considering further measures" (SI1-V-12) | **Partially corroborated** | Retrospectively consistent — no prospective credit |
| F5a — the named Singapore intermediary is under official investigation | Singapore investigation since Feb 2025, "ongoing" (SI1-V-07, SI1-V-09); MITI re-export check (SI1-V-12) | **Confirmed** | Retrospectively consistent — no prospective credit |
| F5b — that the intermediary diverted controlled chips to China | Governments describe servers moving to Malaysia; onward movement is the open question; MITI states it has "never cleared" the companies, which is not an adverse finding | **Not established** | Not applicable |
| RC1 — government statement on a named intermediary within 12 months | SI1-V-03, SI1-V-07, SI1-V-12 | **Confirmed** | Retrospectively consistent — no prospective credit |
| RC2 — NVIDIA changes diversion or end-use disclosure within 12 months | SI1-V-01 (20 May 2026) | **Confirmed** | Retrospectively consistent — no prospective credit |
| RC3 — new Southeast Asian permit or licence measure within 12 months | MITI is "considering further measures"; none adopted in the record | **Unresolved** | Not applicable |
| U.S. BIS post-shipment check at the intermediary, 24 Jun 2025 | Disclosed only in SI1-V-08 (Nov 2026), although the check predates the cutoff | **Confirmed** | Not discoverable with the pre-event evidence |
| Short report: >20% of FY2026 compute revenue China-driven | Reported derivation uses third-party share estimates and price assumptions (SI1-V-14); no primary source examined supports a magnitude | **Not established** | Not discoverable with the pre-event evidence |
| Short report: intermediary financing, upstream server supply, balance-sheet figures | Registry and trade data not accessed; the original report was not examined (SI1-V-14) | **Not established** | Not discoverable with the pre-event evidence |
| Hypothesis that the report triggered an immediate share-price decline | NVDA rose 6.8% over days 0–1, a positive abnormal return (§3) | **Contradicted** | Not applicable |
| Hypothesis that the report caused the six-month underperformance | Confounded (§3) | **Unresolved** | Not applicable |

**No finding of unlawful conduct.** Investigations, a customs check, a post-shipment verification and a statement that a regulator "has never cleared" a company are procedural facts. None establishes an offence, an unlawful final destination, or responsibility by NVIDIA or any intermediary. Singapore's insufficient-evidence conclusion about one officer (SI1-V-09) is equally not an exoneration of the company.

## 3. Market performance (descriptive; no causal attribution)

Base: close of 12 May 2026 (day −1). Day 0 is 13 May 2026; the report was announced around 18:04 UTC (14:04 New York), during the session. Market model by OLS over 4 Nov 2025 – 28 Apr 2026 (120 sessions).

| Window | Observed NVDA return | Abnormal vs SMH (CAR, t) | Abnormal vs SPY (CAR, t) |
|---|---|---|---|
| [0,0] | +2.29% | +0.8% (0.58) | +1.3% (0.78) |
| [0,+1] | +6.78% | +4.6% (2.22) | +4.2% (1.84) |
| [0,+5] | — | +1.8% (0.51) | +0.8% (0.20) |
| [0,+10] | — | −6.5% (−1.35) | −6.6% (−1.22) |

| Buy-and-hold from 12 May close to | NVDA | SMH | SPY | NVDA − SMH | NVDA − SPY |
|---|---|---|---|---|---|
| 27 May 2026 | −3.7% | +6.1% | +1.7% | −9.8 pp | −5.4 pp |
| 12 Jun 2026 | −7.0% | +10.5% | +0.5% | −17.4 pp | −7.4 pp |
| 12 Aug 2026 | +1.6% | +4.2% | +4.9% | −2.6 pp | −3.3 pp |
| 13 Nov 2026 | −26.1% | −13.3% | +2.7% | −12.8 pp | −28.8 pp |

**Keeping five things separate:**

1. **Observed movement.** NVDA rose on days 0 and +1 and fell about 26% over six months.
2. **Abnormal return.** Benchmark-adjusted moves were positive on days 0–1 and negative over [0,+10].
3. **Statistical significance.** Eight tests were run (4 windows × 2 benchmarks). The Bonferroni-adjusted two-sided 5% threshold is |t| > 2.73. **None of the post-event CARs clears it.** The first pass described CAR[0,+1] vs SMH (t = 2.22) without this adjustment; it is nominally significant only (correction SI1-PE-02 below).
4. **Economic materiality.** A 4–6% move in a company of this size is economically large in dollar terms, but materiality of a price move is not evidence about its cause.
5. **Causal attribution.** **None.**
   - Earnings were released after the close on day +5 (SI1-PST-006).
   - An $11.9bn acquisition was announced on 2 Sep 2026 (SI1-PST-005).
   - The Singapore and Malaysian statements of 12–13 Nov 2026 fall in the last sessions of the window.
   - The CEO resigned on 11–12 Nov 2026 (SI1-PST-003).
   - The sector fell 13.3% (SMH).
   - Any same-day news was not screened.

**Method limitations:**
- Event windows and horizons were chosen by the researcher, not pre-registered.
- SMH holds NVDA, which biases NVDA-vs-SMH comparisons toward zero.
- t-statistics assume normal, independent residuals over a 120-session estimation window.
- Adjusted closes were retrieved after the events (2026-11-15). Recomputing on unadjusted closes changes the post-event CARs by at most 0.07 pp.
- A decline after an event does not show the event caused it.

## 4. What changed in this pass (2026-11-15, second pass)

| Change | Reason |
|---|---|
| Added SI1-PST-013 (MHA), SI1-PST-014 (MITI) and SI1-PST-015 (3 Mar 2025 transcript, located post hoc), with claims SI1-V-07 to SI1-V-13 | Primary sources retrieved directly (HTTP 200) and checked against their text |
| Culper report status restated: not directly examined; index excerpts recorded as SI1-PST-016 / SI1-V-14 (S2) | The earlier "secondary summaries" status was accurate; this pass adds index excerpts without presenting them as direct examination |
| Replaced "Independently anticipated" with a separate retrospective-relation column | The case was reconstructed with the outcome known; the old label overstated predictive validity |
| F5 split into F5a (investigation exists: Confirmed) and F5b (diversion to China: Not established) | A government investigation proves neither an unlawful act nor a final destination |
| Corrected SI1-V-03 (erratum SI1-PE-01) | The original paraphrase dropped "such" |
| Added a multiple-comparison note to the market section (SI1-PE-02) | The first pass reported nominal significance only |
| Pre-event statistics and availability corrections SI1-E-01 to SI1-E-04 | Recorded as append-only errata; no pre-event interpretation changed |

**SI1-PE-02 (2026-11-15).** The first pass reported "CAR[0,+1] +4.6% vs SMH, t = 2.2" as part of the F6 row without a multiple-comparison adjustment. After Bonferroni adjustment it is not significant. The direction stands; its statistical weight is lower. The F6 row has been replaced by the two market-hypothesis rows above.

## 5. What this case does not show

- That MON-SI methods predict anything.
- That NVIDIA, Megaspeed, Speedmatrix or any other party acted unlawfully.
- That any NVIDIA chip reached China through the channels examined.
- That the short report's figures are right or wrong.
- That any share-price change was caused by the report, the investigations or any disclosure.
