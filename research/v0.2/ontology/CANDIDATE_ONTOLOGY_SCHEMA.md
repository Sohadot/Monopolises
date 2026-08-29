# Candidate Ontology Schema — Monopolises v0.2

**Gate:** MON-G2-OF (Ontology Fidelity)
**Schema ID:** `mon-g2-of-candidate-v0.2`
**Version:** 0.2-candidate
**Status:** **Draft for review** (Step 2 — no instances; no evaluation)
**Gate spec:** `../ONTOLOGY_FIDELITY_GATE.md` (DESIGN FROZEN — accepted 2026-08-29)
**Machine-readable companion:** `candidate-schema.json` (JSON Schema draft 2020-12; validation aid only)
**Opened:** 2026-08-29

> This document is the **canonical** definition of the candidate ontology schema. The JSON Schema companion expresses the same constraints for machine validation; it is not the ontology. **No MON-G1 instances, no round-trip evaluation, and no gate closeout** are included in Step 2.

## Purpose

Define the **general structure** — primitives, enumerations, cardinalities, required/optional fields, cross-field constraints, and prohibited constructs — sufficient for a later Step 3 round-trip test against the eight frozen MON-G1-LI cases.

The schema is designed from **general semantic primitives**, not from individual case shapes. Whether the eight cases can live inside this structure without case-specific exceptions is a Step 3 question.

## Design principles

1. **Outcome ≠ Layer.** Classification outcome is a case-level enum. Active layer type appears only on evidenced layer records.
2. **Mechanism ≠ Evidence.** Control mechanism is the concrete instrument established from S0/S1. Source citations and supporting facts live in evidence bindings.
3. **Locus ≠ Holder.** Locus is *where* control sits. Holders are *who* occupies the locus — optional, 0..n, absent when discrete actors are not evidenced.
4. **Per-record ownership.** Each evidenced layer record owns its mechanism, locus, holders, evidence bindings, claim boundary, and layer-scoped metadata.
5. **Assessments for zero-record outcomes.** `ambiguous_layer` and `no_evidenced_control_layer` require populated assessments; zero layer records is not missing data.
6. **Refusal references only.** Research candidates and refused/untriggered probes appear as assessment references (open labels), never as active-layer enum values or classifiable layer records.
7. **No inference surface.** The schema carries structure only. It does not compute outcomes, assign layers, or rank records.
8. **No case identity.** No `case_id`, `expected_*`, or ground-truth escape fields.

---

## Enumerations

### `Outcome` (case-level — exactly four values)

| Value | Evidenced layer records | Required assessment |
|---|---|---|
| `evidenced_control_layer` | exactly `1` | none |
| `multiple_evidenced_layers` | `≥ 2` | none |
| `ambiguous_layer` | exactly `0` | `ambiguity_assessment` |
| `no_evidenced_control_layer` | exactly `0` | `negative_assessment` |

`ambiguous_layer` and `no_evidenced_control_layer` are **not** layer types.

### `ActiveLayerType` (evidenced layer records only — exactly four values)

| Value | Definition (frozen) |
|---|---|
| `legal_exclusivity` | Statute, license, patent grant, or franchise conferring an exclusive right. |
| `capacity_control` | Documented facility, node, or capacity the function must pass through and that is hard to bypass. |
| `access_gatekeeping` | Documented rule or control governing admission to a market, platform, or channel. |
| `switching_dependency` | Documented cost or difficulty of leaving an incumbent. |

No other values. Research candidates (`qualification_control`, `standard_interface_control`, `temporal_constraint`) are **not** members of this enum.

### `EvidenceClass` (evidence bindings only)

| Value | May establish classification? |
|---|---|
| `S0` | Yes — source-native fact |
| `S1` | Yes — reproducible mechanical derivation from S0 |

`S2` is **excluded** from evidence bindings. The schema has no field for interpretive synthesis that carries classification.

### `RefusalStatus` (assessment references only)

| Value | Meaning |
|---|---|
| `refused` | Candidate considered and declined on source-native grounds |
| `not_established` | Candidate not evidenced by admitted primary material |
| `probe_not_triggered` | Held-out layer probe not activated by a source-native instrument |

---

## Primitives (classes)

