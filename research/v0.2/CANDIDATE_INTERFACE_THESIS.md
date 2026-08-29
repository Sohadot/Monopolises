# Candidate Interface Thesis — Monopolises v0.2

**Gate:** MON-G3-IT (Interface Thesis)
**Thesis ID:** `mon-g3-it-candidate-v0.2`
**Status:** **Draft for review** (Step 2 — grammar only; no evaluation; no implementation)
**Gate spec:** `INTERFACE_THESIS_GATE.md` (DESIGN FROZEN — accepted 2026-08-29, revision 2)
**Ontology binding:** `mon-g2-of-candidate-v0.2` (DEC-006 adopted)
**Authority:** DEC-005 + DEC-006 + frozen MON-G3-IT gate — **not** archived `INTERFACE_THESIS.md`
**Opened:** 2026-08-29

> This document is the **canonical candidate interface thesis**. It defines a testable **interface grammar**: how adopted ontology primitives become readable surfaces. It does **not** specify pixels, components, HTML/CSS/JS, or a site. Step 3 readback will apply this grammar to the eight frozen cases under the blind protocol.

### Governing principle (inherited)

> The interface must make the ontology easier to read, never easier to overclaim.

---

## 1. Primitive → presentation role

Each ontology primitive occupies exactly one presentation role in the reading unit. Roles are semantic, not CSS classes.

| Ontology primitive | Presentation role | Reader is meant to take it as |
|---|---|---|
| **SystemRecord** | **Reading unit (primary object)** | The whole bounded analysis: one system under a dated scope — not a company page. |
| **Outcome** | **Result state banner** | The classification result of the unit (evidenced / multiple / ambiguous / none) — categorical, not a score. |
| **scope** (system) | **Bound label — function** | What critical function is under analysis. |
| **date** (system) | **Bound label — time** | When the finding is anchored. |
| **EvidencedLayerRecord** | **Layer panel** | One independently evidenced control layer; one panel per record. |
| **ActiveLayerType** (`layer_type`) | **Layer type mark** | Which of the four active types — a category name, not intensity. |
| **ControlMechanism** | **Instrument block** | The concrete instrument/cause of control (must be readable as *why/how*, not a paraphrase of the type mark). |
| **Locus** | **Where block** | Where control sits inside the system — never substituted by a company name. |
| **Holder** | **Who list** (0..n) | Who occupies the locus when evidenced; empty list = absent holders, shown as explicit absence, not inventing an actor. |
| **EvidenceBinding** | **Claim–evidence row** | One row: claim ↔ class ↔ source ↔ fact (+ derivation if S1). |
| **ClaimBoundary** | **Boundary block** | Admissible record + excluded claims — co-present with the layer panel (or with the assessment for zero-layer outcomes). |
| **scope / date / jurisdiction** (layer) | **Layer-bound labels** | Overrides when the layer’s bounds differ from system defaults; jurisdiction only when load-bearing. |
| **NegativeAssessment** | **Negative result body** | Complete “no evidenced layer” reasoning — examined + refusals + boundary. |
| **AmbiguityAssessment** | **Ambiguity result body** | Competing interpretations + separation gap + boundary — not provisional layers. |
| **RefusalAssessment** / **RefusalReference** | **Refusal note** | Assessment context only: candidate_label + status + reason — never a layer mark. |
| **CompetingInterpretation** | **Ambiguity option line** | One source-defensible reading inside the ambiguity body — not an evidenced layer panel. |

**Forbidden role collisions:** Holder must not occupy the Locus role. Layer type mark must not replace the Instrument block. Company/holder must not occupy the Reading-unit role.

---

## 2. Reading order / information hierarchy

A single **System Reading Unit** is encountered top-to-bottom in this **mandatory order**. Later surfaces may not visually outrank earlier ones via size, color intensity, or motion that implies dominance.

```
1. System identity strip
      scope (function) · date (anchor)
2. Outcome state banner
      outcome enum (categorical)
3. Bounds reminder (if jurisdiction load-bearing anywhere in the unit)
      jurisdiction statement(s) from layer record(s) that carry them
      — placed early so the unit cannot be read as timeless/global before bounds are seen
4. Body (exactly one branch by outcome — see §3)
      A. Evidenced body (1 or ≥2 layer panels), or
      B. Negative result body, or
      C. Ambiguity result body
5. System-level refusal notes (if RefusalAssessment present on positive outcomes)
      after layer panels; never as layer marks
```

### Inside each Layer panel (positive outcomes)

Mandatory **linear reading order** within the panel (PASS-9 / Falsifier 17):

```
a. Layer type mark
b. Instrument block (mechanism)
c. Where block (locus)
d. Layer-bound labels (scope / date / jurisdiction overrides when present)
e. Boundary block (admissible + excluded)
f. Who list (holders) — or explicit “holders not resolved at discrete-actor level”
g. Claim–evidence rows (each EvidenceBinding)
```

**Boundary salience rule:** Layer-scoped bounds and the Claim Boundary appear **before** the Who list (or may be presented in parallel with it in a non-linear layout, but **never after** holder/entity interpretation in the linear order). A reader must not encounter holder/company interpretation before recovering bounds and admissible-vs-excluded boundary from the same panel.

