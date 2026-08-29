# Monopolises

Monopolises is a **governed strategic-reference research project**. It investigates where control concentrates inside complex systems, through which mechanism, and with what evidence — without inferring legal monopoly status, dominance, or unbounded company control.

GitHub is the **source of truth**. Binding decisions live in [`DECISION_LOG.md`](DECISION_LOG.md).

---

## Quick Start (~10 min)

**For:** external research readers — journalists, policy or competition analysts, or anyone curious about the project (e.g. a first visit from a link).

**Goal:** understand **one complete record** — system, layer, mechanism, locus, evidence, and claim boundary — without prior context.

**Start with S8** (U.S. Private Express Statutes). It is the clearest positive control: a named legal instrument, bounded locus, and explicit claim boundary. It does not represent all of Monopolises, but it is the least ambiguous entry point.

| Step | Read | What you get |
|---|---|---|
| 1 | This page (above) | What Monopolises is — and what it is **not** (no legal monopoly finding) |
| 2 | [`cases/MON-G1-S8.md`](research/v0.2/cases/MON-G1-S8.md) | The full case record: system, layer, mechanism, S0 evidence, claim boundary |
| 3 | [`interface/representations/MON-G1-S8.md`](research/v0.2/interface/representations/MON-G1-S8.md) | How the record is presented under the adopted interface grammar |
| 4 | [`SOURCE_REGISTER_v0.2.md`](research/v0.2/SOURCE_REGISTER_v0.2.md) — rows MON2-SRC-001…004 | Primary sources behind the evidence |
| 5 | [`research/v0.2/README.md`](research/v0.2/README.md) | Full methodology — gates, ontology, evaluations (when you want the *how*) |

**Self-check** — after following the Quick Start, **without looking at an answer key**, can you state:

- What exactly is the bounded **System**?
- Which **control layer** was evidenced?
- What is the **control mechanism**?
- Where exactly is the **locus**?
- Which primary instruments carry the **evidence**?
- Which broader claims does the **claim boundary exclude**?

Verify your answers against the [S8 case record](research/v0.2/cases/MON-G1-S8.md) and [G3 representation](research/v0.2/interface/representations/MON-G1-S8.md).

All eight cases: [`research/v0.2/cases/README.md`](research/v0.2/cases/README.md).

---

## What is currently adopted? (v0.2)

The active research line is **Layered Monopolisation v0.2**. Its logical specification chain is **complete**:

| Layer | Status | Decision | Canonical artifact |
|---|---|---|---|
| Thesis | Ratified | [DEC-005](DECISION_LOG.md#dec-005--ratify-layered-monopolisation-as-the-monopolises-v02-thesis) | [`research/v0.2/THESIS_CANDIDATE.md`](research/v0.2/THESIS_CANDIDATE.md) |
| Layer identifiability | Closed PASS | DEC-005 | [`MON-G1-LI`](research/v0.2/LAYER_IDENTIFIABILITY_GATE.md) |
| Ontology | Adopted | [DEC-006](DECISION_LOG.md#dec-006--close-mon-g2-of-and-adopt-the-layered-monopolisation-ontology-v02) | `mon-g2-of-candidate-v0.2` |
| Interface thesis | Adopted | [DEC-007](DECISION_LOG.md#dec-007--close-mon-g3-it-and-adopt-the-layered-monopolisation-interface-thesis-v02) | `mon-g3-it-candidate-v0.2` |
| Data architecture | Adopted | [DEC-008](DECISION_LOG.md#dec-008--close-mon-g4-da-and-adopt-the-layered-monopolisation-data-architecture-v02) | `mon-g4-da-candidate-v0.2` |

**Active taxonomy (four evidenced layers):** `legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `switching_dependency`.

**Unit of record:** `System × Layer × Control Mechanism × Evidence`

**Build policy:** The logical specification chain is complete. **Production implementation is not authorized.** Any production database, API, UI/interface implementation, publishing system, or other operationalization requires separate authorization under a new falsifiable gate **or** binding decision (DEC-008). Scored, ranked, or scaled surfaces — and admission of new layers — require a new decision **and** a new falsifiable gate (DEC-005). Monetization remains unauthorized.

---

## What was rejected or archived?

Earlier repository-era research is **retained as provenance**, not deleted:

| Research line | Verdict | Decision | Where to read |
|---|---|---|---|
| Declared Dependency (SaaS 10-K Item 1/1A as primary thesis) | Rejected | [DEC-001](DECISION_LOG.md#dec-001--reject-declared-dependency-as-primary-data-thesis) | `DECISION_LOG.md` |
| Strategic Replaceability / Replacement Horizon v0.1 | Gate FAIL | [DEC-004](DECISION_LOG.md#dec-004--close-mon-g0-rh-and-reject-strategic-replaceability-v01-as-the-primary-measurement-thesis) | [`research/GATE_0_CLOSEOUT.md`](research/GATE_0_CLOSEOUT.md), [`FOUNDATION_THESIS.md`](FOUNDATION_THESIS.md) |

These lines are **not** the current adopted thesis. They explain why the project pivoted to Layered Monopolisation.

---

## Where should I start reading?

**New here?** Follow [Quick Start (~10 min)](#quick-start-10-min) above — one complete record (S8) first.

**Full methodology:** [`research/v0.2/README.md`](research/v0.2/README.md) — the v0.2 Research Reading Map.

Short path (internal / research order):

1. [Thesis](research/v0.2/THESIS_CANDIDATE.md) — what Layered Monopolisation claims
2. [Eight evidence cases](research/v0.2/cases/) — how the thesis was tested (MON-G1-LI)
3. [Decision log](DECISION_LOG.md) — binding decisions DEC-005 through DEC-008
4. Adopted specifications — ontology → interface thesis → data architecture (details in the reading map)

For Gate 0 history only: [`research/GATE_0.md`](research/GATE_0.md) and [`research/GATE_0_CLOSEOUT.md`](research/GATE_0_CLOSEOUT.md).

---

## Public site

The public site is intentionally small and may lag the repository. For current adopted status, use this README and [`DECISION_LOG.md`](DECISION_LOG.md).
