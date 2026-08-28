# MON-G1-S6 — Rare-earth permanent magnets (NdFeB)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S6
**Role in set:** The test of whether `qualification_control` is a **real, independent** layer — or just a relabel of missing productive capacity, letting the Gate-0 sufficiency problem back in through the word "qualification."
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `qualification_control` and/or `capacity_control`
**Extraction order position:** 4 of 8

## 0. Governing extraction question

> For NdFeB permanent magnets, is there a documented control layer classifiable from primary evidence — and specifically, does `qualification_control` exist as a mechanism **independent** of `capacity_control`, without smuggling back the Gate-0 sufficiency question?

## 0.1 The three things that must be kept apart

The Gate-0 defect returns the moment these are blurred:

1. **capacity exists** — can anyone produce the magnet at all, and where?  → `capacity_control` territory.
2. **qualified supply exists** — is there a formal certification/approval an alternative must hold, that some existing alternative does **not**?  → `qualification_control` territory.
3. **sufficient qualified supply exists** — is the qualified/domestic supply *enough to replace* the incumbent?  → **the Gate-0 replacement-sufficiency question. This is S2. It is excluded from every classification below.**

`qualification_control` is admissible **only** as (2): a documented approval barrier that an existing, capacity-holding alternative fails. It is **not** admissible as a rephrasing of (1) "there isn't enough domestic capacity," nor as (3) "the qualified supply isn't sufficient."

## 1. Result (provisional)

```
result = multiple_evidenced_layers
  Layer A: capacity_control       — locus: offshore-concentrated NdFeB magnet-making capacity (general market), dated 2021
  Layer B: qualification_control  — locus: U.S. defense procurement, via statutory sourcing disqualification
```

The two layers sit at **different loci** and rest on **different, independent** instruments. Establishing one does not establish the other — which is exactly what makes `qualification_control` a real layer here rather than a relabel.

---

## 2. Layer A — capacity_control (general NdFeB magnet-making)

### S0 evidence
**Source:** The White House / Department of Defense, *100-Day Reviews under Executive Order 14017* (critical-materials review), June 2021.
- p. 174, verbatim: "from 1992 to 2020, the United States lost **at least four NdFeB production facilities**, and the United States also lost **at least three rare earth separation facilities**."
- p. 174, verbatim: "In 2003, following acquisition by a conglomerate including a Chinese entity, **the United States' leading NdFeB magnet producer ceased operations and relocated its operations to China**."
- p. 166, verbatim: China "stepped up its efforts to **capture the entire value chain** in a variety of modern technologies such as **permanent magnets**, batteries, and semiconductors."

### Three-element test (the frozen `capacity_control` definition)
| Element | Met? | Basis |
|---|---|---|
| documented facility/capacity | **Yes — S0** | US lost ≥4 NdFeB production + ≥3 separation facilities; leading producer relocated to China (p.174) |
| function must pass through it | **Yes — S1** | domestic magnet-making capacity largely absent ⇒ NdFeB magnet supply must pass through offshore (China-concentrated) capacity |
| hard to bypass | **Yes — S1** | the capacity was *lost* (facilities closed/relocated), so it cannot presently be routed domestically |

### Classification derivation
S0 facts (capacity lost/relocated, value chain captured) → **S1** conjunction → `capacity_control` at an offshore-concentrated **collective** locus. No S2.

### Excluded (S2 — the Gate-0 trap)
- p. 192, verbatim: "Even if DoD limited all of its peacetime NdFeB procurement … to a single domestic producer, that arrangement **would not be sufficient to hedge the risk** to essential civilian industry …" — a **sufficiency/replacement** judgment. Excluded. (It also shows *a* domestic producer now exists, so Layer A is a concentration, not a literal zero — the claim is bounded accordingly.)

---

## 3. Layer B — qualification_control (U.S. defense procurement)

This is the independent-qualification test. Here an alternative **exists and has abundant capacity** (covered-nation magnets), yet is barred from the defense function because it fails a **documented approval requirement** — the definition of `qualification_control`.

### S0 evidence
- **Statute — 10 U.S.C. § 4872** ("Acquisition of sensitive materials from non-allied foreign nations"): prohibits DoD acquisition of covered sensitive materials — expressly including **samarium-cobalt and neodymium-iron-boron permanent magnets** — mined, refined, separated, melted, or produced in a covered nation.
- **Implementing regulation — DFARS 252.225-7052** ("Restriction on the Acquisition of Certain Magnets, Tantalum, and Tungsten"), verbatim: "The Contractor **shall not deliver** under this contract any covered material melted or produced in any covered country, or any end item, manufactured in any covered country, that contains a covered material." For NdFeB specifically the restriction covers "melting neodymium with iron and boron" and "**all subsequent phases of production** of the magnets" (powder formation, pressing, sintering/bonding, magnetization).
- **Covered countries** (DFARS 252.225-7052), verbatim: "(1) The Democratic People's Republic of North Korea; (2) The People's Republic of China; (3) The Russian Federation; or (4) The Islamic Republic of Iran."

