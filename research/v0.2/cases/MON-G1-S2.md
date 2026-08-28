# MON-G1-S2 — Leading-edge foundry fabrication (the moving-frontier test)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S2
**Role in set:** The real stress test. This is where the moving frontier — the defect that sank part of v0.1 — could pull us back into an analyst-defined monopoly claim.
**Status:** Evidence extraction complete — provisional case result (revised after review)
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `capacity_control` at high-volume manufacturing (HVM) of the leading logic node
**Extraction order position:** 3 of 8

## 0. Governing extraction question

> Can a capacity-control layer be identified at a **specifically dated** leading-edge logic node from primary evidence, **without turning moving-frontier leadership into an analyst-defined monopoly claim**?

## 0.1 Correction notice (this revision)

The first version of this case introduced a rule the gate never contained — "two producers ⇒ not single-source ⇒ no `capacity_control`" — and reached `no_evidenced_control_layer` from it. That imported the **single-source** condition from the EUV case (S1). **The frozen gate has no single-company requirement.** The frozen definition is:

> `capacity_control` — a documented facility, node, or capacity **that the function must pass through and that is hard to bypass**.

and the v0.2 unit is `System × Layer × Control Mechanism × Evidence`, which asks *where control is concentrated*, not whether one actor owns it. This revision deletes the single-source rule and re-applies the frozen definition literally. A layer may be held by a **small set** of actors (an oligopolistic chokepoint); reducing "monopolised" to "one company" would undo the whole reason for moving to layered monopolisation.

## 1. The moving-frontier discipline — four separated truths

| # | Truth | What it asks | Status here |
|---|---|---|---|
| 1 | **node capability** | Who can *actually fabricate* a specific node? | S0 — dated 2021 |
| 2 | **HVM status** | *High-volume* production, or announced/ramping/pilot? | S0 — dated 2021 |
| 3 | **capacity locus** | Where is the *measurable* capacity, and must the function pass through it? | S0/S1 |
| 4 | **frontier date** | What counted as "leading-edge" *on the date of the evidence*? | S0 — fixed at 2021 = 5 nm |

Cardinal rule (unchanged): `capacity_control` may not be inferred from market share or technological leadership **alone**. But a documented capacity the function must pass through and cannot presently route around **is** the definition — whether that capacity sits in one producer or a small set.

## 2. The frozen definition, applied literally — three elements

`capacity_control` requires three things, each testable from S0/S1:

1. **a documented facility / node / capacity** — S0?
2. **the function must pass through it** — S0?
3. **hard to bypass** — S0/S1, or does it need S2?

The classification stands only if all three are met without S2.

## 3. S0 evidence (all from the same primary document, dated 2021)

**Source throughout:** The White House / Department of Commerce, *Building Resilient Supply Chains … 100-Day Reviews under Executive Order 14017*, June 2021.

### E01 — Dated frontier + the HVM capacity set (elements 1 & 2)
p. 39, verbatim: "The United States lacks semiconductor production capability at the most advanced semiconductor process node—currently 5 nm—at which **only TSMC (Taiwan) and Samsung (South Korea) currently operate**."
**Class:** S0. Fixes frontier = 5 nm (2021) and that leading-edge production operates at the TSMC+Samsung capacity set.

### E02 — HVM status confirmed (element 2)
p. 64, verbatim: "Samsung is one of **only two companies that are producing volume** in the leading edge 7 nm and 5 nm chips."
**Class:** S0. Confirms *high-volume* (not pilot/announced) at the two-producer set.

### E03 — Hard to bypass: the largest non-participant economy lacks the capability (element 3)
p. 39, verbatim: "The most advanced fabs in the United States are **10 nm** operated by Intel, which does not expect to enter full 7 nm production until 2023 …"; and "U.S. fabless chip companies now rely **almost exclusively** on Asian producers (especially TSMC) for production of the most advanced (7 nm or less) chips."
**Class:** S0. The U.S. — a major economy with strong domestic firms — cannot presently route leading-edge logic around this capacity set.

### E04 — Hard to bypass: the nearest alternative foundry is two nodes behind (element 3)
p. 40, verbatim: China's "most advanced pure-play foundry, Semiconductor Manufacturing International Corporation (SMIC), **can only produce at the 14 nm node, with limited capacity**."
**Class:** S0. No third HVM producer exists at the frontier; the nearest alternative is ~two nodes back with limited capacity.

## 4. Three-element test — result

| Element | Met? | Basis |
|---|---|---|
| Documented facility/node/capacity | **Yes — S0** | "most advanced … 5 nm" node; the operating capacity of TSMC and Samsung (E01, E02) |
| Function must pass through it | **Yes — S0** | leading-edge logic HVM operates *only* at this set; US fabless "rely almost exclusively" on it (E01, E03) |
| Hard to bypass | **Yes — S1 from S0 facts** | only two HVM producers exist (E01/E02); the US lacks the capability (E03); the nearest alternative foundry is stuck at 14 nm (E04) — so there is **no present alternative route**. This is a mechanical reading of absence-of-alternative facts, not a viability judgment. |

All three elements are met from S0/S1.

## 5. Classification (provisional, revised)

```
result = evidenced_control_layer
layer  = capacity_control
locus  = COLLECTIVE — dated 2021 leading-edge (5 nm) HVM logic capacity
```

