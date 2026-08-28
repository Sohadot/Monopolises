# MON-G1-S1 — EUV lithography (first real test of capacity_control)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S1
**Role in set:** First case beyond the easy positive control. This is where Layered Monopolisation must prove it can classify from a source-native control instrument rather than a dominance narrative.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `capacity_control` — held as a hypothesis, not asserted because ASML is the well-known EUV supplier
**Extraction order position:** 2 of 8

## 0. Governing extraction question

> Is there source-native evidence that a specific productive capability inside leading-edge EUV lithography is controlled through **capacity that cannot presently be bypassed**, rather than merely evidence that one supplier has very high market share?

The bar is deliberately higher than "ASML is the only supplier." A market-share statement alone would not establish `capacity_control`; the result would then be `ambiguous_layer`. The classification below is admitted only because the primary source ties the sole-production fact to a **specific productive capability** (manufacturing the EUV scanner) that is **essential** to the function and has **no present alternative source**.

## 1. The four tests

### function — the critical function, stated narrowly
Producing the **EUV lithography scanner** — the exposure tool required to pattern integrated circuits at the leading edge (linewidth of 5 nm or less). This is **not** "semiconductor manufacturing" and **not** "advanced chips" in general; it is the specific step of supplying the EUV patterning tool.

### locus — where the hypothesized control sits
**EUV scanner production** (the manufacture of the complete EUV stepper/scanner system), not the downstream chip fabrication that TSMC/Samsung perform, and not DUV lithography (which has multiple suppliers). The primary source also locates the EUV **light source** (Cymer) inside ASML, indicating the light-source capacity is vertically integrated rather than a separate external locus.

### mechanism — what makes it `capacity_control` specifically
A single productive capability — manufacturing the EUV scanner — for which the primary source states there is **one producer** and **no present alternative**, and which is **essential** for ≤5 nm patterning. Sole productive capacity for an essential, presently-unsubstitutable tool is a capacity chokepoint, not merely a high market share.

### boundary — the leap that is refused
The case must not jump from "ASML is the sole producer of EUV scanners" to "ASML monopolises advanced semiconductors." ASML supplies **one (critical) tool**; the chipmakers manufacture the chips. The evidenced layer is confined to the EUV-scanner production locus.

## 2. S0 evidence

### E01 — Sole producer of EUV scanners, tied to essentiality
**Publisher:** The White House (report includes reviews by the Department of Commerce)
**Source:** *Building Resilient Supply Chains, Revitalizing American Manufacturing, and Fostering Broad-Based Growth: 100-Day Reviews under Executive Order 14017*, June 2021, p. 51.
**Verbatim:** "for lithography, ASML (Netherlands) is the sole producer of EUV stepper/scanners, which are essential for producing integrated circuits with a linewidth of 5 nm or less."
**Evidence class:** S0
**Use:** Establishes both the sole-production fact **and** the essentiality of the tool to the leading-edge function — the two elements `capacity_control` requires. This is more than a market-share statement.

### E02 — Independent restatement of single-source supply
**Publisher:** The White House / Department of Commerce (same report)
**Source:** 100-Day Reviews under EO 14017, June 2021, p. 54.
**Verbatim:** "only ASML supplies EUV equipment, and the top three providers (ASML, Nikon, Canon) account for virtually all of the overall market share."
**Evidence class:** S0
**Use:** A second source-native statement of single-source EUV supply within the same authoritative primary document. Note the deliberate contrast the source itself draws: EUV is single-source (only ASML), whereas the broader lithography market is a top-three oligopoly — which is why the layer is confined to EUV, not lithography generally.

### E03 — EUV light source is vertically integrated into ASML
**Publisher:** The White House / Department of Commerce (same report)
**Source:** 100-Day Reviews under EO 14017, June 2021, p. 50.
**Supported facts:** Cymer produces the lasers (light source) for ASML's EUV stepper/scanner machines; ASML acquired Cymer in 2013; Cymer remains a separate operating unit within ASML, located in the United States.
**Evidence class:** S0
**Use:** Locates the critical EUV light-source capacity **inside** ASML, so the light source is not a distinct external control locus. Corroborates that the capacity is concentrated at the scanner producer.

