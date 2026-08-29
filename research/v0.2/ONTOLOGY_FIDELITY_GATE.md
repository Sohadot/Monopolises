# Ontology Fidelity Gate — Monopolises v0.2

**Gate ID:** MON-G2-OF
**Version:** 0.2
**Status:** **DESIGN FROZEN — accepted 2026-08-29**
**Opened:** 2026-08-29
**Closed:** —
**Thesis under test:** Layered Monopolisation v0.2 (`THESIS_CANDIDATE.md`, ratified by DEC-005)
**Evaluation:** `GATE_MON-G2-OF_EVALUATION.md` (not yet created)
**Decision:** pending gate close
**Predecessor gate:** MON-G1-LI — Closed PASS (`LAYER_IDENTIFIABILITY_GATE.md`, `GATE_MON-G1-LI_EVALUATION.md`)

> This gate tests whether the four ratified control layers can be **represented as a stable ontology** without losing the evidence boundaries that made MON-G1-LI reproducible. The gate **design is frozen** as of 2026-08-29 (revision 4). **Step 2 — candidate ontology schema** — is now authorized. Step 3 (round-trip evaluation) and gate closeout remain blocked until Step 2 exists.

## Governing question

> Can the four ratified control layers be represented as a stable ontology **without losing the evidence boundaries** that made MON-G1-LI reproducible?

Note what the question is not: it is not "what is the best ontology design," not "how should we model markets," and not "can we add useful derived fields." It is a question about whether a **formal representation** can carry the same discriminations — outcome, layer, mechanism, locus, holder, claim boundary — that the gate cases already established, **without distortion, inflation, or silent inference**.

## What this gate tests — and what it does not

This gate tests **representational fidelity**, not re-classification. The MON-G1-LI case results are the **ground truth** for round-trip evaluation. If a candidate ontology forces a change to any case result to fit the schema, the gate **FAILS**. We do not change history to fit the model.

| In scope | Out of scope |
|---|---|
| Representing the four active layers | Building production data architecture |
| Preserving evidence boundaries from MON-G1-LI | Interface implementation or UI surfaces |
| Round-tripping the eight frozen cases | Scores, rankings, entity pages, monetization |
| Structural separation of ontology primitives | Admitting new layers or research candidates |
| Representing negatives (`no_evidenced_control_layer`) and ambiguity (`ambiguous_layer`) | Re-opening MON-G1-LI classifications |

## Active taxonomy (frozen — exactly four layers)

Only these four values may appear in the **active-layer enum**. They are layer types, not classification outcomes:

| Layer | Definition (frozen from MON-G1-LI) |
|---|---|
| `legal_exclusivity` | A statute, license, patent grant, or franchise conferring an exclusive right. |
| `capacity_control` | A documented facility, node, or capacity that the function must pass through and that is hard to bypass. |
| `access_gatekeeping` | A documented rule or control governing admission to a market, platform, or channel. |
| `switching_dependency` | A documented cost or difficulty of leaving an incumbent (held-out probe, admitted by S7). |

**Research candidates are outside the active taxonomy and must not appear as reserved slots, placeholders, enums, or nullable fields in the ontology under test:**

- `qualification_control` — not evidenced; refused in S6
- `standard_interface_control` — not evidenced; refused in S5 and S3
- `temporal_constraint` — never targeted; untested

Non-proof is information, not a reason to hold a slot in the production structure.

**Refused/research candidate references:** A refused or research candidate may appear **only** as an assessment reference inside a negative, ambiguity, or refusal assessment. Such a reference is **not** an active-layer value, schema slot, placeholder class, or classifiable layer record. This preserves refusal history without re-admitting the three research candidates through the back door.

## Outcome vs Layer (mandatory invariant)

**Classification outcome and active-layer type are separate primitives.** This is the central structural invariant of MON-G2-OF.

| Concept | Role | Is it a layer? |
|---|---|---|
| **Outcome** | The case-level classification result | **No** |
| **Active layer** | One of the four evidenced control types | **Yes** — but only when evidenced |

