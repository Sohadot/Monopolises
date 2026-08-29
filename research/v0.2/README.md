# Monopolises v0.2 — Research Reading Map

This map orients an external reader through the **adopted** Layered Monopolisation research line. It does not authorize production implementation.

**Checkpoint:** merge `ee97aca` (2026-08-29) — MON-G4-DA Closed PASS; DEC-008 adopted `mon-g4-da-candidate-v0.2`.

---

## Reading order

Follow this path top to bottom. Each step has a gate that tested a specific question before the next layer was authorized.

### 1. Thesis — what the project claims

| Read | Purpose |
|---|---|
| [`THESIS_CANDIDATE.md`](THESIS_CANDIDATE.md) | Layered Monopolisation v0.2 proposition, unit of record, four active layers |
| [`../GATE_0_CLOSEOUT.md`](../GATE_0_CLOSEOUT.md) | Why v0.1 (Replacement Horizon) failed — context only |
| [`../../DECISION_LOG.md`](../../DECISION_LOG.md) § DEC-005 | Binding ratification of the thesis |

### 2. Gate MON-G1-LI — can layers be identified from evidence?

| Read | Purpose |
|---|---|
| [`LAYER_IDENTIFIABILITY_GATE.md`](LAYER_IDENTIFIABILITY_GATE.md) | Governing question, PASS criteria, falsifiers |
| [`cases/`](cases/) | Eight fixed evidence cases (`MON-G1-S1` … `MON-G1-S8`) |
| [`GATE_MON-G1-LI_EVALUATION.md`](GATE_MON-G1-LI_EVALUATION.md) | Full-set evaluation — Gate PASS; 7/8 second-review convergence, S2 marginal |
| [`SOURCE_REGISTER_v0.2.md`](SOURCE_REGISTER_v0.2.md) | Primary sources for the eight cases |

**Outcome:** DEC-005 ratifies the thesis and authorizes ontology → interface → data architecture (in that order).

### 3. Gate MON-G2-OF — can identifications survive formal ontology?

| Read | Purpose |
|---|---|
| [`ONTOLOGY_FIDELITY_GATE.md`](ONTOLOGY_FIDELITY_GATE.md) | Gate spec (Closed PASS) |
| [`ontology/CANDIDATE_ONTOLOGY_SCHEMA.md`](ontology/CANDIDATE_ONTOLOGY_SCHEMA.md) | Adopted ontology (`mon-g2-of-candidate-v0.2`) |
| [`GATE_MON-G2-OF_EVALUATION.md`](GATE_MON-G2-OF_EVALUATION.md) | 8/8 round-trip evaluation |
| [`../../DECISION_LOG.md`](../../DECISION_LOG.md) § DEC-006 | Binding adoption |

### 4. Gate MON-G3-IT — can ontology be presented without overclaiming?

| Read | Purpose |
|---|---|
| [`INTERFACE_THESIS_GATE.md`](INTERFACE_THESIS_GATE.md) | Gate spec (Closed PASS) |
| [`CANDIDATE_INTERFACE_THESIS.md`](CANDIDATE_INTERFACE_THESIS.md) | Adopted interface grammar (`mon-g3-it-candidate-v0.2`) |
| [`interface/representations/`](interface/representations/) | Rendered representations of the eight cases |
| [`GATE_MON-G3-IT_EVALUATION.md`](GATE_MON-G3-IT_EVALUATION.md) | Blind readback evaluation (8/8 PASS) |
| [`../../DECISION_LOG.md`](../../DECISION_LOG.md) § DEC-007 | Binding adoption |

### 5. Gate MON-G4-DA — can meaning survive storage and retrieval?

| Read | Purpose |
|---|---|
| [`DATA_ARCHITECTURE_GATE.md`](DATA_ARCHITECTURE_GATE.md) | Gate spec (Closed PASS) |
| [`CANDIDATE_DATA_ARCHITECTURE.md`](CANDIDATE_DATA_ARCHITECTURE.md) | Adopted logical architecture (`mon-g4-da-candidate-v0.2`) |
| [`GATE_MON-G4-DA_EVALUATION.md`](GATE_MON-G4-DA_EVALUATION.md) | Persistence/retrieval evaluation (8/8 PASS) |
| [`data-architecture/persistence-report.json`](data-architecture/persistence-report.json) | Machine-readable evaluation report |
| [`../../DECISION_LOG.md`](../../DECISION_LOG.md) § DEC-008 | Binding adoption |

### 6. Decision log — binding record

| Read | Purpose |
|---|---|
| [`../../DECISION_LOG.md`](../../DECISION_LOG.md) | Append-only decisions DEC-001 … DEC-008 |

DEC-005 through DEC-008 are the adopted v0.2 chain. Earlier decisions (DEC-001, DEC-004) record rejected or superseded research lines.

---

## What this map is not

- **Not** a product roadmap — production DB, API, UI, and publishing are **not authorized** (DEC-008).
- **Not** a scoreboard — no rankings, dominance levels, or entity/sector pages.
- **Not** a legal finding — "monopolised" here means structural control concentration, not antitrust conclusion.

---

## One-minute summary

> Markets are rarely monopolised all at once. They are monopolised **layer by layer**.
>
> Monopolises v0.2 asks: **where** does control concentrate, **through which mechanism**, and **with what evidence** — recorded as `System × Layer × Control Mechanism × Evidence`, classifiable from public primary sources.

The thesis passed identifiability testing (MON-G1-LI), survived formal ontology (MON-G2-OF), can be presented without semantic distortion (MON-G3-IT), and can be stored and retrieved without ownership loss (MON-G4-DA). The logical specification chain is complete. What comes next requires a separate decision about the first operational surface worth building.
