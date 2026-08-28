# MON-G1-S2 — Leading-edge foundry fabrication (the moving-frontier test)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S2
**Role in set:** The real stress test. This is where the moving frontier — the defect that sank part of v0.1 — could pull us back into an analyst-defined monopoly claim. The gate must survive it without S2.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `capacity_control` at high-volume manufacturing (HVM) of the leading logic node
**Extraction order position:** 3 of 8

## 0. Governing extraction question

> Can a present-tense capacity-control layer be identified at a **specifically dated** leading-edge logic node from primary evidence, **without turning moving-frontier leadership into an analyst-defined monopoly claim**?

## 1. The moving-frontier discipline — four separated truths

"Leading-edge foundry" is not one fact. The gate is defeated if these four are blurred. Each is tagged with its evidence status.

| # | Truth | What it asks | Status here |
|---|---|---|---|
| 1 | **node capability** | Who can *actually fabricate* a specific node? | S0 — dated |
| 2 | **HVM status** | Is it *high-volume* production, or announced/ramping/pilot? | S0 — dated |
| 3 | **capacity locus** | Where is the *measurable* productive capacity, and is it single-source? | S0/S1 — see result |
| 4 | **frontier date** | What counted as "leading-edge" *on the date of the evidence*? | S0 — must be fixed per source |

The cardinal rule: **`capacity_control` may not be inferred from market share or technological leadership alone.** A dominant share is not, without S2, a control instrument.

## 2. S0 evidence

### E01 — At the 2021 frontier (5 nm), the leading node had *two* HVM producers
**Publisher:** The White House / Department of Commerce
**Source:** *100-Day Reviews under Executive Order 14017*, June 2021, p. 39.
**Verbatim:** "The United States lacks semiconductor production capability at the most advanced semiconductor process node—currently 5 nm—at which **only TSMC (Taiwan) and Samsung (South Korea) currently operate**."
**Frontier date:** 2021 → leading node = 5 nm.
**Evidence class:** S0.
**Use:** Fixes the dated frontier (5 nm) and — decisively — that **two** firms operate at it, not one.

