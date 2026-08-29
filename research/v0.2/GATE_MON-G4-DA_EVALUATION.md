# MON-G4-DA — Persistence/Retrieval Evaluation (Step 3)

**Gate:** MON-G4-DA (Data Architecture Fidelity)
**Gate spec:** `DATA_ARCHITECTURE_GATE.md` (DESIGN FROZEN — accepted 2026-08-29, revision 2)
**Architecture under test:** `CANDIDATE_DATA_ARCHITECTURE.md` (`architecture_id`: `mon-g4-da-candidate-v0.2`) — **Accepted for Step 3 — 2026-08-29** (unchanged in this evaluation)
**Ontology binding:** `mon-g2-of-candidate-v0.2` (DEC-006); interface binding `mon-g3-it-candidate-v0.2` (DEC-007)
**Evaluation date:** 2026-08-29
**Status:** **Draft for review** (Step 3 complete for human acceptance; Step 4 blocked)
**Branch checkpoint base:** `a5a9a67` (candidate architecture merge)
**Method:** Instance → logical write → generic retrieval → canonical SystemRecord → semantic canonicalization → full-content compare + interface composability
**Runner:** `data-architecture/tools/run_persistence_eval.py`
**Logical store:** `data-architecture/tools/logical_store.py`
**Machine report:** `data-architecture/persistence-report.json`
**Ground truth:** `ontology/ground-truth/normalized-fields.json`

> This evaluation tests **semantic persistence and retrieval fidelity** under the accepted logical architecture. It does not implement DDL/DB/API/UI, does not amend the architecture spec, and does not close the gate.

## 0. Pipeline (fixed)

1. **Load** — eight adopted ontology instances (`ontology/instances/MON-G1-S{1-8}.json`).
2. **Write** — `LogicalStore.write(instance)` validates full ontology + architecture probes; persists normalized owned records (not opaque JSON blob).
3. **Retrieve** — `LogicalStore.read(snapshot_id)` reconstructs canonical `SystemRecord` (`system` object only).
4. **Canonicalize** — case-independent semantic canonicalization on system + normalized extract (gate § Semantic comparison canonicalization).
5. **Compare** — full-content compare to locked ground truth; case identity used **only after** retrieve to select GT.
6. **Interface composability** — retrieved `system` → `mon-g3-it-candidate-v0.2` grammar render (no case-specific adapter).
7. **Structural (outside 8/8)** — MON-G3-IT ambiguity fixture unchanged; frozen history A/B + lineage key; W1/W2 write-integrity probes only.

### Blind / tautology control

| Control | Result |
|---|---|
| No case ID in `write` / `read` bodies | Static scan clean |
| No GT / `expected_*` / `EVALUATION_ORDER` in write/read | Static scan clean |
| Uniform write/read contracts | Yes |
| Case identity after retrieve only | Yes |
| Architecture semantics unchanged during evaluation | Yes |

---

## 1. Aggregate result

| Level | Result |
|---|---|
| Eight-case persistence round-trip | **8/8 PASS** |
| Interface composability (8/8) | **8/8 PASS** |
| `ambiguous_layer` structural (MON-G3-IT fixture) | **PASS** (outside 8/8) |
| History-preservation structural (A/B + lineage) | **PASS** (outside 8/8) |
| Write-integrity W1/W2 | **PASS** (outside 8/8) |
| Gate falsifiers triggered | **None** |
| Blocker (return to Step 2) | **No** |

**Provisional evaluation verdict (not a closeout decision):** under full-content compare after semantic canonicalization, candidate logical architecture `mon-g4-da-candidate-v0.2` survived lossless persistence/retrieval on the fixed eight-case set; structural checks PASS outside the denominator; interface composability holds without interpretive reconstruction.

---

## 2. Per-case results (audit order)

| Case | Persistence round-trip | Interface composability | Loss | Inflation | Distortion | Tautology | Case verdict |
|---|---|---|---|---|---|---|---|
| S8 | PASS | PASS | no | no | no | no | **PASS** |
| S1 | PASS | PASS | no | no | no | no | **PASS** |
| S2 | PASS | PASS | no | no | no | no | **PASS** |
| S3 | PASS | PASS | no | no | no | no | **PASS** |
| S6 | PASS | PASS | no | no | no | no | **PASS** |
| S4 | PASS | PASS | no | no | no | no | **PASS** |
| S5 | PASS | PASS | no | no | no | no | **PASS** |
| S7 | PASS | PASS | no | no | no | no | **PASS** |