### `SystemRecord` (root)

The bounded function or market structure under analysis. Unit of a single classification result.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `scope` | 1 | **yes** | Bounded critical function under analysis (not an entire industry by default). |
| `date` | 1 | **yes** | Temporal anchor for the system record (`DateExpression`). |
| `outcome` | 1 | **yes** | Case-level `Outcome`. |
| `evidenced_layer_records` | 0..n | conditional | Independent evidenced control layers. Cardinality governed by `outcome` (see Invariants). |
| `ambiguity_assessment` | 0..1 | conditional | Required iff `outcome = ambiguous_layer`; forbidden otherwise. |
| `negative_assessment` | 0..1 | conditional | Required iff `outcome = no_evidenced_control_layer`; forbidden otherwise. |

**Forbidden on `SystemRecord`:** system-level `evidence_bindings`, system-level `claim_boundary`, `score`, `ranking`, `case_id`, `expected_*`, `ground_truth`, inference rules.

---

### `EvidencedLayerRecord`

One independently evidenced control layer. Exists only when `outcome` is `evidenced_control_layer` or `multiple_evidenced_layers`.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `layer_type` | 1 | **yes** | `ActiveLayerType` only. |
| `control_mechanism` | 1 | **yes** | Concrete instrument/mechanism from S0/S1 — not a source citation. |
| `locus` | 1 | **yes** | Where control sits — not who holds it. |
| `holders` | 0..n | no | Discrete actors who hold/operate the locus. Empty/absent when not evidenced. |
| `evidence_bindings` | 1..n | **yes** | Claim-specific S0/S1 bindings; minimum one per record. |
| `claim_boundary` | 1 | **yes** | Admissible record and exclusions for **this** layer record. |
| `scope` | 0..1 | no | Layer-scoped scope override when it differs from system `scope`. |
| `date` | 0..1 | no | Layer-scoped date override when the finding is layer-specific. |
| `jurisdiction` | 0..1 | conditional | Present only when load-bearing for this layer record; must not be invented. |

**Forbidden on `EvidencedLayerRecord`:** `primary`/`secondary` rank, merge pointers to sibling records, shared evidence pools, dominance fields.

---

### `ControlMechanism`

The concrete control instrument or mechanism **established from S0 facts or a reproducible S1 derivation**.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `statement` | 1 | **yes** | Mechanism description: statute, capacity chokepoint, admission rule, switching barrier, or conjunction of source-native facts establishing the mechanism. |

**Must not contain:** source citation strings standing in for the mechanism (e.g. a report title alone), layer-type label paraphrase, market-share or dominance assertions.

---

### `Locus`

The specific place, capacity, channel, or boundary inside the system where control sits — the **where**.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `statement` | 1 | **yes** | Locus description without actor identity. |

**Invariant:** Actor names, company names, and holder identities must not appear in `locus.statement`. Holders belong in `holders[]`.

---

### `Holder`

A discrete actor evidenced to hold, operate, or occupy the locus — the **who**.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `label` | 1 | **yes** | Evidence-level actor designation (name or bounded descriptor from primary material). |

**Cardinality:** 0..n per `EvidencedLayerRecord`. An empty `holders` array means holders are absent — not resolved at discrete-actor level. **Do not** populate with geography, capacity structures, or channel names to fill the field.

**Not an entity registry.** `label` is a record-local string, not a foreign key to a company/market ontology.

---

### `EvidenceBinding`

One S0 or S1 fact bound to a specific claim within a layer record.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `claim` | 1 | **yes** | The specific claim this binding supports (e.g. "function must pass through this capacity"). |
| `evidence_class` | 1 | **yes** | `S0` or `S1` only. |
| `source` | 1 | **yes** | Source citation (title, locator, identifier sufficient to retrieve the primary material). |
| `fact` | 1 | **yes** | Source-native fact (S0) or input fact(s) for derivation. |
| `derivation` | 0..1 | required if `evidence_class = S1` | Reproducible, non-interpretive derivation steps from `fact`. |

**Invariant:** Every binding attaches to a `claim`. Unattached evidence lists are forbidden.

---

### `ClaimBoundary`

