# Monopolises Strategic Intelligence — Candidate Research Charter

**Status:** CANDIDATE — non-binding. Not ratified. No decision recorded in `DECISION_LOG.md`.
**Prepared:** 2026-11-15 (research-preparation branch; draft pull request only)
**Proposed gate:** [`GATE_MON-SI-G0.md`](GATE_MON-SI-G0.md) — status **PROPOSED, not opened**
**Protocol:** [`EVIDENCE_PROTOCOL.md`](EVIDENCE_PROTOCOL.md)
**First prototype case:** [`cases/MON-SI-001/`](cases/MON-SI-001/) — NVIDIA advanced AI compute supply-chain exposure (retrospective)

> This charter proposes a complementary research discipline. It does not amend the Layered Monopolisation v0.2 thesis, its four-layer taxonomy, the adopted ontology, interface thesis, or data architecture, and it does not reopen any closed gate. Nothing here is published on the six public routes.

---

## 1. Purpose

Investigate economic structures — market structure, physical and contractual supply chains, ownership and financing, trade regulation, financial exposure, and market expectations — in order to identify **potentially material risks or opportunities before they are fully reflected in public expectations**, using only reproducible, dated, source-traceable evidence.

The output is **research records**, not reports for sale, trading signals, price targets, rankings, or legal conclusions.

## 2. Six analytical disciplines

| # | Discipline | Primary evidence it relies on | What it must never infer alone |
|---|---|---|---|
| 1 | Market structure / industrial economics | Filings, official supply-chain reviews | Dominance, legal monopoly status |
| 2 | Physical vs contractual supply chain | Filings, customs/permit regimes, enforcement records | Physical destination from billing or HQ geography |
| 3 | Ownership, financing, incentives | Registries, filings, court records | Misconduct from incentive |
| 4 | Trade regulation / geopolitical exposure | BIS rules and guidance, foreign trade-ministry instruments | Violation from exposure |
| 5 | Financial statements and valuation sensitivity | 10-K/10-Q/8-K, company outlook | Probabilities or allocations the sources do not state |
| 6 | Market reactions and later validation | Contemporaneous price data, benchmark-relative event studies | Causation from co-movement |

## 3. Relationship to Layered Monopolisation v0.2 (DEC-005 … DEC-008)

- Strategic intelligence **adds no layer** and **assigns no layer**. Its records carry no `layer`, score, rank, severity, or dominance field (enforced by `tools/check_registers.py`).
- An export-control dispute, a corporate dependency, or a diversion investigation is **not** evidence of monopolisation. Where a strategic-intelligence finding appears to touch the adopted ontology, it may be recorded only as an **ontology lead** with an explicit justification; turning it into a v0.2 record would require a separate case under the existing governance.
- MON-SI-001 concerns NVIDIA. It does **not** revisit **MON-G1-S3** (CUDA, 2025: `no_evidenced_control_layer`). That result stands unchanged.

## 4. Governance position and identified conflicts

| Binding constraint | Effect on this work | How this branch complies |
|---|---|---|
| DEC-004 next-thesis rule / DEC-005 next-gate rule — new research lines begin with a **new decision and a new falsifiable gate** | Opening MON-SI-G0 formally requires owner authorization | MON-SI-G0 is written as **PROPOSED**; MON-SI-001 is labelled **pre-gate exploratory prototype**; no PASS/FAIL is declared |
| DEC-005 — no scores, rankings, entity/sector pages; unit of record is not `Company × Score` | An entity-focused case risks drifting into an entity dossier | The case is bounded to a dated *system* (NVIDIA-originated advanced compute flowing to China-linked demand, 2025 – May 2026); no score or ranking exists |
| DEC-008 — no production DB, API, publishing system, or operationalization | Registers could be mistaken for a database | Registers are static JSON research artifacts (same status as `ontology/instances/*.json`); no service, ingestion or API |
| DEC-009 / DEC-010 — public routes are editorial/presentation-only | Publication would require a separate decision | No public route, sitemap, `llms.txt` or design file is touched (enforced by test) |
| Monetization unauthorized (DEC-004, DEC-005, DEC-008) | "Commercially relevant" intelligence could be read as a product | No commercialization, subscription, client delivery, or investment advice is authorized or prepared |

**Conflict noted, not bypassed:** the request to "open" a research gate cannot be fulfilled by documentation alone. The draft authorization below is offered for owner decision.

## 5. Independence and conflicts of interest (required disclosure for every case)

- **MON-SI-001 disclosure status: Not independently verified / declaration pending.** No signed declaration of positions, funding, or engagements exists for this case. A declaration is required from the repository owner and from each human contributor or reviewer before any further use. *Correction (2026-11-15): the first pass stated that the preparer held no position; that statement was not based on a verified declaration and is withdrawn.*
- Every future case must record: researcher positions (including derivatives and short positions), funding source, any engagement with a party named in the case, and any reliance on a party with a disclosed position (e.g. a short-seller report).
- A short-seller or activist report may be used **only** in a post-event validation section, labelled with the author's disclosed position. Such a report is primary evidence of **what its author alleged**, never of the truth of the allegations, and it is S0 only for the existence and wording of the allegation, and only where the document itself was examined.

## 6. Publication and commercialization restrictions

- No case, dossier, register, or finding is published on monopolises.com or elsewhere without a separate owner decision.
- No trading signals, price targets, buy/sell language, or personalized advice — ever, under this charter.
- No allegation of unlawful conduct by a named party unless a court, regulator, or charging document states it — and then only with that document's own wording, including any presumption-of-innocence language.
- Proprietary data (trade databases, consensus estimates, paid registries) are not reproduced; their absence is recorded as a limitation.

## 7. Draft authorization proposal (NON-BINDING — for owner review only)

> *The following is a proposal text. It is deliberately **not** inserted into `DECISION_LOG.md`.*
>
> **Proposed DEC-0XX — Open MON-SI-G0 (Strategic Economic Intelligence Feasibility Gate) as a bounded research experiment.**
> Authorize, as research only: (1) opening gate MON-SI-G0 exactly as specified in `research/strategic-intelligence/GATE_MON-SI-G0.md` at a frozen commit; (2) treating MON-SI-001 as a *retrospective calibration case* that cannot by itself pass the gate; (3) registering prospective cases under §6 of the gate.
> **Not authorized:** publication, entity pages, scores or rankings, new layers, changes to v0.2 artifacts, production systems, live monitoring, client delivery, or monetization. Any of these requires a further decision.
> **Closure:** MON-SI-G0 closes only on its predefined criteria; it is not broadened or redefined to obtain a pass.

## 8. Reading order

1. This charter → 2. [`EVIDENCE_PROTOCOL.md`](EVIDENCE_PROTOCOL.md) → 3. [`GATE_MON-SI-G0.md`](GATE_MON-SI-G0.md) →
4. [`cases/MON-SI-001/PRE_EVENT_ANALYSIS.md`](cases/MON-SI-001/PRE_EVENT_ANALYSIS.md) (with `register.pre-event.json`) →
5. [`cases/MON-SI-001/POST_EVENT_VALIDATION.md`](cases/MON-SI-001/POST_EVENT_VALIDATION.md) (with `register.post-event.json`).

Checks: `python3 -m unittest discover -s tests -v` (runs the existing public-reference tests and `tests/test_strategic_intelligence.py`).