### Why this is `qualification_control` and independent of capacity
| Element | Basis |
|---|---|
| a documented approval/qualification the function requires | S0 — the statute/DFARS clause: a magnet must be a **compliant (non-covered-country) source** to be deliverable to DoD |
| an existing alternative holds capacity but **not** the qualification | S1 — covered-nation NdFeB magnets have **abundant capacity** (Layer A), yet are **disqualified** for defense delivery |
| independence from capacity | S1 — the barrier is **not** "capacity doesn't exist" (it does, in China); it is that the existing capacity is **approval-barred**. Removing the capacity shortage would not remove this barrier, and vice-versa. |

### Classification derivation
S0 (statutory disqualification of covered-nation magnets) → **S1** (an existing, capacity-holding alternative fails a required approval) → `qualification_control` at the **defense-procurement** locus. No S2.

### Why not `legal_exclusivity` (the S8 layer)
`legal_exclusivity` confers an exclusive **right** on an actor (as the Private Express Statutes do for USPS). § 4872 confers no right on anyone; it **disqualifies certain sources**. The effect is an approval barrier — only compliant sources qualify — which is `qualification_control`, not an exclusive right. (Two statutes, two different layers — useful evidence the framework separates mechanisms, not just cites laws.)

### Excluded (S2)
- Whether compliant/qualified magnet supply is **sufficient** to meet defense need — the Gate-0 sufficiency question. Excluded.
- Enforcement intensity, waiver frequency, effectiveness — all S2.

---

## 4. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Domestic NdFeB magnet capacity was lost | ≥4 NdFeB + ≥3 separation facilities lost; leading producer relocated to China (p.174) | supply must pass through offshore capacity ⇒ `capacity_control` | whether a rebuild can *replace* it (p.192) |
| Covered-nation magnets are barred from DoD delivery | 10 USC 4872; DFARS 252.225-7052 "shall not deliver … covered material … covered country"; countries = PRC/DPRK/Russia/Iran | an existing capacity-holding alternative fails a required approval ⇒ `qualification_control` | whether compliant supply is *sufficient* |
| The two layers are independent | different instruments (industrial history vs statute), different loci (general vs defense) | neither classification implies the other | ranking which layer "matters more" |

## 5. Direct answer to the governing question

**Yes — `qualification_control` is a real, independent layer, but only under a strict test the evidence here happens to pass:** a *documented approval instrument* (10 USC 4872 / DFARS 252.225-7052) barring an *existing, capacity-holding* alternative. It is **not** established by the report's "qualified"/"sufficient" language — on inspection those refer to **workers** (p.179, "enough qualified U.S. workers") or to **sufficiency of replacement** (p.192), and one nearby "only one factory … is qualified" line (p.173) is about a high-modulus/high-strength material, **not** NdFeB, so it is not used here. Absent the statute, this case would have been `capacity_control` alone, and calling the capacity shortage "qualification" would have been the Gate-0 relabel we were guarding against.

## 6. Claim boundary

### Admissible record
> NdFeB permanent magnets carry two independent, source-evidenced control layers: (A) a `capacity_control` layer at offshore-concentrated magnet-making capacity — the U.S. lost its domestic NdFeB production and separation facilities and its leading producer relocated to China (dated 2021); and (B) a `qualification_control` layer in U.S. defense procurement — 10 U.S.C. § 4872 and DFARS 252.225-7052 disqualify covered-nation (PRC/DPRK/Russia/Iran) NdFeB magnets from delivery to DoD, so an existing, capacity-holding source fails a required approval.

### Not admissible
- ❌ "China monopolises magnets." — Layer A is a capacity concentration, not an evidenced single-source monopoly; a domestic producer exists (p.192).
- ❌ Any **sufficiency / replacement** claim ("domestic supply can't replace," "not enough qualified supply") — Gate-0 S2.
- ❌ Treating Layer A's capacity shortage **as** qualification, or extending Layer B beyond defense procurement.
- ❌ Calling Layer B `legal_exclusivity` — it is a disqualification, not a granted right.

## 7. Running gate picture (four of eight)

- S8 → `legal_exclusivity` (single-actor, statutory right)
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `multiple_evidenced_layers`: `capacity_control` (offshore) + `qualification_control` (defense)

Three distinct mechanisms now appear across four cases (`legal_exclusivity`, `capacity_control`, `qualification_control`), and S6 shows two of them **co-locating in one system at different loci**. This is real progress on the "genuine layer diversity" pass condition — and, more importantly, `qualification_control` survived its independence test instead of collapsing into capacity. Still four cases; the gate verdict waits on the full fixed set.

## 8. Next step

Stop at S6 for review before extracting the next case in the frozen order (MON-G1-S4 — native app distribution). Do not batch.
