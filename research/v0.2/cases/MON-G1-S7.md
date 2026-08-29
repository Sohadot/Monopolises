# MON-G1-S7 — Cloud hyperscaler dependency (the deliberate skeptical case, UK/EU evidence, 2025)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S7
**Role in set:** The built-in guard against confirmation bias. A large, concentrated, heavily-investigated market is the easiest place to *assume* control. This case exists to check that the framework can return **`no_evidenced_control_layer`** where the evidence does not support a documented control layer.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** deliberate skeptical case — `no_evidenced_control_layer` is a live outcome; any evidenced layer more likely `switching_dependency`/`standard_interface_control` at a specific mechanism, not the market as a whole
**Extraction order position:** 8 of 8 (final)

## 0. Scope

> **Large-scale general-purpose (IaaS) cloud infrastructure — UK/EU evidence, dated 2025.**

The market is global, but the strongest primary evidence is the UK CMA cloud-services market investigation (final decision, 31 July 2025) and the EU Data Act. Dating matters here: the main candidate switching instrument is changing fast (see §4).

## 0.1 Governing extraction question

> Is there a source-native, single-actor control layer in general-purpose cloud infrastructure — or is this a **concentrated but contested** market whose frictions are (a) a regulator's *competition assessment* (S2) and (b) a switching cost currently being removed by regulation?

## 1. Result (provisional)

```
result = no_evidenced_control_layer
  market-level single-actor control  = NOT EVIDENCED (contested, dynamic oligopoly; concentration ≠ control)
  switching_dependency probe          = NOT TRIGGERED for a present-tense layer (candidate egress fee is being regulated away)
  standard_interface_control          = NOT ESTABLISHED (no named required interface; "technical barriers" are a market-wide S2 assessment)
```

This is a **layer-identifiability** result. It does **not** say cloud is unconcentrated or unproblematic — a regulator has found the opposite. It says: **no control layer is classifiable from primary evidence without S2.**

## 2. S0 evidence

**Source:** UK Competition and Markets Authority, *Cloud services market investigation — Summary of Final Decision*, 31 July 2025.
- **Contested, dynamic oligopoly:** "the two largest providers, Microsoft and AWS, **each has a high share of supply at [30-40]%** in 2024. **Microsoft has grown its share while AWS' share has decreased** since 2020."
- **Multi-cloud exists, especially for large customers:** "Use of multiple cloud providers is more prevalent than switching … **Large cloud customers are more likely than smaller ones to use multiple clouds**."
- **The documented commercial switching instrument is egress fees:** "A key commercial barrier is the **presence and magnitude of egress fees** required to transfer data between cloud providers for the purposes of switching and/or multi-cloud."

## 3. Market-level control — NOT evidenced

- Two providers at **[30-40]% each** (plus Google and others) is a **concentrated oligopoly**, not single-actor control; and the shares are **moving in opposite directions** (Microsoft up, AWS down since 2020) — the opposite of an entrenched single controller.
- **Multi-cloud is common among large customers**, so the function does not pass through one provider.
- Treating "concentration" as "control" is the S2 market-power inference the gate forbids (the same discipline as S2-foundry, where a two-producer set only became `capacity_control` once *no-alternative* evidence appeared — which is **absent** here, since multi-cloud exists).

## 4. switching_dependency probe — candidate found, NOT triggered for a present-tense layer

