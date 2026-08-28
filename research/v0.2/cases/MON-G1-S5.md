# MON-G1-S5 — Card-payment acceptance (Visa network, US, dated 2026)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S5
**Role in set:** First real test of `standard_interface_control` (still unproven), inside a two-sided market where it is easy to slide from "a specific controlled interface" to "the whole payments market."
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `standard_interface_control` and/or `access_gatekeeping`
**Extraction order position:** 6 of 8

## 0. Scope (fixed to a specific network, not "payments")

> **Acceptance of transactions on the Visa network, in the United States, dated 2026** (Visa Core Rules and Visa Product and Service Rules, effective 18 April 2026).

Two-sided-market discipline: this case is about the **Visa network specifically**, not "card payments" or "payment acceptance" in general. Merchants can also accept Mastercard, American Express, Discover, cash, ACH, etc. Mastercard and the others each run their own rules and would be **separate** instances of the same layer type on their own networks — **not** classified here.

## 0.1 Governing extraction question

> Does a network-native rule establish a specific controlled interface/admission point that participants must pass through to operate on this network, or are we merely observing that Visa is a large payments company?

The bar: classification must rest on Visa's **own binding rules**, not on Visa's size, transaction share, or any antitrust conclusion (those are S2).

## 1. Result (provisional)

```
result = multiple_evidenced_layers
  Layer A: access_gatekeeping         — restricted, Visa-approved access to Visa systems + licensing
  Layer B: standard_interface_control — mandatory compliance with the Visa Rules governing acceptance/processing
```

Both hold at one locus — **participation in the Visa network for card acceptance (US, 2026)** — but rest on **distinct instruments** (who may access vs. what rules all participants must follow). They are separated below so this is not one fact counted twice.

## 2. S0 evidence (Visa's own rules, 18 April 2026 edition)

**Source throughout:** *Visa Core Rules and Visa Product and Service Rules*, 18 April 2026.

### E01 — Restricted access to Visa systems (Layer A)
§1.1.1.6 "Restricted Use of Visa Systems and Services", verbatim: "Any entity that accesses or uses a Visa system and/or service must both: **Restrict its use of the Visa system and/or service to purposes expressly approved by Visa**; Comply with Visa requirements and documentation for system and/or service access and use."
**Class:** S0. Access to Visa systems is limited to Visa-approved use.

### E02 — Licensing controls who may participate (Layer A)
§1.2.1 "Licensing – General Membership" / §2.2 (BIN and Acquiring Identifier License): participation requires a Visa-issued **BIN or Acquiring Identifier license**; "A BIN or an Acquiring Identifier may have only one … Licensee," and a Principal-Type Member is responsible and liable for all activity under any BIN/Acquiring Identifier it licenses.
**Class:** S0. To acquire/process on the network an entity must hold (or be sponsored under) a Visa license — Visa controls admission.

### E03 — Mandatory compliance with the Visa Rules governing acceptance/processing (Layer B)
Core-Rules general provision (Merchant obligations), verbatim: participants must "**Comply with the Visa Rules regarding use of the Visa-Owned Marks, Visa acceptance, risk management, Transaction processing**, and any Visa Products, programs, or services in which the Merchant is required to, or chooses to, participate."
**Class:** S0. The Visa Rules are the mandatory rule-set/interface governing acceptance and transaction processing on the network.

### E04 — The rules bind the whole acceptance chain, via the acquirer
Introduction (rule-reading convention), verbatim: "'A Merchant must…' means 'An **Acquirer must ensure that its Merchant**…'."
**Class:** S0. Merchant-level obligations are enforced through the acquirer, so the rule-set reaches every participant in acceptance, not just direct members.

## 3. Layer classification

### Layer A — access_gatekeeping
- **Frozen definition:** "a documented rule or control governing admission to a market, platform, or channel."
- **Instrument (S0):** §1.1.1.6 restricted, Visa-approved use (E01) + Visa licensing of BIN/Acquiring Identifiers (E02).
- **Derivation:** to reach the network at all, an entity must be Visa-approved/licensed ⇒ Visa controls **admission** to the network. **S1**, no S2.

