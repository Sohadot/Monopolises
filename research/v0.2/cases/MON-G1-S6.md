# MON-G1-S6 — Rare-earth permanent magnets (NdFeB)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S6
**Role in set:** The test of whether `qualification_control` is a **real, independent** layer — or whether the taxonomy will swallow any kind of "ineligibility" under that name and let the Gate-0 sufficiency problem back in.
**Status:** Evidence extraction complete — provisional case result (revised after review)
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `qualification_control` and/or `capacity_control`
**Extraction order position:** 4 of 8

## 0. Governing extraction question

> For NdFeB permanent magnets, which control layers are classifiable from primary evidence — and does `qualification_control` (a certification/approval an existing alternative must hold and does not) actually appear, or only something that resembles it?

## 0.1 What this revision changed and why

The first version classified the defense sourcing restriction as `qualification_control` by reasoning "covered-country source → lacks approval → qualification_control." **The phrase "lacks approval" was added by the framework; it is not the instrument the law creates.** 10 U.S.C. § 4872 / DFARS 252.225-7052 do not test whether a magnet holds a certification — they restrict, by **source-origin**, what may be **delivered into the DoD procurement channel**. That is the frozen definition of **`access_gatekeeping`** ("a documented rule or control governing admission to a market, platform, or channel"), not `qualification_control`. The regime is a **prohibition + exceptions/waiver** (a nonavailability determination), not a certification regime — further confirming it is admission control, not qualification.

Consequently:
- Layer B is reclassified `qualification_control` → **`access_gatekeeping`**.
- **`qualification_control` is recorded as NOT established by S6.** It is not rescued; it remains unproven until a case presents a genuine certification/approval/qualification an existing alternative fails.
- Layer A keeps `capacity_control` but is re-grounded on a magnet-specific primary source (BIS Section 232 report) instead of an inference from U.S. facility losses alone.

## 1. Result (provisional, revised)

```
result = multiple_evidenced_layers
  Layer A: capacity_control    — locus: China-dominated NdFeB value-chain capacity, evidenced from 2020–2022 data (dated finding)
  Layer B: access_gatekeeping  — locus: U.S. defense procurement channel (source-origin admission restriction)

  qualification_control = NOT ESTABLISHED by this case
```

---

## 2. Layer A — capacity_control (China-dominated NdFeB value chain)

### S0 evidence (primary, magnet-specific)
**Source:** U.S. Department of Commerce / BIS, *The Effect of Imports of Neodymium-Iron-Boron (NdFeB) Permanent Magnets on the National Security* (Section 232 investigation report, June 2022; published Federal Register 2023-02-14).
- p. 7, verbatim: "The United States has **no domestic production of rare earth oxides or metal**. The United States is **dependent on foreign sources, especially China**, for NdFeB magnets. China dominates all steps of the global NdFeB magnet value chain. In 2020, China controlled about **92 percent** of the global NdFeB magnet and magnet alloy market."
- p. 7, verbatim: "China is the **only country with operations in all steps** of the NdFeB magnet value chain … All other countries maintain operations in only some steps."
- p. 6, verbatim: "There is currently **only one firm in the United States, Noveon** (formerly Urban Mining Company), that produces sintered NdFeB magnets"; and "In 2021, the United States imported **75 percent** of its sintered NdFeB magnet supply from China."

### Corroborating history (S0)
2021 EO 14017 critical-materials review, p. 174: the U.S. lost ≥4 NdFeB production and ≥3 rare-earth separation facilities (1992–2020) and its leading NdFeB producer relocated to China (2003). Used as background to the BIS findings, not as the primary basis.

### Three-element test (frozen `capacity_control` definition)
| Element | Met? | Basis |
|---|---|---|
| documented capacity | **Yes — S0** | China ~92% of the 2020 magnet/alloy market; only country across all value-chain steps; US has no domestic oxide/metal production and one small sintered producer (BIS 232, pp.6–7) |
| function must pass through it | **Yes — S0** | US "dependent on foreign sources, especially China"; 75% of US sintered supply imported from China (BIS 232, pp.6–7) |
| hard to bypass | **Yes — S1** | no domestic oxide/metal production + single small domestic magnet producer ⇒ the function cannot presently be routed off the China-dominated value chain |

### Classification derivation
S0 (China-dominated value chain; no domestic upstream; single small US producer) → **S1** conjunction → `capacity_control` at a **China-dominated value-chain capacity** locus. Not a claim that China is the *sole* producer (Japan and others hold small shares) — a **dominant, all-stage** locus, which is what the definition requires.

### Excluded (S2 — the Gate-0 trap)
Whether a domestic rebuild is or will be **sufficient to replace** the incumbent (e.g. 2021 review p.192, "would not be sufficient to hedge the risk") is the replacement-sufficiency question. Excluded.

---

## 3. Layer B — access_gatekeeping (U.S. defense procurement channel)