### Outcome enum (case-level)

Each system/case resolves to exactly one outcome (frozen from MON-G1-LI — all four):

- `evidenced_control_layer` — one evidenced layer record is present.
- `multiple_evidenced_layers` — two or more independent evidenced layer records are present.
- `ambiguous_layer` — **zero** evidenced layer records; a complete ambiguity assessment.
- `no_evidenced_control_layer` — **zero** evidenced layer records; a complete negative assessment.

`ambiguous_layer` and `no_evidenced_control_layer` are **not** layer types, **not** null layers, **not** empty enum values, and **not** "pending" states. They are first-class outcomes that require explicit assessments. Neither may be collapsed into the other: genuine ambiguity is not a negative, and a clean negative is not ambiguity.

### Ambiguity assessment (required when outcome = `ambiguous_layer`)

When outcome is `ambiguous_layer`, the ontology must carry **zero** evidenced layer records and a populated **ambiguity assessment** recording:

1. The two or more source-defensible layer interpretations that remain in play.
2. Why no source-native rule separates them (the specific evidentiary gap).
3. A claim boundary (admissible record + explicit exclusions).

**Candidate interpretations recorded in an ambiguity assessment must not become evidenced layer records.** They are assessment references only — the framework declines to classify, not to provisionally classify.

The frozen eight-case round-trip set contains no `ambiguous_layer` instance (all eight resolved to a definite outcome). Structural support for this outcome is nonetheless required: MON-G1-LI allowed it, and an ontology that cannot represent it would force real ambiguity into a false positive or false negative.

### Negative assessment (required when outcome = `no_evidenced_control_layer`)

When outcome is `no_evidenced_control_layer`, the ontology must carry **zero** evidenced layer records and a populated **negative assessment** recording what was examined, what was refused or not triggered, and what the claim boundary excludes. S3 is the canonical test.

### Evidenced layer records (0..n per system)

**Invariant:** A system carries **0..n evidenced layer records**, where *n* is the count of independently evidenced control layers — not the outcome label.

| Outcome | Evidenced layer record count | Required assessment |
|---|---|---|
| `evidenced_control_layer` | 1 | — |
| `multiple_evidenced_layers` | ≥ 2 | — |
| `ambiguous_layer` | **0** | Ambiguity assessment |
| `no_evidenced_control_layer` | **0** | Negative assessment |

**Zero evidenced layer records does not mean missing data.** When the count is zero, the ontology must carry an explicit ambiguity assessment or negative assessment — never an empty shell. S3 is the canonical negative test: a complete, valid record with zero layer records and a populated negative assessment.

The outcome field summarizes the classification result; it does not substitute for layer records and must not be the only place zero-record outcomes live.

## Ontology primitives (mandatory separation)

The ontology must maintain **strict separation** among these primitives. A primitive may not collapse into another, and a layer must not become a loose entity description.

```
System (mandatory date, scope; jurisdiction when load-bearing)
  ├── Outcome (case-level classification result — separate from active-layer enum)
  ├── Ambiguity assessment (required when outcome = ambiguous_layer)
  ├── Negative assessment (required when outcome = no_evidenced_control_layer)
  └── Evidenced Layer Record (0..n)
        ├── Layer (one of four active types)
        ├── Control Mechanism (concrete instrument/mechanism from S0 or S1 — not the evidence source)
        ├── Locus (where control sits — not who holds it)
        ├── Holder / Actor (who occupies or holds the locus — optional; present only when evidenced at discrete-actor level)
        ├── Evidence bindings (S0/S1 facts bound to specific claims)
        ├── Claim Boundary (admissible record + explicit exclusions — per layer record)
        └── Layer-scoped metadata (date, scope, jurisdiction — per layer record when they differ)
```

### Primitive definitions

