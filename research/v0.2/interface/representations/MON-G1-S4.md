=== SYSTEM READING UNIT ===
SYSTEM_SCOPE: General-public native iOS app distribution to users in the United States
SYSTEM_DATE: {"as_of": "2026-08-28", "label": "2026 — App Review Guidelines (Last Updated June 8, 2026) and Apple Support retrieved 2026-08-28"}
OUTCOME: evidenced_control_layer

=== LAYER PANEL ===
LAYER_TYPE: access_gatekeeping
INSTRUMENT: Apple's App Review Guidelines require general-public native iOS apps to reach users through the App Store, where Apple reviews and approves/rejects every app distributed through the App Store; and within the US scope no alternative marketplace or web-distribution route is available (only Brazil, Japan, and the EU can install apps through alternative distribution). Apple therefore controls admission to the sole sanctioned channel for general-public native iOS apps to US users.
WHERE: General-public App Store channel for native iOS app distribution to US users
LAYER_DATE: {"as_of": "2026-08-28", "label": "2026"}
LAYER_JURISDICTION: United States
BOUNDARY_ADMISSIBLE: For general-public native iOS app distribution to users in the United States in 2026, Apple's App Review Guidelines and support documentation establish an access_gatekeeping layer: every app distributed through the App Store is reviewed and approved/rejected by Apple, and the App Store is the sole Apple-sanctioned channel for reaching US users, since Only users based in Brazil, Japan, or the European Union are able to install apps through alternative app distribution — subject to narrow enterprise/custom/TestFlight exceptions and the separate non-native web route.
BOUNDARY_EXCLUDED:
- Apple monopolises apps.
- Extending the layer to iOS globally.
- Any claim resting on App Store market share or iOS install base.
- Reading US anti-steering/payment-link changes as opening the distribution channel.
- Any undated claim.
WHO:
- Apple

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Apple reviews every app distributed through the App Store
EVIDENCE_CLASS: S0
SOURCE: Apple, App Review Guidelines (Last Updated June 8, 2026), Introduction
FACT: We do this by offering a highly curated App Store where every app is reviewed by experts.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: Alternative native distribution is limited to some markets
EVIDENCE_CLASS: S0
SOURCE: Apple, App Review Guidelines (2026), Introduction
FACT: In some markets and on certain platforms, developers can also distribute notarized apps from alternative app marketplaces and directly from their website.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: US users cannot use alternative app distribution (exhaustive boundary)
EVIDENCE_CLASS: S0
SOURCE: Apple Support, Installing apps through alternative app distribution (support.apple.com/en-us/117767)
FACT: Only users based in Brazil, Japan, or the European Union are able to install apps through alternative app distribution.

=== CLAIM_EVIDENCE_ROW ===
CLAIM: US general-public native distribution has one admitted channel with Apple admission authority
EVIDENCE_CLASS: S1
SOURCE: Conjunction of Apple App Review Guidelines and Apple Support S0 facts
FACT: Every App Store app is reviewed; alternative distribution is exhaustively limited to Brazil/Japan/EU.
DERIVATION: S0 conjunction yields one admitted channel for US general-public native apps and Apple decides admission to it under frozen access_gatekeeping.
