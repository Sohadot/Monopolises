# Layer Identifiability Gate — Monopolises v0.2

**Gate ID:** MON-G1-LI
**Version:** 0.2
**Status:** DESIGN FROZEN — evidence extraction not started
**Opened:** 2026-08-28
**Thesis under test:** `THESIS_CANDIDATE.md` (Layered Monopolisation v0.2)
**Predecessor gate:** MON-G0-RH — Closed FAIL (`../GATE_0.md`, `../GATE_0_CLOSEOUT.md`)

> This gate tests whether the v0.2 thesis is buildable at all. It is deliberately smaller and harder than Gate 0. Nothing here authorizes the site, an ontology, a score, or DEC-005. Only a PASS on the fixed case set below does.

## Governing question

> Can the **locus and mechanism** of concentrated control inside a complex system be classified **reproducibly** from **public primary evidence**, **without inferring legal monopoly status**?

Note what the question is not: it is not "how concentrated is the market," not "who is dominant," and not "how long does replacement take." It is a question about whether a **reproducible classification** of *where* and *by what mechanism* control sits can be built from primary sources.

## Unit of record

```
System × Layer × Control Mechanism × Evidence
```

Never `Company × Monopoly Score`. A system may yield multiple layered records, one, or none.

## Evidence classes (carried over from Gate 0)

- **S0 — Source-native.** The primary source explicitly states the fact establishing the layer and mechanism (an exclusive right, a required certification/approval, a mandatory standard, a controlled facility/capacity, an access rule).
- **S1 — Mechanical derivation.** A reproducible, non-interpretive derivation from S0 facts.
- **S2 — Interpretive synthesis.** A domain judgment is required to decide whether control is present, durable, or decisive.

S2 may be recorded to explain uncertainty. **S2 cannot establish a layer classification.** A layer that exists only under S2 is not an evidenced layer.

## Allowed outcomes per case

Each case must resolve to exactly one of:

- `evidenced_control_layer` — a layer and mechanism are established from S0/S1 primary evidence, with a reconstructable claim boundary.
- `multiple_evidenced_layers` — more than one distinct, separately-evidenced layer is present.
- `ambiguous_layer` — evidence exists but two reasonable reviewers could source-defensibly assign different layers; no source-native rule separates them.
- `no_evidenced_control_layer` — **a first-class, valid, expected-in-some-cases result.** Concentration may be visible in commentary, but no layer/mechanism is establishable from primary evidence without S2.

A gate that cannot produce `no_evidenced_control_layer` on any case is proving only that it was designed to find monopoly everywhere.

## Layer classification rule

A layer is assigned only when a primary source names the concrete control instrument:

- `legal_exclusivity` — a statute, license, patent grant, or franchise conferring an exclusive right.
- `access_gatekeeping` — a documented rule or control governing admission to a market, platform, or channel.
- `capacity_control` — a documented facility, node, or capacity that the function must pass through and that is hard to bypass.
- `qualification_control` — a documented certification/approval/qualification an alternative must hold and does not.
- `standard_interface_control` — a documented standard, protocol, interface, or ecosystem dependency required to operate.
- `temporal_constraint` — documented evidence that an alternative cannot arrive within a required time. (This is the *only* place a Replacement-Horizon-style signal may appear, and only as a bounded, source-native fact.)

If the assignment requires the reviewer to *argue* that control exists rather than *cite* the instrument that creates it, the correct result is `ambiguous_layer` or `no_evidenced_control_layer`, never a forced layer.

## Falsifier

The gate FAILS if any of the following hold across the fixed set:

1. Layer assignment **predominantly depends on S2** interpretation rather than source-native control instruments.
2. Two reasonable reviewers can classify the **same evidence into different layers** without a source-native rule that separates them (pervasive `ambiguous_layer`).
3. The layers turn out to be **different names for the same "market concentration"** finding rather than genuinely distinct mechanisms of control.
4. The framework **cannot return `no_evidenced_control_layer`** where primary evidence is genuinely absent — i.e. it finds a layer everywhere.

## Pass condition

The gate PASSES only if **all** of the following hold:

1. **Reviewer reproducibility.** An independent reviewer reaches the **same layer + mechanism** from the **same cited primary evidence** in a clear majority of the fixed cases, with reconstructable claim boundaries.
2. **Genuine layer diversity.** Several **materially different** control mechanisms appear across the set — not one mechanism relabeled.
3. **Bounded S2.** S2 is confined to explaining uncertainty; it does not carry any layer classification.
4. **Locus usefulness.** The resulting layer tells a reader **specifically where** control sits inside the system, not merely that the market is "concentrated."

## Fixed case set (frozen before evidence extraction)

Eight systems are fixed. They are deliberately heterogeneous, and the **pre-registered layer hypothesis is a hypothesis to be tested, not asserted** — each case may resolve to a different layer, to `ambiguous_layer`, or to `no_evidenced_control_layer`. No case may be swapped out because its evidence proves inconvenient.

### MON-G1-S1 — EUV lithography
- **System / critical function:** Leading-edge chip patterning at EUV nodes.
- **Layer hypothesis to test:** `capacity_control` (single-source production of EUV scanners).
- **Candidate primary-source pathway:** ASML annual report / regulatory filings; export-control and government supply-chain reports.
- **Evidentiary challenge:** Distinguish an evidenced production chokepoint from a mere "high market share" statement.

