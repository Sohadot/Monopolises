# MON-G1-LI — Full-Set Gate Evaluation (8/8)

**Gate:** MON-G1-LI (Layer Identifiability)
**Thesis under test:** Layered Monopolisation v0.2 (`THESIS_CANDIDATE.md`)
**Evaluation date:** 2026-08-28
**Method:** Each PASS condition assessed on its own; each falsifier assessed on its own; then a single verdict. This is a test, not a summary of wins. A layer count is **not** a verdict.

## 0. The fixed set and its results

| Case | System (scope) | Result | Layer(s) | Locus |
|---|---|---|---|---|
| S8 | US Private Express Statutes | evidenced | `legal_exclusivity` | letters over post routes |
| S1 | EUV lithography | evidenced | `capacity_control` | EUV scanner production (single-actor) |
| S2 | Leading-edge foundry (2021) | evidenced | `capacity_control` | 5 nm HVM capacity set (collective) |
| S6 | NdFeB magnets | evidenced (×2) | `capacity_control` + `access_gatekeeping` | China value chain; US defense procurement |
| S4 | Native iOS app distribution (US) | evidenced | `access_gatekeeping` | general-public App Store channel |
| S5 | Card-payment acceptance (Visa, US) | evidenced | `access_gatekeeping` | Visa-network admission |
| S3 | Accelerated computing (CUDA) | **negative** | `no_evidenced_control_layer` | — |
| S7 | Cloud hyperscaler (UK) | evidenced | `switching_dependency` (held-out probe **triggered**) | provider egress boundary |

- **Mechanisms evidenced (4):** `legal_exclusivity`, `capacity_control`, `access_gatekeeping`, `switching_dependency`.
- **Refused / unproven (3):** `qualification_control` (refused in S6 — relabel of capacity), `standard_interface_control` (refused in S5 rulebook and S3 CUDA), `temporal_constraint` (never targeted by a case).
- **Negatives / refusals:** S3 negative; plus in-case refusals in S6, S5, S3, and S2's first pass.

---

## 1. PASS conditions (all four must hold)

### PASS-1 — Reviewer reproducibility
*Can an independent reviewer reach the same layer + mechanism from the same cited primary evidence in a clear majority, with reconstructable claim boundaries?*

- Every evidenced classification is anchored to a **named, quotable primary instrument**: statutes (S8: 18 USC 1696 / 39 USC 601; S6: 10 USC 4872 / DFARS 252.225-7052), government findings of fact (S1/S2: EO 14017 review; S6: BIS 232; S7: CMA final decision), and operator/network binding rules (S4: Apple App Review Guidelines; S5: Visa Core Rules).
- Clean, reproducible on re-reading: **S8, S1, S6 (both layers), S4, S5, S7, and the S3 negative** — 7 of 8.
- **Marginal case: S2.** Its third element ("hard to bypass") is an S1 derivation from S0 no-alternative facts; a strict reviewer could defensibly call S2 `ambiguous_layer`. Its claim boundary is reconstructable and the S1/S2 line is explicitly flagged, but it is the one classification a second reviewer might move.
- **Honest caveat:** several cases (S2, S6, S4, S5, S7) required **revision in review** to reach the correct label. Reproducibility here means "reproducible under disciplined application of the frozen definitions," not "obvious on a casual first read." That is acceptable for a research gate but is a real limit.

**Assessment: HOLDS** (clear majority reproducible; one marginal case; reproducibility is discipline-dependent).

### PASS-2 — Genuine layer diversity
*Do several materially different control mechanisms appear — not one relabeled?*

- Four genuinely distinct mechanisms: an **exclusive legal right** (S8), a **productive-capacity chokepoint** (S1/S2), an **admission gate** (S6/S4/S5), and a **switching cost** (S7). These are not restatements of one another.
- Diversity is corroborated by the framework's **refusals**: S6 refused to relabel a capacity shortage as `qualification_control`; S5 refused to call a rulebook `standard_interface_control`; S3 refused to call popularity `standard_interface_control`. A framework that saw one mechanism everywhere could not have drawn these lines.
- `access_gatekeeping` recurs 3× but at **distinct loci on distinct instruments** (a defense statute, a platform's app-review rules, a payment network's licensing) — breadth of one real mechanism, not padding.

**Assessment: HOLDS (strongly).**

### PASS-3 — Bounded S2
*Is S2 confined to explaining uncertainty, never carrying a classification?*

- S2 was quarantined in every case and **never** carried a label: DOJ monopolization (S5), CMA "competition not working well" / AECs (S7), replacement sufficiency (S6, the Gate-0 trap), egress magnitude/lock-in (S7), market share / dominance (S2, S3, S7), antitrust conclusions throughout — all recorded as excluded.
- The negatives and refusals are exactly where S2 was declined: S3 (popularity ≠ control), S6 (qualification relabel), S2 first pass.

