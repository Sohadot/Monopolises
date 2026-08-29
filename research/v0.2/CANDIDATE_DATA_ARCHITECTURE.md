# Candidate Data Architecture — Monopolises v0.2

**Gate:** MON-G4-DA (Data Architecture Fidelity)
**Architecture ID:** `mon-g4-da-candidate-v0.2`
**Status:** **ADOPTED — MON-G4-DA Closed PASS — 2026-08-29**
**Gate spec:** `DATA_ARCHITECTURE_GATE.md` (DESIGN FROZEN — accepted 2026-08-29, revision 2)
**Ontology binding:** `mon-g2-of-candidate-v0.2` (DEC-006 adopted)
**Interface binding:** `mon-g3-it-candidate-v0.2` (DEC-007 adopted)
**Authority:** DEC-005 + DEC-006 + DEC-007 + frozen MON-G4-DA gate
**Opened:** 2026-08-29

> This document is the **canonical candidate logical data architecture**. It defines how adopted ontology `SystemRecord`s may be **stored and retrieved** without reorganizing meaning. It does **not** specify DDL, a database engine, ORM, API, or production deployment. Step 3 will apply these contracts under the blind persistence/retrieval protocol.

### Governing principle (inherited)

> The data architecture may reorganize storage. It may not reorganize meaning.

### Design stance (not a JSON blob; not a meaning rewrite)

This architecture **normalizes storage** into owned logical records so that:

- per-layer ownership is explicit in storage relationships (not only inside a nested document);
- secondary indexes and optional label tables can exist without becoming semantic authority;
- dated snapshots remain independently addressable for history;

…while a **single generic read path** always reconstructs a canonical `SystemRecord` identical in semantic content to the adopted ontology (after the gate’s case-independent comparison canonicalization).

It is **not** “persist the input JSON as one opaque blob.”  
It is **not** a relational redesign that makes company/entity the root, shares boundaries/evidence across layers, or invents score/confidence fields.

---

## 1. Ownership / relationship model

### 1.1 Logical record kinds

| Logical record | Owns / role | Semantic authority? |
|---|---|---|
| **SystemSnapshot** | One immutable write of a dated system finding: system `scope`, `date`, `outcome`, and pointers to child records | **Yes** — participates in canonical read root |
| **SystemLineage** (technical only) | Optional opaque grouping of snapshots that are successive dated states of the “same logical system” for history/access | **No** — harness/external keys and internal lineage IDs never appear in canonical `SystemRecord` |
| **EvidencedLayer** | One evidenced layer under exactly one SystemSnapshot; may carry non-semantic presence marker for optional `holders` | **Yes** — layer owner |
| **HolderOccurrence** | One holder label occurrence under exactly one EvidencedLayer | **Yes** as layer-owned list member; label string is semantic |
| **EvidenceBinding** | One claim↔class↔source↔fact↔(derivation?) under exactly one EvidencedLayer | **Yes** — binding owned by that layer |
| **ClaimBoundary** | Admissible + excluded[] owned by exactly one EvidencedLayer **or** exactly one zero-record assessment | **Yes** — not shared |
| **NegativeAssessment** | Examined + refusals + boundary for `no_evidenced_control_layer` | **Yes** when outcome requires it |
| **AmbiguityAssessment** | Competing interpretations + separation_gap + refusals? + boundary | **Yes** when outcome requires it |
| **RefusalAssessment** | System-level refusal notes on positive outcomes only | **Yes** when present |
| **RefusalReference** | candidate_label + status + reason under exactly one assessment owner | **Yes** as assessment content |
| **CompetingInterpretation** | One ambiguity option under AmbiguityAssessment | **Yes** as assessment content |
| **EntityLabel** (optional technical) | Normalized spelling/alias table for holder strings | **No** — convenience only; HolderOccurrence remains valid with a bare label |
| **SourceLabel** (optional technical) | Normalized citation string table | **No** — EvidenceBinding still owns the binding; not a global evidence bag |

