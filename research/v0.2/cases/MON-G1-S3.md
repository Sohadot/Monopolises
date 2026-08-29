# MON-G1-S3 — Accelerated-computing ecosystem (NVIDIA CUDA, dated 2025)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S3
**Role in set:** The hardest discipline test. CUDA is universally called a "moat" — so this is where the framework is most tempted to convert a **popularity/leadership** narrative into a documented control layer, and where the held-out `switching_dependency` layer is probed.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `standard_interface_control`, possibly `switching_dependency`
**Extraction order position:** 7 of 8

## 0. Scope

> **The NVIDIA CUDA accelerated-computing software ecosystem — dated 2025** (NVIDIA Form 10-K, FY2025).

CUDA is a global technical platform, so jurisdiction is not load-bearing here (unlike S4/S5); the date is fixed to the FY2025 10-K.

## 0.1 Governing extraction question

> Is there source-native evidence of an ecosystem/interface **lock** — a named dependency required to operate, or a documented switching barrier — or only evidence that CUDA is a **large, popular, proprietary platform** (leadership), which the gate forbids treating as control?

The bar (frozen challenge): "Separate an evidenced interface/ecosystem lock from a general statement of popularity or performance leadership." A large installed base is popularity; it is not, without S2, a control instrument.

## 1. Result (provisional)

```
result = no_evidenced_control_layer
  standard_interface_control = NOT ESTABLISHED (named but not source-natively "required to operate"; control significance rests on undocumented lock-in)
  switching_dependency probe  = NOT TRIGGERED (held-out; no source-native switching-cost instrument)
```

This is a **layer-identifiability** result, **not** a claim that CUDA confers no advantage. It says: from primary evidence, no control layer is establishable **without S2**.

## 2. S0 evidence (NVIDIA's own documents)

