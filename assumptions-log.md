# Assumptions Log — Pixxel Commercial Strategy

Every number used in analysis or `final.md` appears here with source or `[ASSUMPTION]` label.

**FX reference:** ₹83 = $1 USD (A016) — approximate mid-2025/26 rate for planning.

---

## Company facts (verified)

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A001 | Pixxel total funding raised | **$95M** | S005, S009, PS (S011) | CEO cited in Orbital Today Jan 2026 |
| A002 | Indian private space-tech entities | **400+** | S011 (ICG PS) | Market context |
| A003 | Indian space sector cumulative capital | **>$500M** | S011 (ICG PS) | Market context |
| A004 | PPP constellation size | **12 satellites** | S001, S002 | National EO constellation |
| A005 | PPP consortium investment | **>₹1,200 crore** (~$145M) | S001, S002, S004 | Over 4–5 years |
| A006 | PPP consortium members | Pixxel, Dhruva Space, PierSight, SatSure | S001 | — |
| A007 | Firefly satellites operational | **3** (early 2025) | S002, S009 | 135+ bands, ~5 m resolution |
| A008 | Aurora Professional price | **$150/user/month** | S006, S010 | 150 free tokens/mo |
| A009 | Aurora Enterprise price | **$180/user/month** (annual) | S006, S010 | 300 free tokens/mo |
| A010 | Hyperspectral archive price | **$6/km²** | S010 | Pixxel published |
| A011 | Hyperspectral tasking price | **$8/km²** | S010 | Pixxel published |

---

## Agriculture & land (verified)

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A012 | Net sown area (India) | **139.0 M ha** (13,899 lakh ha) | S016 | FY 2023-24 |
| A013 | Gross cropped area | **217.9 M ha** | S016, S017 | Cropping intensity 156.8% |
| A014 | Net irrigated area | **82.4 M ha** | S016 | FY 2023-24 |
| A015 | Ag GVA (current prices, FY2024-25) | **₹53.85 lakh crore** | S013 | MOSPI provisional |
| A016 | USD/INR planning rate | **₹83 = $1** | `[ASSUMPTION]` | Planning convenience; S013 conversion |
| A017 | Ag GVA in USD (planning) | **~$648B** | Derived | ₹53.85L cr ÷ 83 |

---

## PMFBY (verified)

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A018 | Farmers enrolled (2024-25) | **4.19 crore** (41.9M) | S018 | Highest since launch |
| A019 | Cumulative farmer applications insured | **78.41 crore** since 2016 | S018 | — |
| A020 | Total claims disbursed (cumulative) | **₹1.83 lakh crore** | S018 | As of 30.06.2025 |
| A021 | PMFBY scheme continuation budget | **₹35,951.71 crore** | S019 | Cabinet approval Jan 2025 |
| A022 | YES-TECH mandatory tech weight | **30%** of yield estimate | S021 | Paddy & wheat, Kharif 2023+ |
| A023 | Farmer premium (Kharif food/oilseeds) | **2% of sum insured** max | S020 | Govt subsidizes remainder |

---

## Market reports (secondary — triangulation)

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A024 | India precision ag market (2025) | **$334.2M** | S023 | IMARC |
| A025 | India precision ag CAGR | **9.22%** (2026–34) | S023 | IMARC |
| A026 | Satellite precision-ag app CAGR (India) | **17.6%** through 2031 | S025 | Mordor Intelligence |
| A027 | India satellite EO market (2026) | **$0.8B** | S026 | MarkWide — broader than ag analytics |

---

## TAM model assumptions

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A028 | Addressable % of net sown area | **55%** → 76.5 M ha | `[ASSUMPTION]` | Irrigated + commercial/notified crops; excludes uneconomic subsistence plots |
| A029 | Adoption rate FY2028 — conservative | **6%** | `[ASSUMPTION]` | Slow policy rollout |
| A030 | Adoption rate FY2028 — base | **12%** | `[ASSUMPTION]` | Anchored to A026 CAGR from ~5% 2025 base |
| A031 | Adoption rate FY2028 — optimistic | **22%** | `[ASSUMPTION]` | National EO + YES-TECH expansion |
| A032 | Blended $/ha/year — conservative | **$6.00** | `[ASSUMPTION]` | Govt bulk pricing pressure |
| A033 | Blended $/ha/year — base | **$11.10** | `[ASSUMPTION]` | Weighted DaaS + SaaS |
| A034 | Blended $/ha/year — optimistic | **$18.00** | `[ASSUMPTION]` | Hyperspectral premium adoption |
| A035 | **TAM FY2028 — conservative** | **$27.5M** | Derived | 76.5M × 6% × $6 |
| A036 | **TAM FY2028 — base** | **$102.0M** | Derived | 76.5M × 12% × $11.10 |
| A037 | **TAM FY2028 — optimistic** | **$303.0M** | Derived | 76.5M × 22% × $18 |
| A038 | Satellite share of precision ag market | **30%** | `[ASSUMPTION]` | Top-down triangulation; remote sensing subset |
| A039 | Ag GVA digital satellite analytics share | **0.016%** | `[ASSUMPTION]` | Top-down B → ~$104M |
| A040 | PMFBY sub-TAM FY2028 | **$72M** | `[ASSUMPTION]` | 600 contracts × $120K |
| A041 | Enterprise precision ag sub-TAM FY2028 | **$30M** | `[ASSUMPTION]` | 200 accounts × $150K ARR |
| A042 | PMFBY district-season contracts | **600** | `[ASSUMPTION]` | ~100 districts × 2 seasons × 3 yr ramp |
| A043 | Avg PMFBY analytics contract value | **$120K/year** | `[ASSUMPTION]` | State/insurer monitoring package |
| A044 | Enterprise accounts (FY2028) | **200** | `[ASSUMPTION]` | FPOs, sugar, horticulture exporters |
| A045 | Avg enterprise ARR | **$150K** | `[ASSUMPTION]` | Aurora + imagery + custom analytics |