### 1.2 Relationship sketch (logical — not DDL)

```
SystemLineage? 1 ──< * SystemSnapshot          (technical grouping only)
SystemSnapshot 1 ──< * EvidencedLayer          (0..n; [] means zero child rows)
SystemSnapshot 0..1 ── NegativeAssessment      (xor with Ambiguity / layers per outcome)
SystemSnapshot 0..1 ── AmbiguityAssessment
SystemSnapshot 0..1 ── RefusalAssessment       (positive outcomes only)

EvidencedLayer 1 ──< * HolderOccurrence        (0..n)
EvidencedLayer 1 ──< * EvidenceBinding         (1..n when layer exists)
EvidencedLayer 1 ── 1 ClaimBoundary
EvidencedLayer 0..1 ── layer scope / date / jurisdiction fields

NegativeAssessment | AmbiguityAssessment | RefusalAssessment
        1 ──< * RefusalReference
AmbiguityAssessment 1 ──< * CompetingInterpretation  (≥2 when present)
NegativeAssessment | AmbiguityAssessment ── 1 ClaimBoundary

HolderOccurrence * ──? 0..1 EntityLabel        (optional; never required)
EvidenceBinding  * ──? 0..1 SourceLabel        (optional; never required)
```

**Ownership invariant:** every EvidenceBinding, ClaimBoundary (layer path), HolderOccurrence, and layer jurisdiction/scope/date is reachable from exactly one EvidencedLayer parent. No sibling-layer share. No SystemSnapshot-level evidence pool or system-level claim boundary.

---

## 2. Cardinalities and integrity constraints

These mirror `mon-g2-of-candidate-v0.2` and are **enforced on write** (see §3). They are **architecture-critical highlights** for review — not a replacement validation schema.

> **Canonical ontology precedence:** write validity is determined by the **complete** adopted `mon-g2-of-candidate-v0.2` ontology, including its primitive constraints and **INV-1…INV-11** (Locus/Holder separation, mechanism/evidence separation, jurisdiction load-bearing rules, RefusalReference semantics, `DateExpression` constraints, no-tautology fields, and all other schema invariants). The constraints summarized in the table below are architecture-critical highlights, **not** a replacement or weaker validation schema.

| Constraint | Rule |
|---|---|
| Outcome ↔ layers | `evidenced_control_layer` → exactly 1 EvidencedLayer; `multiple_evidenced_layers` → ≥2; `ambiguous_layer` / `no_evidenced_control_layer` → exactly 0 EvidencedLayer rows |
| Outcome ↔ assessments | `ambiguous_layer` ↔ AmbiguityAssessment required, NegativeAssessment forbidden; `no_evidenced_control_layer` ↔ NegativeAssessment required, AmbiguityAssessment forbidden; positive outcomes forbid both zero-record assessments |
| RefusalAssessment | Allowed only on positive outcomes; zero-record outcomes carry RefusalReference only inside Negative/Ambiguity assessment |
| Layer type | `ActiveLayerType` ×4 only |
| Holders | 0..n HolderOccurrence per layer; **absent** `holders` field vs explicit `holders: []` must be distinguishable in storage and preserved on read (see optional collection presence fidelity) |
| EvidenceBinding | ≥1 per EvidencedLayer; S0 ⇒ no derivation; S1 ⇒ derivation required |
| ClaimBoundary | Exactly one per EvidencedLayer; exactly one per Negative/Ambiguity assessment; never one shared across layers or at SystemSnapshot |
| Jurisdiction | Optional on EvidencedLayer only; never on SystemSnapshot as semantic field |
| CompetingInterpretation | ≥2 when AmbiguityAssessment present |
| No scores | No score/rank/confidence/dominance/probability attributes on any logical record that participates in classification |