### MON-G1-S2 — Leading-edge foundry fabrication
- **System / critical function:** High-volume manufacturing at the leading logic node.
- **Layer hypothesis to test:** `capacity_control` (leading-edge fab capacity).
- **Candidate primary-source pathway:** Foundry annual reports; U.S. Commerce/CHIPS and comparable government supply-chain assessments.
- **Evidentiary challenge:** The frontier moves; "leading-edge" at one date differs from another. Must source the concrete capacity, not a reputation.

### MON-G1-S3 — Accelerated-computing software ecosystem
- **System / critical function:** GPU compute for AI workloads via a dominant programming ecosystem.
- **Layer hypothesis to test:** `standard_interface_control` (ecosystem/interface dependency), possibly with `switching_dependency` — a probe for whether the held-out layer is actually needed.
- **Candidate primary-source pathway:** Vendor developer documentation and 10-K risk disclosures; competition-authority market studies that quote primary evidence.
- **Evidentiary challenge:** Separate an evidenced interface/ecosystem lock from a general statement of popularity or performance leadership.

### MON-G1-S4 — Native app distribution on a mobile OS
- **System / critical function:** Distributing software to users of a closed mobile platform.
- **Layer hypothesis to test:** `access_gatekeeping` (single sanctioned distribution channel).
- **Candidate primary-source pathway:** Platform developer policy documents; court findings and regulatory decisions that reproduce primary platform rules.
- **Evidentiary challenge:** Use the platform's own documented access rule as the instrument; avoid importing a legal conclusion as if it were the mechanism.

### MON-G1-S5 — Card-payment acceptance infrastructure
- **System / critical function:** Routing consumer card payments through acceptance networks.
- **Layer hypothesis to test:** `standard_interface_control` or `access_gatekeeping` (network rules / acceptance rails).
- **Candidate primary-source pathway:** Network operating-rule disclosures; central-bank / competition-authority payment-system reports quoting primary rules.
- **Evidentiary challenge:** Two-sided-market complexity; must locate the specific controlled interface, not describe the whole payments market.

### MON-G1-S6 — Rare-earth permanent magnets (NdFeB)
- **System / critical function:** High-performance permanent magnets and their upstream processing.
- **Layer hypothesis to test:** `qualification_control` and/or `capacity_control` (processing capacity; qualified alternative supply).
- **Candidate primary-source pathway:** Government supply-chain and defense-industrial reports; company statutory disclosures.
- **Evidentiary challenge:** A new facility can reduce dependence without being a control layer; sufficiency and qualification must be source-native (carries the Gate 0 lesson).

### MON-G1-S7 — Cloud hyperscaler dependency
- **System / critical function:** Large-scale general-purpose cloud infrastructure.
- **Layer hypothesis to test:** **Deliberate skeptical case.** Several viable hyperscalers exist, so `no_evidenced_control_layer` is a live and plausible outcome; if any layer is evidenced it is more likely `switching_dependency`/`standard_interface_control` at a specific service, not the market as a whole.
- **Candidate primary-source pathway:** Provider documentation on egress/lock-in; competition-authority cloud market studies quoting primary evidence.
- **Evidentiary challenge:** Resist labeling a large-but-contested market as a control layer; this case is the guard against confirmation bias.

### MON-G1-S8 — A legally granted exclusivity
- **System / critical function:** A function served under an explicit statutory/licensed exclusivity (e.g. a regulated utility franchise or a patent-backed exclusive right).
- **Layer hypothesis to test:** `legal_exclusivity` (the clean positive control — the mechanism is written into law).
- **Candidate primary-source pathway:** The enabling statute, license, franchise agreement, or patent grant itself.
- **Evidentiary challenge:** This case tests the *easy* end: if even an explicit legal exclusivity cannot be classified cleanly and reproducibly, the framework is not usable. The specific instance is fixed during extraction from a primary legal instrument.

## Freeze rules

1. These eight systems are fixed for MON-G1-LI v0.2.
2. No case may be removed because it yields `no_evidenced_control_layer` or `ambiguous_layer`.
3. No ninth case may be added to rescue a weak result.
4. Formal source admission begins only when evidence extraction starts for a case.
5. S0 and reproducible S1 may establish a layer; S2 may not.
6. The gate closes on the performance of this fixed set, not on selected successful examples.
7. The pre-registered layer hypothesis is a prediction under test, not a result.

## Extraction order (fixed for auditability; not a priority ranking)

1. MON-G1-S8 — legal exclusivity (positive control)
2. MON-G1-S1 — EUV lithography
3. MON-G1-S2 — leading-edge foundry
4. MON-G1-S6 — rare-earth magnets
5. MON-G1-S4 — mobile app distribution
6. MON-G1-S5 — card-payment acceptance
7. MON-G1-S3 — accelerated-computing ecosystem
8. MON-G1-S7 — cloud hyperscaler (skeptical case)

## What a PASS authorizes — and only then

A PASS authorizes recording **DEC-005 — Open Layered Monopolisation as the Monopolises v0.2 thesis**, and after that, in order: a layer ontology, an interface thesis, and a data architecture. It does **not** authorize any of those before the decision is recorded. A FAIL is recorded like Gate 0 — honestly, without a rescue case — and the site remains untouched.
