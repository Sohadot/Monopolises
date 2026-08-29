# MON-G1-S5 — Card-payment acceptance (Visa network, US, dated 2026)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S5
**Role in set:** First real test of `standard_interface_control` (still unproven), inside a two-sided market where it is easy to slide from "a specific controlled interface" to "the whole payments market."
**Status:** Evidence extraction complete — provisional case result (revised after review)
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `standard_interface_control` and/or `access_gatekeeping`
**Extraction order position:** 6 of 8

## 0. Scope (fixed to a specific network, not "payments")

> **Acceptance of transactions on the Visa network, in the United States, dated 2026** (Visa Core Rules and Visa Product and Service Rules, effective 18 April 2026).

Two-sided-market discipline: this case is about the **Visa network specifically**, not "card payments" or "payment acceptance" in general. Merchants can also accept Mastercard, American Express, Discover, cash, ACH, etc. Mastercard and the others each run their own rules and would be **separate** instances of the same layer type on their own networks — **not** classified here.

## 0.1 Correction notice (this revision)

The first version classified **two** layers — `access_gatekeeping` **and** `standard_interface_control` — reading the mandatory Visa Rules as the "interface." Review rejected the second: a rulebook that participants must obey is **mandatory governance**, not a **named standard/protocol/interface**. Converting "mandatory rules to operate ⇒ standard_interface_control" would let almost any network, franchise, or contractual platform carry that layer merely for having a rulebook — exactly what the gate forbids ("cite the instrument that creates the layer"). This revision keeps only `access_gatekeeping`, records `standard_interface_control` as **not established**, and does not rescue it by relabeling.

## 0.2 Governing extraction question

> Does a network-native rule establish a specific controlled admission point that participants must pass through to operate on this network, or are we merely observing that Visa is a large payments company?

The bar: classification rests on Visa's **own binding rules**, not on Visa's size, transaction share, or any antitrust conclusion (those are S2).

## 1. Result (provisional, revised)

```
result = evidenced_control_layer
  layer  = access_gatekeeping
  locus  = admission to direct Visa-network participation and to sponsored acceptance access (US, 2026)

  standard_interface_control = NOT ESTABLISHED on current evidence
```

## 2. S0 evidence (Visa's own rules, 18 April 2026 edition)

**Source throughout:** *Visa Core Rules and Visa Product and Service Rules*, 18 April 2026.

### E01 — Restricted access to Visa systems
§1.1.1.6 "Restricted Use of Visa Systems and Services", verbatim: "Any entity that accesses or uses a Visa system and/or service must both: **Restrict its use of the Visa system and/or service to purposes expressly approved by Visa**; Comply with Visa requirements and documentation for system and/or service access and use."
**Class:** S0. Access to Visa systems is limited to Visa-approved use.

### E02 — Licensing controls who may participate directly
§1.2.1 "Licensing – General Membership" / §2.2 (BIN and Acquiring Identifier License): direct participation requires a Visa-issued **BIN or Acquiring Identifier license**; "A BIN or an Acquiring Identifier may have only one … Licensee," and a Principal-Type Member is responsible and liable for all activity under any BIN/Acquiring Identifier it licenses.
**Class:** S0. Direct network participation requires a Visa license — Visa controls that admission.

### E03 — Merchant access is admitted through the acquiring chain, not direct membership
Introduction (rule-reading convention), verbatim: "'A Merchant must…' means 'An **Acquirer must ensure that its Merchant**…'." Merchant-obligation clause: a Merchant must "Comply with the Visa Rules regarding … Visa acceptance … Transaction processing."
**Class:** S0. Merchants are **not** direct Visa licensees; they gain acceptance access **through** a licensed acquirer, which is contractually responsible for the merchant's compliance. Admission to acceptance therefore runs through the licensed acquiring relationship.

## 3. Layer classification — access_gatekeeping (evidenced)

- **Frozen definition:** "a documented rule or control governing admission to a market, platform, or channel."
- **Instrument (S0):** §1.1.1.6 restricted, Visa-approved use (E01) + Visa licensing of BIN/Acquiring Identifiers for direct participants (E02) + admission of merchants to acceptance through a licensed acquiring relationship (E03).
- **Two admission points, one layer:**
  1. **Direct participation** — a Member must hold a Visa license (BIN/Acquiring Identifier); Visa admits directly.
  2. **Sponsored acceptance** — a merchant is admitted to acceptance **via** a licensed acquirer that Visa holds responsible; Visa admits indirectly, through the acquiring chain.
- **Derivation:** in both paths, reaching the network is governed by Visa's admission rules ⇒ Visa controls admission ⇒ `access_gatekeeping`. **S1**, no S2.