> **Optional collection presence fidelity:** for ontology-optional collection fields, normalized storage must preserve whether the field was **absent** versus **explicitly present as an empty array** (`[]`). Child-row count alone is insufficient. A non-semantic presence marker (or equivalent storage mechanism) may be used on the owning logical record, but it **must not** appear in the canonical `SystemRecord`. **No defaulting** from omitted → `[]`.

Frozen optional collections covered by this rule (minimum):

| Field | Written `[]` | Written omitted |
|---|---|---|
| `EvidencedLayerRecord.holders` | Read returns `"holders": []` | Read omits `holders` |
| `negative_assessment.refusal_references` | Read returns `"refusal_references": []` | Read omits `refusal_references` |
| `ambiguity_assessment.refusal_references` | Read returns `"refusal_references": []` | Read omits `refusal_references` |

---

## 3. Canonical write contract

### 3.1 Input

A complete ontology instance conforming to `mon-g2-of-candidate-v0.2` (`schema_version` + `system` SystemRecord). Optional **external** lineage key may be supplied by the harness for history grouping; it is **not** part of the SystemRecord payload.

### 3.2 Lossless-or-reject

| Input class | Behavior |
|---|---|
| Ontology-**valid** SystemRecord | Persist **losslessly**: every semantic field stored under its owning logical record; no silent drop, merge, inference, auto-fill, promote, or rewrite |
| Ontology-**invalid** semantic write | **Reject explicitly**; do not persist a coerced “fixed” record |

Frozen gating probes (from gate; **complete gating probe set** — not an exhaustive definition of ontology validity):

- **W1:** `S0` binding with `derivation` present → reject  
- **W2:** `outcome = no_evidenced_control_layer` with non-empty layers → reject  

Any write that fails **any** adopted ontology constraint must be rejected, even if it is not one of W1/W2.

### 3.3 Write steps (logical)

1. **Validate the complete write against the adopted canonical ontology** (`mon-g2-of-candidate-v0.2` — all primitives, enums, cross-field rules, and INV-1…INV-11).
2. **Enforce architecture ownership/history constraints** (per-layer ownership, no system-level evidence/boundary/jurisdiction, immutable snapshots, lineage outside SystemRecord, lossless-or-reject).
3. If invalid → return explicit rejection; stop.
4. Create a new **immutable** SystemSnapshot (new technical snapshot id).
5. If an external lineage key is provided, attach the snapshot to that SystemLineage (create lineage if needed). Do **not** copy the lineage key into snapshot semantic fields.
6. Persist child records by ownership (layers or zero-record assessment path), including **non-semantic presence markers** for optional collections where absent vs `[]` must be distinguished (§2).
7. Optionally upsert EntityLabel / SourceLabel rows keyed by normalized string — **never** fail a write because a label table row is missing.
8. Optionally update a lineage “latest” pointer to this snapshot — without mutating or deleting prior snapshots.

### 3.4 Immutability

A SystemSnapshot and its owned semantic children are **append-only / immutable** after successful write. Corrections are new snapshots, not in-place semantic edits.

---

## 4. Canonical read model

### 4.1 Read root

The canonical read operation is:

> **Retrieve SystemSnapshot *S* → reconstruct SystemRecord**

Secondary indexes (holder, entity, source, layer_type, date, lineage) may locate snapshot ids, but **must** finish by returning the same SystemRecord reconstruction. They do not redefine ownership.

### 4.2 Generic reconstruction algorithm (case-independent)

Given snapshot id (or equivalent technical handle), reconstruct a **`SystemRecord` object** using the **same ontology field names and wrappers** as `mon-g2-of-candidate-v0.2` — not flattened equivalents. See §4.4 for the canonical serialization mapping.

