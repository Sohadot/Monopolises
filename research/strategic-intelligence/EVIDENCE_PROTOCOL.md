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

## 7. Hindsight controls (retrospective cases)

1. Cutoff fixed before analysis; pre-event register frozen before the validation file is written.
2. The outcome document (e.g. a short-seller report) is never a pre-event source.
3. The researcher's prior knowledge of the outcome, and the effect it had on the research question and on search queries, is disclosed in the case.
4. Retrospective agreement with the outcome is **never** presented as predictive performance.

## 8. Source discipline

Primary first: SEC filings, BIS rules/guidance, foreign trade-ministry instruments, government statements, charging documents, official registries. Secondary reporting is a **lead** — recorded as excluded or S2 until traced to a primary document. Inaccessible documents (paywall, 403/404, blocked archive) are recorded as such, never reconstructed from memory or summaries.