What the record does and does not say.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `admissible` | 1 | **yes** | The admissible record statement. |
| `excluded` | 0..n | **yes** (may be empty list) | Explicit exclusions — claims the framework must not make. |

Used on `EvidencedLayerRecord`, `NegativeAssessment`, and `AmbiguityAssessment` — never as a system-level shared bag across layer records.

---

### `NegativeAssessment`

Required when `outcome = no_evidenced_control_layer`.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `examined` | 1 | **yes** | What was examined under the frozen scope. |
| `refusal_references` | 0..n | no | Refused candidates and untriggered probes (assessment references only). |
| `claim_boundary` | 1 | **yes** | What evidence does and does not establish. |

---

### `AmbiguityAssessment`

Required when `outcome = ambiguous_layer`.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `competing_interpretations` | 2..n | **yes** | Two or more source-defensible readings that remain in play. |
| `separation_gap` | 1 | **yes** | Why no source-native rule separates the interpretations. |
| `claim_boundary` | 1 | **yes** | Admissible record and exclusions for the ambiguous result. |

**Invariant:** Competing interpretations are assessment content only. They **must not** be promoted to `evidenced_layer_records`.

---

### `RefusalReference`

Assessment-only reference to a refused research candidate or untriggered probe. **Not** a layer type.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `candidate_label` | 1 | **yes** | Open string (e.g. `qualification_control`, `switching_dependency` probe). Not an `ActiveLayerType` enum member unless the reference is to an active type that was considered and not established in this record. |
| `status` | 1 | **yes** | `RefusalStatus`. |
| `reason` | 1 | **yes** | Source-defensible basis for refusal or non-trigger. |

---

### `CompetingInterpretation`

One source-defensible reading within an ambiguity assessment.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `interpretation` | 1 | **yes** | Description of the source-defensible reading. |
| `active_layer_type_considered` | 0..1 | no | Optional `ActiveLayerType` if the competing reading maps to an active type — assessment reference only, not an evidenced layer record. |

---

### `DateExpression`

Temporal anchor. Supports point-in-time and bounded ranges without imposing a single date format beyond machine readability.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `as_of` | 0..1 | conditional | Point-in-time anchor (ISO 8601 date). |
| `start` | 0..1 | conditional | Range start (ISO 8601 date). |
| `end` | 0..1 | conditional | Range end (ISO 8601 date). |
| `label` | 0..1 | no | Human-readable date qualifier when ISO alone is insufficient (e.g. "FY2025"). |

**Constraint:** At least one of `as_of`, (`start` + optional `end`), or `label` must be present.

---

### `JurisdictionExpression`

Present only when jurisdiction is load-bearing.

| Field | Cardinality | Required | Description |
|---|---|---|---|
| `statement` | 1 | **yes** | Jurisdiction descriptor (e.g. `US`, `UK`, `US DoD procurement channel`). |

---

## Structural diagram

```
SystemRecord
  scope, date, outcome
  ├── ambiguity_assessment?     (required iff outcome = ambiguous_layer)
  ├── negative_assessment?      (required iff outcome = no_evidenced_control_layer)
  └── evidenced_layer_records[] (cardinality per outcome)
        ├── layer_type          ActiveLayerType
        ├── control_mechanism   ControlMechanism.statement
        ├── locus               Locus.statement
        ├── holders[]           Holder.label  (0..n)
        ├── evidence_bindings[] EvidenceBinding (claim-bound)
        ├── claim_boundary      ClaimBoundary
        └── scope?, date?, jurisdiction?  (layer-scoped overrides)
```

---

## Cross-field invariants

These constraints are **general** — they do not reference case identities.

### INV-1 — Outcome ↔ layer-record cardinality

| `outcome` | `len(evidenced_layer_records)` | Assessments |
|---|---|---|
| `evidenced_control_layer` | `= 1` | no `ambiguity_assessment`; no `negative_assessment` |
| `multiple_evidenced_layers` | `≥ 2` | no `ambiguity_assessment`; no `negative_assessment` |
| `ambiguous_layer` | `= 0` | `ambiguity_assessment` required; no `negative_assessment` |
| `no_evidenced_control_layer` | `= 0` | `negative_assessment` required; no `ambiguity_assessment` |

