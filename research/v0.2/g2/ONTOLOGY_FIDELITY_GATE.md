# Ontology Fidelity Gate — Monopolises v0.2

**Gate ID:** MON-G2-OF
**Version:** 0.2
**Status:** DESIGN FROZEN — modelling not started
**Opened:** 2026-08-29
**Authorized by:** `DECISION_LOG.md` DEC-005 (MON-G1-LI Closed / PASS)
**Predecessor gate:** MON-G1-LI — Closed PASS (`../LAYER_IDENTIFIABILITY_GATE.md`, `../GATE_MON-G1-LI_EVALUATION.md`)

> This gate tests whether the four ratified layers can be **represented** without loss — before any ontology becomes a production structure. It authorizes nothing on its own. A schema, classes, or a data architecture may be built **only** on a PASS. It is deliberately small and falsifiable: the ontology must carry the eight existing case records unchanged, or it fails.

## Governing question

> Can the four ratified control layers be represented as a stable ontology **without losing the evidence boundaries that made MON-G1-LI reproducible** — and without adding any inference the case records do not contain?

## Scope

- **In scope:** a representation (conceptual model / schema shape) for the eight MON-G1 case records, over the four **active** layers only.
- **Out of scope (and not authorized by this gate):** scores, severity, dominance level, ranking, monopoly probability, any quantitative or ordinal value; scaled/programmatic entity or sector pages; the public interface; monetization. Those require their own decision and gate.

## What the ontology MUST represent (fidelity requirements)