### Pressure-case notes

- **S6:** two independent layer records after retrieve; `holders: []` preserved; DoD jurisdiction only on access_gatekeeping layer; qualification refusal in `refusal_assessment`.
- **S3:** zero layers + negative assessment; no layer rows invented in store.
- **S2:** collective holders recovered; locus ≠ holder labels.
- **S4/S5/S7:** layer-scoped jurisdiction not promoted to system level in store or read model.

---

## 3. Structural conformance (outside 8/8)

### A. `ambiguous_layer` — MON-G3-IT fixture unchanged

Fixture: `interface/fixtures/ambiguous_layer_structural.json` (byte/content unchanged). Write → read → semantic match; ≥2 competing interpretations; `evidenced_layer_records = []`.

### B. History-preservation — frozen A/B

Fixtures: `data-architecture/fixtures/history_payload_{a,b}.json`  
Lineage key: `mon-g4-da-history-lineage-001` (external; not in SystemRecord). After write B, A and B independently retrievable; latest pointer = B; A unchanged.

### C. Write-integrity — W1/W2 only

| Probe | Result |
|---|---|
| W1 (`S0` + `derivation`) | Explicit reject |
| W2 (negative + non-empty layers) | Explicit reject |

---

## 4. Pass-condition checklist (gate)

| # | Condition | Result |
|---|---|---|
| 1 | 8/8 readback fidelity | **PASS** |
| 2 | No case-specific write/read logic | **PASS** |
| 3 | Multi-layer ownership (S6) | **PASS** |
| 4 | No cross-record leakage | **PASS** |
| 5 | Zero-record preservation (S3) | **PASS** |
| 6 | Refusal / candidate hygiene | **PASS** |
| 7 | Holder / Locus discipline | **PASS** |
| 8 | Jurisdiction discipline | **PASS** |
| 9 | S0/S1 derivation discipline | **PASS** |
| 10 | Interface composability | **PASS** |
| 11 | Ambiguity structural | **PASS** (outside 8/8) |
| 12 | History-preservation structural | **PASS** (outside 8/8) |
| 13 | Write-integrity / lossless-or-reject | **PASS** (outside 8/8) |
| 14 | No scores / entity-as-semantic-root | **PASS** |
| 15 | Technical normalization ≠ semantic authority | **PASS** |

---

## 5. Honest limits

1. Evaluation uses an **in-memory logical store** implementing the Step 2 contracts — not production DDL/DB/API.
2. Comparator applies **semantic canonicalization** to both retrieved extract and locked GT for order-independent collections (per frozen gate rule).
3. Optional collection **absent vs `[]`** fidelity is implemented in the logical store; the fixed eight instances mostly use explicit `[]` where applicable (e.g. S6).
4. **This is not Step 4.** Acceptance of this evaluation is required before closeout.

---

## 6. Artifact inventory

| Artifact | Role |
|---|---|
| `CANDIDATE_DATA_ARCHITECTURE.md` | Accepted architecture under test (**not amended**) |
| `data-architecture/tools/logical_store.py` | Normalized logical store (write/read) |
| `data-architecture/tools/run_persistence_eval.py` | Step 3 runner |
| `data-architecture/fixtures/history_payload_{a,b}.json` | Frozen history payloads |
| `data-architecture/persistence-report.json` | Machine report |
| `interface/fixtures/ambiguous_layer_structural.json` | Reused ambiguity fixture |
| This file | Human evaluation record |

---

## 7. Recommended disposition (for review — not enacted)

If this evaluation is accepted:

1. Proceed to **Step 4 closeout only** — adopt `mon-g4-da-candidate-v0.2` as the data architecture conforming to DEC-005 / DEC-006 / DEC-007.
2. Do **not** authorize production DB/API/UI from this evaluation alone.

If a **contract** defect is found: reject evaluation and return formally to **Step 2** — do not patch architecture inside this evaluation artifact.

---

## 8. Disposition

**Step 3 — awaiting review.** Provisional: 8/8 persistence PASS; interface composability 8/8; structural checks PASS (outside 8/8); no falsifiers; architecture unchanged.

**Step 4 — Blocked** until Step 3 is accepted.