| Primitive | Role | Must not become |
|---|---|---|
| **System** | The bounded function or market structure under analysis (with mandatory date and scope) | A company, sector, or "the market" |
| **Outcome** | Case-level classification result (`evidenced_control_layer`, `multiple_evidenced_layers`, `ambiguous_layer`, `no_evidenced_control_layer`) | A layer type; a null; a synonym for "no data" |
| **Evidenced Layer Record** | One independently evidenced control layer with its own mechanism, locus, holders, evidence, and boundary | A bag of layers sharing one evidence pool |
| **Layer** | One of the four active control types, assigned only when evidenced | A synonym for dominance, concentration, or "moat" |
| **Control Mechanism** | The concrete control instrument or mechanism established from S0 facts or a reproducible S1 derivation (statute, capacity chokepoint, admission rule, switching barrier; or a conjunction of source-native facts that establishes the mechanism) | A paraphrase of the layer label; an evidence source citation; S2 synthesis |
| **Locus** | The specific place or capacity inside the system where control sits — the **where** | A company name, actor identity, or "who controls" |
| **Holder / Actor** | The entity or set of entities that hold, operate, or occupy the locus — the **who** (final class name TBD at schema step). **Optional:** present only when discrete actors are evidenced; absent when the admitted evidence resolves only to a geography/capacity structure | The locus itself; a geography or capacity structure standing in for actors; a dominance ranking |
| **Evidence bindings** | S0 facts and reproducible S1 derivations, each bound to a specific claim within the layer record | A system-level `evidence[]` bag unattached to claims; S2 synthesis |
| **Claim Boundary** | The admissible record and explicit exclusions for **this layer record** | A system-level narrative; an open-ended free-text field |
| **Ambiguity assessment** | Explicit statement of source-defensible competing interpretations, why no source-native rule separates them, and claim boundary — when outcome = `ambiguous_layer` | Provisional layer records; a forced classification |
| **Negative assessment** | Explicit statement of what was examined, refused, and excluded — when outcome = `no_evidenced_control_layer` | Absence of data; a null outcome; a synonym for `ambiguous_layer` |

### Locus vs Holder invariant

**Locus answers *where*; Holder answers *who*.** These must not be conflated.

| Case | Locus (where) | Holder (who) |
|---|---|---|
| S2 | 2021 5 nm HVM capacity | TSMC, Samsung |
| S7 | Provider-specific data-egress / switching boundary | Named cloud provider(s) |
| S1 | EUV scanner production capacity | ASML (single holder) |
| S6 Layer A | China-dominated NdFeB value-chain capacity | **Absent** — not resolved at discrete-actor level from admitted evidence |

If the schema places TSMC/Samsung inside `locus` only, it confuses **where** with **who**. If it places "China-dominated value chain" in `holder`, it confuses a **capacity structure** with **actors**. Holder is a primitive that may be absent when evidence does not resolve discrete actors — not a field that must be filled with the locus relabeled. If it places the provider name inside `locus` in S7, it loses the boundary-specific locus. The Holder primitive (or an equivalent structurally separate field) is required; its final class name is deferred to the schema step, but the **invariant** is fixed here: locus must not carry actor identity.

This does not open entity pages. It preserves the meaning of the original case records.

### Per-layer-record ownership invariant

**Evidence bindings and claim boundaries belong to each evidenced layer record, not to the system as a whole.**

S6 is the decisive test. `capacity_control` and `access_gatekeeping` have:

- different loci
- different mechanisms
- different evidence bindings
- different claim boundaries
- different date/scope/jurisdiction load (Layer B is jurisdiction-specific; Layer A is a dated geographic finding)

If the schema places evidence, date, scope, or claim boundary in a single system-level bag and merely links two layer names to it, the round-trip may recover the correct layer **labels** while losing **fidelity**. That is a gate failure.

Each evidenced layer record must independently round-trip:

- mechanism
- locus
- holder (when evidenced)
- evidence bindings (claim-specific, not a generic array)
- claim boundary (admissible + excluded)
- layer-scoped date / scope / jurisdiction (when they differ from system defaults or from sibling layer records)