### S0 evidence
- **Statute — 10 U.S.C. § 4872** ("Acquisition of sensitive materials from non-allied foreign nations"): restricts DoD acquisition of covered sensitive materials — expressly including samarium-cobalt and **neodymium-iron-boron permanent magnets** — by **source-origin** (covered nations).
- **Implementing clause — DFARS 252.225-7052 / 225.7018-2**, verbatim: "do not acquire any covered material melted or produced in any covered country, or any end item, manufactured in any covered country, that contains a covered material." Covered countries: "(1) The Democratic People's Republic of North Korea; (2) The People's Republic of China; (3) The Russian Federation; or (4) The Islamic Republic of Iran."
- **Dated scope (important):** *through Dec 31, 2026* the NdFeB restriction covers "melting neodymium with iron and boron" and "all subsequent phases of production" (powder formation, pressing, sintering/bonding, magnetization). *Beginning Jan 1, 2027* it expands to "the entire supply chain from mining … through production of finished magnets."
- **Exceptions / waiver:** the regime is prohibition-plus-exception — DFARS 225.7018-3 (Exceptions) and 225.7018-4 (Nonavailability Determination) permit acquisition in defined cases (e.g. certain COTS/commercial and electronic-device contexts, recycled/reclaimed material, and where compliant material of satisfactory quality/quantity/form is not available).

### Why `access_gatekeeping` (frozen definition)
The instrument is "a documented rule … governing admission to a … channel." It controls **which source-origin materials may be delivered into the DoD procurement channel**. It does not certify or qualify a supplier; it admits or excludes by origin, subject to exceptions.

### Why NOT `qualification_control`
`qualification_control` requires a **certification/approval/qualification an alternative must hold and does not**. § 4872 defines no such credential; covered-nation magnets are not "unqualified," they are **origin-excluded from a channel** (and can even be admitted via a nonavailability determination). Calling that a qualification an alternative "lacks" would be the framework supplying the instrument.

### Why NOT `legal_exclusivity` (the S8 layer)
No exclusive right is granted to anyone. § 4872 excludes sources from a channel; it does not confer a monopoly right (contrast the Private Express Statutes in S8, which grant USPS an exclusive right). Same source-type (statute), different layer.

### Excluded (S2)
Whether compliant supply is **sufficient**, enforcement intensity, and waiver frequency — all S2.

---

## 4. `qualification_control` — explicitly NOT established

S6 does **not** evidence `qualification_control`. The report's "qualified"/"sufficient" language does not supply it: p.179 is about **workers** ("enough qualified U.S. workers"); p.192 is **replacement sufficiency** (S2); and a nearby "only one factory … is qualified" line (p.173) is about a **high-modulus/high-strength material, not NdFeB**, so it is not used. The layer remains unproven and awaits a case with a genuine certification/approval/qualification barrier. Not rescuing it here is the point of the exercise.

## 5. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| China dominates the NdFeB value chain | ~92% of 2020 magnet/alloy market; only country across all steps; US no domestic oxide/metal; one small US sintered producer (BIS 232 pp.6–7) | function must pass through China-dominated capacity ⇒ `capacity_control` | whether a rebuild can *replace* it (S2) |
| DoD channel excludes covered-origin magnets | 10 USC 4872; DFARS 252.225-7052/225.7018-2 "do not acquire … covered material … covered country"; PRC/DPRK/Russia/Iran | a documented rule governs admission to the procurement channel ⇒ `access_gatekeeping` | sufficiency of compliant supply; waiver frequency |
| It is not qualification_control | the instrument is origin-based admission + exceptions, not a credential test | no certification an alternative "lacks" is present ⇒ layer NOT established | — |

## 6. Claim boundary

### Admissible record
> NdFeB permanent magnets carry two independent, source-evidenced control layers: (A) a `capacity_control` layer at a **China-dominated NdFeB value-chain capacity** locus — the 2022 BIS report states that China controlled ~92% of the 2020 magnet/alloy market and was the only country operating across all value-chain steps, and that the U.S. had no domestic rare-earth oxide/metal production and a single small sintered-magnet producer; and (B) an `access_gatekeeping` layer in the **U.S. defense procurement channel** — 10 U.S.C. § 4872 / DFARS 252.225-7052 restrict, by source-origin, delivery of covered-nation (PRC/DPRK/Russia/Iran) NdFeB magnets to DoD, on a dated scope (melting-and-after through 2026; full chain from 2027) and subject to exceptions and a nonavailability determination.

### Not admissible
- ❌ "China monopolises magnets." — a dominant, all-stage locus, not an evidenced sole producer (Japan and others hold small shares).
- ❌ "Covered-country magnets are banned from DoD" without qualification — the restriction is dated and carries exceptions / a nonavailability waiver.
- ❌ Calling Layer B `qualification_control` (no credential test) or `legal_exclusivity` (no granted right).
- ❌ Any **sufficiency / replacement** claim — Gate-0 S2.

## 7. Running gate picture (four of eight)

- S8 → `legal_exclusivity` (single-actor, statutory right)
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `multiple_evidenced_layers`: `capacity_control` (China-dominated value chain) + `access_gatekeeping` (defense procurement channel)

Layers evidenced so far: `legal_exclusivity`, `capacity_control`, `access_gatekeeping` (three distinct mechanisms). **`qualification_control` and the other frozen layers remain unproven.** The discipline that produced this — refusing to let "ineligibility" be relabelled as qualification — is the result that matters more than the count. Still four cases; the gate verdict waits on the full fixed set.

## 8. Next step

Stop at S6 for review before extracting MON-G1-S4 (native app distribution), per the frozen order. Do not batch.