### INV-2 — Active layer enum ceiling

`layer_type` on any `EvidencedLayerRecord` must be one of the four `ActiveLayerType` values. No other layer-classification field exists.

### INV-3 — Mechanism/evidence separation

`control_mechanism.statement` must not duplicate a `source` citation from an `evidence_binding` as its sole content. Mechanism and evidence are independently extractable.

### INV-4 — Locus/holder separation

`locus.statement` must not contain holder `label` values from the same record's `holders[]`. Holders must not duplicate the locus statement.

### INV-5 — Per-record evidence ownership

`evidence_bindings` and `claim_boundary` are owned by each `EvidencedLayerRecord`. No system-level evidence or boundary field may substitute.

### INV-6 — S2 exclusion

No field may carry S2 interpretive synthesis as classification-bearing evidence. `evidence_class` accepts only `S0` and `S1`.

### INV-7 — Refusal references are not layers

`refusal_references[].candidate_label` and `competing_interpretations[]` are assessment content. They do not create `evidenced_layer_records` and do not extend `ActiveLayerType`.

### INV-8 — Jurisdiction conditional

`jurisdiction` on a layer record is optional. When absent, it must not be inferred or defaulted. When present, it must be load-bearing for that record.

### INV-9 — No ranking or merge

Multiple `evidenced_layer_records` have no `rank`, `primary`, `weight`, or `merge_group` fields.

### INV-10 — No tautology fields

The schema defines no `case_id`, `expected_outcome`, `expected_layer`, `original_result`, `raw_case`, `ground_truth`, or equivalent stored-answer fields.

---

## Prohibited constructs (explicit negative)

The candidate schema **does not define** and **must not be extended** with:

| Category | Examples |
|---|---|
| Quantitative composites | `score`, `severity`, `dominance_level`, `ranking`, `monopoly_probability` |
| Research-candidate enum slots | `qualification_control`, `standard_interface_control`, `temporal_constraint` as classifiable values |
| Inference / derivation engine | rules that assign `outcome` or `layer_type` from dominance, share, or antitrust inputs |
| Entity model | company registry, sector taxonomy, foreign keys to market ontologies |
| UI / data architecture | page mappings, API shapes, persistence layout |
| Case identity | `case_id`, case-keyed exception tables |
| Escape hatches | free-text blobs from which round-trip answers are reconstructed |
| Default layer on absence | auto-assignment when evidence is missing |

---

## Machine-readable companion

`candidate-schema.json` expresses this document as JSON Schema (draft 2020-12) for structural validation of instance documents in Step 3.

**Precedence:** Where the JSON Schema and this document diverge, **this document is canonical**. The JSON Schema is a validation aid, not the ontology definition.

**Step 2 scope:** The JSON Schema validates **shape only**. It does not encode S1–S8, does not perform round-trip extraction, and does not include sample instances.

---

## Gate falsifier mapping (schema-level)

| Frozen falsifier (gate) | Schema response |
|---|---|
| Outcome conflated with layer | Separate `Outcome` and `ActiveLayerType` enums; INV-1 |
| Mechanism conflated with evidence | Separate `ControlMechanism` and `EvidenceBinding`; INV-3 |
| Locus carries who | Separate `Locus` and `Holder`; INV-4 |
| Shared evidence/boundary bag | Per-record ownership; INV-5; forbidden system-level fields |
| Cannot represent ambiguity/negative | `AmbiguityAssessment`, `NegativeAssessment`; INV-1 |
| Research slots | Four-value `ActiveLayerType` only; INV-2, INV-7 |
| Tautological round-trip | INV-10; prohibited constructs |
| Case-specific tailoring | General primitives only; no case-keyed fields |
| Quantitative / inference surfaces | Prohibited constructs |

---

## Artifact status

| Step | Artifact | Status |
|---|---|---|
| 1 | `ONTOLOGY_FIDELITY_GATE.md` | Frozen |
| 2 | This document + `candidate-schema.json` | **Draft for review** |
| 3 | `GATE_MON-G2-OF_EVALUATION.md` + instances | Blocked |
| 4 | Gate closeout | Blocked |

**Stop point:** Review this schema definition. No instances. No evaluation. Amendments require review before Step 3.
