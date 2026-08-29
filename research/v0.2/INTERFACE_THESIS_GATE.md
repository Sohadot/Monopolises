# Interface Thesis Gate — Monopolises v0.2

**Gate ID:** MON-G3-IT
**Version:** 0.2
**Status:** **Open — draft for review** (not frozen; revision 2 pending acceptance; Step 1 — gate specification only)
**Opened:** 2026-08-29
**Closed:** —
**Thesis under test:** Layered Monopolisation v0.2 (`THESIS_CANDIDATE.md`, DEC-005) via adopted ontology `mon-g2-of-candidate-v0.2` (DEC-006)
**Evaluation:** `GATE_MON-G3-IT_EVALUATION.md` (not yet created)
**Decision:** pending gate close
**Predecessor gate:** MON-G2-OF — Closed PASS (`ONTOLOGY_FIDELITY_GATE.md`, DEC-006)
**Adopted ontology:** `research/v0.2/ontology/CANDIDATE_ONTOLOGY_SCHEMA.md` (`schema_version`: `mon-g2-of-candidate-v0.2`)

> This gate tests whether the **adopted Layered Monopolisation ontology** can be translated into an **interface thesis** that makes bounded control legible without semantic distortion. It is deliberately small and fail-fast. **Step 1 is this gate specification only.** No candidate interface thesis, mockups, HTML/CSS/JS, site changes, component system, or data architecture may proceed until this gate design is reviewed and frozen.

## Governing question

> Can the adopted Layered Monopolisation ontology be translated into an interface thesis that makes bounded control legible — System, evidenced Layer, Control Mechanism, Locus, Holder(s), Evidence, and Claim Boundary — **without implying legal monopoly status, ranking, dominance, or evidence beyond the record?**

Note what the question is not: it is not "can we design a beautiful interface," not "can we ship a product UI," and not "can we make monopolies more dramatic." It is a question about whether a **visual/readback thesis** can carry the same discriminations the ontology already proved — without making overclaim easier than underclaim.

### Governing principle

> **The interface must make the ontology easier to read, never easier to overclaim.**

This principle guides design. It is **not** itself a PASS condition. Falsifiable salience is stated as PASS-9 (Boundary salience) below.

## Provenance — what this gate does *not* inherit as binding

| Source | Role for MON-G3-IT |
|---|---|
| DEC-005 | Binding thesis + four-layer taxonomy |
| DEC-006 | Binding ontology adoption; authorizes this successor gate only |
| `mon-g2-of-candidate-v0.2` | Binding structural primitives under test for interface translation |
| `INTERFACE_THESIS.md` (repo root, v0.1) | **Archived provenance only** — written for Strategic Replaceability / MON-G0-RH (FAIL). **Not** the starting point for this gate. Candidate interface thesis must be derived from DEC-005 + DEC-006 + adopted ontology, not from that archived document. |

## What this gate tests — and what it does not

This gate tests **semantic interface fidelity**: whether a candidate interface thesis can present ontology records so that a disciplined reader recovers the bounded claim — not aesthetic preference, not production readiness.

| In scope | Out of scope |
|---|---|
| Interface thesis that maps ontology primitives to readable surfaces | Production UI, site rewrite, component library |
| Semantic/readback evaluation on the eight frozen cases | Re-classification of MON-G1-LI cases |
| Visual encoding rules that preserve categorical (non-ordinal) meaning | Scores, rankings, dominance meters, monopoly probability |
| Negative and ambiguity outcomes as first-class readable states | Data architecture, APIs, persistence |
| Structural representability of `ambiguous_layer` (conformance check, not a ninth case) | Adding a ninth rescue case |
| | Mockups used as substitute for a frozen thesis (illustrative wires optional in Step 2 only after DESIGN FROZEN) |

## Ontology binding (frozen input)

The interface thesis under test **must** bind to these adopted primitives. It may not invent parallel concepts that collapse them.

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
Research candidates appear only as assessment references — never as visible “possible layers.”

## Frozen interface design rules

These rules freeze **meaning**, not pixels. A later candidate thesis must satisfy them; pixel choices are free only within these constraints.

