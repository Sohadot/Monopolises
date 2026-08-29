# Data Architecture Fidelity Gate — Monopolises v0.2

**Gate ID:** MON-G4-DA
**Version:** 0.2
**Status:** **Open — draft for review — not DESIGN FROZEN** (revision 2 — required changes applied)
**Opened:** 2026-08-29
**Closed:** —
**Thesis under test:** Layered Monopolisation v0.2 (`THESIS_CANDIDATE.md`, DEC-005) via adopted ontology `mon-g2-of-candidate-v0.2` (DEC-006) and adopted interface thesis `mon-g3-it-candidate-v0.2` (DEC-007)
**Evaluation:** `GATE_MON-G4-DA_EVALUATION.md` (not yet created)
**Decision:** pending gate close
**Predecessor gate:** MON-G3-IT — Closed PASS (`INTERFACE_THESIS_GATE.md`, DEC-007)
**Adopted ontology:** `research/v0.2/ontology/CANDIDATE_ONTOLOGY_SCHEMA.md` (`schema_version`: `mon-g2-of-candidate-v0.2`)
**Adopted interface thesis:** `research/v0.2/CANDIDATE_INTERFACE_THESIS.md` (`thesis_id`: `mon-g3-it-candidate-v0.2`)

> This gate tests whether the **adopted Layered Monopolisation ontology and interface thesis** can be carried by a **data architecture** that stores and retrieves bounded `SystemRecord`s without semantic distortion. This document is **Open — draft for review** (revision 2). It is **not** DESIGN FROZEN. Step 2 (candidate logical data architecture) must not begin until this gate design is accepted and frozen. This is a **fidelity gate**, not a database-design gate and not an implementation gate.

## Governing question

> Can the adopted Layered Monopolisation ontology and interface thesis be carried by a data architecture that stores and retrieves bounded SystemRecords **without loss, inflation, semantic distortion, hidden inference, entity-centric restructuring, or destructive loss of dated history?**

Note what the question is not: it is not “PostgreSQL vs SQLite,” not “which API framework,” not “caching or performance,” and not “can we ship a database.” It is a question about whether a **persistent / retrievable data architecture** can carry the same semantic ownership the ontology and interface thesis already proved — without making overclaim or silent rewrite easier than fidelity.

### Governing principle

> **The data architecture may reorganize storage. It may not reorganize meaning.**

This principle guides design. It is **not** itself a PASS condition. Falsifiable ownership and reconstruction rules are stated as PASS conditions and falsifiers below.

## Provenance — what this gate does *not* inherit as binding

| Source | Role for MON-G4-DA |
|---|---|
| DEC-005 | Binding thesis + four-layer taxonomy; dated findings remain records of their date |
| DEC-006 | Binding ontology adoption (`mon-g2-of-candidate-v0.2`) |
| DEC-007 | Binding interface-thesis adoption; authorizes **opening** this successor gate only — not building data architecture, not implementing UI |
| `mon-g2-of-candidate-v0.2` | Binding structural primitives under test for persistence/retrieval |
| `mon-g3-it-candidate-v0.2` | Binding interface grammar that canonical retrieval must be able to feed **without interpretive reconstruction** |
| MON-G3-IT ambiguity fixture | Binding structural fixture reused unchanged: `research/v0.2/interface/fixtures/ambiguous_layer_structural.json` |

## What this gate tests — and what it does not

This gate tests **semantic persistence and retrieval fidelity**: whether a candidate logical data architecture can store and retrieve ontology `SystemRecord`s so that ownership, bounds, and meaning survive — not engine choice, not production readiness.

| In scope | Out of scope |
|---|---|
| Logical data architecture that preserves ontology ownership under store/retrieve | Production DB deployment, DDL as product surface, ORM choice |
| Persistence/retrieval evaluation on the eight frozen cases | Re-classification of MON-G1-LI cases |
| Canonical write contract + canonical read model → `SystemRecord` | API frameworks, caching, performance, indexing strategy as PASS criteria |
| Composability: retrieved read model → adopted interface grammar | Interface implementation, site redesign, production pages |
| Structural conformance: `ambiguous_layer` + history-preservation + write-integrity (outside 8/8) | Adding a ninth semantic rescue case |
| Identifier / version / history policy that preserves dated findings | Treating secondary indexes or optional entity/source tables as semantic roots |
| Optional technical normalization of entity/source labels | Making Holder existence depend on a global company registry, or detaching evidence from claim ownership |

