# MON-G0-C01 — RD-180 → Domestically Powered NSSL Launch Capability

**Gate:** MON-G0-RH  
**Case ID:** MON-G0-C01  
**Status:** Evidence extraction complete — provisional case result  
**Evidence rule:** S0 + reproducible S1 only  
**Canonical horizon status:** NOT YET EVIDENCED AS A SINGLE INTERVAL

## 1. Critical function

Certified U.S. medium/heavy national-security launch capability that does not rely on the Russian-manufactured RD-180 engine used by Atlas V.

## 2. Current source / system

Atlas V used the Russian-manufactured RD-180 engine. GAO documented in 2014 that DOD and Congress were weighing how to reduce U.S. reliance on the engine and that replacing it could require a new launch vehicle and potentially new launch infrastructure.

## 3. Replacement target

A domestically powered launch system certified by the U.S. Space Force for National Security Space Launch (NSSL) missions.

The target is deliberately certification, not first commercial launch and not first operational NSSL mission. Certification is an official qualification event with a discrete public date.

## 4. S0 evidence

### E01 — Reliance / replacement difficulty
**Publisher:** U.S. Government Accountability Office  
**Source:** GAO-14-776T, *U.S. Launch Enterprise: Acquisition Best Practices Can Benefit Future Efforts*  
**Date:** 2014  
**Supported facts:**
- Atlas V used the RD-180 engine produced in Russia.
- DOD and Congress were considering reducing U.S. reliance on Russian-produced rocket engines.
- GAO stated that replacing the RD-180 could require development of a new launch vehicle and potentially new launch infrastructure.

**Evidence class:** S0  
**Use:** Establishes the strategic replacement problem, not the start date of a formal replacement program.

### E02 — New engine development milestone
**Publisher:** U.S. Government Accountability Office  
**Source:** GAO-24-106831, NSSL program timeline  
**Supported fact:** The NSSL timeline records **01/2016 — New engine development**.

**Evidence class:** S0  
**Use:** Candidate program anchor A.

### E03 — Launch-system prototype procurement pathway
**Publisher:** U.S. Government Accountability Office  
**Source:** B-417839, *Blue Origin Florida, LLC*  
**Supported facts:**
- Following statutory restrictions on Russian-manufactured engines, DOD reassessed its NSSL strategy.
- The Air Force issued an RFP in **October 2017** for launch-system prototypes, including rocket propulsion, launch systems, infrastructure, manufacturing processes, and related items required to provide domestic commercial launch services meeting NSSL requirements.
- The Air Force entered OTA agreements with ULA and others in **October 2018**.

**Evidence class:** S0  
**Use:** Candidate program anchors B and C.

### E04 — New launch vehicle development milestone
**Publisher:** U.S. Government Accountability Office  
**Source:** GAO-24-106831, NSSL program timeline  
**Supported fact:** The NSSL timeline records **10/2018 — New launch vehicle development**.

**Evidence class:** S0  
**Use:** Candidate program anchor C; independently consistent with the October 2018 OTA milestone.

### E05 — Historical synthesis of RD-180 transition
**Publisher:** U.S. Government Accountability Office  
**Source:** GAO-25-107228, *National Security Space Launch*  
**Date:** 2025-06-30  
**Supported facts:**
- 2014 geopolitical events created concern over DOD reliance on Atlas V / RD-180.
- New propulsion systems and launch vehicle prototypes were developed during the 2014–2022 period.
- Vulcan certification flights occurred in 2024, later than originally planned.
- Space Force certified Vulcan in March 2025.

**Evidence class:** S0  
**Use:** Cross-check / chronology. Not used alone to choose a canonical start anchor.

### E06 — Certification endpoint
**Publisher:** U.S. Space Force / Space Systems Command  
**Source:** *U.S. Space Force Certifies United Launch Alliance Vulcan for National Security Space Launch Missions*  
**Date:** 2025-03-26  
**Supported facts:**
- Vulcan was certified for NSSL missions.
- ULA became eligible to launch NSSL missions as one of two certified providers.
- Certification encompassed 52 certification criteria, more than 180 discrete tasks, two certification flight demonstrations, payload-interface verifications, subsystem reviews, and hardware/software audits.

**Evidence class:** S0  
**Use:** Canonical replacement-target endpoint.

## 5. S1 mechanical derivations

All start milestones before the endpoint are official S0 dates, but they represent different stages. Therefore none is silently promoted to the unique beginning of the Replacement Horizon.

Using month-level precision where the source gives only month/year:

### Anchor A
`01/2016 new engine development → 26 Mar 2025 certification`

Approximate elapsed interval: **9 years 2 months**.

### Anchor B
`10/2017 launch-system prototype RFP → 26 Mar 2025 certification`

Approximate elapsed interval: **7 years 5 months**.

### Anchor C
`10/2018 new launch vehicle development / OTA agreements → 26 Mar 2025 certification`

Approximate elapsed interval: **6 years 5 months**.

These are mechanical chronology intervals, not three competing claims that the “true” Replacement Horizon has three values.

## 6. Certification-flight milestones

- **08 Jan 2024:** first Vulcan certification flight (Cert-1).
- **04 Oct 2024:** second certification flight (Cert-2).
- **26 Mar 2025:** NSSL certification.

These milestones establish a reproducible qualification sequence but do not solve the start-boundary problem.

## 7. Uncertainties / claim boundary

The endpoint is strong and discrete.

The start boundary is not uniquely source-native:
- 2014 establishes the strategic reliance problem.
- January 2016 is an official new-engine-development milestone.
- October 2017 is the prototype RFP.
- October 2018 is the official new-launch-vehicle-development / OTA milestone.

Selecting one of these as the canonical beginning requires a definition of what event starts a Replacement Horizon. That definition has not yet been ratified and would be an S2 methodological choice if made solely for this case.

## 8. Provisional result

**Result:** `bounded_milestone_sequence`

**Single canonical Replacement Horizon:** `not_evidenced`

**What is evidenced:** Public primary/official sources reproducibly show that the RD-180 transition moved through a multi-year sequence from formal engine / launch-system development milestones to NSSL certification in March 2025. Depending on which official development milestone is used as a non-canonical chronology anchor, the mechanically derived interval is approximately **6 years 5 months to 9 years 2 months**.

**What is not evidenced:** That any one of those anchors is, by itself, the uniquely correct start of a general Replacement Horizon measure.

## 9. Gate implication

C01 does **not** fail the Strategic Replaceability thesis, but it exposes a methodological requirement:

> A Replacement Horizon protocol must define the start event before calculating a single interval.

Until that rule is validated across the fixed candidate set, Monopolises must publish milestone sequences or bounded chronology rather than a single pseudo-precise replacement number.