### E02 — Independent-of-share confirmation of "only two" at the leading edge
**Publisher:** The White House / Department of Commerce (same report)
**Source:** 100-Day Reviews under EO 14017, June 2021, p. 64.
**Verbatim:** "Samsung is one of **only two companies that are producing volume** in the leading edge 7 nm and 5 nm chips."
**Evidence class:** S0.
**Use:** Second source-native statement (same document) that leading-edge HVM at the 2021 frontier is a **two-producer** structure. Confirms HVM status (truth #2), not merely capability.

### E03 — TSMC is the dominant share, but that is stated as *reliance/leadership*, not a control instrument
**Publisher:** The White House / Department of Commerce (same report)
**Source:** 100-Day Reviews under EO 14017, June 2021, p. 39.
**Verbatim:** "U.S. fabless chip companies now rely **almost exclusively** on Asian producers (especially TSMC) for production of the most advanced (7 nm or less) chips."
**Evidence class:** S0 for the *reliance/dominance fact*.
**Use:** Records that TSMC is the dominant supplier — but the source frames this as reliance and leadership, **not** as an exclusive right, a required qualification, or a single-source capacity. Converting "especially TSMC" into "TSMC controls the layer" is an S2 step (see §5), which the gate forbids.

### E04 — Context: no third producer was at the leading edge in 2021
**Publisher:** The White House / Department of Commerce (same report)
**Source:** 100-Day Reviews under EO 14017, June 2021, p. 40.
**Verbatim:** China's "most advanced pure-play foundry, Semiconductor Manufacturing International Corporation (SMIC), can only produce at the 14 nm node, with limited capacity."
**Evidence class:** S0.
**Use:** Confirms the 2021 leading edge was a **two-producer** set (not one, not many). Rules out a "many producers" reading without making it single-source.

## 3. Present-frontier context (dated 2025–2026) — NOT admitted as S0

The 2021 evidence is five years old; the frontier has moved. To avoid classifying a stale frontier, the present node is dated from current reporting. **This is trade-press reporting, not a primary source, and is used only to date the present frontier — it carries no part of the classification.**

- The present leading edge is the **2 nm class**, and as of late 2025–2026 it is entered by **three** producers: **TSMC N2**, **Samsung SF2**, and **Intel 18A**, all having begun volume/HVM production in 2025. (Trade press: Tom's Hardware and others.)

Direction of the correction: moving from the 2021 frontier to the present frontier makes the structure **more** contested (two producers → three), not less. Whatever the exact current shares, the leading node is **not** single-source at either date.

## 4. Classification (provisional)

```
result = no_evidenced_control_layer
hypothesis capacity_control = NOT SUPPORTED at the "leading logic node" framing
```

**The frozen `capacity_control` hypothesis fails on its own evidence.** At every frontier we can date from primary sources, the leading logic node has **more than one** HVM producer. There is no single-source productive capacity and no control instrument that primary evidence ties to one actor. The only way to reach `capacity_control` here is to treat TSMC's larger share as "control" — an S2 market-share/leadership judgment, which the gate excludes.

## 5. Per-claim evidence ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Leading node in 2021 was 5 nm | "most advanced … currently 5 nm" (p.39) | — | — |
| Leading-edge HVM was a two-producer set (2021) | "only TSMC … and Samsung … currently operate" (p.39); "only two companies … producing volume" (p.64) | Two named HVM producers ⇒ **not single-source** ⇒ capacity_control not mechanically derivable | Judging TSMC's lead as "control" |
| TSMC is the dominant supplier | "rely almost exclusively … especially TSMC" (p.39) | Dominant share ≠ control instrument (no S1 path from share to control) | "TSMC controls / monopolises advanced chips" |
| Present frontier is 2 nm class, multi-producer | *(trade press, not S0)* | — | Any present-tense single-source claim |
| Therefore no single-actor control layer | conjunction of the above S0 facts | **S1:** absence of a single-source locus ⇒ `no_evidenced_control_layer` | Supplying the missing control via analyst judgment |

Note the asymmetry with S1 (EUV): there, an S0 **sole-producer** fact plus an S0 **essentiality** fact yielded a valid S1 capacity_control derivation. Here the parallel S0 fact is the opposite — **two/three producers** — so the same rule mechanically yields *no* control layer. Same rule, opposite input, honest opposite result.

## 6. Why not the other outcomes

- **Why not `evidenced_control_layer`:** no primary evidence of single-source capacity or a control instrument at the leading node; the node is multi-producer at every dated frontier.
- **Why not `ambiguous_layer`:** reviewers would not disagree about *which* layer applies — they would agree that **no** control layer is source-native without S2. Ambiguity of layer is not the problem; absence of an evidenced layer is.
- **Why `no_evidenced_control_layer` is not "there is no concentration":** the same government report is *about* concentration and supply-chain risk (geographic concentration in Taiwan/Korea). But geographic concentration and market dominance are **not** an evidenced single-actor capacity-control layer. The gate result is about layer identifiability, not about whether risk exists.

## 7. Claim boundary

### Admissible record
> At the leading logic node, primary evidence (dated 2021, frontier = 5 nm) shows a **two-producer** HVM structure (TSMC and Samsung), with TSMC the dominant supplier; the present frontier (2 nm class) is entered by three producers. No single-source capacity or control instrument is evidenced at the leading node, so **no capacity-control layer is established** without analyst judgment.

### Not admissible (exceeds the evidence)
- ❌ "TSMC monopolises advanced chips." — the leading node is multi-producer; this requires S2.
- ❌ "There is a capacity_control layer at the leading node." — not evidenced; would need to convert dominance into control.
- ❌ Any classification that fixes "leading-edge" without a date — the frontier moves.

## 8. What this case tells us about the framework

This is the result the gate most needed to produce. For the single most famous "dominance" case in the set, the framework returns an honest **negative** — `no_evidenced_control_layer` — because dominance is not source-native control, and because the moving frontier was handled by **dating** every frontier rather than freezing a reputation. The v0.1 defect (letting an analyst define the answer at a moving frontier) is not repeated: no S2 judgment was smuggled in to manufacture a layer.

Two genuine leads are recorded but **not** classified (doing so would be scope expansion mid-gate):
- The **EUV tool** feeding these fabs is a distinct upstream locus — already captured as S1 (`capacity_control`), a different layer than "the foundry node."
- **Advanced packaging** (e.g. CoWoS) may be more concentrated than front-end fabrication and could carry its own layer — a candidate for a future, separately-gated case, not this one.

## 9. Result and next step

- **Case result:** `no_evidenced_control_layer`; the frozen `capacity_control` hypothesis is **not supported** at the leading-logic-node framing, on present S0 evidence, without S2.
- Stop at S2 for review before extracting MON-G1-S6 (rare-earth magnets), per the frozen order. Do not batch.

## 10. Running gate picture (three of eight)

- S8 → `evidenced_control_layer` / `legal_exclusivity`
- S1 → `evidenced_control_layer` / `capacity_control` (S1-derived label)
- S2 → `no_evidenced_control_layer`

The set is now producing **both** evidenced layers and an honest negative, of **different** kinds — early signs of a discriminating instrument rather than a monopoly-finding machine. Still three cases; the gate verdict waits on the full fixed set.