## Binding inputs (frozen)

The data architecture under test **must** bind to these adopted primitives. It may not invent parallel concepts that collapse them.

```
SystemRecord
  outcome
  scope, date
  evidenced_layer_records[]   (always present; [] when zero)
  negative_assessment? / ambiguity_assessment? / refusal_assessment?
  └── EvidencedLayerRecord
        layer_type (ActiveLayerType ×4 only)
        control_mechanism
        locus
        holders[] (0..n)
        evidence_bindings[] (claim-specific)
        claim_boundary
        scope? / date? / jurisdiction?
```

Active layers only: `legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `switching_dependency`.  
Research candidates appear only as assessment references — never as active-layer enum members, reserved slots, or placeholder rows.

Adopted interface thesis `mon-g3-it-candidate-v0.2` remains the presentation contract that canonical retrieval must be able to feed without analyst judgment or case-specific adapters.

## Frozen data-architecture invariants (Step 1 — meaning, not storage engine)

These rules freeze **semantic ownership**, not physical tables. A later candidate architecture must satisfy them; storage normalization is free only within these constraints.

| Dimension | Frozen rule |
|---|---|
| **Canonical semantic / read root** | `SystemRecord` is the **canonical semantic root** and the **canonical read root**. Company/entity is **not** the semantic authority and must not redefine ownership, outcome, layer meaning, or claim boundaries. |
| **Secondary access paths** | Secondary indexes or query entry points **may** exist (including by holder, entity, source, layer, or date), provided they **resolve back** to canonical `SystemRecord`s and do **not** redefine ownership, outcome, layer meaning, or claim boundaries. |
| **Optional entity/source normalization** | Technical normalization tables for entity or source labels are **allowed**. Forbidden: making Holder validity depend on a global company registry; turning evidence into a shared bag without claim ownership. |
| **Storage normalization** | Free, provided meaning is reconstructible by a **generic** canonical read path with **no interpretive judgment**. |
| **Outcome cardinality** | All four outcomes remain first-class. Rules for evidenced-layer counts stay: 1 / ≥2 / 0+ambiguity / 0+negative. Outcome ≠ Layer. |
| **Per-layer ownership** | Mechanism, locus, holders, evidence bindings, claim boundary, and layer metadata (scope/date/jurisdiction) remain owned by the layer record that carries them — not semantically detached into shared bags. |
| **Evidence binding** | Each `EvidenceBinding` remains one unit: `claim ↔ evidence_class ↔ source ↔ fact ↔ derivation` (derivation only when S1). |
| **Claim Boundary** | Per owning record (layer or zero-record assessment). No system-wide shared boundary; no cross-layer leakage. |
| **Jurisdiction** | Layer-scoped only when load-bearing. Must not be promoted to System-level authority. |
| **Holders** | Support **0..n**. Architecture must not require a master-company / global entity registry record for a Holder to be valid. |
| **Refusals** | Assessment-only. Must not become evidenced layer rows or active-layer enum members. |
| **Research candidates** | No enum slots, reserved placeholders, or provisional layer rows. |
| **S0 / S1** | S0 forbids derivation; S1 requires derivation. No S2 / confidence / score classification field. |
| **Negative / ambiguity** | Zero evidenced layer records are an **explicit preserved state** (`[]` semantics) — not null, missing, or “data unavailable.” |
| **Historical integrity** | A dated finding must not be silently overwritten by a newer state or collapsed into present-tense “current truth.” A later “latest” convenience pointer, if present, may select a newer snapshot but must not erase or rewrite older dated snapshots. |
| **Scores / inference** | No score, rank, confidence, dominance, or monopoly-probability fields may carry classification. |
| **Technical IDs** | Allowed internally only if opaque and non-semantic, and only if they do not alter the canonical read model’s meaning. |
| **Lossless-or-reject** | An ontology-**valid** canonical write must be preserved **losslessly**. An ontology-**invalid** semantic write must be **rejected explicitly**. The architecture must not silently coerce, infer, auto-fill, drop, merge, promote, or rewrite semantic fields to manufacture validity. |

## Step 2 artifact requirements (frozen after DESIGN FROZEN — testable logical architecture)

A candidate data architecture (Step 2) is **incomplete** — and Step 3 must not begin — unless it specifies **all** of the following as an explicit, testable **logical architecture**. Prose aspiration without these contracts fails Step 2 completeness. Production DDL, DB deployment, and APIs are **not** required. Pseudo-schema or ER-style logical diagrams are **optional** illustrations only.

| Required section | What it must define |
|---|---|
| **Ownership / relationship model** | How SystemRecord, outcomes, layer records, assessments, evidence bindings, boundaries, holders, and metadata relate — preserving per-layer ownership. |
| **Cardinalities and integrity constraints** | Outcome ↔ layer-count rules; holders 0..n; bindings and boundaries owned by their records; refusals not layer rows. |
| **Canonical write contract** | What must be accepted on write from an adopted ontology instance; **lossless-or-reject** (no silent drop, merge, inference, coerce, auto-fill, promote, or rewrite to manufacture validity). |
| **Canonical read model** | How retrieval reconstructs a `SystemRecord` conforming to `mon-g2-of-candidate-v0.2` — generically, without case branching. |
| **Identifier strategy** | Separation of technical identity from semantic fields; opaque IDs must not become meaning; secondary indexes (if any) resolve to canonical SystemRecords. |
| **Version / history policy** | How dated findings are retained; no silent overwrite / present-tense collapse; how (if at all) a “latest” pointer coexists with preserved older snapshots. |
| **Layer-specific evidence / boundaries / jurisdiction** | How each remains attached to its owning layer (jurisdiction never System-promoted). |
| **Zero-record / refusal / ambiguity storage paths** | Explicit paths for `[]` + negative/ambiguity/refusal assessments — not null/missing. |
| **Retrieval → interface contract** | How the canonical read model can feed `mon-g3-it-candidate-v0.2` directly, without interpretive reconstruction or case-specific adapters. |
| **Explicit prohibited fields / relationships** | Scores, ranks, confidence, dominance, probability, entity-as-semantic-root, shared system boundary, candidate enum slots, S2 fields, silent coercion paths, etc. |

Without these contracts, ownership and history falsifiers cannot be tested; a vague architecture that “could store the JSON” is out of process.

## Fixed evaluation set

The **same eight MON-G1-LI systems**, in the same audit order. No swap, no drop, no ninth **semantic** rescue case. Cases are **not** re-classified; they are persistence/retrieval fixtures for the data architecture.

| Order | Case | Architecture pressure |
|---|---|---|
| 1 | S8 | Bounded `legal_exclusivity`; boundary must survive store/retrieve without inflation |
| 2 | S1 | Single-holder capacity; locus ≠ entity semantic root |
| 3 | S2 | Collective holders (0..n > 1); Locus ≠ Holder collapse |
| 4 | S6 | Multi-layer independence; layer-specific jurisdiction; absent holders (`[]`); refusal assessment |
| 5 | S4 | Layer-scoped jurisdiction / bounds must not lift to System |
| 6 | S5 | Positive-path refusal assessment; layer-scoped jurisdiction |
| 7 | S3 | Zero-record negative as explicit preserved state — not null/missing |
| 8 | S7 | Provider-specific switching; refusal assessment; layer-scoped jurisdiction |

### Structural conformance only (outside 8/8)

There is **no** live `ambiguous_layer` instance in the fixed eight, and the eight do not exercise multi-version history overwrite or invalid-write rejection. Step 3 therefore runs **three structural conformance checks only** — **outside** the 8/8 denominator:

#### A. `ambiguous_layer` conformance — **reuse MON-G3-IT fixture unchanged**

**Frozen fixture (binding):** `research/v0.2/interface/fixtures/ambiguous_layer_structural.json`  
Do **not** invent a new ambiguity payload after seeing a candidate architecture. Reuse this fixture **byte-for-byte / content-unchanged**.

| Required | Forbidden |
|---|---|
| Architecture stores/retrieves this fixture under `outcome = ambiguous_layer` | Treating the check as a ninth evaluation case |
| Retrieved `evidenced_layer_records = []` | Promoting competing interpretations to evidenced layer records |
| Populated ambiguity assessment reconstructible as first-class | Ghost / provisional / candidate layer rows |
| ≥2 competing interpretations as assessment content | Counting this check toward 8/8 PASS/FAIL |
| Fixture content unchanged from MON-G3-IT | Redesigning the fixture to fit the architecture |

#### B. History-preservation fixture — **frozen payloads A/B (below)**

A **technical, non-published, non-classification** fixture (not a MON-G1 case). The adopted ontology has **no** global `system_id`; therefore “same logical system” for this check is defined **only** by an **external opaque fixture-lineage key** belonging to the test harness.

| Rule | Requirement |
|---|---|
| **Lineage key** | Fixed test key: `mon-g4-da-history-lineage-001` |
| **Key placement** | External to the architecture write of the SystemRecord. The key **must not** enter the canonical `SystemRecord`, must not become an ontology field, and must not appear in the canonical read model. |
| **Snapshots** | Two complete ontology-valid `SystemRecord` payloads **A** then **B** (frozen below), sharing that external lineage key in the harness only. |
| **Dates** | A and B have **different** dated anchors. |
| **After writing B** | A and B must both remain **independently retrievable** as their own dated snapshots. |
| **Latest pointer (optional)** | If the architecture exposes a “latest” convenience pointer for the lineage, it may select B — but must **not** erase A, rewrite A, or convert B into timeless/present-tense truth. |

| Required | Forbidden |
|---|---|
| A survives after B is written | Treating the fixture as a ninth semantic case |
| Each version reconstructible to its own dated claim bounds | Silent replace / “current only” destructive update |
| Lineage key stays outside canonical SystemRecord | Collapsing both into one present-tense record |
| Check counted outside 8/8 | Using the fixture to re-classify any MON-G1 case; defining “same system” inside Step 2 instead of this frozen recipe |

##### Frozen history payload A

```json
{
  "schema_version": "mon-g2-of-candidate-v0.2",
  "system": {
    "scope": "MON-G4-DA history fixture — synthetic capacity probe (not a MON-G1 case)",
    "date": { "as_of": "2020-01-01", "label": "History fixture snapshot A — 2020" },
    "outcome": "evidenced_control_layer",
    "evidenced_layer_records": [
      {
        "layer_type": "capacity_control",
        "control_mechanism": {
          "statement": "Fixture-only: sole dated productive capacity for the synthetic probe tool in snapshot A."
        },
        "locus": { "statement": "Synthetic probe-tool production (fixture locus A)" },
        "holders": [{ "label": "FixtureHolder" }],
        "evidence_bindings": [
          {
            "claim": "Fixture A — sole producer statement for the synthetic tool",
            "evidence_class": "S0",
            "source": "MON-G4-DA history fixture source A (non-published)",
            "fact": "Snapshot A states FixtureHolder is the sole producer of the synthetic probe tool as of 2020-01-01."
          }
        ],
        "claim_boundary": {
          "admissible": "Fixture A admits only a dated 2020 capacity_control record at the synthetic probe-tool locus for FixtureHolder.",
          "excluded": [
            "Any present-tense restatement of snapshot A.",
            "Any claim that this fixture is a MON-G1 classification case.",
            "Any sufficiency or market-monopoly claim."
          ]
        },
        "date": { "as_of": "2020-01-01", "label": "Snapshot A layer date" }
      }
    ]
  }
}
```

##### Frozen history payload B

```json
{
  "schema_version": "mon-g2-of-candidate-v0.2",
  "system": {
    "scope": "MON-G4-DA history fixture — synthetic capacity probe (not a MON-G1 case)",
    "date": { "as_of": "2024-06-01", "label": "History fixture snapshot B — 2024" },
    "outcome": "evidenced_control_layer",
    "evidenced_layer_records": [
      {
        "layer_type": "capacity_control",
        "control_mechanism": {
          "statement": "Fixture-only: sole dated productive capacity for the synthetic probe tool in snapshot B (later dated finding)."
        },
        "locus": { "statement": "Synthetic probe-tool production (fixture locus B)" },
        "holders": [{ "label": "FixtureHolder" }],
        "evidence_bindings": [
          {
            "claim": "Fixture B — sole producer statement for the synthetic tool at the later date",
            "evidence_class": "S0",
            "source": "MON-G4-DA history fixture source B (non-published)",
            "fact": "Snapshot B states FixtureHolder is the sole producer of the synthetic probe tool as of 2024-06-01."
          }
        ],
        "claim_boundary": {
          "admissible": "Fixture B admits only a dated 2024 capacity_control record at the synthetic probe-tool locus for FixtureHolder.",
          "excluded": [
            "Any claim that snapshot B erases or replaces snapshot A.",
            "Any undated or timeless restatement of the fixture finding.",
            "Any claim that this fixture is a MON-G1 classification case."
          ]
        },
        "date": { "as_of": "2024-06-01", "label": "Snapshot B layer date" }
      }
    ]
  }
}
```

Harness procedure (fixed): write A under external lineage key `mon-g4-da-history-lineage-001` → write B under the **same** external lineage key → retrieve A and B independently → full-content compare each to its frozen payload (after semantic canonicalization below). Optional latest-pointer may resolve to B only.

#### C. Write-integrity / lossless-or-reject (structural, outside 8/8)

Architecture must **reject explicitly** ontology-invalid semantic writes. It must **not** silently coerce them into validity. Minimum frozen negative probes (illustrative; Step 3 may add equivalent probes under the same rule):

| Probe | Invalid condition | Required behavior |
|---|---|---|
| W1 | `evidence_class = S0` **with** a `derivation` field present | Explicit reject — must not drop derivation and accept |
| W2 | `outcome = no_evidenced_control_layer` **with** non-empty `evidenced_layer_records` | Explicit reject — must not empty the array and accept |

| Required | Forbidden |
|---|---|
| Invalid writes fail closed with an explicit rejection | Silent coerce / auto-fill / drop / merge / promote / rewrite to manufacture validity |
| Valid ontology writes still lossless | Counting this check toward 8/8 |
| Check outside 8/8 | Using rejection probes as classification cases |

## Evaluation method (Step 3 — frozen in design; executed later)

After a complete Step 2 candidate logical data architecture exists, evaluation has four parts:

### A. Eight-case persistence/retrieval round-trip (denominator = 8)

1. Start from each adopted ontology instance (`ontology/instances/MON-G1-S{1-8}.json`).
2. Apply the candidate architecture **write contract** (logical store — not production DB required).
3. Apply a **generic retrieval** path that produces the canonical **read model**.
4. Reconstruct to a `SystemRecord` conforming to the adopted ontology.
5. Apply **semantic comparison canonicalization** (below), then **full-content compare** to locked ground truth.
6. Case identity used **only after** retrieval/extract to select ground truth — never to drive write/read logic.

### Semantic comparison canonicalization (frozen before Step 2)

Ontology and interface do **not** treat incidental array order as semantic meaning for every collection. Adopted interface thesis allows multiple evidenced layers in array order **or any stable non-ranking order**. Therefore Step 3 must **not** FAIL a case solely because storage returned correct members in a different incidental order.

**Rule:** Compare **semantic content after deterministic, case-independent canonicalization** of collections whose order is not defined as meaning by the adopted ontology.

At minimum, canonicalize (content-based; preserve multiplicity; **no** case ID; **no** expected-result lookup):

| Collection | Canonicalization requirement |
|---|---|
| `evidenced_layer_records` | Deterministic order by content key (e.g. hash/sort of layer_type + mechanism + locus + boundary + bindings) — not by storage insertion order |
| `holders` | Deterministic order by holder label (or equivalent content key) |
| `evidence_bindings` | Deterministic order by content key (claim + class + source + fact [+ derivation]) |
| `refusal_references` | Deterministic order by content key (candidate_label + status + reason) |
| `competing_interpretations` | Deterministic order by content key (interpretation + active_layer_type_considered) |
| `claim_boundary.excluded` | Deterministic order by excluded-string content |

Canonicalization is a **comparator concern**, not a license for the architecture to reorder meaning-bearing structure arbitrarily inside a single binding or to drop/merge members. Multiplicity must be preserved. Incidental storage order must not become a new ontology.

### Blind / anti-tautology protocol (mandatory)

| Rule | Requirement |
|---|---|
| **No case ID at write/read** | Write and generic retrieve must not branch on `MON-G1-S1`…`S8`. |
| **No ground truth at retrieve** | Must not consult locked GT or case files to produce the read model. |
| **Uniform contracts** | Same write/read rules for all eight; no case-keyed adapters. |
| **Case identity after extract only** | Used only to select GT for comparison. |
| **Canonicalization case-independent** | Sort/hash keys derived from retrieved content only — never from expected GT or case id. |

### B. Structural conformance (outside 8/8)

1. `ambiguous_layer` — MON-G3-IT fixture reused unchanged.
2. History-preservation — frozen payloads A/B + lineage key above.
3. Write-integrity / lossless-or-reject — probes W1/W2 (and equivalents) above.

### C. Interface composability check

Retrieved canonical read models must be feedable into adopted interface thesis `mon-g3-it-candidate-v0.2` **without interpretive reconstruction** and **without case-specific adapters**. Failure here is architecture failure even if raw fields “look similar.”

**Ownership-failure falsifier (decisive):**

> **If the architecture can retrieve the facts but cannot reconstruct who owns each claim, boundary, and layer-specific bound without analyst judgment, the architecture has failed.**

That outcome means the architecture preserved **data** while losing **semantic ownership**.

## Pass condition

The gate PASSES only if **all** hold:

1. **Readback fidelity.** All eight cases round-trip without loss, inflation, or semantic distortion of outcome, layers, mechanism, locus, holders, evidence bindings, claim boundaries, and load-bearing metadata — after semantic comparison canonicalization.
2. **No case-specific logic.** Write/read paths do not branch on case identity (`S1`…`S8`).
3. **Multi-layer ownership.** S6’s (and any multi-layer system’s) layers remain independently owned and reconstructible (order-independent under canonicalization).
4. **No cross-record leakage.** EvidenceBindings and ClaimBoundaries do not leak across layer or assessment ownership.
5. **Zero-record preservation.** Negative (and structurally, ambiguity) outcomes preserve explicit `[]` + assessment — not null/missing.
6. **Refusal / candidate hygiene.** Refusals and research candidates remain outside active layers.
7. **Holder / Locus discipline.** Holders 0..n; Locus ≠ Holder; Holder validity does not depend on a forced master-company registry.
8. **Jurisdiction discipline.** Layer-scoped jurisdiction is not promoted to System.
9. **S0/S1 derivation discipline.** S0 without derivation; S1 with derivation; no S2/score classification fields.
10. **Interface composability.** Canonical retrieval can feed `mon-g3-it-candidate-v0.2` without interpretive reconstruction.
11. **Ambiguity structural conformance.** PASS outside 8/8 (MON-G3-IT fixture unchanged).
12. **History-preservation structural conformance.** PASS outside 8/8 (frozen A/B + lineage key).
13. **Write-integrity / lossless-or-reject.** Invalid semantic writes rejected explicitly; valid writes lossless — PASS outside 8/8.
14. **No scores / inference / entity-as-semantic-root.** Classification is not carried by score/rank/confidence/dominance/probability; secondary indexes do not redefine meaning.
15. **Technical normalization ≠ semantic authority.** Opaque IDs, joins, optional entity/source tables, and storage shapes do not redefine outcome/layer meaning in the canonical read model.

## Falsifier

The gate FAILS if **any** of the following hold:

1. **Entity-as-semantic-root.** Company/entity becomes the semantic / canonical-read authority instead of `SystemRecord` (secondary indexes alone are not this failure if they resolve back without redefining meaning).
2. **Forced company registry.** Architecture requires a global company/entity master record for a Holder to be valid.
3. **Multi-layer merge.** S6 (or any multi-layer system) collapses into one storage unit that cannot be separated without interpretation.
4. **Evidence bag.** Evidence becomes a global source bag detached from claim ownership.
5. **Shared system boundary.** ClaimBoundary is shared at System level or leaks across layers.
6. **Jurisdiction promotion.** Layer jurisdiction is lifted to System authority.
7. **Null zero-records.** Explicit `[]` becomes null/missing/unavailable.
8. **Candidate as layer.** Refused/research candidates become layer rows or active enum members.
9. **Score/inference fields.** S2 / confidence / score / rank / dominance / probability fields influence or replace classification.
10. **Destructive history.** A later update erases or silently replaces an older dated finding (including history fixture A after B).
11. **Case-keyed paths.** Write/read succeeds only via case ID branching or S1…S8-specific adapters.
12. **Analyst reconstruction required.** Architecture output needs analyst judgment to rebuild the canonical `SystemRecord`.
13. **Technical IDs change meaning.** Opaque IDs or joins alter outcome/layer semantics in the canonical read model.
14. **History rewritten to fit architecture.** Any MON-G1 classification is altered to make persistence work.
15. **Tautological round-trip.** Evaluation “succeeds” only via stored answers, case-id branching, GT leakage into write/read, or escape hatches that bypass structural retrieval. **If retrieval must know which case it is handling to succeed → FAIL.**
16. **Incomplete Step 2 architecture.** Candidate lacks any required Step 2 section (ownership model, cardinalities, write/read contracts including lossless-or-reject, ID strategy, history policy, layer-specific ownership, zero-record/refusal/ambiguity paths, interface retrieval contract, or prohibited fields).
17. **Ownership-failure test.** Facts retrieve, but claim/boundary/layer-bound ownership cannot be reconstructed without analyst judgment.
18. **Ambiguity conformance failure.** Structural check for `ambiguous_layer` fails (including fixture redesign).
19. **History-preservation failure.** Structural history fixture fails (overwrite, present-tense collapse, versions not separately retrievable, or lineage key injected into canonical SystemRecord).
20. **Interface non-composability.** Retrieved read model cannot feed `mon-g3-it-candidate-v0.2` without interpretive reconstruction or case-specific adapters.
21. **Silent semantic coercion.** Architecture accepts an ontology-invalid write by silently coercing, inferring, auto-filling, dropping, merging, promoting, or rewriting semantic fields to manufacture validity (write-integrity probes W1/W2 or equivalents).
22. **Order-as-ontology.** Evaluation treats incidental collection order as semantic failure despite equal content under the frozen case-independent canonicalization rules — or conversely, uses case-id / expected-result keyed sorting to manufacture a PASS.

## Freeze rules

1. This gate **design is not frozen** until accepted on review. Amendments before freeze require documented revision and re-review. After DESIGN FROZEN, amendments require a documented revision before Step 2 proceeds or restarts.
2. The eight MON-G1 cases are the only semantic evaluation set. No ninth semantic case. No re-classification. `ambiguous_layer`, history-preservation, and write-integrity are structural conformance only (outside 8/8).
3. Structural fixtures for ambiguity (MON-G3-IT reuse) and history (payloads A/B + lineage key) are **frozen in this gate** before Step 2 — not designed by the candidate architecture.
4. Candidate data architecture (Step 2) must derive from DEC-005 + DEC-006 + DEC-007 + adopted ontology + adopted interface thesis, and must satisfy the Step 2 artifact requirements above.
5. No production database, API, site change, interface implementation, or “shipping storage” until this gate closes PASS (and even then, PASS authorizes only **adoption of the tested data architecture** — not production implementation).
6. Evaluation (`GATE_MON-G4-DA_EVALUATION.md`) is the sole closeout evidence artifact for this gate. No separate beauty-score or engine-benchmark report.
7. A FAIL returns to revise the candidate data architecture (or abandon it). It does not reopen MON-G3-IT, MON-G2-OF, or MON-G1-LI.

## Artifact sequence (strict)

| Step | Artifact | Status |
|---|---|---|
| 1 | This gate spec (`DATA_ARCHITECTURE_GATE.md`) | **Open — draft for review — not DESIGN FROZEN** (revision 2) |
| 2 | Candidate logical data architecture meeting **Step 2 artifact requirements** | Blocked until Step 1 DESIGN FROZEN |
| 3 | Persistence/retrieval fidelity evaluation on S8…S7 + structural checks (`GATE_MON-G4-DA_EVALUATION.md`) | Blocked until Step 2 exists and is complete |
| 4 | Gate closeout decision | Blocked until Step 3 complete |

**Do not skip steps.** A DB build before Step 1 freeze / Step 2 acceptance is out of process. A Step 2 document without the required logical contracts is incomplete.

## What a PASS authorizes — and only then

A PASS authorizes:

- **Adoption of the tested data architecture** as the persistence/retrieval posture conforming to DEC-005 / DEC-006 / DEC-007.

A PASS does **not** authorize:

- Production database implementation or deployment
- APIs, services, or caching layers as product surfaces
- Interface **implementation**, site redesign, or production pages
- Scores, rankings, entity/sector pages, new layers, monetization

Any move from **adopted data architecture** to **production implementation** requires a **separate later authorization**. DEC-005 build order remains: **ontology → interface thesis → data architecture**. MON-G4-DA completes the data-architecture step only when Closed PASS — and even then does not itself authorize build-out.

## Relationship to prior gates

| Gate | Question |
|---|---|
| MON-G1-LI | Can control layers be identified reproducibly from primary evidence? → **PASS** |
| MON-G2-OF | Can those identifications survive formal ontology without distortion? → **PASS** |
| MON-G3-IT | Can that ontology be translated into an interface thesis that stays legible without making overclaim easier? → **PASS** |
| MON-G4-DA | Can that ontology + interface thesis be carried by a data architecture that stores/retrieves bounded SystemRecords without semantic ownership loss? → **under draft (revision 2)** |

MON-G4-DA does not re-test identifiability, ontology fidelity, or interface grammar. It tests whether **storage and retrieval** preserve what the **instrument**, **container**, and **surface** already proved.
