=== SYSTEM READING UNIT ===
SYSTEM_SCOPE: Acceptance of transactions on the Visa network in the United States
SYSTEM_DATE: {"as_of": "2026-04-18", "label": "Visa Core Rules effective 18 April 2026"}
OUTCOME: evidenced_control_layer

=== LAYER PANEL ===
LAYER_TYPE: access_gatekeeping
INSTRUMENT: Visa controls admission to the Visa network: access to Visa systems is limited to Visa-approved use; direct participation requires a Visa-issued BIN or Acquiring Identifier license; and merchants are admitted to acceptance through a licensed acquiring relationship that Visa holds responsible for their compliance.
WHERE: Visa-network admission — direct participation and sponsored acceptance access
LAYER_DATE: {"as_of": "2026-04-18"}
LAYER_JURISDICTION: United States
BOUNDARY_ADMISSIBLE: For acceptance of transactions on the Visa network in the United States in 2026, the Visa Core Rules establish an access_gatekeeping layer held by the network operator: access to Visa systems is limited to Visa-approved use; direct participation requires a Visa-issued license (BIN/Acquiring Identifier); and merchants are admitted to acceptance through a licensed acquiring relationship that Visa holds responsible for their compliance.
BOUNDARY_EXCLUDED:
- Visa monopolises payments / Visa controls card acceptance.
- Every entity must be Visa-licensed.
- Classifying standard_interface_control from the mandatory rulebook.
- Using the DOJ monopolization allegation or Visa's transaction share as classification evidence.
- Extending the layer to Mastercard/Amex/Discover.
- Any undated claim.
WHO:
- Visa

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Access to Visa systems is limited to Visa-approved use
EVIDENCE_CLASS: S0
SOURCE: Visa Core Rules and Visa Product and Service Rules, 18 April 2026, §1.1.1.6
FACT: Any entity that accesses or uses a Visa system and/or service must both: Restrict its use of the Visa system and/or service to purposes expressly approved by Visa; Comply with Visa requirements and documentation for system and/or service access and use.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Direct participation requires a Visa-issued license
EVIDENCE_CLASS: S0
SOURCE: Visa Core Rules, 18 April 2026, §1.2.1 / §2.2 (BIN and Acquiring Identifier License)
FACT: Direct participation requires a Visa-issued BIN or Acquiring Identifier license; a BIN or an Acquiring Identifier may have only one Licensee; a Principal-Type Member is responsible and liable for all activity under any BIN/Acquiring Identifier it licenses.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Merchants are admitted to acceptance through a licensed acquiring relationship
EVIDENCE_CLASS: S0
SOURCE: Visa Core Rules, 18 April 2026, Introduction (rule-reading convention) and merchant-obligation clause
FACT: 'A Merchant must…' means 'An Acquirer must ensure that its Merchant…'. A Merchant must Comply with the Visa Rules regarding Visa acceptance and Transaction processing.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Visa's admission rules govern reaching the network on both paths
EVIDENCE_CLASS: S1
SOURCE: Conjunction of Visa Core Rules S0 facts (§1.1.1.6, §1.2.1/§2.2, acquiring-chain convention)
FACT: Restricted Visa-approved system use + licensed direct participation + merchant admission via licensed acquirer.
DERIVATION: In both paths, reaching the network is governed by Visa's admission rules under frozen access_gatekeeping; no S2.

=== REFUSAL NOTES STRIP ===

=== REFUSAL NOTE ===
CANDIDATE_LABEL: standard_interface_control
STATUS: not_established
REASON: Mandatory Visa Rules are binding governance, not a named standard/protocol/interface required to operate for general US acceptance. No such named technical instrument was cited from Visa's own rules for general US acceptance.
