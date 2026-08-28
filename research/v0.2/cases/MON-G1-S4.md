# MON-G1-S4 — Native iOS app distribution to users in the United States (dated 2026)

**Gate:** MON-G1-LI
**Case ID:** MON-G1-S4
**Role in set:** The discipline test for `access_gatekeeping`. That layer is now evidenced once (S6, defense procurement). We must not stamp the same label on every platform by reflex — the rule must establish a specific gate, not merely reflect platform ownership or market power.
**Status:** Evidence extraction complete — provisional case result
**Evidence rule:** S0 + reproducible S1 only; S2 may explain but may not classify
**Frozen hypothesis under test:** `access_gatekeeping`
**Extraction order position:** 5 of 8

## 0. Scope fixed BEFORE evidence (jurisdiction + date + OS)

> **Native iOS app distribution to users in the United States — dated 2026.**

Jurisdiction is load-bearing here: Apple's own rules differ by region, so "iOS distribution" without a jurisdiction is not a classifiable object. This case is **US-scoped**. It makes **no** claim about the EU, Brazil, or Japan, where Apple's rules differ (see §3).

## 0.1 Governing extraction question

> Does a **platform-native rule** establish a specific gate through which native app distribution must pass, or are we merely observing platform ownership and market power?

The bar: the classification must rest on a documented **admission rule** and a documented **single sanctioned channel within the scope**, from Apple's own materials — not on Apple's size, iOS's install base, or the App Store's revenue share (all of which would be S2 market-power observations).

## 1. The four tests

- **required channel** — what channel must a native iOS app pass through to reach US users?
- **who decides admission** — who reviews and approves/rejects?
- **alternative routes within scope** — are there other routes for native app distribution to US users?
- **exceptions** — what narrow routes exist, and do they defeat the gate?

## 2. S0 evidence (Apple's own documents)

### E01 — App Review is the admission control; Apple reviews every app
**Source:** Apple, *App Review Guidelines* (2025), Introduction.
**Verbatim:** "We do this by offering a highly curated App Store where **every app is reviewed by experts** …"
**Class:** S0. Apple reviews (and can reject) every app before it appears on the App Store.

### E02 — Alternative distribution exists only "in some markets" (not universal)
**Source:** Apple, *App Review Guidelines* (2025), Introduction.
**Verbatim:** "In **some markets and on certain platforms**, developers can also distribute notarized apps from alternative app marketplaces and directly from their website."
**Class:** S0. Alternative native distribution is the exception, limited to named markets — establishing that it is **not** available everywhere.

### E03 — The named markets are EU / Brazil / Japan — the U.S. is not among them
**Source:** Apple Support, *Installing apps through alternative app distribution* (support.apple.com/en-us/117767).
**Verbatim:** "Alternative app distribution is available in **Brazil, Japan, and the countries or regions of the European Union**."
**Class:** S0. The U.S. is not listed. So for US users in 2026, alternative marketplaces and web distribution of native iOS apps are **not** available.

## 3. Why jurisdiction is decisive (the discipline this case enforces)

E03 is the reason the case is US-scoped. In the EU, Brazil, and Japan, Apple permits alternative app marketplaces and/or web distribution — so in those jurisdictions the "single sanctioned channel" premise **fails**, and `access_gatekeeping` at the iOS-distribution locus would **not** be cleanly evidenced (there are multiple admitted routes). Classifying "iOS globally" would therefore be wrong. The layer holds only where the evidence shows a single admitted channel — here, the **US**.

## 4. Classification (provisional)

```
result = evidenced_control_layer
layer  = access_gatekeeping
locus  = native iOS app distribution to US users (dated 2026)
```

### Control mechanism
> Apple's App Review Guidelines require native iOS apps to reach users through the App Store, where Apple reviews and approves/rejects every app; and within the US scope no alternative marketplace or web-distribution route is available (alternative distribution is limited to the EU, Brazil, and Japan). Apple therefore controls admission to the sole sanctioned channel for native iOS apps to US users.

### Classification derivation
S0 facts (every app reviewed; alternative distribution limited to named non-US markets) → **S1** conjunction (US native app distribution has one admitted channel, and Apple decides admission to it) → `access_gatekeeping`. No S2.