1. **Exactly the four active layers** — `legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `switching_dependency`. No fifth active layer; the three research candidates (`qualification_control`, `standard_interface_control`, `temporal_constraint`) get **no reserved slot, enum member, or placeholder class**.
2. **Strict separation of the record fields** — `System`, `Layer`, `Control Mechanism`, `Evidence`, `Locus`, `Claim Boundary` are **distinct** and independently addressable. A `Layer` may not collapse into a free-text description of the entity; the `Control Mechanism` is its own field, not folded into the layer label.
3. **Multiple layers per system** — as in S6 (`capacity_control` + `access_gatekeeping` in one system, at different loci).
4. **Collective locus** — as in S2 (a capacity set held by more than one actor), not only single-actor loci.
5. **Provider/instance-specific mechanism** — as in S7 (a mechanism instantiated at each provider's boundary), without forcing a single market-wide actor.
6. **The negative** — `no_evidenced_control_layer` must be a **first-class representable outcome**, as in S3. An ontology that cannot record "a system was examined and no layer was evidenced" re-imports the find-control-everywhere bias.
7. **Evidence linkage** — every `Layer` instance links to its `Evidence` (the admitted primary sources / register IDs) and its evidence class (S0/S1; S2 recorded as excluded, never as classifying).
8. **Date and scope mandatory; jurisdiction conditional** — every record carries a `date` and a `scope`; `jurisdiction` is required **only where jurisdiction is load-bearing** (S4/S5/S7), not forced onto a global technical locus (S1).
9. **Derivation transparency** — where the layer label is an S1 derivation rather than a verbatim source term (S1, S2, S6, S7), the record can mark it as such (S0 facts vs S1-derived label), so no S1 step is silently presented as source-native.

## What the ontology MUST NOT do (prohibitions)

- **No added inference.** The ontology may not introduce any relation, attribute, or computed value that is not present in the case's evidence record. It represents; it does not infer.
- **No masked quantities.** No score, weight, severity, confidence number, dominance tier, ranking order, or monopoly-probability — including any field that is ordinal or numeric by another name.
- **No S2 promotion.** No field may let a market-share figure alone, or an antitrust/competition conclusion, carry a classification.
- **No reserved research-candidate slots** (restates requirement 1 as a prohibition).
- **No lossy normalization.** The schema may not require dropping or merging a record's `Locus` or `Claim Boundary` to fit a shape.

## The fidelity test (PASS condition)

The test is a **round-trip**, run on the eight existing case records:

> Encode each of the eight MON-G1 case records into the candidate ontology, then re-express each record **out** of the ontology, and compare to the merged case file on main.

**PASS requires all of the following:**

1. **Round-trip completeness.** All eight records encode and re-express with **the same `Layer` + `Control Mechanism` + `Locus` + `Evidence` + `Claim Boundary`** as the merged case files — including S6's two layers, S2's collective locus, S7's provider-specific mechanism, and **S3's `no_evidenced_control_layer`**.
2. **No record was altered to fit the schema.** If any case result had to change to be representable, that is a FAIL, not a fix (see Falsifier 1). The history is fixed; the model bends to it.
3. **Field separation preserved.** `System / Layer / Control Mechanism / Evidence / Locus / Claim Boundary` remain distinct after the round trip; none is inferred from another.
4. **Boundaries preserved.** Every `Claim Boundary` (including the "not admissible" refusals) survives the round trip intact; no boundary is widened or dropped.
5. **No addition.** The re-expressed record contains **nothing** that was not in the original evidence record (no new relation, attribute, or value).

## Falsifier

The gate FAILS if any of these hold:

1. **A case result must be changed** (layer, mechanism, locus, evidence, or boundary) to fit the schema — the schema is dictating the finding.
2. **The negative cannot be represented** — `no_evidenced_control_layer` (S3) has no first-class encoding, or is forced into a degenerate "empty layer."
3. **Fields collapse** — `Layer` and `Control Mechanism`, or `Locus` and `System`, cannot be kept distinct; or the model needs a free-text "entity description" standing in for a layer.
4. **The model adds inference or a masked quantity** — any relation/attribute/value not in the evidence record, or any score/severity/ranking/probability by any name.
5. **A research-candidate layer requires a slot** — the schema cannot be expressed without reserving space for `qualification_control` / `standard_interface_control` / `temporal_constraint`.
6. **Multiplicity fails** — the model cannot hold multiple layers per system (S6), a collective locus (S2), or a provider-specific mechanism (S7) without distortion.

## Pass/Fail discipline

- The gate closes on the **round-trip performance over the fixed eight records**, not on the elegance of the schema.
- No rescue: if the model fails a case, we do not edit the case to pass; we record FAIL and redesign or narrow the model.
- A PASS authorizes, in order, a layer ontology spec then (under DEC-005) the interface thesis and data architecture — still no scores/rankings/monetization.
- A FAIL is recorded honestly, like Gate 0; the ontology work stops until a new design is gated.

## Fixed reference set (the eight records the model must carry)

Frozen before modelling — these are the exact results the round-trip is checked against:

| Case | System / scope | Layer(s) | Locus | Note the model must preserve |
|---|---|---|---|---|
| MON-G1-S8 | US Private Express Statutes | `legal_exclusivity` | letters over post routes | single-actor statutory right |
| MON-G1-S1 | EUV lithography | `capacity_control` | EUV scanner production | single-actor; **global locus, no jurisdiction field** |
| MON-G1-S2 | Leading-edge foundry (2021) | `capacity_control` | 5 nm HVM capacity set | **collective locus** (two actors); dated 2021 |
| MON-G1-S6 | NdFeB magnets | `capacity_control` **+** `access_gatekeeping` | China value chain; US defense procurement | **two layers, one system, two loci** |
| MON-G1-S4 | Native iOS app distribution (US) | `access_gatekeeping` | general-public App Store channel | jurisdiction load-bearing; dated |
| MON-G1-S5 | Card-payment acceptance (Visa, US) | `access_gatekeeping` | Visa-network admission | dated to 18 Apr 2026 rules |
| MON-G1-S3 | Accelerated computing (CUDA) | **`no_evidenced_control_layer`** | — | **the negative must be representable** |
| MON-G1-S7 | Cloud hyperscaler (UK) | `switching_dependency` | provider egress boundary | **provider-specific mechanism**; dated 2025 |

## Next step

This is the frozen gate document only. **Do not** build a schema or classes yet. After review of these PASS/FALSIFIER criteria and the fixed reference set, the next artifact is a candidate ontology model, tested by the round-trip above — then a verdict.
