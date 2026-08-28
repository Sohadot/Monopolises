# Thesis Candidate — Monopolises v0.2: Layered Monopolisation

**Version:** 0.2 (candidate)
**Status:** UNRATIFIED — working hypothesis under test
**Opened:** 2026-08-28
**Predecessor:** Strategic Replaceability v0.1 — rejected as primary measurement thesis (see `../GATE_0_CLOSEOUT.md` and `DECISION_LOG.md` DEC-004)
**Governing gate:** `LAYER_IDENTIFIABILITY_GATE.md`

> This is a candidate thesis. It is not ratified, not a public claim, and not authorized for the site, an ontology, a score, or any scaled surface. It becomes a build thesis only if its gate passes and a new decision (DEC-005) is recorded.

## Candidate thesis

> Markets are rarely monopolised all at once. They are monopolised layer by layer.
>
> Monopolises investigates **where** control concentrates inside complex systems, **through which mechanism**, and **with what evidence**.

Here "monopolised" is a **structural description of a category** — where control concentrates inside a system — **not** a legal finding that any named entity is a monopoly.

## What changed from v0.1

v0.1 asked a single quantitative question — *how long does replacement take?* — and made the unit `Company → Replacement Horizon`. Gate 0 closed FAIL: the horizon could not be evidenced reproducibly from public primary sources without S2 interpretive judgment.

v0.2 does not ask "how long." It asks **where and by what mechanism** control sits, and it treats the answer as a **classification** to be checked for reproducibility, not a number to be computed. Replacement Horizon is demoted: it may reappear only as one possible signal inside a single layer (`temporal_constraint`), never as the core of the project.

## Unit of record

```
System × Layer × Control Mechanism × Evidence
```

Explicitly **not** `Company × Monopoly Score`.

A record names a **system** (e.g. leading-edge lithography), the **layer** at which control concentrates, the **mechanism** that produces the control, and the **primary evidence** for it. A system may carry more than one layered record, one record, or — a valid and important outcome — none.

## Boundaries

1. **No legal judgment.** Monopolises never asserts that a named entity is a monopoly, holds monopoly power, or has violated any law. It describes structural loci of control.
2. **No monopoly score.** No numeric power score, index, or ranking of entities.
3. **No inference from market share alone.** A concentration statistic is not, by itself, an evidenced control layer. The mechanism and its primary evidence must be identified.
4. **Locus + mechanism + evidence, always.** Every claim must state *where inside the system* control sits, *through which mechanism*, and *on what primary evidence*. A claim missing any of the three is not admissible.
5. **Control may be absent.** The framework must be able to return `no_evidenced_control_layer`. A framework that finds a monopoly layer everywhere is biased and fails its own gate.
6. **Structural, not moral.** "Monopolised" describes structure. It carries no implication of wrongdoing, illegality, or bad conduct.

## Test layers (provisional — not an ontology)

Six provisional layers are fixed for the gate. They are a **test instrument**, not a final taxonomy, and may be revised, merged, or dropped based on gate results:

- `legal_exclusivity` — an exclusive right or legally granted franchise/exclusivity.
- `access_gatekeeping` — control over access to a market, platform, or channel.
- `capacity_control` — productive capacity or infrastructure that is hard to bypass.
- `qualification_control` — an alternative exists but is not qualified / certified / approved.
- `standard_interface_control` — a standard, protocol, interface, or ecosystem required to operate.
- `temporal_constraint` — an alternative is possible but cannot arrive within the required time.

`switching_dependency` is deliberately **held out** for now. It is added only if case design shows it is genuinely needed and distinct — the gate is meant to be small and hard, not a large list.

## Success is conditional

If — and only if — `LAYER_IDENTIFIABILITY_GATE.md` passes on its fixed case set do we record **DEC-005 — Open Layered Monopolisation as the Monopolises v0.2 thesis**, and only then design an ontology, interface, or data architecture. Until then, the public site is not touched; it stands as a truthful record that v0.1 failed until v0.2 proves itself.