**Hierarchy rule for falsifiers:** The primary takeaway of the unit is **outcome + bounded system + (for evidenced cases) locus + mechanism + bounds/boundary**. An unbounded holder/company name must not appear above or instead of steps 1–3 and panel items b–e as the headline of the unit.

---

## 3. Outcome-state rules (all four)

| Outcome | Body composition | Must show | Must not show |
|---|---|---|---|
| `evidenced_control_layer` | Exactly **one** Layer panel | Full panel order (§2) | Empty state; “data unavailable”; second ranked layer |
| `multiple_evidenced_layers` | **≥2** Layer panels, same visual weight | Each panel complete and independent | Primary/secondary badges; merged “control summary”; rank numbers |
| `no_evidenced_control_layer` | **Negative result body** only; layer region = explicit empty (`[]` semantics) | Examined statement; refusal notes; claim boundary | Blank page; error chrome; spinner; ghost layer panels |
| `ambiguous_layer` | **Ambiguity result body** only; layer region = explicit empty | Separation gap; ≥2 competing interpretation lines; claim boundary | Provisional layer panels; faded type marks; “possible layers” chips |

**Shared zero-record rule:** For both negative and ambiguity outcomes, the reading unit must state that **zero evidenced layer records** are present — as a positive assertion of result type, not as missing data.

---

## 4. Multi-layer treatment

When `outcome = multiple_evidenced_layers`:

1. Render **one Layer panel per** `EvidencedLayerRecord`, in array order (or any stable order that does not encode rank).
2. Panels share the same structural template and the same typographic weight — **no** “primary layer” styling.
3. No cross-panel merge card, score, or summary that collapses mechanisms/loci into one claim.
4. Refusal notes (system-level) appear **after** all panels, not inside a selected “main” panel.
5. A reader must be able to recover each panel’s mechanism, locus, holders, bindings, and boundary **independently**.

This is the presentation rule that S6 must satisfy in Step 3.

---

## 5. Evidence → claim relationship

Each `EvidenceBinding` is a **Claim–evidence row** with fixed columns/fields in one row-group:

| Field | Role in row |
|---|---|
| `claim` | The assertion this row supports (required lead) |
| `evidence_class` | `S0` or `S1` mark (categorical) |
| `source` | Citation |
| `fact` | Source-native or input fact |
| `derivation` | Present **only** if `S1`; forbidden if `S0` |

**Rules:**

- **EvidenceBinding rows render only inside evidenced Layer panels.** Zero-record assessments (NegativeAssessment, AmbiguityAssessment) render **only** their ontology-owned assessment fields; **no structured claim–evidence rows are invented.**
- Material that appears inside examined, claim-boundary prose, or other assessment text remains **assessment text as owned by the ontology** — it must not be restructured into EvidenceBinding presentation primitives the ontology does not attach to that assessment.
- No detached system-wide “Sources” cabinet that lists facts without their claims on a Layer panel.
- No aggregation of all bindings into a single paragraph that drops claim attachment.
- S0 vs S1 must remain visually distinguishable as class marks, not as confidence meters.

---

## 6. Claim-boundary placement

| Context | Placement |
|---|---|
| Each Layer panel | **Boundary block** appears **after** layer-bound labels and **before** Who list and Claim–evidence rows (panel order §2: … bounds → **boundary** → holders → evidence). |
| Negative result body | Boundary block is **inside the negative body**, after examined + refusals. No EvidenceBinding rows. |
| Ambiguity result body | Boundary block is **inside the ambiguity body**, after competing interpretations + separation gap. No EvidenceBinding rows. |

**Admissible** and **excluded** are both required surfaces:

- Admissible: the bounded statement the record supports.
- Excluded: explicit list of claims the framework must not make (each item readable).

**Forbidden:** moving the only copy of the boundary to a site footer, “legal” accordion default-collapsed out of the reading unit, or a tooltip on the company name. Boundary may be repeated in a global help page, but the **reading unit must carry its own copy**.

This placement is what PASS-9 (Boundary salience) tests.

---

## 7. Refusal / ambiguity treatment

### Refusal notes (all paths)

A `RefusalReference` renders as a **Refusal note** with three fields only:

- `candidate_label` (open string — not an ActiveLayerType mark)
- `status` (`refused` / `not_established` / `probe_not_triggered`)
- `reason`

**Visual rules:**

- Same weight as assessment prose; **not** the Layer type mark style.
- No faded layer chips, progress rings, or “near miss” meters.
- On positive outcomes: notes live in a **Refusal notes** strip after layer panels (`RefusalAssessment`).
- On negative/ambiguity: notes live inside the respective assessment body.

### Ambiguity body

1. State outcome = `ambiguous_layer` and zero evidenced layers.
2. List ≥2 **Ambiguity option lines** (`CompetingInterpretation`), each clearly labeled as assessment content.
3. If `active_layer_type_considered` is present, show it as text inside the option line — **not** as a Layer type mark that opens a Layer panel.
4. Show `separation_gap`.
5. Show Boundary block.

