# MON-SI-G0 — Strategic Economic Intelligence Feasibility Gate

**Gate ID:** MON-SI-G0
**Status:** PROPOSED
**Opened:** — (requires owner authorization; see `CHARTER.md` §7)
**Verdict:** none. This gate has **not** been evaluated and **cannot** pass on documentation or on retrospective work.
**Relationship to v0.2:** complementary; adds no layer and alters no closed gate (MON-G0-RH FAIL; MON-G1-LI, MON-G2-OF, MON-G3-IT, MON-G4-DA PASS remain as recorded).

## Governing question

> Can Monopolises produce, from **dated public primary evidence**, economic-intelligence findings that are (a) reproducible by a second reviewer, (b) free of cross-period contamination, (c) economically material, and (d) **prospectively** borne out more often than a pre-registered naive baseline — without legal conclusions, monopoly classifications, scores, or trading signals?

## Scope

In scope: supply-chain, ownership, regulatory and financial-exposure analysis of bounded, dated systems; market-expectation analysis using benchmark-relative event studies.
Excluded: legal or antitrust conclusions; monopoly/dominance classification; entity rankings or scores; trading signals, price targets, personalized advice; live monitoring; publication; commercialization.

## Fixed case design

- **Calibration case (retrospective):** MON-SI-001 (NVIDIA, cutoff 2026-05-12T23:59Z). It tests **process** criteria P1–P4 only. It is **permanently excluded from P5**, because its outcome was known before the research began. Agreement between its reconstruction and later events is labelled *retrospectively consistent — no prospective credit* and never counts as a prediction.
- **Prospective cases:** at least **5** cases registered under §6 below, each with ≥1 pre-registered risk condition, observation windows of 90–365 days, registered at different dates over ≥ 90 days of calendar time. Case selection criteria are written down before any case is chosen.

## Pass criteria (all must hold)

| ID | Criterion | Measurement |
|---|---|---|
| P1 | **Provenance integrity** — 100% of admitted pre-event sources have availability ≤ cutoff; 0 post-event identifiers or forbidden facts in pre-event analyses | `tools/check_registers.py` passes on every case |
| P2 | **Reproducibility** — an independent second reviewer, given only the frozen pre-event register, reaches the same S0/S1 findings (or records a disagreement) on ≥ 80% of material claims | Second-review sheet per case |
| P3 | **Materiality** — each case states a mechanism linking the finding to a named line item (revenue, margin, inventory, guidance) with a mechanical sensitivity | Present / absent per case |
| P4 | **Honest negatives** — each case records what could *not* be inferred, and at least one case reports a negative or unresolved result | Present / absent |
| P5 | **Prospective validity** — of all pre-registered risk conditions with closed windows, the share resolved "occurred" exceeds the pre-registered naive baseline for the same conditions, with ≥ 10 resolved conditions | Resolution log; baseline fixed at registration |

## Failure conditions (any one → FAIL)

- F1 A pre-event finding is shown to rest on information not available at the cutoff.
- F2 A registered hypothesis, window or success criterion is edited after registration (other than an appended, dated correction that leaves the original visible and is scored as originally written).
- F3 Fewer than 10 prospective conditions resolve within 18 months of opening (insufficient evidence ⇒ FAIL, not "pending forever").
- F4 Prospective hit rate ≤ baseline.
- F5 Any case relies on S2 for a finding, asserts unlawful conduct without a charging or adjudicating document, or attributes a price move to a cause without stating that the attribution is a hypothesis.
- F6 Any output introduces a layer, score, ranking, or trading signal.

## Look-ahead bias controls

Fixed cutoffs; separate registers; availability ≠ publication; `discovery_path` + `hindsight_flag` on every source; frozen commit hash for each registration; prospective cases scored only after their windows close.

## §6 Prospective validation protocol

1. **Registration record** (committed before the window opens; commit hash and UTC timestamp are the registration proof): case ID, system boundary, cutoff, frozen pre-event register (all sources archived or hashed), hypotheses, the alternative explanations considered, and *predicted risk conditions* — each a concrete, externally observable development (e.g. "a government of jurisdiction X announces a licensing/permit change covering product class Y"), not a price direction.
2. **Observation window** with explicit start/end dates; resolution sources named in advance (which registry, docket, filing type).
3. **Success / failure criteria and a naive baseline** fixed at registration (e.g. the base rate of comparable events over the prior 24 months, or 50% where no base rate exists — whichever is stated in advance).
4. **No retroactive edits.** Corrections are appended, dated, and scored against the original text.
5. **Negative results are recorded** in the same file as positives; a case cannot be withdrawn after registration.
6. **Resolution** by a reviewer other than the registrant where possible; disagreements recorded.
7. Market data may be reported descriptively at resolution; it is **not** a success criterion.

Prospective validation will **not** be claimed until real observation windows have closed.

## Current evaluation state

| Criterion | State |
|---|---|
| P1 | MON-SI-001 passes the automated check (process evidence only). Second pass (2026-11-15): freeze hashes, availability review and dated errata added; one source (SI1-SRC-013) rated insufficiently demonstrated, carrying S2 only |
| P2 | Not run — no second reviewer yet |
| P3 | MON-SI-001: mechanism and mechanical sensitivity documented |
| P4 | MON-SI-001: negatives and unresolved items documented |
| P5 | **Not started** — zero prospective cases registered; MON-SI-001 contributes nothing to P5 |

**Verdict: none (PROPOSED).**
