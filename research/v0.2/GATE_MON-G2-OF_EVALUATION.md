# MON-G2-OF — Round-Trip Evaluation (Step 3)

**Gate:** MON-G2-OF (Ontology Fidelity)
**Gate spec:** `ONTOLOGY_FIDELITY_GATE.md` (DESIGN FROZEN — accepted 2026-08-29)
**Schema under test:** `ontology/CANDIDATE_ONTOLOGY_SCHEMA.md` + `ontology/candidate-schema.json` (`schema_version`: `mon-g2-of-candidate-v0.2`)
**Evaluation date:** 2026-08-29
**Branch checkpoint base:** `bed909b` (candidate schema merge)
**Method:** Encode → Validate → Generic extract → Normalize → Field-by-field compare
**Runner:** `ontology/tools/run_roundtrip.py`
**Machine report:** `ontology/roundtrip-report.json`

> This evaluation tests **representational fidelity**. It does not re-classify MON-G1-LI cases. MON-G1 ground truth is fixed. No schema amendment was made during this step. No case was altered to fit the schema.

## 0. Pipeline (fixed)

1. **Encode** — eight instances in `ontology/instances/MON-G1-S{1-8}.json` from the frozen MON-G1-LI case records (no reinterpretation).
2. **Validate** — each instance against `candidate-schema.json` (JSON Schema draft 2020-12).
3. **Generic extract** — `extract_normalized(instance)` only; no case-id argument; no filename read inside the extractor; no branching on `S1`…`S8`.
4. **Normalize** — structural fields listed in the gate (outcome, layer count, layers, refusals, assessments, metadata presence).
5. **Compare** — after extract, map file stem → `ground-truth/normalized-fields.json` for comparison selection only.
6. **Record** — three separate levels per case (below).

**Tautology control:** static scan of `extract_normalized` forbids tokens `MON-G1-S`, `case_id`, `expected_outcome`, `expected_layer`, `ground_truth`, `EVALUATION_ORDER`. Result: no flags.

---

## 1. Aggregate result

| Level | Result |
|---|---|
| Schema validation | **8/8 PASS** |
| Structural round-trip | **8/8 PASS** |
| Gate falsifiers triggered | **None** |
| Blocker (return to Step 2) | **No** |
| Gate closeout | **Not enacted** — this file is the evaluation for review; Step 4 decision remains separate |

**Provisional evaluation verdict (not a closeout decision):** the candidate ontology version `mon-g2-of-candidate-v0.2` survived lossless structural round-trip on the fixed eight-case set with no falsifier trigger under this run.

---

## 2. Per-case results

Evaluation order matches the gate (not a priority ranking).

| Case | Schema validation | Structural round-trip | Loss | Inflation | Distortion | Tautology | Gate falsifiers | Case verdict |
|---|---|---|---|---|---|---|---|---|
| S8 | PASS | PASS | no | no | no | no | none | **PASS** |
| S1 | PASS | PASS | no | no | no | no | none | **PASS** |
| S2 | PASS | PASS | no | no | no | no | none | **PASS** |
| S6 | PASS | PASS | no | no | no | no | none | **PASS** |
| S4 | PASS | PASS | no | no | no | no | none | **PASS** |
| S5 | PASS | PASS | no | no | no | no | none | **PASS** |
| S3 | PASS | PASS | no | no | no | no | none | **PASS** |
| S7 | PASS | PASS | no | no | no | no | none | **PASS** |

### MON-G1-S8 — legal exclusivity (positive control)

- **Encoded:** `evidenced_control_layer` / `legal_exclusivity`; locus letters over post routes; holder USPS; three S0 bindings; claim boundary intact.
- **Schema validation:** PASS
- **Structural round-trip:** PASS — outcome, layer type, mechanism, locus, holder, evidence bindings, claim boundary recovered.
- **Gate falsifiers:** none
- **Case verdict:** PASS

### MON-G1-S1 — EUV capacity (single holder)

- **Encoded:** `evidenced_control_layer` / `capacity_control`; locus EUV scanner production; holder ASML; S0+S1 bindings; mechanism ≠ source citation.
- **Schema validation:** PASS
- **Structural round-trip:** PASS
- **Gate falsifiers:** none
- **Case verdict:** PASS

### MON-G1-S2 — collective holders; locus ≠ who

- **Encoded:** `evidenced_control_layer` / `capacity_control`; locus `2021 leading-edge (5 nm) HVM logic capacity set`; holders TSMC + Samsung (sorted on extract); locus does not carry actor identity.
- **Schema validation:** PASS
- **Structural round-trip:** PASS
- **Gate falsifiers:** none (Falsifier 10/11 not triggered)
- **Case verdict:** PASS

### MON-G1-S6 — multiple layers; per-record ownership; R7 refusal

- **Encoded:** `multiple_evidenced_layers`; Layer A `capacity_control` (mechanism = concentrated all-stage capacity; evidence = BIS 232; holders `[]`); Layer B `access_gatekeeping` (mechanism = source-origin admission restriction; evidence = statute/DFARS; jurisdiction present); `refusal_assessment` for `qualification_control` `not_established`.
- **Schema validation:** PASS
- **Structural round-trip:** PASS — both records independently recovered; refusal recovered without entering active-layer enum.
- **Gate falsifiers:** none (Falsifier 8/9/12/14 not triggered)
- **Case verdict:** PASS