## 3. Layer classification (provisional)

```
result = evidenced_control_layer
layer  = capacity_control
```

### Control mechanism
> Sole present productive capacity for the EUV lithography scanner — the exposure tool a primary U.S. government review states is essential for producing integrated circuits at ≤5 nm and is produced by only one supplier — with the EUV light source vertically integrated into the same producer.

Reached from source-native government statements. **No S2 is required** to assign the layer: the sole-production fact and the essentiality are both stated in the source.

## 4. Claim boundary

### Admissible record
> Within leading-edge (≤5 nm) semiconductor patterning, a `capacity_control` layer sits at **EUV scanner production**: a primary U.S. government review states that ASML is the sole producer of EUV stepper/scanners essential for ≤5 nm linewidths, with no present alternative supplier and the EUV light source vertically integrated into the same producer.

### Not admissible (exceeds the evidence)
- ❌ "ASML monopolises advanced semiconductors." — ASML supplies one tool; it does not fabricate chips.
- ❌ "ASML controls lithography." — the same source says the broader lithography market is a top-three oligopoly (ASML, Nikon, Canon); the single-source fact holds only for **EUV**.
- ❌ Any claim of permanence. The record is present-tense; whether the capacity "cannot be bypassed" in the future is a forward-looking judgment (S2) and is excluded from the classification.

## 5. v0.2 record elements

| Element | Value |
|---|---|
| **System** | Leading-edge (≤5 nm) semiconductor patterning |
| **Layer** | `capacity_control` |
| **Control Mechanism** | Sole present productive capacity for the essential EUV scanner tool; light source vertically integrated |
| **Evidence** | White House / Dept. of Commerce, 100-Day Reviews under EO 14017 (June 2021), pp. 50–54 |

## 6. S2 note (recorded, not used for classification)

- Whether ASML's EUV capacity is durably unbypassable (future entrants, alternative patterning approaches) is forward-looking and would require domain judgment — S2. It is excluded from the classification, which is present-tense.
- The economic significance of the chokepoint (pricing power, geopolitical leverage) is likewise S2 and out of scope for a *layer identifiability* result.

## 7. Result and honest limitations

- **Case result:** `evidenced_control_layer` / `capacity_control`, at the EUV-scanner-production locus, from S0 government-primary evidence, no S2 needed for classification.
- **Why not `ambiguous_layer`:** the source does not merely state market share; it ties sole production to essentiality for the ≤5 nm function, which is the specific capacity mechanism the gate requires.
- **Limitation to note for review:** the source-native "sole producer / only ASML" language is carried by a **single authoritative primary document** (the June 2021 EO 14017 review). Notably, ASML's own investor materials and Form 20-F reviewed for this case do **not** self-characterize as the "only/sole" EUV producer, so no operator self-statement is admitted as corroboration (unlike the USPS corroboration in S8). Before this case is treated as final rather than provisional, a second independent primary source (e.g. a later government supply-chain assessment or a competition-authority finding quoting primary evidence) should be admitted to confirm the single-source fact still holds and is not artifact of one document's phrasing.

## 8. What this case tells us about the framework

`capacity_control` was classifiable here **without** S2 — but only because the primary source did the hard work of pairing sole production with essentiality. This is the first evidence that Layered Monopolisation can produce a source-native result beyond the easy legal-exclusivity case. It is **one** such case; the gate's verdict still depends on the fixed set as a whole. Two cases (S8, S1) now show two genuinely different mechanisms (`legal_exclusivity`, `capacity_control`), which is early support for the "genuine layer diversity" pass condition — not yet a pass.

## 9. Next step

Stop at S1 for review before extracting MON-G1-S2 (leading-edge foundry fabrication), per the frozen extraction order. Do not batch. Single-case checkpoints preserve auditability.
