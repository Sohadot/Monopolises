# Interface Thesis Gate — Monopolises v0.2

**Gate ID:** MON-G3-IT
**Version:** 0.2
**Status:** **Open — draft for review** (not frozen; Step 1 — gate specification only)
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
| Structural representability of `ambiguous_layer` | Adding a ninth rescue case |
| | Mockups used as substitute for a frozen thesis (mockups only after Step 1 freeze, and only as thesis illustrations in Step 2 if needed) |

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

**`ambiguous_layer`:** no live instance in the fixed set. The gate requires **structural representability** in the interface thesis (zero layers + ambiguity assessment readable as first-class). No artificial ninth case.

## Evaluation method (Step 3 — frozen now, executed later)

After a candidate interface thesis exists (Step 2), evaluation is a **semantic readback**, not a beauty contest:

1. Present each of the eight records through the candidate interface thesis (static description / wire specification sufficient; production code not required).
2. An independent reader (or scripted readback checklist) recovers normalized fields: outcome, layer type(s), mechanism, locus, holders, evidence–claim bindings, claim boundary, date/scope/jurisdiction, assessments/refusals.
3. Compare recovered meaning to MON-G1 / ontology ground truth (full-content discipline inherited from MON-G2-OF).
4. Score only PASS/FAIL per case on loss / inflation / semantic distortion / tautology of presentation — **no aesthetic score.**

**Reader-failure falsifier (decisive):**

> **If a reader can correctly name the company but cannot correctly state the bounded locus and mechanism, the interface thesis has failed.**

That outcome means the thesis built an **entity interface in disguise**, not a Layered Monopolisation interface.

## Pass condition

The gate PASSES only if **all** hold:

1. **Readback fidelity.** All eight cases read back without loss, inflation, or semantic distortion of outcome, layer, mechanism, locus, holders, evidence bindings, claim boundary, and load-bearing metadata.
2. **Primary-unit discipline.** `SystemRecord` remains the primary reading unit; company/entity is never the primary object.
3. **Primitive separation in presentation.** Mechanism ≠ layer label; Locus ≠ Holder; Evidence stays claim-bound; Claim Boundary is co-present with the record.
4. **Multiple-layer independence.** S6’s two layers remain separately legible without merge or rank.
5. **Negative / ambiguity semantics.** `no_evidenced_control_layer` and (structurally) `ambiguous_layer` are complete readable states — not blanks, errors, or provisional layers.
6. **Refusal hygiene.** Refused/research candidates appear only as assessment context — never as visual layer types.
7. **Non-ordinal encoding.** No score, intensity, rank, dominance, or monopoly-probability encoding — explicit or via color/size/motion.
8. **No overclaim affordance.** Date/scope/jurisdiction and claim boundaries prevent treating a bounded record as a general monopoly claim.
9. **Governing principle.** The thesis demonstrably makes underclaim/boundary easier to see than overclaim.

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
13. **History changed to fit UI.** Any MON-G1 classification is altered softed, or relabeled to make the interface work.
14. **Case-specific UI tailoring.** Layout or component exceptions keyed to case identity (`S1`…`S8`) rather than general ontology states.
15. **Tautological readback.** Evaluation “succeeds” only via stored expected labels, case-id branching, or free-text escape hatches that bypass structural readback.

## Freeze rules

1. This gate **design** freezes only upon review acceptance (`DESIGN FROZEN`). Until then it is draft for review.
2. The eight MON-G1 cases are the only evaluation set. No ninth case. No re-classification.
3. Candidate interface thesis (Step 2) must derive from DEC-005 + DEC-006 + adopted ontology — not from archived `INTERFACE_THESIS.md` as binding input.
4. No production interface, component system, site change, or data architecture until this gate closes PASS (and even then, PASS authorizes only adoption of the interface thesis and opening a **data-architecture gate** — not implementation).
5. Evaluation (`GATE_MON-G3-IT_EVALUATION.md`) is the sole closeout evidence artifact for this gate. No separate beauty-score report.
6. A FAIL returns to revise the interface thesis (or abandon it). It does not reopen MON-G2-OF or MON-G1-LI.

## Artifact sequence (strict)

| Step | Artifact | Status |
|---|---|---|
| 1 | This gate spec (`INTERFACE_THESIS_GATE.md`) | **Current — draft for review** |
| 2 | Candidate interface thesis (document mapping ontology → readable surfaces; optional illustrative wires only) | Blocked until Step 1 **DESIGN FROZEN** |
| 3 | Semantic/readback evaluation on S8…S7 (`GATE_MON-G3-IT_EVALUATION.md`) | Blocked until Step 2 exists |
| 4 | Gate closeout decision | Blocked until Step 3 complete |

**Do not skip steps.** A UI build before this gate freezes is out of process.

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