1. Load SystemSnapshot → emit system-level `scope`, `date` (`DateExpression`), `outcome`.
2. Load all EvidencedLayer children → for each, emit an `EvidencedLayerRecord` with ontology-shaped fields (§4.4).
3. If zero layers: load the required `negative_assessment` or `ambiguity_assessment` (per outcome) with nested `refusal_references`, `competing_interpretations`, and `claim_boundary` using ontology names.
4. If positive outcome: load optional `refusal_assessment` with `refusal_references`.
5. Emit `evidenced_layer_records` as an **array always present** (`[]` when zero layers — never null/omitted).
6. Emit **no** technical ids, lineage keys, EntityLabel surrogates, or SourceLabel surrogates in the SystemRecord.
7. Resolve optional label FKs back to the **original semantic strings** stored on HolderOccurrence / EvidenceBinding (or denormalized copies kept on those rows at write time so read never requires the optional tables).

### 4.3 Read completeness

Reconstruction is **lossless** relative to the written SystemRecord. Comparator-side canonicalization of unordered collections (per gate) is outside the architecture; the architecture must not drop members or collapse multiplicity.

### 4.4 Canonical serialization mapping

The canonical read returns a **`system` object** conforming to adopted ontology `SystemRecord` shape. Field names and wrappers below are **normative** — not shorthand.

#### SystemRecord (`system`)

| Field | Canonical read shape |
|---|---|
| `scope` | string |
| `date` | `DateExpression` object (`as_of` / `start` / `end` / `label` as written) |
| `outcome` | `Outcome` enum |
| `evidenced_layer_records` | array — **always present**; `[]` when zero layers |
| `negative_assessment` | present iff outcome requires it; absent otherwise — **not** fabricated |
| `ambiguity_assessment` | present iff outcome requires it; absent otherwise — **not** fabricated |
| `refusal_assessment` | present iff positive outcome and refusals exist; absent otherwise — **not** fabricated |

#### EvidencedLayerRecord (each element of `evidenced_layer_records`)

| Field | Canonical read shape |
|---|---|
| `layer_type` | `ActiveLayerType` enum |
| `control_mechanism` | `{ "statement": string }` |
| `locus` | `{ "statement": string }` |
| `holders` | `[{ "label": string }, …]` — **present as `[]` only if written `[]`**; **omitted if `holders` was absent on write**; never default omitted → `[]` |
| `evidence_bindings` | array of binding objects (below) |
| `claim_boundary` | `{ "admissible": string, "excluded": string[] }` |
| `scope` | string — present only if written on layer; absent if not written |
| `date` | `DateExpression` — present only if written on layer; absent if not written |
| `jurisdiction` | `{ "statement": string }` — present only if load-bearing on layer; absent if not written |

#### EvidenceBinding (each element of `evidence_bindings`)

| Field | Canonical read shape |
|---|---|
| `claim` | string |
| `evidence_class` | `S0` \| `S1` |
| `source` | string |
| `fact` | string |
| `derivation` | string — **present only** when `evidence_class = S1`; **absent** when `S0` |

#### Assessments (ontology names preserved)

- `negative_assessment`: `{ examined, refusal_references[]?, claim_boundary }` — `refusal_references` present as `[]` only if written `[]`; omitted if absent on write
- `ambiguity_assessment`: `{ competing_interpretations[], separation_gap, refusal_references[]?, claim_boundary }` — same `refusal_references` presence rule
- `refusal_assessment`: `{ refusal_references[] }` — required when assessment exists; array members as written
- `refusal_references[]`: `{ candidate_label, status, reason }`
- `competing_interpretations[]`: `{ interpretation, active_layer_type_considered? }`

#### Optional-field and envelope rules

