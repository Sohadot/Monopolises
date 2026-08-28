# MON-G1-S8 — U.S. Private Express Statutes (legal-exclusivity positive control)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S8
**Role in set:** Positive control — the easy end. The control instrument is written into statute, so no market-share or market-analysis inference is required.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Extraction order position:** 1 of 8 (extracted first by design)

## 1. Fixed specific instance

> U.S. Private Express Statutes — restriction on compensated private carriage of **letters** over **post routes**.

This instance was chosen for the positive control because the control instrument is a statute, not an inference. If even an explicit legal exclusivity cannot be classified cleanly and reproducibly, the v0.2 framework is not usable.

## 2. System / critical function

Carriage of defined **letters** over U.S. **post routes** — a bounded slice of the broader communications/logistics system, not "mail delivery" in general and not parcels, freight, or electronic communication.

## 3. Layer classification (provisional)

```
result = evidenced_control_layer
layer  = legal_exclusivity
```

### Control mechanism

> Statutory restriction on compensated private carriage of letters over post routes, with legislatively and regulatorily defined exceptions and suspensions.

Reached from source-native statutory text. **No S2 judgment is required** to assign the layer: the exclusive right and its restriction are enacted, not inferred.

## 4. S0 evidence

### E01 — Statutory prohibition on private carriage
**Publisher:** United States Code (federal statute)
**Source:** 18 U.S.C. § 1696 — *Private express for letters and packets*
**Supported facts:**
- Federal law establishes penalties for establishing a private express for the conveyance of letters or packets, or in any manner causing or providing for their regular conveyance, over post routes.
- The prohibition is subject to enumerated statutory exceptions.

**Evidence class:** S0
**Use:** Establishes the restriction (the control instrument itself), not any claim about market outcomes.

### E02 — Conditions for lawful private carriage / restriction on taking letters out of the mail
**Publisher:** United States Code (federal statute)
**Source:** 39 U.S.C. § 601 — *Letters carried out of the mail*
**Supported facts:**
- Defines the conditions under which a letter may lawfully be carried out of the mail (including specified price/weight and other regulatory conditions and exceptions).

**Evidence class:** S0
**Use:** Establishes that the exclusivity is bounded and conditional — it is not a total prohibition on all private letter carriage.

### E03 — Implementing regulations / enforcement
**Publisher:** Code of Federal Regulations
**Source:** 39 CFR Part 310 — *Enforcement of the Private Express Statutes*
**Supported facts:**
- A dedicated federal regulatory part exists specifically to enforce and define the operation of the Private Express Statutes, including exceptions and suspensions.

**Evidence class:** S0
**Use:** Confirms the mechanism is an operative, enforced legal regime with defined boundaries, not merely a dormant statute.

### E04 — Operator's own summary of the mechanism
**Publisher:** U.S. Postal Service
**Source:** USPS description of the Private Express Statutes
**Supported facts:**
- USPS summarizes that the statutes make it generally unlawful for an entity other than the Postal Service to carry letters over post routes, except under the defined conditions, exceptions, and suspensions.

**Evidence class:** S0 (operator statement of the legal regime; corroborative, not the primary instrument)
**Use:** Plain-language corroboration of E01–E03. Not relied on where it would exceed the statutory text.

## 5. Claim boundary

### Admissible record
> Within the U.S. letter-carriage system, federal law creates a **legal-exclusivity layer** by restricting private carriage of defined **letters** over **post routes**, subject to enumerated exceptions and suspensions.

### Not admissible (exceeds the evidence)
- ❌ "USPS monopolises delivery." — broader than the evidence; delivery ≠ letters over post routes.
- ❌ "USPS has a legal monopoly over all mail." — the statutes contain exceptions and do not cover all shipping or communication.
- ❌ Any claim extending the layer to parcels, freight, or electronic communication.

The v0.2 boundary rule holds: the record states **where** (letters over post routes), **which mechanism** (statutory restriction on private carriage), and **on what evidence** (the statutes and implementing regulations) — and refuses the broader "monopoly" framing the evidence does not support.

## 6. v0.2 record elements

| Element | Value |
|---|---|
| **System** | U.S. carriage of defined letters over post routes |
| **Layer** | `legal_exclusivity` |
| **Control Mechanism** | Statutory restriction on compensated private carriage, with defined exceptions/suspensions |
| **Evidence** | 18 U.S.C. § 1696 + 39 U.S.C. § 601 + 39 CFR Part 310 (USPS summary corroborative) |

## 7. S2 note

None required for classification. The layer is assigned from source-native statutory text. Any discussion of how *economically significant* the exclusivity is would be S2 and is deliberately excluded from the classification.

## 8. Result and scope of the result

- **Case result:** `evidenced_control_layer` / `legal_exclusivity`, with a reconstructable claim boundary, from S0 evidence, no S2 needed.
- **Scope:** S8 succeeds **as the positive control**. This does **not** mean MON-G1-LI passes. S8 is the intentionally easy end. The gate's real test is whether EUV, leading-edge foundry, the accelerated-computing ecosystem, app distribution, and card-payment acceptance can be classified with the same source-native discipline — where no document simply writes "this is an exclusive right."

## 9. Next step

Stop at S8 for review before extracting MON-G1-S1 (EUV lithography), per the frozen extraction order. Do not batch the remaining seven cases; single-case checkpoints preserve auditability.