### Layer B — standard_interface_control
- **Frozen definition:** "a standard, protocol, interface, or ecosystem required to operate."
- **Instrument (S0):** mandatory compliance with the Visa Rules governing Visa acceptance and Transaction processing (E03), binding on the whole chain via acquirers (E04).
- **Derivation:** to operate on the network, every participant must follow Visa's rule-set/interface, which Visa sets ⇒ Visa controls the **required interface**. **S1**, no S2.

### Why these are two layers, not one
E01/E02 answer **who may connect** (admission). E03/E04 answer **what rules govern operating once connected** (interface). A network could in principle gate access without a rich mandatory rule-set, or publish an open interface with light admission — here Visa does both, on separate clauses. Counting them as one would hide a real distinction (the same split we drew in S6 between admission and the underlying instrument).

## 4. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Access to Visa systems is Visa-approved only | §1.1.1.6 "expressly approved by Visa" | Visa controls admission ⇒ `access_gatekeeping` | whether that admission is anticompetitive |
| Participation requires a Visa license | §1.2.1/§2.2 BIN/Acquiring Identifier license | licensed-only participation ⇒ `access_gatekeeping` | Visa's network share / dominance |
| Operating requires compliance with the Visa Rules | Merchant-obligation clause; rules govern acceptance/processing | mandatory required interface ⇒ `standard_interface_control` | whether the rules are exclusionary (the DOJ theory) |
| The rules reach every participant | "An Acquirer must ensure that its Merchant…" | interface binds the whole chain | — |

## 5. What is deliberately excluded (S2)

- The **DOJ suit** *United States v. Visa Inc.* (filed Sept 2024) alleges Visa **monopolized** U.S. debit network services. That is a **market-power/antitrust conclusion** — exactly the S2 the gate forbids for classification. It is noted as context only; the layers above rest on Visa's own binding rules, **not** on the DOJ theory or on Visa's transaction share.
- Whether Visa's rules are exclusionary, whether alternatives are viable, and Visa's market position — all S2.

## 6. Claim boundary

### Admissible record
> For acceptance of transactions **on the Visa network** in the **United States** in **2026**, the Visa Core Rules establish two control layers held by the network operator: (A) an `access_gatekeeping` layer — access to Visa systems is limited to Visa-approved use and participation requires a Visa-issued license (BIN/Acquiring Identifier); and (B) a `standard_interface_control` layer — every participant, down to merchants via their acquirers, must comply with the Visa Rules governing Visa acceptance and transaction processing.

### Not admissible
- ❌ "Visa monopolises payments" / "Visa controls card acceptance." — this is **per-network**; merchants accept other networks and non-card methods. Any whole-market claim is S2.
- ❌ Using the DOJ monopolization allegation as classification evidence.
- ❌ Any claim resting on Visa's transaction share or size.
- ❌ Extending the layer to Mastercard/Amex/Discover — each is a separate, un-classified instance on its own network.
- ❌ Any undated claim — the rules edition is 18 April 2026.

## 7. Running gate picture (six of eight)

- S8 → `legal_exclusivity`
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `capacity_control` + `access_gatekeeping`
- S4 → `access_gatekeeping` (general-public native iOS distribution, US)
- S5 → `access_gatekeeping` + `standard_interface_control` (Visa network acceptance, US)

Four distinct mechanisms now evidenced across six cases (`legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `standard_interface_control`). `standard_interface_control` is newly proven here — and, as with the app-distribution case, the discipline was to bound it to a **specific network** rather than let it swallow "payments." `qualification_control` and `temporal_constraint` remain unproven. The gate verdict waits on the full fixed set.

## 8. Next step

Stop at S5 for review before extracting MON-G1-S3 (accelerated-computing ecosystem), per the frozen order. Do not batch.