| Rule | Requirement |
|---|---|
| **Optional-field fidelity** | Except `evidenced_layer_records` (always `[]` at zero), **optional-field presence/absence is preserved as written**. No null fabrication, no default empty objects, no inferring absent fields from storage convenience. |
| **Optional collection presence fidelity** | For ontology-optional collections (`holders`, `negative_assessment.refusal_references`, `ambiguity_assessment.refusal_references`): storage must record absent vs explicit `[]`; canonical read restores exactly as written — **no defaulting omitted → `[]`**. Presence markers are storage-only and never emitted in the read model. |
| **`schema_version`** | **Ontology-envelope metadata only** — not a `SystemRecord` field. Write validates against adopted `mon-g2-of-candidate-v0.2`; read returns **`system` only** inside the canonical read model. If history/evaluation needs to re-wrap a fixture envelope, do so deterministically with `schema_version: "mon-g2-of-candidate-v0.2"` outside the SystemRecord — never inside canonical root. |
| **Write input vs read output** | Write accepts a full ontology instance (`schema_version` + `system`). Canonical read returns `SystemRecord` (`system` object) conforming to adopted ontology — the gate’s comparison target. |

---

## 5. Identifier strategy and access paths

| Identifier | Scope | Enters canonical SystemRecord? |
|---|---|---|
| `snapshot_id` | Technical primary key for SystemSnapshot | **No** |
| `lineage_id` / external lineage key | Technical / harness grouping for history | **No** |
| `layer_row_id`, `binding_row_id`, … | Internal row keys | **No** |
| Holder `label`, source citation strings, scope/date/outcome/layer fields | Semantic | **Yes** (as ontology fields) |

**Secondary access paths (allowed):** index snapshot_id by holder label, entity label, source string, layer_type, system/layer date, lineage_id. Each hit returns snapshot ids → canonical read (§4).

**Forbidden access semantics:** treating “all layers for company X” as a new SystemRecord; treating EntityLabel as proof of Holder; treating SourceLabel rows as evidence without claim ownership.

---

## 6. Version / history policy

| Rule | Policy |
|---|---|
| Unit of history | Immutable SystemSnapshot |
| Same logical system over time | SystemLineage (technical) grouping snapshots; external keys (e.g. gate fixture `mon-g4-da-history-lineage-001`) bind only in the harness/lineage table |
| Write B after A | Both remain independently retrievable by snapshot_id (and by lineage listing) |
| Latest pointer | Optional convenience on SystemLineage → current snapshot_id; may move to B; **must not** delete, rewrite, or present-tense-collapse A |
| Canonical read of A or B | Returns that snapshot’s own dated SystemRecord only |
| Present-tense collapse | Forbidden |

---

## 7. Layer-specific evidence, boundaries, and jurisdiction

| Concern | Storage rule |
|---|---|
| EvidenceBinding | Child of EvidencedLayer only; columns/fields keep claim, evidence_class, source, fact, derivation?; no snapshot-level evidence table used as semantic bag |
| ClaimBoundary | Child of owning EvidencedLayer **or** owning Negative/Ambiguity assessment; admissible + excluded[] local to owner |
| Jurisdiction | Optional field on EvidencedLayer only; SystemSnapshot has **no** jurisdiction semantic field |
| Layer scope/date | Optional overrides on EvidencedLayer; system scope/date remain on SystemSnapshot |

Cross-layer joins for analytics are allowed only as **derived queries** that still attribute each binding/boundary/jurisdiction to its layer owner when reconstructing meaning.

---

## 8. Zero-record, refusal, and ambiguity storage paths

| Outcome path | Storage |
|---|---|
| `no_evidenced_control_layer` | SystemSnapshot with **zero** EvidencedLayer rows + NegativeAssessment (examined, RefusalReference*, ClaimBoundary) |
| `ambiguous_layer` | SystemSnapshot with **zero** EvidencedLayer rows + AmbiguityAssessment (≥2 CompetingInterpretation, separation_gap, optional RefusalReference*, ClaimBoundary) |
| Positive + refusals | EvidencedLayer rows as required + optional RefusalAssessment with RefusalReference* |
| Explicit empty layers | Absence of EvidencedLayer children **and** read model emits `evidenced_layer_records: []` — not null, not omitted |