The refinement matters: it would be wrong to say "every entity must be Visa-licensed" — a corner store is not a Visa licensee. The accurate mechanism is that **direct** participants are licensed and **merchants** are admitted through a licensed acquiring relationship. The layer holds on the actual acceptance chain, not on a fiction of universal direct membership.

## 4. standard_interface_control — NOT ESTABLISHED

The mandatory Visa Rules govern acceptance and transaction processing, and reach merchants contractually through the acquiring chain — but that is **binding governance**, not a **named standard, protocol, interface, or ecosystem dependency required to operate**, which the frozen definition requires. No such named technical instrument was cited from Visa's own rules for **general US acceptance**.

A quick check of the 18 April 2026 rules for a named-interface mandate found only **region- and product-specific** processing requirements — e.g. "All Visa Mobile Prepaid Transactions completed on a BIN **must be processed through VisaNet**" applies to the **LAC/AP/CEMEA** regions and a specific product, not to general US acceptance; and a VisaNet/VROL requirement appears only in the **dispute-processing** context. None is a US-scoped, general "you must operate through named interface X" instrument. So the layer is **not established here**. It is **not rescued** by relabeling the rulebook as an interface, and it remains available to a future case that presents a genuine named-standard instrument (e.g. a mandated messaging protocol or technical acceptance standard).

## 5. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Access to Visa systems is Visa-approved only | §1.1.1.6 "expressly approved by Visa" | Visa controls system access ⇒ `access_gatekeeping` | whether that admission is anticompetitive |
| Direct participation requires a Visa license | §1.2.1/§2.2 BIN/Acquiring Identifier license | licensed-only direct participation ⇒ admission control | Visa's network share / dominance |
| Merchants are admitted via the acquiring chain | "An Acquirer must ensure that its Merchant…" | the rule-set reaches merchants contractually through the acquiring chain; admission runs through a licensed acquirer | treating merchants as direct members |
| Mandatory rules ≠ a named interface | rules govern acceptance/processing, but no named standard/protocol is mandated for general US acceptance | `standard_interface_control` **not** derivable | relabeling the rulebook as an "interface" |

## 6. What is deliberately excluded (S2)

- The **DOJ suit** *United States v. Visa Inc.* (filed Sept 2024) alleges Visa **monopolized** U.S. debit network services — a market-power/antitrust conclusion, the S2 the gate forbids for classification. Noted as context only; the layer above rests on Visa's own binding rules, **not** the DOJ theory or Visa's transaction share.
- Whether Visa's rules are exclusionary, whether alternatives are viable, and Visa's market position — all S2.

## 7. Claim boundary

### Admissible record
> For acceptance of transactions **on the Visa network** in the **United States** in **2026**, the Visa Core Rules establish an `access_gatekeeping` layer held by the network operator: access to Visa systems is limited to Visa-approved use; **direct** participation requires a Visa-issued license (BIN/Acquiring Identifier); and **merchants** are admitted to acceptance through a licensed acquiring relationship that Visa holds responsible for their compliance.

### Not admissible
- ❌ "Visa monopolises payments" / "Visa controls card acceptance." — this is **per-network**; merchants accept other networks and non-card methods. Any whole-market claim is S2.
- ❌ "Every entity must be Visa-licensed." — merchants are admitted through acquirers, not as direct licensees.
- ❌ Classifying `standard_interface_control` from the mandatory rulebook — not established; needs a named standard/protocol/interface instrument.
- ❌ Using the DOJ monopolization allegation, or Visa's transaction share, as classification evidence.
- ❌ Extending the layer to Mastercard/Amex/Discover — each is a separate, un-classified instance on its own network.
- ❌ Any undated claim — the rules edition is 18 April 2026.

## 8. Running gate picture (six of eight)

- S8 → `legal_exclusivity`
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `capacity_control` + `access_gatekeeping`
- S4 → `access_gatekeeping` (general-public native iOS distribution, US)
- S5 → `access_gatekeeping` (Visa-network acceptance admission, US)

Three distinct mechanisms evidenced across six cases (`legal_exclusivity`, `capacity_control`, `access_gatekeeping`). That S5 resolved to **one** layer — with `standard_interface_control` refused for lack of a named instrument — is itself a result: the framework does not multiply layers just because a single document has many clauses. `standard_interface_control`, `qualification_control`, and `temporal_constraint` remain unproven. The gate verdict waits on the full fixed set.

## 9. Next step

Stop at S5 for review before extracting MON-G1-S3 (accelerated-computing ecosystem), per the frozen order. Do not batch.