**Source:** NVIDIA Corporation, Form 10-K, FY2025.
- **Named platform:** "foundational **CUDA programming model that runs on all NVIDIA GPUs**"; "CUDA parallel programming model" with "hundreds of domain-specific software libraries, SDKs, and APIs."
- **Installed base / popularity:** "There are **over 5.9 million developers** worldwide using CUDA and our other software tools."
- **Ecosystem value (NVIDIA's framing):** "The large and growing number of developers and installed base across our platforms **strengthens our ecosystem and increases the value of our platform to our customers**."

## 3. Testing the candidates (burden of proof is on the positive layer)

### 3a. standard_interface_control — NOT established
- **Frozen definition:** "a standard, protocol, interface, or ecosystem **required to operate**."
- CUDA **is** a named proprietary interface (this part is source-native). But the burden is on the positive layer to show the frozen function **requires** it: **NVIDIA's admitted primary evidence does not establish that the frozen function — GPU compute for AI workloads — requires CUDA.** Establishing that requirement would need additional evidence not in the register. (We do **not** rest the result on an out-of-register claim that alternatives exist; the negative follows from the *absence of a source-native "required to operate" instrument*, not from a counter-fact.)
- Narrowing the locus to "the CUDA ecosystem itself" makes "CUDA is required" **tautological** (to use CUDA software you use CUDA) and empty of control content.
- The meaningful control content people intend — that the ecosystem is **hard to leave** — is a **switching/lock** claim (see 3b), not a "required interface" fact. Absent that, what remains is a named, popular, proprietary platform: **leadership**, which the gate excludes.

### 3b. switching_dependency — held-out probe, NOT triggered
- **Held-out probe:** switching cost / difficulty of migration. `switching_dependency` is **not** one of the six frozen layers; the thesis holds it out, to be added only if a case shows it is genuinely needed *and* distinct. So this is a test of whether the evidence justifies **adding** it — not a test of an existing taxonomy layer.
- NVIDIA's own words document ecosystem **value** ("increases the value of our platform to our customers") — not a **documented switching cost or barrier**. "Increases value" is not "imposes a switching cost"; the first is desirability, the second is lock.
- Widely repeated claims that migrating off CUDA "requires significant cost and code rewriting" are **secondary-source** commentary, not primary evidence, and were not admitted.
- So the `switching_dependency` **probe is NOT TRIGGERED** here: the case does not present a source-native switching-cost instrument that would justify adding the held-out layer. Consistent with the thesis rule, it stays held-out until a case genuinely evidences it.

## 4. Why `no_evidenced_control_layer` (and not the others)

- **Not `standard_interface_control`, and the `switching_dependency` probe is untriggered:** each fails its source-native test (3a, 3b) — the positive instrument each would require is simply absent from the admitted evidence.
- **Not `ambiguous_layer`:** a reviewer might argue for `standard_interface_control` on the strength of CUDA being a named proprietary interface. That is why the alternative is stated openly (§6). But the reason to decline is not that reviewers pick *different* layers — it is that **every** candidate layer's *control* content depends on an **undocumented lock/switching** element, i.e. on S2. When no layer is establishable without S2, the precise result is `no_evidenced_control_layer`.
- **Not "CUDA is irrelevant":** the evidence plainly shows a large, valuable, proprietary ecosystem. The gate result is about whether a **control layer** is *source-natively classifiable*, not about whether CUDA matters.

## 5. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| CUDA is a named NVIDIA programming model | "CUDA programming model that runs on all NVIDIA GPUs" (10-K) | it is a named proprietary platform | that it is therefore a control layer |
| CUDA has a very large developer base | "over 5.9 million developers" (10-K) | popularity / installed base | popularity ⇒ control (forbidden) |
| The ecosystem increases platform value | "strengthens our ecosystem and increases the value of our platform" (10-K) | ecosystem desirability | desirability ⇒ lock-in / switching cost |
| No documented required-interface or switching instrument | none present in primary evidence | ⇒ `no_evidenced_control_layer` | supplying the missing lock by analyst judgment |

## 6. Alternative reading, stated openly

A reviewer could hold that CUDA — a **named proprietary interface** on which a large software ecosystem is written — is enough for a bounded `standard_interface_control`, distinguishing it from the Visa rulebook (S5) precisely because CUDA *is* a named interface, not a generic rule-set. That is a reasonable position. This case declines it because: (1) the admitted primary evidence does not establish that the frozen function requires CUDA (and the ecosystem-level "requirement" is tautological); and (2) the control significance still rests on an **undocumented switching cost** (S2). If a future extraction admits a **primary** source that documents either a hard technical dependency (CUDA-written software cannot run off NVIDIA hardware, stated in NVIDIA's own licensing/docs) **and** a concrete migration barrier, the result could move to `standard_interface_control` and/or trigger `switching_dependency`. On present admitted evidence, it does not.

## 7. Claim boundary

### Admissible record
> For the NVIDIA CUDA accelerated-computing ecosystem (2025), primary evidence (NVIDIA's 10-K) establishes a **named, proprietary, widely-adopted** programming platform with 5.9M+ developers that NVIDIA states strengthens its ecosystem and increases platform value. It does **not** establish a source-native control layer: the admitted evidence does not show that the frozen function (GPU compute for AI workloads) requires CUDA, nor does it document a switching-cost barrier. No control layer is classifiable without S2 → `no_evidenced_control_layer`.

### Not admissible
- ❌ "CUDA is a monopoly / control layer." — converts popularity/ecosystem value into control (S2).
- ❌ "Switching off CUDA is prohibitively costly" as a classification basis — secondary-source, not admitted; a switching-cost instrument must be source-native.
- ❌ Any claim resting on NVIDIA's GPU market share or performance leadership.
- ❌ Any undated claim — the record is dated to the FY2025 10-K.

## 8. Running gate picture (seven of eight)

- S8 → `legal_exclusivity`
- S1 → `capacity_control` (single-actor)
- S2 → `capacity_control` (collective)
- S6 → `capacity_control` + `access_gatekeeping`
- S4 → `access_gatekeeping`
- S5 → `access_gatekeeping`
- S3 → `no_evidenced_control_layer`

The framework **resisted two high-profile overclaims**: it **bounded TSMC to an evidenced collective `capacity_control` layer** (a positive result — it refused only the jump from that layer to "TSMC monopolises advanced chips"), and it **returned no evidenced layer for CUDA on the admitted evidence**. It also refused to relabel qualification (S6) and refused a rulebook-as-interface (S5). Three mechanisms are evidenced (`legal_exclusivity`, `capacity_control`, `access_gatekeeping`); `standard_interface_control`, `switching_dependency`, `qualification_control`, and `temporal_constraint` remain **unproven** — a discriminating instrument, not a monopoly-finding machine. One case remains: S7 (cloud hyperscaler, the deliberate skeptical case).

## 9. Next step

Stop at S3 for review before extracting MON-G1-S7 (cloud hyperscaler dependency — the deliberate skeptical case), the last of the fixed set. Do not batch.
