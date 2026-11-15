# Evidence and Provenance Protocol — Monopolises Strategic Intelligence (candidate)

**Status:** CANDIDATE — non-binding; applies to MON-SI cases prepared on this branch.
**Machine enforcement:** `tools/check_registers.py` (run by `tests/test_strategic_intelligence.py`).

## 1. Two periods, two registers, one direction of flow

Every case has a **cutoff** (UTC timestamp) and two registers:

| Register | Admits | May be cited by |
|---|---|---|
| `register.pre-event.json` | Only sources whose **availability** is demonstrated at or before the cutoff | `PRE_EVENT_ANALYSIS.md` and `POST_EVENT_VALIDATION.md` |
| `register.post-event.json` | Sources available after the cutoff, plus later market data | `POST_EVENT_VALIDATION.md` only |

Information flows **pre → post only**. The pre-event analysis may not cite a post-event identifier, and may not use post-event facts outside a delimited hindsight-disclosure block (`<!-- hindsight-disclosure:start -->` … `<!-- hindsight-disclosure:end -->`). Both rules are machine-checked.

## 2. Publication date ≠ availability date

Four dates are kept apart (second pass, 2026-11-15):

| Date | Meaning | What establishes it |
|---|---|---|
| Document date / creation | When the document was written or the file was created | The date on its face; PDF CreationDate/ModDate |
| Official publication date | When the issuer says it released the document | Release header, filing date |
| Demonstrated public availability | When anyone could in fact have read it | EDGAR acceptance (dissemination); a contemporaneous independent capture; same-day third-party citation |
| Research retrieval date | When this project fetched it | Retrieval log |

PDF metadata and an official date **do not by themselves demonstrate** public availability. Each pre-event register carries an append-only `addenda.availability_review` rating every admitted source `demonstrated`, `inferred_from_official_date` or `insufficiently_demonstrated`. An S0/S1 claim may not rest solely on sources rated `insufficiently_demonstrated` (machine-checked). Frozen `availability_utc` values are not rewritten.

- `publication_date` — the date the document bears.
- `availability_utc` — the earliest moment the document is **demonstrably** public, with `availability_basis` stating how that was established (e.g. EDGAR acceptance timestamp, official release date, PDF metadata consistent with the stated date).
- If availability before the cutoff cannot be demonstrated, the source is **excluded** from inference (`status: "excluded"`) and the uncertainty is recorded. Example in MON-SI-001: the BIS diversion-guidance PDF now served carries 2026 creation metadata, so its red-flag text is excluded even though the 13 May 2025 press release that links it is admitted.
- EDGAR `acceptanceDateTime` is recorded as reported. Where an intraday time matters for an event study, the session in which it fell is stated explicitly.

## 3. Evidence classes (carried over from MON-G1-LI, extended for finance)