**Assessment: HOLDS (strongly).**

### PASS-4 — Locus usefulness
*Does each evidenced layer say specifically WHERE control sits, not merely "the market is concentrated"?*

- Each names a specific locus: letters over post routes (S8); EUV scanner production (S1); the 2021 5 nm HVM capacity set (S2); the China NdFeB value chain and the US defense procurement channel (S6); the US general-public App Store channel (S4); Visa-network admission (S5); the provider-specific data-egress boundary (S7). None is "concentrated market."

**Assessment: HOLDS.**

---

## 2. Falsifier conditions (any one triggering = FAIL)

### FALSIFIER-1 — Layer assignment predominantly depends on S2
- Assignments rest on named source-native instruments; S2 was excluded throughout. The closest-to-load-bearing judgment (S2 "hard to bypass") is grounded in S0 no-alternative facts and flagged, not hidden.
- **Not triggered.**

### FALSIFIER-2 — Pervasive `ambiguous_layer` (reviewers pick different layers with no source-native rule to separate them)
- **No case resolved to `ambiguous_layer`.** Where layers could blur, a source-native rule separated them (S6: capacity vs access vs qualification; S5: access vs interface). One marginal judgment point (S2) is flagged; it is not pervasive.
- **Not triggered.**

### FALSIFIER-3 — The layers are different names for the same "market concentration"
- Concentration alone **never** produced a layer: TSMC dominance (S2) became a layer only on source-native no-alternative evidence, never as "monopolises advanced chips"; CUDA (S3) and cloud concentration (S7 market level) yielded no market-level control layer. The four mechanisms are structurally different.
- **Not triggered.**

### FALSIFIER-4 — The framework cannot return `no_evidenced_control_layer` (finds a layer everywhere)
- S3 returned a clean negative; S6 refused `qualification_control`; S5 refused `standard_interface_control`; S2's first pass returned a negative before the collective-capacity reading. The framework demonstrably declines.
- **Not triggered.**

---

## 3. Verdict

> **MON-G1-LI: PASS.**

All four PASS conditions hold; no falsifier triggers. The v0.2 thesis — that control concentrates **layer by layer**, classifiable from public primary evidence as `System × Layer × Control Mechanism × Evidence` without inferring legal monopoly status — is **supported as buildable**, on the performance of the fixed eight-case set, with the honest caveats recorded in PASS-1 (one marginal case, S2; reproducibility is discipline-dependent).

This is a PASS for **layer identifiability**, not a licence for scores, rankings, entity pages, or monetization. Any of those still require their own decision and gate.

---

## 4. Recommended disposition for DEC-005 (for decision, not yet enacted)

Case findings are separated from the gate decision; the following is a **recommendation** for `DEC-005`, to be ratified (or amended) by decision, not by this evaluation.

**Admit to the v0.2 taxonomy (evidenced):**
- `legal_exclusivity` (S8)
- `capacity_control` (S1, S2 — single-actor and collective loci both hold)
- `access_gatekeeping` (S6, S4, S5)
- `switching_dependency` — **admit the held-out probe**: it was triggered by a named, source-native instrument (S7), meeting the thesis's "needed and distinct" condition.

**Do NOT admit yet (unproven on this set) — keep as candidates:**
- `qualification_control` — refused in S6 (would have been a capacity relabel); no case evidenced it.
- `standard_interface_control` — refused in S5 (rulebook) and S3 (popularity); a named required-interface instrument was never source-native. Retain as a candidate; a future case with a mandated protocol/technical standard could evidence it.
- `temporal_constraint` — **never targeted** by a case (Replacement Horizon was demoted into it but not tested). Not refuted; untested. Retain as a candidate; needs its own case.

**Discipline for a successor build (recommended for DEC-005):**
- Every published record must carry `System × Layer × Control Mechanism × Evidence` with a dated, jurisdiction-scoped claim boundary.
- No market-share/dominance or antitrust conclusion may carry a classification (S2 stays excluded).
- Dated findings are records of their date; later change does not erase them, and present-tense restatement needs current primary evidence.
- A new falsifiable gate is required before any scored/ranked/scaled surface.

## 5. Next step

Review this evaluation and the PASS verdict. If accepted, the next action is a **decision** — `DEC-005` — enacting the taxonomy disposition in §4 and opening a **successor gate** for whatever is built next. This evaluation does **not** itself close MON-G1-LI or write DEC-005; those are decisions for you to ratify.
