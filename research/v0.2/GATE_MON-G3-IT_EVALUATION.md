# MON-G3-IT — Semantic/Readback Evaluation (Step 3)

**Gate:** MON-G3-IT (Interface Thesis)
**Gate spec:** `INTERFACE_THESIS_GATE.md` (DESIGN FROZEN — accepted 2026-08-29, revision 2)
**Thesis under test:** `CANDIDATE_INTERFACE_THESIS.md` (`thesis_id`: `mon-g3-it-candidate-v0.2`) — **Accepted for Step 3 — 2026-08-29** (unchanged in this evaluation)
**Ontology binding:** `mon-g2-of-candidate-v0.2` (DEC-006); instances in `ontology/instances/`
**Evaluation date:** 2026-08-29
**Status:** **Accepted — 2026-08-29** (Step 3; Step 4 closeout authorized — not enacted here)
**Branch checkpoint base:** `fad4849` (candidate interface thesis merge)
**Method:** Instance → grammar render (§1–§8 only) → blind extract → full-content compare to locked GT
**Runner:** `interface/tools/run_interface_readback.py`
**Machine report:** `interface/readback-report.json`
**Ground truth:** `ontology/ground-truth/normalized-fields.json` (same locked target as MON-G2-OF)
**Representations:** `interface/representations/MON-G1-S{1-8}.md`

> This evaluation tests **semantic interface fidelity**. It does not re-classify MON-G1-LI cases, does not amend the candidate thesis, and does not implement UI. If a grammar defect is found, disposition is **return to Step 2** — not patch-inside-evaluation.

## 0. Pipeline (fixed)

1. **Load** — eight adopted ontology instances (`ontology/instances/MON-G1-S{1-8}.json`).
2. **Render** — `render_representation(instance)` applies only the general interface grammar (§1–§8). No case-id argument; no consultation of thesis §10; no branching on `S1`…`S8`.
3. **Blind extract** — `extract_from_representation(text)` recovers normalized fields from the representation string alone (no case id, no GT, no filename).
4. **Compare** — after extract, map audit stem → locked ground truth for comparison selection only.
5. **Ambiguity structural** — separate fixture + grammar-doc check; **outside** the 8/8 denominator.

### Full-content comparison target

Same field set as MON-G2-OF Step 3: outcome, system scope/date, per-layer type/mechanism/locus/holders/bounds/jurisdiction, full evidence bindings (incl. S1 derivation), full claim boundaries, refusal references, negative assessment body.

### Blind / tautology control

| Control | Result |
|---|---|
| No case ID in render/extract function bodies | Static scan clean |
| No GT / `expected_*` / `EVALUATION_ORDER` in render/extract | Static scan clean |
| Uniform extraction rules for all eight | Yes |
| Case identity used only after extract to select GT | Yes |
| Thesis §10 not used in render path | Yes (render implements §1–§8 structure only) |

---

## 1. Aggregate result

| Level | Result |
|---|---|
| Eight-case semantic readback | **8/8 PASS** |
| `ambiguous_layer` structural conformance | **PASS** (outside 8/8) |
| Gate falsifiers triggered | **None** |
| Blocker (return to Step 2) | **No** |
| Thesis amended during evaluation | **No** |

**Evaluation verdict (Accepted — 2026-08-29; not a closeout decision):** under full-content compare via the accepted interface grammar, all eight frozen cases read back without loss, inflation, or semantic distortion; ambiguity structural conformance PASSes outside the denominator. Gate remains open until Step 4.

---

## 2. Per-case results (audit order)

| Case | Semantic readback | Loss | Inflation | Distortion | Tautology | Gate falsifiers | Case verdict |
|---|---|---|---|---|---|---|---|
| S8 | PASS | no | no | no | no | none | **PASS** |
| S1 | PASS | no | no | no | no | none | **PASS** |
| S2 | PASS | no | no | no | no | none | **PASS** |
| S6 | PASS | no | no | no | no | none | **PASS** |
| S4 | PASS | no | no | no | no | none | **PASS** |
| S5 | PASS | no | no | no | no | none | **PASS** |
| S3 | PASS | no | no | no | no | none | **PASS** |
| S7 | PASS | no | no | no | no | none | **PASS** |

### Pressure-case notes (from readback, not thesis §10)