- **S0** — the primary source states the fact.
- **S1** — reproducible mechanical derivation from S0 facts (arithmetic shown, inputs cited).
- **S2** — interpretive synthesis, secondary reporting, or a primary document that only *relays* a secondary claim (e.g. a legislator's letter citing a newspaper). S2 may motivate a hypothesis or record a lead; **S2 cannot carry a finding.**

## 4. Mandatory fields per material claim

`claim_id`, `source_ids`, `pinpoint`, `supporting_passage` (short verbatim quote or table reference), `evidence_class`, `scope` (incl. jurisdiction and period), `excluded_implications` (≥1), `counterevidence_or_alternative`. Each source carries `publisher`, `title`, `canonical_ref`, `url`, `publication_date`, `availability_utc`, `availability_basis`, `retrieved`, `discovery_path`, `hindsight_flag`.

`discovery_path` and `hindsight_flag` record **how the researcher found the source**. A source located by a query that was shaped by knowledge of the outcome is flagged, even when its pre-cutoff availability is proven: availability shows the evidence *existed*; it does not show a blind analyst would have *prioritized* it.

## 5. Supply-chain distinctions that must stay separate

Physical movement · contractual purchaser · billing/invoicing location · customer headquarters · corporate ownership · financing · end user / beneficial demand · cloud-compute access vs physical chip ownership.

No claim may move from one of these to another without a source that bridges them. In particular: **billing geography is not shipment evidence; HQ geography is not end-use evidence; an indictment is an allegation.**

## 6. Financial-analysis standards

- Figures come from the filing that was public at the cutoff; later recasts are post-event evidence.
- No invented revenue allocations or probabilities. Sensitivities are mechanical (e.g. "each 1% of Data Center revenue = $X") and labelled as such.
- Market data: adjusted closes, exchange trading dates (America/New_York), day 0 = first session at or after the event timestamp.
- Event study: market model by OLS over sessions [−130, −11]; report CAR and t-statistics for fixed windows; report benchmark-relative buy-and-hold for longer horizons with **no causal attribution**. Benchmarks: a sector ETF (SMH) and the broad market (SPY). SMH holds NVIDIA itself, which biases NVDA-vs-SMH comparisons toward zero; this is disclosed, not corrected.
- Confounding events inside a window (earnings, other corporate actions, macro shocks) are listed whenever the researcher knows of them; an unlisted confounder is not evidence that none existed.
- Raw vendor price files are not committed (redistribution terms); the retrieval source and date are recorded, and the computation is reproducible with `tools/event_study.py`.

## 6b. Inference (third pass, 2026-11-15)

- **Reference distribution:** Student-t with T − 2 = 118 degrees of freedom (120 estimation sessions; intercept and slope). Normal critical values may be quoted only as a labelled asymptotic reference.
- **Residual variance** uses n − 2 degrees of freedom. `event_study.py` uses `statistics.stdev` (n − 1); its frozen outputs are kept, and the corrected values are in `event-study-inference-correction.json` (from `tools/inference_correction.py`).
- **CAR standard error** includes market-model estimation error: Var(CAR) = s²·[L + L²/T + (Σ_event(R_m,t − R̄_m))² / S_xx] (Campbell, Lo and MacKinlay 1997, ch. 4).
- **Family-wise control:** Bonferroni at 5% two-sided over every window × benchmark test reported for the case. MON-SI-001 thresholds: 24 pre-event tests → |t| > 3.148; 8 post-event tests → |t| > 2.784. Overlapping windows make Bonferroni conservative.
- **Assumptions:** i.i.d. normal residuals with constant variance and no event-induced variance change. Daily returns have heavy tails and volatility clustering, so all statistics are approximate.

## 6a. Market-reaction limits (second pass)

Report the following as five separate things: observed price movement; benchmark-relative abnormal return; statistical significance after multiple-comparison adjustment (Bonferroni across every window × benchmark test run for the case); economic materiality; and causal attribution, which is never inferred from co-movement. Also disclose: whether windows were pre-registered; known confounders; benchmark contamination; and the data vintage (adjusted prices retrieved after the event, with a raw-close sensitivity check).

## 7. Hindsight controls (retrospective cases)

1. Cutoff fixed before analysis; pre-event register frozen before the validation file is written.
2. The outcome document (e.g. a short-seller report) is never a pre-event source.
3. The researcher's prior knowledge of the outcome, and the effect it had on the research question and on search queries, is disclosed in the case.
4. Retrospective agreement with the outcome is **never** presented as predictive performance. Validation uses two columns: an evidentiary status (Confirmed · Partially corroborated · Unresolved · Contradicted · Not established) and a retrospective relation (Retrospectively consistent — no prospective credit · Not discoverable with the pre-event evidence · Not applicable). Labels such as "anticipated" or "predicted" are rejected by the checker.
5. **Freeze and errata.** After a pre-event reconstruction is complete, its hashes are recorded in `FREEZE_MANIFEST.json`. Later corrections are appended as dated errata stating the original text, the correction, and whether the interpretation changes; the frozen text is never edited. A pre-cutoff document located after the fact through post-event material stays out of the pre-event inference and is flagged `pre_cutoff_document_located_post_hoc` in the post-event register.
6. **Allegation documents.** Claims from an allegation document are classed A (documented primary fact, verified in a primary source), B (reproducible calculation from public inputs), C (allegation or hypothesis, S2) or D (unsupported or unresolved). A regulator's investigation, check or refusal to "clear" a company is a procedural fact, not evidence of an offence.

## 8. Source discipline

Primary first: SEC filings, BIS rules/guidance, foreign trade-ministry instruments, government statements, charging documents, official registries. Secondary reporting is a **lead** — recorded as excluded or S2 until traced to a primary document. Inaccessible documents (paywall, 403/404, blocked archive) are recorded as such, never reconstructed from memory or summaries.