### Why this is a rule-based gate, not a market-power observation
The classification cites **Apple's own admission rule** (App Review) and Apple's **own statement** of where alternative routes exist. It does **not** use the App Store's market share, iOS's install base, or Apple's size. A platform whose rules admitted multiple native-distribution routes in-scope (as Apple's do in the EU/Brazil/Japan) would fail this test — which is exactly why the result is jurisdiction-bounded.

## 5. Per-claim ledger (S0 fact / S1 derivation / S2 excluded)

| Claim | S0 fact | S1 derivation | S2 (excluded) |
|---|---|---|---|
| Apple reviews/approves every app | "every app is reviewed by experts" (Guidelines) | Apple holds admission authority | whether review is applied fairly / anticompetitively |
| Alternative distribution is not universal | "in some markets and on certain platforms" (Guidelines) | alternative native routes are the exception | — |
| US has no alternative native route (2026) | "available in Brazil, Japan, and the … EU" (Apple Support); US not listed | US native app distribution has one admitted channel ⇒ `access_gatekeeping` | whether the single channel is an antitrust "monopoly" |
| Payment-link (anti-steering) changes ≠ distribution channel | Apple's 2025 US guideline update concerns external links/buttons | steering/payment ≠ the distribution gate | market-power / normative conclusions |

## 6. Exceptions (recorded, do not defeat the gate)

Narrow routes exist and are noted so the claim is not absolute, but none is general public native distribution to US users:
- **Enterprise (in-house) distribution** — apps to an organization's own employees, not the public.
- **Custom / unlisted apps** (Apple Business/School Manager) — private distribution to specified organizations.
- **TestFlight** — time-limited beta testing to a capped set of testers.
- **The open web (Safari/PWAs)** — a **non-native** route; Apple itself points to "Safari for a great web experience." Web apps are outside the native-app locus.

These are exceptions to, not defeaters of, a gate on **general public native app distribution**.

## 7. Claim boundary

### Admissible record (dated, US-scoped)
> For native iOS app distribution to users in the **United States** in **2026**, Apple's App Review Guidelines and support documentation establish an `access_gatekeeping` layer: every app is reviewed and approved/rejected by Apple, and the App Store is the sole Apple-sanctioned channel for reaching US users, since alternative app marketplaces and web distribution are available only in the EU, Brazil, and Japan — subject to narrow enterprise/custom/TestFlight exceptions and the separate non-native web route.

### Not admissible
- ❌ "Apple monopolises apps." — a normative/market-power claim (S2); the record classifies an admission gate, not a monopoly.
- ❌ Extending the layer to **iOS globally** — the EU/Brazil/Japan admit alternative routes; the gate is US-scoped.
- ❌ Any claim resting on App Store market share or iOS install base — not used, and not needed.
- ❌ Reading the US anti-steering/payment-link court changes as opening the **distribution** channel — they concern external purchase links, not app distribution.
- ❌ Any undated claim — Apple's regional rules change (the carve-out already grew from EU to EU+Brazil+Japan); the record is dated 2026.

## 8. Running gate picture (five of eight)

- S8 → `legal_exclusivity` (statutory right)
- S1 → `capacity_control` (single-actor locus)
- S2 → `capacity_control` (collective locus)
- S6 → `capacity_control` + `access_gatekeeping` (defense procurement channel)
- S4 → `access_gatekeeping` (native iOS app distribution to US users, 2026)

`access_gatekeeping` now appears twice — but at **very different loci** (a government procurement channel vs a consumer app-distribution channel), each on a **documented admission rule**, and S4's is explicitly jurisdiction-bounded to avoid stamping the label on "iOS" as a whole. That the same layer recurs on distinct, separately-evidenced instruments is a sign of a real category, not a lazy default. Three mechanisms evidenced across five cases (`legal_exclusivity`, `capacity_control`, `access_gatekeeping`); `qualification_control`, `standard_interface_control`, and `temporal_constraint` remain unproven. The gate verdict waits on the full fixed set.

## 9. Next step

Stop at S4 for review before extracting MON-G1-S5 (card-payment acceptance), per the frozen order. Do not batch.
