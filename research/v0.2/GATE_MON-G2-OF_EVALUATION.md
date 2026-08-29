# MON-G2-OF — Round-Trip Evaluation (Step 3)

**Gate:** MON-G2-OF (Ontology Fidelity)
**Gate spec:** `ONTOLOGY_FIDELITY_GATE.md` (DESIGN FROZEN — accepted 2026-08-29)
**Schema under test:** `ontology/CANDIDATE_ONTOLOGY_SCHEMA.md` + `ontology/candidate-schema.json` (`schema_version`: `mon-g2-of-candidate-v0.2`)
**Evaluation date:** 2026-08-29
**Revision:** full-content compare — **Step 3 Accepted 2026-08-29**
**Status:** Evaluation accepted; provisional Gate verdict PASS; gate closeout (Step 4) authorized but not enacted in this artifact.
**Branch checkpoint base:** `bed909b` (candidate schema merge)
**Method:** Encode → Validate → Generic extract → Normalize → **Full-content** field-by-field compare
**Runner:** `ontology/tools/run_roundtrip.py` (`compare_mode: full_content`)
**Machine report:** `ontology/roundtrip-report.json`
**Ground truth:** `ontology/ground-truth/normalized-fields.json` (see `ground-truth/README.md`)

> This evaluation tests **representational fidelity**. It does not re-classify MON-G1-LI cases. MON-G1 ground truth is fixed. **No schema amendment and no instance amendment** were made in this revision. The comparator and locked ground truth were strengthened; the eight instances are unchanged.

## 0. Pipeline (fixed)

1. **Encode** — eight instances in `ontology/instances/MON-G1-S{1-8}.json` from the frozen MON-G1-LI case records (unchanged in this revision).
2. **Validate** — each instance against `candidate-schema.json`.
3. **Generic extract** — `extract_normalized(instance)` only; no case-id argument; no filename read inside the extractor; no branching on `S1`…`S8`.
4. **Normalize** — full structural content (not counts/presence alone).
5. **Compare** — after extract, map file stem → locked ground truth for comparison selection only.
6. **Record** — three separate levels per case.

### Full-content comparison target

| Field | Compare mode |
|---|---|
| `outcome`, layer count | exact |
| system `scope`, `date` | exact object/string |
| per-layer `layer_type`, `mechanism`, `locus`, `holders` | exact (holders sorted) |
| per-layer `scope`, `date`, `jurisdiction` | exact value or null |
| each `evidence_bindings[]` | `claim`, `evidence_class`, `source`, `fact`; `derivation` required/compared for S1, forbidden for S0 |
| each `claim_boundary` | full `admissible` + ordered `excluded[]` |
| refusal references | `candidate_label` + `status` + `reason` |
| `negative_assessment` (S3) | `examined` + full claim boundary |
| `ambiguity_assessment` | full body when present |

### Tautology control

- Static scan of `extract_normalized` forbids tokens `MON-G1-S`, `case_id`, `expected_outcome`, `expected_layer`, `ground_truth`, `EVALUATION_ORDER`.
- **Any tautology flag forces that case's `structural_round_trip` to FAIL** and records **Falsifier 15** (fixed: previously summary could reject while per-case stayed PASS).
- Result this run: no flags.

---

## 1. Aggregate result

| Level | Result |
|---|---|
| Schema validation | **8/8 PASS** |
| Structural round-trip (full content) | **8/8 PASS** |
| Gate falsifiers triggered | **None** |
| Blocker (return to Step 2) | **No** |
| Gate closeout | **Not enacted** — Step 4 authorized; separate closeout required |

**Provisional evaluation verdict (not a closeout decision):** under full-content compare, candidate ontology `mon-g2-of-candidate-v0.2` survived lossless structural round-trip on the fixed eight-case set with no falsifier trigger.

---

## 2. Per-case results

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

### Pressure-case notes (full content)

- **S2:** locus text recovered as capacity set (not actor names); holders `["Samsung","TSMC"]` exact; all five bindings (claim/source/fact + S1 derivation) match.
- **S6:** two independent records; Layer A mechanism is capacity statement (not BIS title); BIS appears only in evidence `source`/`fact`; holders `[]`; Layer B jurisdiction string exact; refusal `qualification_control` / `not_established` / full `reason` match.
- **S3:** `evidenced_layer_records` length 0; `negative_assessment.examined` and full claim boundary match; both refusal reasons match.
- **S7:** locus = egress boundary string; holders named providers; UK jurisdiction; refusal reason for `standard_interface_control` match.

---

## 3. Three-level assessment

### 3.1 Schema validation — PASS (8/8)

Unchanged instances still validate, including INV-1 cardinalities, S0/S1 derivation discipline, refusal placement, and explicit `[]` for zero-record outcomes.

### 3.2 Structural round-trip — PASS (8/8)

Full-content compare (not count/presence projection). No loss, inflation, distortion, or tautology.

### 3.3 Gate falsifiers — none triggered

Including Falsifier 15 (tautology path now fails the case when flagged). Falsifier 6 (`ambiguous_layer`) remains structurally supported but unexercised by the fixed set (no ambiguity instance).

---

## 4. What changed in this revision (Step 3 only)

| Changed | Unchanged |
|---|---|
| `run_roundtrip.py` — full-content extract/compare; tautology fails case | Schema |
| `ground-truth/normalized-fields.json` — full bindings, boundaries, metadata, reasons | All eight instances |
| This evaluation + report | MON-G1 case classifications |
| Gate header blockquote bookkeeping (Step 2 accepted / Step 3 awaiting review) | Gate design / falsifier set |

---

## 5. Honest limits

1. Ground truth is a **locked expected normalize form** of the MON-G1 encode (see `ground-truth/README.md`). It is not live-derived from instances at runtime; editing instances without updating GT must fail.
2. **`ambiguous_layer`** still has no live instance in the fixed set.
3. **This is not Step 4.** Acceptance of this evaluation is required before closeout.

---

## 6. Artifact inventory

| Artifact | Role |
|---|---|
| `ontology/instances/MON-G1-S{1-8}.json` | Encoded instances (**unchanged**) |
| `ontology/ground-truth/normalized-fields.json` | Full-content comparison targets |
| `ontology/ground-truth/README.md` | Provenance |
| `ontology/tools/run_roundtrip.py` | Validate + generic extract + full compare |
| `ontology/roundtrip-report.json` | Machine-readable run output |
| This file | Human evaluation record |

---

## 7. Recommended disposition (for review — not enacted)

If this strengthened evaluation is accepted:

1. Proceed to **Step 4 closeout only** — adopt `mon-g2-of-candidate-v0.2` as conforming to DEC-005.
2. Only then open the successor gate for the interface thesis.
3. Do not open data architecture, scores, entity pages, or monetization from this evaluation alone.

---

## 8. Disposition

**Step 3 — Accepted 2026-08-29.** Provisional Gate verdict: PASS. No return to Step 2.

**Next:** Step 4 closeout only — record final gate verdict, adopt `mon-g2-of-candidate-v0.2` as the ontology conforming to DEC-005, and authorize opening the successor gate for the interface thesis. No interface implementation, data architecture, scores, entity pages, or monetization from Step 4 alone.