### MON-G1-S4 — jurisdiction-bounded access

- **Encoded:** `access_gatekeeping`; US jurisdiction on layer record; holder Apple.
- **Schema validation:** PASS
- **Structural round-trip:** PASS
- **Gate falsifiers:** none
- **Case verdict:** PASS

### MON-G1-S5 — positive outcome + refusal (R7)

- **Encoded:** `access_gatekeeping`; `refusal_assessment` for `standard_interface_control` `not_established` (not a layer record).
- **Schema validation:** PASS
- **Structural round-trip:** PASS — refusal path on positive outcome works.
- **Gate falsifiers:** none
- **Case verdict:** PASS

### MON-G1-S3 — zero records + negative assessment

- **Encoded:** `no_evidenced_control_layer`; `evidenced_layer_records: []`; populated `negative_assessment` with refusals (`standard_interface_control` not_established; `switching_dependency` probe_not_triggered).
- **Schema validation:** PASS
- **Structural round-trip:** PASS — empty array present (not null/omission); negative assessment recovered.
- **Gate falsifiers:** none (Falsifier 5/7 not triggered)
- **Case verdict:** PASS

### MON-G1-S7 — provider-specific switching; locus ≠ provider-as-locus

- **Encoded:** `switching_dependency`; locus = provider-specific data-egress / switching boundary; holders AWS/Microsoft/Google/Civo (named in CMA Appendix N); jurisdiction UK; refusal of `standard_interface_control`.
- **Schema validation:** PASS
- **Structural round-trip:** PASS
- **Gate falsifiers:** none (Falsifier 10/13 not triggered)
- **Case verdict:** PASS

---

## 3. Three-level assessment

### 3.1 Schema validation

All eight instances validate against `candidate-schema.json`, including:

- Outcome ↔ cardinality constraints (INV-1)
- S0 forbids `derivation` / S1 requires `derivation` (INV-6)
- `refusal_assessment` allowed on positive outcomes; forbidden on S3
- Zero-record outcomes use explicit `[]`

**Level result: PASS (8/8)**

### 3.2 Structural round-trip

Compared normalized fields: outcome, evidenced_layer_count, layer_type, mechanism, locus, holders (sorted), evidence_binding_count / evidence_classes, claim_boundary excluded count + admissible presence, jurisdiction presence, refusal references (label+status), negative/ambiguity assessment presence, system scope/date presence.

No loss, inflation, distortion, or tautology on any case.

**Level result: PASS (8/8)**

### 3.3 Gate verdict (falsifier scan)

| Falsifier (gate) | Triggered? |
|---|---|
| 1 History changed to fit schema | No — cases unchanged |
| 2 Loss on round-trip | No |
| 3 Inflation on round-trip | No |
| 4 Layer → entity collapse | No |
| 5 Outcome conflated with layer | No |
| 6 Cannot represent ambiguity | Not exercised by fixed set (structural support present; no instance required) |
| 7 Cannot represent negatives | No — S3 PASS |
| 8 Mechanism conflated with evidence | No — S6 Layer A mechanism ≠ BIS citation |
| 9 Cannot represent multiples | No — S6 PASS |
| 10 Locus carries who | No — S2/S6/S7 PASS |
| 11 Cannot represent collective holders | No — S2 PASS |
| 12 Holder invented when absent | No — S6 holders `[]` |
| 13 Cannot represent provider-specific scope | No — S7 PASS |
| 14 Reserved research slots | No — refusals assessment-only |
| 15 Tautological round-trip | No — extractor static check clean |
| 16 Prohibited quantitative surface | No — absent from schema/instances |
| 17 Inference beyond evidence | No |
| 18 Case-specific tailoring | No — general schema; generic extract |

**Level result: no falsifier triggered**

---

## 4. Honest limits of this evaluation

1. **Semantic paraphrase:** mechanism/locus comparison uses the encoded statements (faithful transcriptions of MON-G1 admissible wording). This tests whether the schema **can carry** those statements without structural loss — not whether an independent human would paraphrase them identically.
2. **`ambiguous_layer`:** structural support exists in the schema; the fixed eight-case set contains no ambiguity instance, so that outcome was not round-tripped with live data (same limitation noted in the frozen gate).
3. **This is not Step 4.** A PASS evaluation does not itself adopt the ontology or open the interface-thesis gate. Closeout requires a separate decision after review of this file.

---

## 5. Artifact inventory

| Artifact | Role |
|---|---|
| `ontology/instances/MON-G1-S{1-8}.json` | Encoded instances |
| `ontology/ground-truth/normalized-fields.json` | Post-extract comparison targets |
| `ontology/tools/run_roundtrip.py` | Validate + generic extract + compare |
| `ontology/roundtrip-report.json` | Machine-readable run output |
| This file | Human evaluation record |

---

## 6. Recommended disposition (for review — not enacted)

If this evaluation is accepted:

1. Record a gate closeout decision (Step 4) adopting `mon-g2-of-candidate-v0.2` as the ontology conforming to DEC-005.
2. Only then open the successor gate for the **interface thesis**.
3. Do **not** open data architecture, scores, entity pages, or monetization from this evaluation alone.

If review finds a fidelity defect not caught here: return to Step 2; do not amend cases.

---

## 7. Stop point

Step 3 execution complete: **8 instances + this evaluation**. Awaiting review before Step 4 closeout.