**Forbidden:** promoting any competing interpretation into an `EvidencedLayerRecord` panel.

---

## 8. Visual-encoding policy (non-ordinal)

### Allowed

| Variable | Allowed use |
|---|---|
| **Label / typography role** | Distinguish roles (banner vs panel vs note) by hierarchy of *kind*, not intensity of monopoly. |
| **Grouping / spacing** | Separate panels and blocks. |
| **Borders / rules** | Separate reading regions without encoding severity. |
| **Categorical marks** | Fixed labels for outcome enums and four layer types — same visual weight across types. |
| **Lists** | Holders, excluded claims, claim–evidence rows, competing interpretations. |

### Forbidden (ordinal / overclaim proxies)

| Variable | Forbidden use |
|---|---|
| Color scale / heat / red-alert | Severity, dominance, “danger,” monopoly intensity |
| Bar length / meter / gauge | Score, probability, “how monopolistic” |
| Size / weight / glow of holder or company | Dominance or rank |
| Motion / pulse | Urgency or live certainty beyond evidence |
| Map / network / graph chrome | Unsupported spatial or connection rhetoric |
| Stacked rank badges on layers | Primary/secondary among multiple layers |

**Certainty rule:** Presentation must not look more precise than sources (no fake live feeds, no over-resolved global maps). Dated and scoped labels remain visible; present-tense restyling of dated findings is forbidden without new evidence (out of scope for this thesis to invent).

---

## 9. Illustrative reading-unit sketch (optional — not pixels)

ASCII sketch of grammar only — not a component spec:

```
┌─ System Reading Unit ─────────────────────────────────────┐
│ [scope: function]                    [date: anchor]       │
│ OUTCOME: <categorical enum>                               │
│ [jurisdiction bounds if load-bearing]                     │
│                                                           │
│ ┌─ Layer panel ─────────────────────────────────────────┐ │
│ │ TYPE: <ActiveLayerType>                               │ │
│ │ INSTRUMENT: <mechanism statement>                     │ │
│ │ WHERE: <locus>                                        │ │
│ │ [layer date/scope/jurisdiction if present]            │ │
│ │ BOUNDARY: admissible / excluded…                      │ │
│ │ WHO: <holders…> | “not resolved at discrete-actor…” │ │
│ │ Claim–evidence rows…                                  │ │
│ └───────────────────────────────────────────────────────┘ │
│ (repeat panel for multiple_evidenced_layers)              │
│ — or Negative / Ambiguity body instead of panels —        │
│ Refusal notes (if any)…                                   │
└───────────────────────────────────────────────────────────┘
```

For `multiple_evidenced_layers`, two panels stack with equal weight. For zero-record outcomes, replace the panel region with the assessment body and an explicit zero-layer statement.

---

## 10. Pressure-case application notes (grammar only — not evaluation)

These notes show how the grammar *intends* to carry known pressures. They are **not** Step 3 results.

> **Non-operative review provenance.** These notes must **not** be consulted when generating Step 3 representations. Step 3 representation generation must use **only** the general interface grammar (§1–§8) and must **not** branch on case identity (`S1`…`S8`) or on this section. Using §10 to tailor presentation is out of process (Falsifier 14 / blind protocol).

| Pressure | Grammar application (review aid only) |
|---|---|
| S2 collective locus | WHERE = capacity set; WHO = TSMC + Samsung as holder list — holder names must not replace WHERE in the headline strip |
| S6 two layers | Two equal panels; holders absent shown explicitly; qualification refusal = Refusal note after panels |
| S3 negative | Negative body + zero layers; not blank; no invented EvidenceBinding rows |
| S7 provider boundary | WHERE = egress/switching boundary; WHO = named providers; no market-level outcome banner |
| S4/S5 jurisdiction | Bounds (including jurisdiction) in strip / layer labels before unconstrained reading; boundary before WHO in panel order |
| S8 legal exclusivity | TYPE + INSTRUMENT stay statute-bounded; excluded list blocks “USPS monopolises delivery” |
| Ambiguity (structural) | Ambiguity body only; ≥2 option lines; no layer panels; no EvidenceBinding rows |

---

## 11. Completeness checklist (Step 2 gate requirements)

| Required section | This document |
|---|---|
| Primitive → presentation role | §1 |
| Reading order / information hierarchy | §2 |
| Outcome-state rules (all four) | §3 |
| Multi-layer treatment | §4 |
| Evidence → claim relationship | §5 |
| Claim-boundary placement | §6 |
| Refusal / ambiguity treatment | §7 |
| Visual-encoding policy | §8 |

---

## 12. Artifact status

| Step | Status |
|---|---|
| 1 Gate design | DESIGN FROZEN |
| 2 This candidate interface thesis | **Draft for review** |
| 3 Readback evaluation | Blocked |
| 4 Closeout | Blocked |

**Stop point:** Review this grammar. No HTML/CSS/JS. No site change. No `GATE_MON-G3-IT_EVALUATION.md` until this thesis is accepted.