- **Held-out probe:** switching cost / difficulty of migration. The candidate instrument is **egress fees** (E-CMA above).
- **Why it is not a durable present-tense control instrument:** the egress switching cost is **being removed under regulation**. The **EU Data Act** (in force 11 Jan 2024) requires removing obstacles to effective switching; Google, AWS, and Microsoft each introduced **free-switching / waived-egress programmes in 2024** (documented in the CMA's own Appendix N, "Egress fees – free switching programmes"); and from **12 Jan 2027** providers serving EU customers are prohibited from charging switching fees, including egress.
- So the probe **surfaces a candidate but it fails the durability/present-tense test**: a switching cost that is actively being regulated out of existence in the dated scope is not a source-native *control layer*. (Dated at ~2022 it might have been a stronger candidate — the dating discipline is load-bearing, as in S2.)
- Even at its peak, egress was a **pricing friction**, not single-actor control; and it was charged by all providers, not a mechanism one actor uses to control the others.

## 5. standard_interface_control — NOT established

The CMA also cites **technical barriers** ("differentiation of features and interfaces"). But that is the CMA's **competition assessment** of a market-wide friction, not a **named standard/protocol/interface required to operate** held by one actor. No single named interface instrument is present. (Same bar S5 set: a named interface, not a general friction.)

## 6. What is deliberately excluded (S2)

- The CMA's headline conclusion — "**competition is not working well**" — and its three **Adverse Effects on Competition** (market concentration/barriers to entry; switching barriers; committed-spend discounts and software-licensing practices) are **competition conclusions**, the exact S2 the gate forbids for classification. Noted as context; not used to classify.
- The CMA's recommendation to open **Strategic Market Status** investigations into AWS and Microsoft is a regulatory-process step, not a documented control instrument.
- Market shares, entrenchment judgments, and "market power" findings — all S2.

## 7. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Two providers ~30-40% each, shares diverging | CMA: "[30-40]% … Microsoft has grown … AWS' share has decreased" | contested, dynamic oligopoly ⇒ no single-actor control | "the market is monopolised" |
| Multi-cloud common for large customers | CMA: "more likely … to use multiple clouds" | function not routed through one provider | — |
| Egress fees are the switching instrument | CMA: "presence and magnitude of egress fees" | candidate `switching_dependency` | that this is decisive control |
| Egress is being removed | EU Data Act (2024); provider programmes (CMA Appendix N); 2027 prohibition | candidate fails present-tense durability ⇒ probe not triggered | whether removal is sufficient |
| No named required interface | only a market-wide "technical barriers" assessment | `standard_interface_control` not established | the AEC competition conclusion |

## 8. Claim boundary

### Admissible record
> For general-purpose (IaaS) cloud infrastructure (UK/EU, 2025), primary evidence (UK CMA final decision) shows a **concentrated but contested and dynamic** market — the two largest providers each at [30-40]% with shares diverging, and multi-cloud common among large customers — whose principal documented switching instrument (egress fees) is **being removed** under the EU Data Act (provider programmes from 2024; switching-fee prohibition from 2027). **No source-native single-actor control layer is classifiable without S2** → `no_evidenced_control_layer`.

### Not admissible
- ❌ "Cloud is monopolised" / "AWS or Microsoft controls cloud." — concentration and a regulator's competition concern are **not** a documented control layer (S2).
- ❌ Using the CMA's "competition not working well" / AEC / SMS findings as classification evidence.
- ❌ Treating egress fees as a present control layer while they are being regulated away.
- ❌ Any undated claim — the switching landscape is changing (2024 removals; 2027 prohibition).

## 9. Running gate picture (eight of eight — set complete)

- S8 → `legal_exclusivity`
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `capacity_control` + `access_gatekeeping`
- S4 → `access_gatekeeping`
- S5 → `access_gatekeeping`
- S3 → `no_evidenced_control_layer`
- S7 → `no_evidenced_control_layer`

The skeptical case did its job: faced with a concentrated market a regulator itself calls uncompetitive, the framework still returned **no evidenced control layer**, because the regulator's finding is a competition conclusion (S2), the market is contested/dynamic, and the one concrete switching instrument is being regulated away. Two of eight cases return the negative — the framework is not a monopoly-finding machine.

## 10. Next step

The fixed set is complete (8/8). **Do not** jump to a gate verdict from the layer count. Stop at S7 for review, then run a **full-set MON-G1-LI gate evaluation** against the pass condition and falsifier as a whole (reviewer reproducibility, genuine layer diversity, bounded S2, locus usefulness; and the four falsifier conditions), producing the gate closeout.