| Dimension | Frozen rule |
|---|---|
| **Primary unit** | `SystemRecord` is the unit of reading. **Company/entity is not the primary object.** Holders may appear, but the page/module centers the system + evidenced layer record(s). |
| **Layer** | An evidenced layer is an independent categorical type — **not** a severity grade, intensity, or “how monopolistic.” |
| **Mechanism** | Must be visible as the **instrument/cause of control**, not merely a restatement of the layer label. |
| **Locus** | Answers **where** control sits. Must remain separable from Holder in layout and copy. |
| **Holder** | Answers **who occupies the locus**. Supports **0..n**. Must not invent an actor when holders are absent. |
| **Evidence** | Each binding stays attached to the **claim** it supports. No orphan “evidence bag” detached from claims. |
| **Claim Boundary** | Part of the record’s meaning — admissible + excluded must be readable with the record, **not** buried as a footer disclaimer. |
| **Date / Scope / Jurisdiction** | Must be legible **before** a reader can treat the record as a timeless/global claim. Jurisdiction appears only when load-bearing. |
| **Multiple layers** | Independent records. No primary/secondary hierarchy, merge card, or ranking among layers on one system. |
| **Negative outcome** | `no_evidenced_control_layer` is a **complete cognitive result** — not blank, error, spinner, or “data unavailable.” |
| **Ambiguity** | Zero evidenced layers + ambiguity assessment. Competing interpretations stay assessment content — **no ghost or provisional layer chrome.** |
| **Refusals** | Assessment context only. Must not render as faded layers, “candidate layers,” or near-miss chips that look classifiable. |
| **Visual encoding** | Categorical / non-ordinal. Color, size, weight, or motion must **not** encode dominance, severity, score, or rank. |
| **Evidence certainty** | The interface must not appear more precise or certain than the sources allow (no fake live meters, no over-resolved maps). |

## Step 2 artifact requirements (frozen — testable interface grammar)

A candidate interface thesis (Step 2) is **incomplete** — and Step 3 must not begin — unless it specifies **all** of the following as an explicit, testable **interface grammar**. Prose aspiration without these mappings fails Step 2 completeness. Pixels and components are **not** required. Illustrative wires are **optional**.

| Required section | What it must define |
|---|---|
| **Primitive → presentation role** | For each ontology primitive (`SystemRecord`, `Outcome`, `EvidencedLayerRecord`, `ActiveLayerType`, `ControlMechanism`, `Locus`, `Holder`, `EvidenceBinding`, `ClaimBoundary`, assessments, metadata): the presentation role it occupies in the reading unit (what the reader is meant to take it as). |
| **Reading order / information hierarchy** | The order in which a reader encounters system identity, outcome, bounds (date/scope/jurisdiction), layer record(s), mechanism, locus, holders, evidence–claim pairs, and claim boundary — sufficient to test hierarchy/falsifier claims. |
| **Outcome-state rules (all four)** | Distinct presentation rules for `evidenced_control_layer`, `multiple_evidenced_layers`, `ambiguous_layer`, and `no_evidenced_control_layer`. |
| **Multi-layer treatment** | How ≥2 evidenced layer records on one system remain independent (no merge, rank, or primary/secondary). |
| **Evidence → claim relationship** | How each evidence binding stays attached to its claim in presentation (no detached evidence bag). |
| **Claim-boundary placement** | Where admissible + excluded appear relative to the record (must be co-present with the reading unit, not footer-only). |
| **Refusal / ambiguity treatment** | How refusal references and ambiguity assessments render as assessment context only — never as layer types or ghost layers. |
| **Visual-encoding policy** | Explicit non-ordinal policy: which visual variables are allowed, and that color/size/weight/motion do **not** encode dominance, severity, score, or rank. |

Without this grammar, ordinal-encoding and hierarchy falsifiers cannot be tested; a vague thesis that “feels readable” is out of process.

## Fixed evaluation set

The **same eight MON-G1-LI systems**, in the same audit order. No swap, no drop, no ninth rescue case. Cases are **not** re-classified; they are readback fixtures for the interface thesis.

| Order | Case | Interface pressure |
|---|---|---|
| 1 | S8 | `legal_exclusivity` must not inflate to “USPS monopoly” over all delivery |
| 2 | S1 | Single-holder capacity; tool locus ≠ “monopolises semiconductors” |
| 3 | S2 | Collective locus; must not collapse visually to “TSMC monopolises” |
| 4 | S6 | Two independent layers; no hierarchy; holders absent (`[]`) |
| 5 | S4 | US / general-public / 2026 bounds must block global App Store overclaim |
| 6 | S5 | Per-network Visa admission; refused `standard_interface_control` stays assessment-only |
| 7 | S3 | Negative outcome must read as a full result, not empty UI |
| 8 | S7 | Provider-specific egress boundary; must not lift to market-level cloud control |

### `ambiguous_layer` — structural conformance only (not a ninth case)

There is **no** live `ambiguous_layer` instance in the fixed eight. Step 3 therefore runs a **structural conformance check only** for this outcome — **outside** the 8/8 readback denominator:

| Required | Forbidden |
|---|---|
| Interface grammar defines presentation for `outcome = ambiguous_layer` | Treating the check as a ninth evaluation case |
| Representation shows `evidenced_layer_records = []` | Promoting competing interpretations to evidenced layer records |
| Populated ambiguity assessment is readable as first-class | Ghost / provisional / faded “possible layer” chrome |
| ≥2 competing interpretations visible as assessment content | Counting this check toward 8/8 readback PASS/FAIL |