Ambiguity structural evaluation reuses MON-G3-IT fixture unchanged (`interface/fixtures/ambiguous_layer_structural.json`) via this path.

---

## 9. Retrieval → interface composability

Canonical read (§4) yields a SystemRecord conforming to `mon-g2-of-candidate-v0.2`. That object is a valid input to adopted interface thesis `mon-g3-it-candidate-v0.2` **without**:

- analyst judgment;
- case-specific adapters;
- inventing holders, jurisdictions, evidence rows, or boundaries;
- promoting lineage/technical ids into the reading unit.

Interface grammar (§1–§8 of the interface thesis) consumes the reconstructed SystemRecord directly (same family of render path as MON-G3-IT Step 3, fed by retrieval rather than by static instance files).

---

## 10. Explicit prohibited fields / relationships

| Prohibited | Why |
|---|---|
| Company/entity as canonical read root | Violates SystemRecord semantic/read root |
| Required global company registry for Holder validity | Forced registry falsifier |
| System-level evidence_bindings or claim_boundary | Ownership / leakage |
| Shared ClaimBoundary across layers | Cross-record leakage |
| System-level jurisdiction semantic field | Jurisdiction promotion |
| Active-layer enum slots for research candidates | Candidate-as-layer |
| RefusalReference stored as EvidencedLayer | Refusal hygiene |
| score / rank / confidence / dominance / probability / S2 fields | Inference surface |
| Mutable in-place overwrite of snapshot semantics | Destructive history |
| Lineage key or snapshot_id inside canonical SystemRecord | Technical id as meaning |
| Silent coerce-on-write paths | Lossless-or-reject |
| Default omitted optional collections to `[]` | Optional collection presence fidelity |
| Case-id / expected_* storage fields driving read | Tautology |

---

## 11. Illustrative logical ER sketch (optional — not DDL)

```
[SystemLineage]--< [SystemSnapshot] >--[RefusalAssessment]--< [RefusalReference]
                       |  |  |
                       |  |  +--[NegativeAssessment]--< [RefusalReference]
                       |  |              +--[ClaimBoundary]
                       |  +--[AmbiguityAssessment]--< [CompetingInterpretation]
                       |              +--[ClaimBoundary]
                       +--< [EvidencedLayer] >--< [HolderOccurrence] >--? [EntityLabel]
                                    |  |
                                    |  +--< [EvidenceBinding] >--? [SourceLabel]
                                    +--[ClaimBoundary]
                                    +-- jurisdiction? / layer scope? / layer date?
```

Boxes are logical records. Lines are ownership. Optional `?` edges are non-authoritative normalizations.

---

## 12. Completeness checklist (Step 2 gate requirements)

| Required section | This document |
|---|---|
| Ownership / relationship model | §1 |
| Cardinalities and integrity constraints | §2 |
| Canonical write contract (incl. lossless-or-reject) | §3 |
| Canonical read model | §4 (incl. §4.4 serialization mapping) |
| Identifier strategy / access paths | §5 |
| Version / history policy | §6 |
| Layer-specific evidence / boundaries / jurisdiction | §7 |
| Zero-record / refusal / ambiguity paths | §8 |
| Retrieval → interface contract | §9 |
| Explicit prohibited fields / relationships | §10 |

---

## 13. Artifact status

| Step | Status |
|---|---|
| 1 Gate design | DESIGN FROZEN — accepted 2026-08-29 (revision 2) |
| 2 This candidate logical data architecture | **Accepted — 2026-08-29** |
| 3 Persistence/retrieval evaluation | **Accepted — 2026-08-29** |
| 4 Closeout | **Closed — PASS — 2026-08-29** (DEC-008) |

**Stop point:** Gate MON-G4-DA closed PASS. Architecture `mon-g4-da-candidate-v0.2` adopted. This adoption does **not** authorize production database, API, UI/interface implementation, publishing system, or other operationalization — separate authorization required.