---

## Pixxel revenue share assumptions

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A046 | Pixxel India ag TAM share FY2026 | **4%** → $2.7M | `[ASSUMPTION]` | Early pilots |
| A047 | Pixxel share FY2027 | **8%** → $6.7M | `[ASSUMPTION]` | PPP ramp |
| A048 | Pixxel share FY2028 | **12%** → $12.2M | `[ASSUMPTION]` | 2–3 state PMFBY + 25 enterprise |
| A049 | Interim TAM FY2026 | **$68M** | `[ASSUMPTION]` | Linear interpolation to base |
| A050 | Interim TAM FY2027 | **$84M** | `[ASSUMPTION]` | — |

---

## Unit economics assumptions

| ID | Metric / Claim | Value | Source | Notes |
|----|----------------|-------|--------|-------|
| A051 | DaaS bulk effective rate | **$0.60/ha/year** | `[ASSUMPTION]` | Discounted from list; multi-pass |
| A052 | DaaS gross margin | **45%** | `[ASSUMPTION]` | Satellite capex heavy |
| A053 | SaaS gross margin | **70%** | `[ASSUMPTION]` | Software economics |
| A054 | PMFBY tender CAC | **$80K** | `[ASSUMPTION]` | Bid + compliance |
| A055 | Enterprise SaaS CAC | **$45K** | `[ASSUMPTION]` | ABM + pilot |
| A056 | PMFBY contract LTV (3-yr) | **$2.4M** | `[ASSUMPTION]` | 2-yr renew × $1.2M |
| A057 | Enterprise LTV (3-yr) | **$750K** | `[ASSUMPTION]` | $250K/yr × 3 |
| A058 | FY2028 revenue mix — DaaS | **35%** | `[ASSUMPTION]` | Hybrid model target |
| A059 | FY2028 revenue mix — SaaS | **55%** | `[ASSUMPTION]` | — |
| A060 | FY2028 revenue mix — services | **10%** | `[ASSUMPTION]` | Integration/calibration |

---

## Segment scoring (qualitative → 1–5)

| ID | Metric | Precision Ag | PMFBY | Notes |
|----|--------|--------------|-------|-------|
| A061 | Market size score | 3 | 5 | Sub-TAM $30M vs $72M |
| A062 | WTP score | 4 | 3 | — |
| A063 | Competition score | 3 | 2 | SatSure incumbent |
| A064 | Regulatory score | 4 | 5 | YES-TECH tailwind |
| A065 | **Weighted total** | **3.55** | **3.90** | Weights: 25/25/20/30 |

---

## Sanity checks

| Check | Top-down | Bottom-up | Pass? |
|-------|----------|-----------|-------|
| TAM vs ag GDP share | $104M (0.016% GVA) | $102M base | ✓ 2% variance |
| TAM vs IMARC subset | $129M (30% × growth) | $102M base | ✓ 21% variance |
| Segment sum | $72M + $30M = $102M | $102M base | ✓ Exact |
| Price/ha vs Pixxel list | $0.06/ha single pass × ~10 = $0.60 | A051 $0.60 bulk | ✓ Consistent |
| PMFBY contract vs budget | 600 × $120K = $72M | 0.2% of ₹35,951 cr scheme | ✓ Reasonable admin tech spend |

---

## Sensitivity scenarios (base TAM $102M)

| Scenario | Key lever | TAM result | Used in deck? |
|----------|-----------|------------|---------------|
| Conservative | 6% adoption, $6/ha | **$27.5M** | Yes — Page 2 |
| Base | 12% adoption, $11.10/ha | **$102.0M** | Yes — Page 2 |
| Optimistic | 22% adoption, $18/ha | **$303.0M** | Yes — Page 2 |
| Adoption −20% | 9.6% adoption | **$81.6M** | Sensitivity exhibit |
| Adoption +20% | 14.4% adoption | **$122.4M** | Sensitivity exhibit |

---

## INR equivalents (base case, ₹83/$)

| Metric | USD | INR |
|--------|-----|-----|
| TAM FY2028 (base) | $102.0M | **₹847 crore** |
| PMFBY sub-TAM | $72.0M | **₹598 crore** |
| Enterprise sub-TAM | $30.0M | **₹249 crore** |
| Pixxel FY2028 India ag revenue | $12.2M | **₹101 crore** |