This check may PASS or FAIL independently; it does **not** enter the eight-case readback tally.

## Evaluation method (Step 3 — frozen now, executed later)

After a complete Step 2 candidate interface thesis exists, evaluation has two parts:

### A. Eight-case semantic readback (denominator = 8)

1. Present each of the eight records through the candidate interface thesis (static description / optional illustrative wire sufficient; production code not required).
2. A reader or scripted extractor recovers normalized fields from **that representation alone**.
3. After readback, map case identity → ground truth for comparison only.
4. Case verdict = PASS/FAIL on loss / inflation / semantic distortion / tautology — **no aesthetic score.**

### Blind readback protocol (anti-tautology — mandatory)

Inherited discipline from MON-G2-OF, applied to interface readback:

| Rule | Requirement |
|---|---|
| **No case ID at readback** | The reader/extractor must not see `MON-G1-S1`…`S8` or equivalent case identity while recovering fields. |
| **No ground truth at readback** | Must not see MON-G1 original case files, locked ground-truth JSON, or `expected_outcome` / `expected_layer` / equivalent stored answers. |
| **Representation only** | Input to readback is solely the presentation produced by applying the candidate interface thesis to the record. |
| **Uniform extraction rules** | The same display/extraction rules apply to all eight cases; **no branching on case identity** (`S1`…`S8`). |
| **Case identity after readback only** | Used only to select ground truth for comparison — never to produce the extracted fields. |

If evaluation is scripted, the same anti-tautology controls apply (static scan / no case-keyed recovery paths), making **Falsifier 15** enforceable rather than aspirational.

### B. `ambiguous_layer` structural conformance (outside 8/8)

Verify the Step 2 grammar + a non-case illustration or schema-level presentation rule for ambiguity against the structural table above. Not counted in the eight-case denominator.

**Reader-failure falsifier (decisive for evidenced cases):**

> **If a reader can correctly name the company but cannot correctly state the bounded locus and mechanism, the interface thesis has failed.**

That outcome means the thesis built an **entity interface in disguise**, not a Layered Monopolisation interface.

## Pass condition

The gate PASSES only if **all** hold:

1. **Readback fidelity.** All eight cases read back without loss, inflation, or semantic distortion of outcome, layer, mechanism, locus, holders, evidence bindings, claim boundary, and load-bearing metadata.
2. **Primary-unit discipline.** `SystemRecord` remains the primary reading unit; company/entity is never the primary object.
3. **Primitive separation in presentation.** Mechanism ≠ layer label; Locus ≠ Holder; Evidence stays claim-bound; Claim Boundary is co-present with the record.
4. **Multiple-layer independence.** S6’s two layers remain separately legible without merge or rank.
5. **Negative semantics.** `no_evidenced_control_layer` is a complete readable state — not blank, error, or “data unavailable.”
6. **Ambiguity structural conformance.** The structural check for `ambiguous_layer` PASSes (outside 8/8): empty layer array + ambiguity assessment + ≥2 competing interpretations + no visual promotion to layer records.
7. **Refusal hygiene.** Refused/research candidates appear only as assessment context — never as visual layer types.
8. **Non-ordinal encoding.** No score, intensity, rank, dominance, or monopoly-probability encoding — explicit or via color/size/motion.
9. **Boundary salience.** A reader must recover the bounded scope/date/jurisdiction and the admissible-vs-excluded claim boundary from the **same reading unit**, before or alongside any holder/entity interpretation; no surface may present an unbounded holder/company headline as the record’s primary takeaway.
10. **Blind protocol.** Step 3 readback obeyed the anti-tautology protocol; no case-id branching or stored-answer escape hatch.

## Falsifier

The gate FAILS if **any** of the following hold:

1. **Company-as-primary-object.** The interface thesis makes company/entity the primary unit of reading.
2. **Ordinal monopoly encoding.** Any score, intensity, rank, severity, dominance level, monopoly probability — or visual proxy (color scale, bar length, glow, size) that functions as one.
3. **Mechanism or boundary hidden.** Mechanism or claim boundary is suppressed in favor of a headline, brand, or “control summary.”
4. **Locus/Holder collapse.** Where and who are merged so a reader cannot separate them (e.g. S2 reads as “TSMC = the locus”).
5. **Invented holder.** A record with absent holders is forced to display an actor.
6. **Multiple-layer merge.** S6 (or any multi-layer system) is collapsed into a single ranked or merged “control summary.”
7. **Negative as absence.** S3 (or any `no_evidenced_control_layer`) is presented as blank, error, loading failure, or “data unavailable.”
8. **Ghost layers.** Ambiguity or refusals render as provisional/faded/possible layer chips that look classifiable.
9. **Research candidates as visible layers.** `qualification_control`, `standard_interface_control`, or `temporal_constraint` appear as layer types in the UI thesis.
10. **Unsupported spatial rhetoric.** Graph, map, network, or “connection” visuals that the ontology/evidence do not support.
11. **Hierarchy implies wider claim.** Visual hierarchy invites a claim broader than the admissible record (e.g. S7 → “cloud is monopolised”; S8 → “USPS monopolises delivery”; S4 → global iOS monopoly).
12. **Reader-failure test.** A reader can name the company but cannot correctly state bounded locus and mechanism.
13. **History changed to fit UI.** Any MON-G1 classification is altered, softened, or relabeled to make the interface work.
14. **Case-specific UI tailoring.** Layout or component exceptions keyed to case identity (`S1`…`S8`) rather than general ontology states.
15. **Tautological readback.** Evaluation “succeeds” only via stored expected labels, case-id branching, ground-truth leakage into the readback input, or free-text escape hatches that bypass structural readback. **If extraction/readback must know which case it is handling to succeed → FAIL.**
16. **Incomplete Step 2 grammar.** Candidate interface thesis lacks any required Step 2 section (primitive mapping, reading order, four outcome rules, multi-layer treatment, evidence→claim, claim-boundary placement, refusal/ambiguity treatment, or visual-encoding policy).
17. **Boundary salience failure.** Scope/date/jurisdiction or admissible-vs-excluded boundary cannot be recovered from the same reading unit before/alongside holder interpretation; or an unbounded company/holder headline is the primary takeaway.
18. **Ambiguity conformance failure.** Structural check for `ambiguous_layer` fails (missing empty array semantics, missing assessment, fewer than 2 competing interpretations, or visual promotion to layer records).

## Freeze rules

1. This gate **design** freezes only upon review acceptance (`DESIGN FROZEN`). Until then it is draft for review.
2. The eight MON-G1 cases are the only readback evaluation set. No ninth case. No re-classification. `ambiguous_layer` is structural conformance only.
3. Candidate interface thesis (Step 2) must derive from DEC-005 + DEC-006 + adopted ontology — not from archived `INTERFACE_THESIS.md` as binding input — and must satisfy the Step 2 artifact requirements above.
4. No production interface, component system, site change, or data architecture until this gate closes PASS (and even then, PASS authorizes only adoption of the interface thesis and opening a **data-architecture gate** — not implementation).
5. Evaluation (`GATE_MON-G3-IT_EVALUATION.md`) is the sole closeout evidence artifact for this gate. No separate beauty-score report.
6. A FAIL returns to revise the interface thesis (or abandon it). It does not reopen MON-G2-OF or MON-G1-LI.

## Artifact sequence (strict)

| Step | Artifact | Status |
|---|---|---|
| 1 | This gate spec (`INTERFACE_THESIS_GATE.md`) | **Current — draft for review (revision 2)** |
| 2 | Candidate interface thesis meeting **Step 2 artifact requirements** (optional illustrative wires only) | Blocked until Step 1 **DESIGN FROZEN** |
| 3 | Semantic/readback evaluation on S8…S7 + `ambiguous_layer` structural conformance (`GATE_MON-G3-IT_EVALUATION.md`) | Blocked until Step 2 exists and is complete |
| 4 | Gate closeout decision | Blocked until Step 3 complete |

**Do not skip steps.** A UI build before this gate freezes is out of process. A Step 2 document without the required interface grammar is incomplete.

## What a PASS authorizes — and only then

A PASS authorizes:

- **Adoption of the tested interface thesis** as the interface posture conforming to DEC-005 / DEC-006.
- **Opening the successor falsifiable gate for data architecture** (next in the DEC-005 sequence).

A PASS does **not** authorize:

- Interface **implementation**, production pages, or component libraries
- Site redesign or “shipping the UI”
- Data architecture before its own gate
- Scores, rankings, entity pages, new layers, monetization

DEC-005 build order remains: **ontology → interface thesis → data architecture**. MON-G3-IT completes the interface-thesis step only when Closed PASS.

## Relationship to prior gates

| Gate | Question |
|---|---|
| MON-G1-LI | Can control layers be identified reproducibly from primary evidence? → **PASS** |
| MON-G2-OF | Can those identifications survive formal ontology without distortion? → **PASS** |
| MON-G3-IT | Can that ontology be translated into an interface thesis that stays legible **without making overclaim easier?** → **under test** |

MON-G3-IT does not re-test identifiability or ontology fidelity. It tests whether the **surface** preserves what the **container** and **instrument** already proved.