### Control mechanism
> Leading-edge logic HVM at the 2021 frontier (5 nm) is a documented productive capacity through which that function must pass, concentrated in the **only two source-evidenced HVM producers (TSMC and Samsung)**, and presently hard to bypass — the largest non-participant economy (the U.S.) lacks the capability and the nearest alternative foundry (SMIC) is two nodes behind.

The layer is **not** `TSMC → capacity_control`. It is:

> Leading-edge HVM → `capacity_control` → **TSMC/Samsung capacity set** (TSMC the dominant share within the set).

**Classification derivation:** the underlying facts are S0; the three-element conjunction that yields the `capacity_control` label is an **S1 mechanical derivation** (as in S1/EUV, the label is not written verbatim in the source). No S2 is used.

## 6. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Frontier 2021 = 5 nm | "most advanced … currently 5 nm" (p.39) | — | — |
| HVM operates only at TSMC+Samsung | "only … currently operate" (p.39); "only two companies … producing volume" (p.64) | function passes through this set | which of the two "controls" more |
| No present alternative route | US most-advanced fab 10 nm (p.39); SMIC 14 nm (p.40) | ⇒ **hard to bypass** now | whether it *will remain* hard to bypass; new-entrant viability |
| ⇒ capacity_control at collective locus | conjunction of the above | **S1:** three elements met ⇒ `evidenced_control_layer` | coordinated conduct; that the set is a "monopoly" |
| TSMC is dominant within the set | "especially TSMC" (p.39) | dominance sits *inside* the layer; it does not *define* it | "TSMC monopolises advanced chips" |

## 7. Why this is not "any oligopoly = control"

The result does **not** say every small-number market is a control layer. It clears the bar only because the source supplies **absence-of-alternative** evidence for element 3: the U.S. lacks the capability (E03) and the nearest alternative is two nodes behind (E04). An oligopoly *without* such source-native no-alternative evidence would fail "hard to bypass" and land in `ambiguous_layer` or `no_evidenced_control_layer`. This is the principle for every future oligopolistic chokepoint: concentration in a small set is a layer **only when the function's inability to route around that set is itself source-evidenced**, never assumed from headcount or share.

## 8. Why not the other outcomes

- **Why not `no_evidenced_control_layer` (the earlier answer):** that answer depended entirely on the deleted single-source rule. Under the frozen definition, the three elements are met.
- **Why not `ambiguous_layer` (the conservative fallback):** ambiguity would apply if "hard to bypass" needed S2 — i.e. if establishing no-alternative required judging viability/equivalence. Here it does not: the source *states* the U.S. lacks the capability and SMIC is at 14 nm. If a reviewer judges that "hard to bypass" still imports a viability judgment, the correct fallback is `ambiguous_layer`, **not** `no_evidenced`. This case is logged as `evidenced_control_layer`; the S1/S2 line for element 3 is the single point a reviewer should check.

## 9. Claim boundary

### Admissible record (dated)
> At the **2021** leading-edge frontier (5 nm), a `capacity_control` layer sits at leading-edge logic HVM capacity, held collectively by the only two source-evidenced HVM producers (TSMC and Samsung, TSMC dominant), through which leading-edge logic production must pass and which was presently hard to bypass (the U.S. lacked the capability; SMIC was two nodes behind).

### Not admissible
- ❌ "TSMC monopolises advanced chips." — the layer is a **two-producer** set; TSMC's dominance is *within* the layer, not the layer itself.
- ❌ Attributing the whole layer to any single actor.
- ❌ Any **undated** "leading-edge" claim — the frontier moves.
- ❌ Any claim of **permanence** — whether it stays hard to bypass is S2.
- ❌ Using 2025–26 information in the classification (see §10).

## 10. Freshness note (2025–26) — NOT part of the classification

The admitted evidence is dated 2021. The classification above is therefore a **2021-dated finding**, not a present-tense claim. Present reporting (trade press, **not S0**) indicates the present frontier is the 2 nm class, entered by three producers (TSMC N2, Samsung SF2, Intel 18A). This is recorded only to flag freshness; it plays **no** role in the result and is **not** in the admissible record. Direction of travel: a small (2→3) producer set persists, so the collective-locus reading is not contradicted — but a **current primary source** (government assessment or company/regulatory filing) must be admitted before this finding is restated in the present tense. Recorded as a limitation, exactly as the second-source limitation in S1.

## 11. Result and next step

- **Case result:** `evidenced_control_layer` / `capacity_control` at a **collective** locus — dated 2021 leading-edge (5 nm) HVM logic capacity (TSMC + Samsung), from S0 facts via an S1 derivation, no S2 used.
- **Dated scope / limitation:** 2021 finding; present-tense restatement requires a current primary source (not yet admitted).
- Stop at S2 for review before extracting MON-G1-S6 (rare-earth magnets), per the frozen order. Do not batch.

## 12. Running gate picture (three of eight)

- S8 → `evidenced_control_layer` / `legal_exclusivity` (single-actor, by statute)
- S1 → `evidenced_control_layer` / `capacity_control` (single-actor locus: EUV scanner production)
- S2 → `evidenced_control_layer` / `capacity_control` (**collective** locus: 2021 leading-edge HVM, two producers)

S1 and S2 are the same layer reached two ways — a single-actor capacity chokepoint and a small-set capacity chokepoint. That the framework accommodates both, without collapsing "concentrated" into "one company," is the structural point this review surfaced. Still three cases; the gate verdict waits on the full fixed set, and S2's "hard to bypass" S1/S2 line is the item most worth a second reviewer's eye.
