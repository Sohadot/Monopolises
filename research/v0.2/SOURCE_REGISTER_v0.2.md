# Source Register — Monopolises v0.2

**Version:** v0.2
**Status:** Open register — accrues as MON-G1-LI cases are extracted
**Gate:** MON-G1-LI (Layer Identifiability)
**Cases covered so far:** MON-G1-S8
**Admitted sources:** 4

Sources are admitted because they support an actual v0.2 case classification, not because the publisher is generally reputable. A prestigious publisher does not upgrade a weak claim; source authority and claim fit are separate judgments.

Each row records which case the source serves, the exact claim it supports, and its evidence class. For statutes and regulations, the canonical citation is the locator; the listed URL is the official publisher's stable access point and should be verified against the official source on use.

## Admitted sources

| Source ID | Case | Publisher | Source class | Locator / citation | Canonical access point | Claim supported | Evidence class | Retrieved | Notes |
|---|---|---|---|---|---|---|---|---|---|
| MON2-SRC-001 | MON-G1-S8 | United States Code (federal statute) | Primary legal instrument | 18 U.S.C. § 1696 — Private express for letters and packets | https://uscode.house.gov (Title 18 § 1696) | Federal law penalizes establishing or providing for regular private conveyance of letters/packets over post routes, subject to statutory exceptions | S0 | 2026-08-28 | The control instrument itself; establishes the restriction, not any market outcome |
| MON2-SRC-002 | MON-G1-S8 | United States Code (federal statute) | Primary legal instrument | 39 U.S.C. § 601 — Letters carried out of the mail | https://uscode.house.gov (Title 39 § 601) | Defines the conditions under which a letter may lawfully be carried out of the mail (price/weight and other regulatory conditions and exceptions) | S0 | 2026-08-28 | Establishes that the exclusivity is bounded and conditional, not total |
| MON2-SRC-003 | MON-G1-S8 | Code of Federal Regulations | Primary regulatory instrument | 39 CFR Part 310 — Enforcement of the Private Express Statutes | https://www.ecfr.gov (Title 39, Part 310) | A dedicated federal regulatory part enforces and defines the operation of the Private Express Statutes, including exceptions and suspensions | S0 | 2026-08-28 | Confirms an operative, enforced regime with defined boundaries |
| MON2-SRC-004 | MON-G1-S8 | U.S. Postal Service | Operator statement of legal regime | USPS description of the Private Express Statutes | https://www.usps.com (Private Express Statutes summary) | USPS summarizes that carrying letters over post routes by a non–Postal Service entity is generally unlawful except under defined conditions, exceptions, and suspensions | S0 (corroborative) | 2026-08-28 | Plain-language corroboration of the statutes; not relied on beyond the statutory text |

## Admission rules (v0.2)

1. A source is admitted only when it supports a specific claim in a specific case record.
2. For a `legal_exclusivity` layer, the primary legal instrument (statute/regulation) is the admissible basis; operator or secondary summaries are corroborative only.
3. Evidence class is recorded per source. S2 sources may be listed to explain uncertainty but may not carry a layer classification.
4. Canonical citations are authoritative; access-point URLs are conveniences to be verified against the official publisher.
