# MON-G1-S7 — Cloud hyperscaler dependency (UK, dated 2025)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S7
**Role in set:** The pre-registered skeptical case — and, on the evidence, the case that **first triggers the held-out `switching_dependency` probe**. The real success of a skeptical case is that it *changes* the expectation when a specific, source-native instrument appears.
**Status:** Evidence extraction complete — provisional case result (revised after review)
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** skeptical case — `no_evidenced_control_layer` live; any evidenced layer more likely a specific-mechanism `switching_dependency`/`standard_interface_control`, not market-wide control
**Extraction order position:** 8 of 8 (final)

## 0. Scope

> **Large-scale general-purpose (IaaS) cloud infrastructure — United Kingdom, dated 2025.**

Jurisdiction and date are load-bearing. The governing evidence is the **UK** CMA cloud-services market investigation (final decision, 31 July 2025). The **EU** Data Act (switching-fee prohibition from 12 Jan 2027) is **regulatory-trajectory context**, not a governing instrument for the UK case. Provider free-switching programmes documented by the CMA are used to **bound** the claim, not to govern it.

## 0.1 Correction notice (this revision)

The first version returned `no_evidenced_control_layer`. Review identified two methodological errors, now fixed:
1. **A smuggled "durability" requirement.** The first version rejected the egress switching cost because it is "being regulated away." But a documented **2025** switching cost is real in 2025; its future removal makes it a **dated** mechanism, not an absent one — the same dating discipline applied to the 5 nm frontier (S2) and the NdFeB value chain (S6). Remediation ≠ absence of instrument. (The EU Data Act itself allows **reduced** switching charges until 12 Jan 2027; the full ban starts only then.)
2. **A single-actor / "alternatives exist" test that does not belong to this layer.** `switching_dependency` does not ask "do alternatives exist?"; it asks "is there a documented **cost/difficulty of leaving the incumbent**, *despite* alternatives?" Multi-cloud and switching friction coexist. Using AWS/Microsoft plurality and multi-cloud **against** the layer was the wrong test.

## 0.2 Governing extraction question

> Is there a source-native, **documented cost or difficulty of moving away from an incumbent cloud provider** — an instrument that justifies triggering the held-out `switching_dependency` layer — as distinct from a regulator's competition *assessment*?

## 1. Result (provisional, revised)

```
result = evidenced_control_layer
  held-out probe: switching_dependency = TRIGGERED (first evidenced instance in the set)
  locus  = the provider-specific data-egress / switching boundary within UK large-scale (IaaS) cloud, dated 2025
  mechanism = egress charges incurred in moving workload data away from an incumbent provider for switching and/or multi-cloud

  market-level single-actor control = NOT the claim (and not needed)
  standard_interface_control        = NOT ESTABLISHED
```

## 2. S0 evidence

### E01 — A charge specifically incurred to move data out for switching/multi-cloud (the instrument)
**Source:** UK CMA, *Cloud services market investigation — Summary of Final Decision*, 31 July 2025, para 26.
**Verbatim:** "the presence and magnitude of **egress fees required to transfer data between cloud providers for the purposes of switching and/or multi-cloud**."
**Class:** S0. A charge incurred in moving data **out** to switch or multi-cloud is a documented switching cost. (Dated 31 July 2025 — *after* the 2024 free-switching programmes, so the instrument was **present in 2025**.)

### E02 — Switching friction coexists with multi-cloud (factual context)
**Source:** CMA final decision, para 24.
**Verbatim:** "Very few customers switch between clouds: **less than 1% of customers switch provider each year**. Use of multiple cloud providers is more prevalent than switching but it is still uncommon for small and medium sized customers."
**Class:** S0 (factual observation). Establishes that switching friction and multi-cloud coexist — so plurality does not negate a switching cost.

### E03 — The free-switching programmes are bounded (claim-limiting, not layer-defeating)
**Source:** CMA *Appendix N — Egress fees: free switching programmes*.
**Verbatim:** "Free egress for switching is **only available (and subject to requirements and restrictions in some cases)** for the customers of AWS, Microsoft, Google and Civo. UK customers of other cloud providers do not benefit"; the programme matrix marks **"Ongoing multi-cloud use (non-switching)" as "Not eligible"** (AWS, Google); Google's programme "applies to customers who want to do a **complete exit** from Google Cloud"; AWS requires customers to "**delete all remaining data and workloads**."
**Class:** S0. Free egress is universally eligible for a **full exit**, but **partial switching is provider-specific and restricted** (AWS: single-service switches may be eligible; Google: partial/single-service exit case-by-case; Microsoft: partial switching not covered), and **ongoing multi-cloud is not eligible** under the standard programmes — which also require prior application, defined windows, eligibility conditions, and turn substantially on provider discretion. Egress charges therefore **remained applicable in 2025 outside those bounded, conditional exemptions**.

## 3. Layer classification — switching_dependency (held-out probe → TRIGGERED)