## Mandatory metadata

| Field | Scope | Rule |
|---|---|---|
| **date** | System (minimum); layer record when layer-specific dating applies | **Mandatory** on every system record. Layer records carry their own date when the finding is layer-specific (e.g. S6 Layer A: 2020–2022 BIS data; Layer B: through Dec 31, 2026). |
| **scope** | System (minimum); layer record when scope differs | **Mandatory** on every system record. |
| **jurisdiction** | Layer record (when load-bearing) | **Mandatory only when load-bearing.** Present for S4, S5, S7 layer records. Absent (not invented) for S3. |

## Evidence discipline (carried over from MON-G1-LI)

- **S0 — Source-native.** The primary source explicitly states the fact establishing the layer and mechanism.
- **S1 — Mechanical derivation.** A reproducible, non-interpretive derivation from S0 facts.
- **S2 — Interpretive synthesis.** Domain judgment required. **S2 may explain uncertainty; S2 cannot establish a layer classification or populate ontology fields that carry classification.**

Evidence must bind to **specific claims** within a layer record (e.g. "function must pass through this capacity" ← S0 fact E03), not float as an unattached `evidence[]` list. The ontology must not add inference beyond what the evidence bindings contain.

## Generalization invariant (no case-specific tailoring)

**Every primitive, field, and cardinality rule must be semantically general.** No field, cardinality constraint, or exception may be introduced because a single case (S2, S6, S7, or any other) needed it alone.

A schema that passes round-trip only by embedding case-specific structure — a field that exists for S6 alone, a cardinality rule that exists because S2 needed collective holders, an exception table keyed to case IDs — is not an ontology. It is a serialization of eight answers.

This invariant applies to the candidate schema (Step 2) and is tested implicitly by the round-trip: if the extraction logic must branch on case identity (`S1`…`S8`) to recover ground truth, the gate fails (see Falsifier 12).

## Prohibited ontology features

The ontology under test must **not** include any of the following. Their presence is an automatic falsifier:

