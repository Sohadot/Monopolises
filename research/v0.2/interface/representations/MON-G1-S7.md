=== SYSTEM READING UNIT ===
SYSTEM_SCOPE: Large-scale general-purpose (IaaS) cloud infrastructure
SYSTEM_DATE: {"as_of": "2025-07-31", "label": "UK CMA cloud services final decision, 31 July 2025"}
OUTCOME: evidenced_control_layer

=== LAYER PANEL ===
LAYER_TYPE: switching_dependency
INSTRUMENT: Egress charges incurred in moving workload data away from an incumbent provider for switching and/or multi-cloud, remaining applicable in 2025 outside bounded, conditional free-switching programme exemptions.
WHERE: Provider-specific data-egress / switching boundary
LAYER_DATE: {"as_of": "2025-07-31", "label": "2025"}
LAYER_JURISDICTION: United Kingdom
BOUNDARY_ADMISSIBLE: For UK large-scale (IaaS) cloud infrastructure in 2025, primary evidence (UK CMA final decision, 31 July 2025) establishes a switching_dependency layer at the provider-specific data-egress boundary: an egress charge is incurred in moving workload data away from an incumbent provider for switching and/or multi-cloud; the providers' free-switching programmes universally cover full exit, but partial switching is provider-specific and restricted and ongoing multi-cloud is not eligible under the standard programmes, so egress charges remained applicable in 2025 outside those bounded, conditional exemptions.
BOUNDARY_EXCLUDED:
- Cloud is monopolised / AWS or Microsoft controls cloud.
- Using the egress cost to assert decisive lock-in, market power, or an anticompetitive effect.
- Using the CMA's competition not working well / AEC / SMS findings as classification evidence.
- Importing the EU Data Act 2027 prohibition as governing the UK 2025 case.
- Any undated claim.
WHO:
- AWS
- Microsoft
- Google
- Civo

=== CLAIM_EVIDENCE_ROW ===
CLAIM: A charge is incurred to transfer data out for switching and/or multi-cloud
EVIDENCE_CLASS: S0
SOURCE: UK CMA, Cloud services market investigation — Summary of Final Decision, 31 July 2025, para 26
FACT: the presence and magnitude of egress fees required to transfer data between cloud providers for the purposes of switching and/or multi-cloud.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Switching friction coexists with multi-cloud
EVIDENCE_CLASS: S0
SOURCE: UK CMA final decision, 31 July 2025, para 24
FACT: Very few customers switch between clouds: less than 1% of customers switch provider each year. Use of multiple cloud providers is more prevalent than switching but it is still uncommon for small and medium sized customers.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Free-switching programmes are bounded; egress remained applicable outside exemptions in 2025
EVIDENCE_CLASS: S0
SOURCE: UK CMA Appendix N — Egress fees: free switching programmes
FACT: Free egress for switching is only available (and subject to requirements and restrictions in some cases) for the customers of AWS, Microsoft, Google and Civo. Ongoing multi-cloud use (non-switching) is Not eligible under standard programmes for AWS and Google; programmes turn on full-exit conditions and provider discretion.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: A switch-linked egress charge is a cost of leaving ⇒ switching_dependency
EVIDENCE_CLASS: S1
SOURCE: Conjunction of CMA final decision / Appendix N S0 facts
FACT: Egress charge incurred specifically in moving data away for switching/multi-cloud; programmes leave charges applicable outside bounded exemptions in 2025.
DERIVATION: A charge incurred specifically in leaving/moving data away from the current provider is mechanically a cost of switching under the frozen switching_dependency definition; no magnitude judgment required.

=== REFUSAL NOTES STRIP ===

=== REFUSAL NOTE ===
CANDIDATE_LABEL: standard_interface_control
STATUS: not_established
REASON: CMA cites differentiation of features and interfaces as a market-wide competition assessment, not a named standard/protocol/interface required to operate held by one actor.