- **Held-out probe:** switching cost / difficulty of migration. `switching_dependency` is not one of the six frozen layers; the thesis holds it out, to be added **only if a case shows it is genuinely needed and distinct**. This case is that test.
- **Instrument (S0):** an egress charge incurred **specifically in moving workload data away** from an incumbent provider, for switching and/or multi-cloud (E01), still applicable in 2025 outside the bounded free-switching programmes (E03).
- **Derivation (S1):** a charge incurred specifically in **leaving/moving data away** from the current provider is *mechanically* a cost of switching ⇒ `switching_dependency`. No S2 judgment about magnitude is needed to identify the mechanism.
- **Why this is the first trigger:** unlike CUDA (S3), where **no** specific switching instrument was in the admitted evidence, here the instrument is **named and source-native** (a per-provider egress charge tied to data exit). The held-out layer was **not** a theoretical addition — the data demanded it. This **triggers the held-out probe and makes `switching_dependency` a candidate for admission at full-set closeout** — the admission decision itself belongs to the MON-G1-LI full-set evaluation / DEC-005, not to this single case.
- **Locus is provider-specific, not market-wide:** each incumbent's egress pricing raises the cost of leaving **that** provider. Consistent with the S2 lesson (Monopolises does not require a single actor), the layer is a mechanism instantiated at each provider's exit boundary, not a claim that one firm controls the market.

## 4. What is deliberately excluded (S2)

- Whether the egress cost is **"large enough"** to create market power, decisive lock-in, or an anticompetitive effect — magnitude/effect judgments, all S2. The layer is identified from the **existence** of a switch-linked charge, not its sufficiency.
- The CMA's **"competition is not working well,"** its three **Adverse Effects on Competition**, its "key commercial barrier" characterisation, and its **Strategic Market Status** recommendations are **competition conclusions** — S2, excluded. (We do **not** rely on "key commercial barrier" to establish the layer; the switch-linked charge itself suffices.)
- Market shares and entrenchment findings — S2.

## 5. standard_interface_control — NOT established

The CMA also cites "differentiation of features and interfaces." That is a market-wide competition **assessment**, not a **named standard/protocol/interface required to operate** held by one actor. No named interface instrument is present — same bar S5 set (a named interface, not a general friction). Not established.

## 6. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| A charge is incurred to move data out for switching | CMA para 26: "egress fees required to transfer data … for the purposes of switching and/or multi-cloud" | a cost of leaving ⇒ `switching_dependency` | whether the cost is "large enough" to lock in |
| The charge persisted in 2025 | CMA final decision dated 31 Jul 2025; Appendix N: free egress is full-exit-only, ongoing multi-cloud "Not eligible" | dated-2025 instrument, not removed | whether remediation is sufficient |
| Switching friction coexists with multi-cloud | "less than 1% … switch … multi-cloud more prevalent … still uncommon" | plurality does not negate a switching cost | the AEC / market-power conclusion |
| No named required interface | only a market-wide "technical barriers" assessment | `standard_interface_control` not established | the competition assessment |

## 7. Claim boundary

### Admissible record (dated, UK)
> For UK large-scale (IaaS) cloud infrastructure in **2025**, primary evidence (UK CMA final decision, 31 July 2025) establishes a `switching_dependency` layer at the **provider-specific data-egress boundary**: an egress charge is incurred in moving workload data away from an incumbent provider for switching and/or multi-cloud; the providers' free-switching programmes universally cover **full exit**, but **partial switching is provider-specific and restricted** and **ongoing multi-cloud is not eligible** under the standard programmes, so egress charges **remained applicable in 2025 outside those bounded, conditional exemptions**. This triggers the previously held-out `switching_dependency` probe for the first time.

### Not admissible
- ❌ "Cloud is monopolised" / "AWS or Microsoft controls cloud." — market-level single-actor control is **not** the claim.
- ❌ Using the egress cost to assert decisive lock-in, market power, or an anticompetitive effect — magnitude/effect is S2.
- ❌ Using the CMA's "competition not working well" / AEC / SMS findings as classification evidence.
- ❌ Importing the EU Data Act 2027 prohibition as governing the **UK 2025** case — it is regulatory-trajectory context (freshness), not a governing instrument.
- ❌ Any undated claim — the switching landscape is changing (2024 bounded programmes; EU 2027 prohibition).

## 8. Running gate picture (eight of eight — set complete)

- S8 → `legal_exclusivity`
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `capacity_control` + `access_gatekeeping`
- S4 → `access_gatekeeping`
- S5 → `access_gatekeeping`
- S3 → `no_evidenced_control_layer`
- S7 → `switching_dependency` (held-out probe **triggered**)

The skeptical case did the deeper job: it did not merely "resist" a control finding — it **discriminated**. Where CUDA (S3) offered no source-native switching instrument and returned the negative, cloud (S7) offered a **named, source-native** one (per-provider data-egress on exit) and **triggered the held-out layer**. `switching_dependency` was therefore not a theoretical add-on; the evidence demanded it — so it becomes a **candidate for admission**, to be decided at full-set closeout, not by this case. **Four mechanisms are now evidenced** (`legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `switching_dependency`); `standard_interface_control`, `qualification_control`, and `temporal_constraint` remain unproven; one case (S3) returned the honest negative.

## 9. Next step

The fixed set is complete (8/8). **Do not** close the gate from the layer count. After review of this revised S7, run a **full-set MON-G1-LI gate evaluation** against the pass condition and falsifier as a whole — reviewer reproducibility, genuine layer diversity, bounded S2, locus usefulness, and the four falsifier conditions — including the meta-finding that `switching_dependency` was evidenced and now warrants admission to the taxonomy. Then decide PASS/FAIL and what actually enters DEC-005.