| Prohibited | Rationale |
|---|---|
| `score`, `severity`, `dominance_level`, `ranking`, `monopoly_probability`, or any disguised quantitative composite | DEC-005 forbids scored/ranked surfaces without a new gate |
| Reserved slots or enum values for research candidate layers | Non-proof is not a placeholder |
| Default layer assignment when evidence is absent | Would re-bias toward finding control everywhere (MON-G1 falsifier #4) |
| Inference rules that derive layers from market share, dominance, or antitrust findings | S2 cannot classify |
| Fields that collapse Layer + Mechanism + Locus into a single "control description" | Destroys reproducibility |
| Company-as-primary-key or `Company × Monopoly Score` as unit of record | Forbidden unit of record from MON-G1-LI |
| `expected_layer`, `original_result`, `raw_case`, `ground_truth`, `case_id` as extractable fields, or any free-text blob used to reconstruct answers on round-trip | Serialization fidelity, not ontology fidelity (see Falsifier 12) |
| System-level evidence or claim-boundary bags shared across multiple layer records without per-record bindings | Destroys per-layer fidelity (S6 test) |
| Evidence source cited as Control Mechanism (e.g. report name standing in for the mechanism) | Destroys mechanism/evidence separation (S6 Layer A test) |

## Representational requirements (must-support cases)

The ontology must represent the following patterns **without schema workarounds**. Each pattern is evidenced by a MON-G1-LI case; failure on any one is a gate failure.

### R1 — Single evidenced layer (baseline)

**Cases:** S8 (`legal_exclusivity`), S1 (`capacity_control`), S4/S5 (`access_gatekeeping`), S7 (`switching_dependency`)

One system → outcome `evidenced_control_layer` → **one** evidenced layer record → mechanism + locus + holder (if evidenced) + evidence bindings + claim boundary.

### R2 — Collective holder, locus-specific (not single-actor; locus ≠ who)

**Case:** S2

`capacity_control` where:

- **Locus:** 2021 5 nm HVM capacity (the capacity set itself)
- **Holders:** TSMC, Samsung (actors who hold that capacity — not the locus)

The ontology must represent a multi-holder locus without reducing holders to the locus field or collapsing to a single company or to "market concentration."

### R3 — Multiple evidenced layers per system (per-record independence)

**Case:** S6

One system → outcome `multiple_evidenced_layers` → **two** independent evidenced layer records:

- Layer A: `capacity_control` — locus: China-dominated NdFeB value-chain capacity; holder: **absent** (not resolved at discrete-actor level); mechanism: concentrated all-stage NdFeB productive capacity that the function must pass through and was hard to bypass within the dated scope; evidence: BIS Section 232 findings (bindings **specific to Layer A**); claim boundary **specific to Layer A**; dated 2020–2022.
- Layer B: `access_gatekeeping` — locus: U.S. defense procurement channel; holder: **absent** (channel locus; no discrete actor set evidenced); mechanism: source-origin admission restriction governing delivery into the DoD procurement channel; evidence: 10 U.S.C. § 4872 / DFARS 252.225-7052 (bindings **specific to Layer B**); claim boundary **specific to Layer B**; jurisdiction load-bearing (U.S. DoD channel).

**R3 round-trip requirement (explicit):** Each layer record must independently reproduce its own mechanism, locus, holder(s), evidence bindings, and claim boundary. Shared system-level evidence or boundary fields fail this requirement even if layer names round-trip correctly.

The ontology must not force a single "primary" layer, merge records, or rank layers.

### R4 — Provider-specific mechanism (not market-level)

**Case:** S7

`switching_dependency` where:

- **Locus:** Provider-specific data-egress / switching boundary (UK, 2025)
- **Holder:** Named provider(s) at the egress boundary — distinct from the locus

The ontology must scope mechanism and locus to a provider's exit boundary, not to "cloud market" or "hyperscalers generally."

### R5 — No evidenced control layer (first-class negative; zero layer records)

**Case:** S3

Outcome `no_evidenced_control_layer` → **zero** evidenced layer records → explicit **negative assessment**:

- System scope and date present
- Refused layers recorded as **not established** (`standard_interface_control` NOT ESTABLISHED; `switching_dependency` probe NOT TRIGGERED)
- Negative assessment claim boundary stating what evidence does and does not establish

Not a null, not a schema error, not a pending state. Zero layer records with a populated negative assessment is a complete, valid record.

### R6 — Jurisdiction-bounded vs jurisdiction-agnostic records

**Cases:** S4, S5, S7 (jurisdiction load-bearing at layer-record level) vs S3 (jurisdiction not load-bearing)

Jurisdiction is recorded on the layer record when it matters and is absent (not invented) when it does not.

### R7 — Refused layer candidates (negative capability)

**Cases:** S6 (`qualification_control` NOT ESTABLISHED), S5 (`standard_interface_control` NOT ESTABLISHED), S3 (both refused)

The ontology must record that a candidate layer was **considered and declined** without reserving a slot for it in the active taxonomy. Refusal references appear only inside negative, ambiguity, or refusal assessments — never as active-layer values, schema slots, placeholder classes, or classifiable layer records (see Research candidates above).

## Round-trip test (primary success criterion)

The operational test of ontology fidelity is a **lossless, non-tautological round-trip** of the eight MON-G1-LI cases.

### Procedure

1. **Input:** The eight case records in `research/v0.2/cases/MON-G1-S{1-8}.md` — finalized outcomes, layer records, mechanisms, loci, holders, evidence bindings, and claim boundaries. No re-extraction. No re-interpretation.
2. **Encode:** Represent each case in the candidate ontology (schema + instances).
3. **Extract:** Re-derive all normalized structural fields from the ontology representation alone — using only schema-defined extraction logic that does not branch on case identity.
4. **Compare:** Normalized structural fields against MON-G1-LI ground truth (not label-matching alone).

### Normalized structural fields (comparison target)

Round-trip comparison operates on these fields, normalized to a canonical form before diff:

| Field | Per | Match criterion |
|---|---|---|
| **outcome** | System | Same outcome enum value |
| **evidenced_layer_count** | System | Matches outcome (0, 1, or ≥2) |
| **ambiguity_assessment** | System | Present and complete when outcome = `ambiguous_layer`; competing interpretations not promoted to layer records |
| **negative_assessment** | System | Present and complete when outcome = `no_evidenced_control_layer`; includes refused/triggered probes |
| **layer_type** | Layer record | Same evidenced active layer type(s) only. Refused/untriggered probes are compared within the applicable assessment, never as layer-type values. |
| **mechanism** | Layer record | Same concrete control instrument/mechanism (from S0/S1); distinct from evidence source citations |
| **locus** | Layer record | Same **where** — without actor identity smuggled in |
| **holder** | Layer record | Same **who** — when evidenced; absent when not |
| **evidence_bindings** | Layer record | Same S0/S1 facts bound to same claims; no unattached evidence |
| **claim_boundary** | Layer record | No admissible claim lost; no inadmissible claim gained |
| **date / scope / jurisdiction** | Layer record (and system defaults) | Preserved; jurisdiction present iff load-bearing |

**Loss** = any admissible MON-G1 claim cannot be represented, or any inadmissible claim becomes representable.
**Inflation** = the ontology adds outcome, layer, mechanism, locus, holder, or boundary content not present in the evidence record.
**Distortion** = the ontology forces a different classification to fit the schema.
**Tautological pass** = round-trip succeeds only because the schema stores ground truth in non-structural escape hatches (see Falsifier 12).

Any loss, inflation, distortion, or tautological pass on any case → gate **FAIL**. The schema is revised or rejected; the case results are not revised.

### Ground-truth summary (from MON-G1-LI closeout — for evaluation reference)

| Case | Outcome | Layer record(s) | Locus (where) | Holder (who) | Special demand |
|---|---|---|---|---|---|
| S8 | `evidenced_control_layer` | `legal_exclusivity` | letters over post routes | USPS (statutory grantee) | positive control baseline |
| S1 | `evidenced_control_layer` | `capacity_control` | EUV scanner production | ASML | single holder |
| S2 | `evidenced_control_layer` | `capacity_control` | 2021 5 nm HVM capacity set | TSMC, Samsung | **R2: locus ≠ holders** |
| S6 | `multiple_evidenced_layers` | `capacity_control` + `access_gatekeeping` | China value chain; US defense procurement channel | absent (both layers) | **R3: per-record independence; mechanism ≠ evidence** |
| S4 | `evidenced_control_layer` | `access_gatekeeping` | general-public App Store channel | Apple (platform operator) | **R6: jurisdiction on layer record** |
| S5 | `evidenced_control_layer` | `access_gatekeeping` | Visa-network admission | Visa (network operator) | **R7: refused standard_interface** |
| S3 | `no_evidenced_control_layer` | **(zero records)** | — | — | **R5: negative assessment required** |
| S7 | `evidenced_control_layer` | `switching_dependency` | provider data-egress boundary | Named provider(s) | **R4: locus ≠ provider as locus** |

## Pass condition

The gate PASSES only if **all** of the following hold:

1. **Round-trip fidelity.** All eight cases round-trip on normalized structural fields with no loss, inflation, distortion, or tautological pass.
2. **Outcome/layer separation.** Outcome is a case-level primitive separate from the four-value active-layer enum. Zero evidenced layer records is a valid, explicit state.
3. **Primitive separation.** System, Outcome, Evidenced Layer Record, Layer, Control Mechanism, Locus, Holder, Evidence bindings, and Claim Boundary remain distinct; no field collapses two or more primitives.
4. **Locus/holder separation.** Locus carries *where*; Holder carries *who*. Actor identity does not appear in locus fields.
5. **Per-layer-record ownership.** Each evidenced layer record independently carries its own evidence bindings and claim boundary. S6 round-trips both records without shared bags.
6. **Four-layer ceiling.** Only the four active layers appear as classifiable layer-type values. Research candidates do not appear as reserved schema slots.
7. **Negative representability.** `no_evidenced_control_layer` (zero layer records + negative assessment) is first-class, and refused/untriggered layer references are representable inside the applicable assessment without entering the active-layer enum.
8. **Ambiguity representability.** `ambiguous_layer` (zero layer records + ambiguity assessment) is first-class. The ontology must represent genuine ambiguity without forcing classification into a positive or negative outcome. Competing interpretations stay in the assessment; they do not become evidenced layer records.
9. **Mechanism/evidence separation.** Control Mechanism is distinct from Evidence bindings. A source citation (e.g. a government report) is evidence, not a mechanism.
10. **Metadata discipline.** Date and scope are mandatory; jurisdiction is present only when load-bearing, at the appropriate record level.
11. **No prohibited features.** No score, severity, ranking, dominance, probability, disguised quantitative field, or round-trip escape hatch.
12. **No silent inference.** The schema cannot derive classifications from fields that would require S2 or from market-share/dominance inputs alone.
13. **No case-specific tailoring.** Every primitive is semantically general; extraction logic does not branch on case identity.

## Falsifier

The gate FAILS if **any** of the following hold:

1. **History changed to fit schema.** Any MON-G1-LI case result is altered, softened, or re-labeled to make the ontology work.
2. **Loss on round-trip.** Any case loses outcome, mechanism, locus, holder, evidence-binding, or claim-boundary content on encode → extract.
3. **Inflation on round-trip.** The ontology adds classification content not in the MON-G1 evidence record (e.g. S3 gains a layer record; S2 locus collapses to "TSMC dominates").
4. **Layer → entity collapse.** A layer field becomes a generic "control present" flag or a company/sector descriptor rather than a typed control mechanism.
5. **Outcome conflated with layer.** `ambiguous_layer` or `no_evidenced_control_layer` appears as a layer value, null layer, or empty enum rather than a separate outcome with zero layer records.
6. **Cannot represent ambiguity.** Genuine ambiguity is forced into a positive layer assignment or collapsed into `no_evidenced_control_layer`; competing interpretations become evidenced layer records; or `ambiguous_layer` requires a workaround that implies pending classification.
7. **Cannot represent negatives.** S3 requires a workaround, null hack, or "unclassified" bucket that implies pending classification.
8. **Mechanism conflated with evidence.** A source citation stands in for the control mechanism (e.g. "BIS Section 232 findings" as mechanism rather than as evidence binding).
9. **Cannot represent multiples.** S6's two independent layer records cannot coexist without merge, ranking, or primary/secondary hierarchy; or share a single evidence/boundary bag.
10. **Locus carries who.** S2 places TSMC/Samsung in locus without a separate holder field; S7 places provider name in locus without a distinct egress-boundary locus; S6 Layer A places a capacity structure in holder.
11. **Cannot represent collective holders.** S2's multi-actor holder set cannot be expressed without reducing to a single actor.
12. **Holder invented when absent.** A geography, capacity structure, or channel is placed in `holder` because the field exists, when admitted evidence does not resolve discrete actors (S6 Layer A).
13. **Cannot represent provider-specific scope.** S7's per-provider egress boundary cannot be scoped without lifting to market level.
14. **Reserved research slots.** Schema includes enum values, nullable fields, or placeholder classes for `qualification_control`, `standard_interface_control`, or `temporal_constraint`; or refusal references appear as classifiable layer records.
15. **Tautological round-trip / extraction escape hatch.** Extraction requires any of: case-specific exception; `expected_layer`, `original_result`, `raw_case`, `ground_truth`, or equivalent stored answer fields; opaque free-text blob from which the answer is reconstructed; or logic that branches on case identity (`S1`…`S8`) to recover ground truth. **If extraction must know which case it is handling to succeed → FAIL.**
16. **Prohibited quantitative surface.** Any score, severity, dominance level, ranking, probability, or composite metric appears — explicit or disguised.
17. **Inference beyond evidence.** Schema includes rules, defaults, or computed fields that assign layers from dominance, market share, popularity, or antitrust conclusions.
18. **Case-specific tailoring.** Any field, cardinality rule, or exception exists only because one case required it and is not semantically general.

## Freeze rules

1. This gate spec design is **frozen** as of 2026-08-29. Amendments require a documented revision and re-review.
2. The eight MON-G1-LI cases are the **only** round-trip test set for MON-G2-OF v0.2. No case may be swapped, dropped, or added to rescue a weak schema.
3. MON-G1-LI classifications are ground truth. Re-classification is out of scope.
4. Candidate ontology schema (Step 2) may proceed on a branch from the merged checkpoint. Production adoption awaits gate closeout (Step 4).
5. The round-trip evaluation (`GATE_MON-G2-OF_EVALUATION.md`) is the only closeout artifact. The gate closes on round-trip performance, not on aesthetic schema elegance.
6. A PASS adopts the tested ontology version; it does not authorize skipping ahead in the DEC-005 build sequence.

## Evaluation order (fixed for auditability)

Round-trip evaluation proceeds in the same order as MON-G1-LI extraction (not a priority ranking):

1. MON-G1-S8 — legal exclusivity (positive control baseline)
2. MON-G1-S1 — EUV lithography (single-actor capacity)
3. MON-G1-S2 — leading-edge foundry (collective holders; locus ≠ who)
4. MON-G1-S6 — rare-earth magnets (multiple independent layer records)
5. MON-G1-S4 — mobile app distribution (jurisdiction-bounded access)
6. MON-G1-S5 — card-payment acceptance (refused interface layer)
7. MON-G1-S3 — CUDA ecosystem (zero layer records; negative assessment)
8. MON-G1-S7 — cloud hyperscaler (provider-specific switching; locus ≠ provider)

## Artifact sequence (strict)

| Step | Artifact | Status |
|---|---|---|
| 1 | This gate spec (`ONTOLOGY_FIDELITY_GATE.md`) | **Frozen — accepted 2026-08-29 (revision 4)** |
| 2 | Candidate ontology schema (classes, fields, constraints) | **Authorized — next step** |
| 3 | Round-trip evaluation (`GATE_MON-G2-OF_EVALUATION.md`) | Blocked until Step 2 exists |
| 4 | Gate closeout decision | Blocked until Step 3 complete |

**Do not skip steps.** A round-trip evaluation before a candidate schema exists is out of process.

## What a PASS authorizes — and only then

A PASS authorizes:

- **Adoption of the tested ontology version** as the ontology conforming to DEC-005 (four active layers; primitive separation; evidence discipline as specified here).
- **Opening the successor gate** for the interface thesis (the next step in the DEC-005 build sequence).

A PASS does **not** authorize:

- Interface **implementation** or UI surfaces (the interface thesis has its own gate)
- Data architecture or production surfaces (separate gate, after interface thesis)
- Scores, rankings, severity, dominance levels, or monopoly probability
- Entity or sector pages
- Admission of research candidate layers without a new gate
- Monetization

DEC-005 build order remains: **ontology → interface thesis → data architecture**. A PASS on MON-G2-OF completes the ontology step and opens the interface-thesis gate only. It does not skip to data architecture.

A FAIL is recorded honestly. The schema is revised or abandoned. MON-G1-LI is not reopened.

## Relationship to MON-G1-LI

MON-G1-LI asked: *can control layers be identified reproducibly from primary evidence?*
MON-G2-OF asks: *can those identifications survive formal representation without distortion?*

MON-G1-LI is closed PASS. Its case records are the fidelity benchmark. MON-G2-OF does not re-test identifiability; it tests whether the **container** (ontology) preserves what the **instrument** (layer identifiability framework) already proved.