- **S8:** Single `legal_exclusivity` panel; excluded list recovered intact (blocks delivery-wide overclaim at boundary).
- **S2:** WHERE = capacity-set locus text; WHO = sorted holder list — locus not replaced by holder names in extract.
- **S6:** Two independent Layer panels (equal structure); holders absent on both (`holders not resolved…` → `[]`); jurisdiction recovered **only** on the access_gatekeeping panel; capacity panel has `jurisdiction: null`; no system-level jurisdiction strip; qualification refusal in post-panel Refusal notes strip.
- **S4 / S5 / S7:** Layer-scoped jurisdiction strings recovered on owning panels only; system header = scope + date + outcome only.
- **S3:** Negative result body + `ZERO_EVIDENCED_LAYERS: true`; no Layer panels; no invented Claim–evidence rows; both refusal notes + full claim boundary recovered.
- **S1 / S7:** Mechanism and locus recovered as distinct fields; holder list does not occupy WHERE.

---

## 3. `ambiguous_layer` structural conformance (outside 8/8)

| Required | Result |
|---|---|
| Grammar defines presentation for `outcome = ambiguous_layer` | PASS (thesis §3 / §7) |
| Representation shows zero evidenced layers | PASS (`ZERO_EVIDENCED_LAYERS: true`; extract count 0) |
| Populated ambiguity assessment readable as first-class | PASS (Ambiguity result body) |
| ≥2 competing interpretations as assessment content | PASS (2 option lines) |
| No promotion to Layer panels / EvidenceBinding rows | PASS |
| No ghost / provisional / possible-layer chrome | PASS |
| Counted toward 8/8 | **No** |

Fixture (non-case): `interface/fixtures/ambiguous_layer_structural.json`  
Representation: `interface/representations/ambiguous_layer_structural.md`

---

## 4. Pass-condition checklist (gate § Pass condition)

| # | Condition | Result |
|---|---|---|
| 1 | Readback fidelity (8/8) | **PASS** |
| 2 | Primary-unit discipline (`SystemRecord`) | **PASS** (SYSTEM READING UNIT header; company not primary object) |
| 3 | Primitive separation in presentation | **PASS** (TYPE / INSTRUMENT / WHERE / WHO distinct; claim-bound rows; boundary co-present) |
| 4 | Multiple-layer independence (S6) | **PASS** |
| 5 | Negative semantics (S3) | **PASS** |
| 6 | Ambiguity structural conformance | **PASS** (outside 8/8) |
| 7 | Refusal hygiene | **PASS** (notes only; no layer marks) |
| 8 | Non-ordinal encoding | **PASS** (categorical labels only in grammar representation; no scores/meters) |
| 9 | Boundary salience | **PASS** (bounds + boundary before WHO in panel linear order; enforced in extract) |
| 10 | Blind protocol | **PASS** |

---

## 5. Honest limits

1. Representations are **grammar-faithful static readings**, not production UI pixels. Visual non-ordinal policy is checked at the grammar/representation level (categorical labels, equal panel structure), not as rendered CSS.
2. Ground truth is the **locked MON-G2-OF normalize form**. This gate does not re-litigate ontology encode fidelity.
3. **`ambiguous_layer` has no live MON-G1 instance**; conformance is structural + fixture-only.
4. **This is not Step 4.** Acceptance of this evaluation is required before closeout / thesis adoption.

---

## 6. Artifact inventory

| Artifact | Role |
|---|---|
| `CANDIDATE_INTERFACE_THESIS.md` | Accepted grammar under test (**not amended**) |
| `ontology/instances/MON-G1-S{1-8}.json` | Adopted encodes (input to render) |
| `ontology/ground-truth/normalized-fields.json` | Comparison targets |
| `interface/tools/run_interface_readback.py` | Render + blind extract + compare + ambiguity check |
| `interface/representations/*.md` | Grammar representations |
| `interface/fixtures/ambiguous_layer_structural.json` | Non-case ambiguity fixture |
| `interface/readback-report.json` | Machine-readable run output |
| This file | Human evaluation record |

---

## 7. Authorized next (not enacted here)

Step 3 acceptance authorizes **Step 4 closeout only**. Step 4 alone may:

1. Close MON-G3-IT as PASS and adopt `mon-g3-it-candidate-v0.2` as the interface thesis conforming to DEC-005 / DEC-006.
2. Authorize opening the successor **data-architecture** gate only.

Not authorized by Step 3 alone: interface implementation, site rewrite, scores, entity pages, monetization, or data architecture itself.

---

## 8. Disposition

**Step 3 — Accepted — 2026-08-29.** 8/8 readback PASS; ambiguity structural PASS (outside 8/8); no falsifiers; thesis unchanged; no return to Step 2.

**Step 4 — Authorized — next step** (closeout only). This evaluation does **not** close the gate, adopt the thesis, or open data architecture. Gate remains open until Step 4.
