# Monetization — DaaS vs SaaS

> **Phase 3c complete** | Unit economics, recommendation, conditions to revisit

---

## Models compared

| Dimension | **DaaS** (raw / ARD imagery) | **SaaS** (Aurora analytics) |
|-----------|-------------------------------|----------------------------|
| **Definition** | Provision standardized or analysis-ready hyperspectral imagery ($/km²) | Subscription analytics platform + bundled insights ($/user/mo + tokens) |
| **Buyer** | ISRO stack integrators, insurers with internal GIS, govt agencies | Agribusiness ops teams, insurers without GIS capacity, FPOs |
| **Pixxel list pricing** | $6/km² archive; $8/km² tasking (S010) | Standard $0; Professional $150/user/mo; Enterprise $180/user/mo (S006, S010) |
| **Competitive benchmark** | PlanetScope ~$54/km²/yr monitoring (50 km² min); SkySat $6–40/km² (S031) | Planet Insights Platform $91–916/mo tiers (S031) |

---

## Unit economics table (FY2028 steady state)

*All figures `[ASSUMPTION]` unless sourced — see `assumptions-log.md` IDs A023–A032*

| Metric | **DaaS (ARD bulk)** | **SaaS (Aurora enterprise)** |
|--------|---------------------|--------------------------------|
| **Typical contract** | State PMFBY season: 2M ha monitored | Agribusiness: 15,000 ha + 8 users |
| **Annual revenue** | $1.2M (2M ha × $0.60/ha effective) | $180K platform + $120K imagery tokens = **$300K** |
| **COGS** | Satellite ops, downlink, processing | Cloud compute, support, imagery COGS |
| **COGS %** | 55% | 30% |
| **Gross margin** | **45%** | **70%** |
| **CAC** | $80K (tender bid + compliance) | $45K (ABM + pilot + integration) |
| **Payback period** | 2.0 years | 1.1 years |
| **Scalability** | High (one contract = millions of ha) | Medium (per-account customization) |
| **Customer concentration** | High (top 3 govt/insurer = 60% revenue) | Lower (20+ accounts target) |
| **Churn risk** | Political / tender cycle | Low if embedded in ops workflow |

### DaaS revenue build (example contract)

```
2,000,000 ha = 20,000 km²
Effective bulk rate: $0.60/ha/year [A023] (vs $6/km² = $0.06/ha list for single archive pass × ~10 passes)
Annual revenue = 2M × $0.60 = $1.2M
Gross profit = $1.2M × 45% = $540K
```

*List rate $6/km² (S010) applies to spot purchases; B2G bulk contracts discount 80–90% on per-pass basis but multiply by revisit frequency.*

### SaaS revenue build (example account)

```
8 Enterprise users × $180/mo × 12 = $17,280
Imagery wallet: 15,000 ha × 4 seasonal campaigns × $0.80/ha imagery = $48,000
Custom analytics / API: $235,000 [A024]
Total ARR = ~$300K
Gross profit = $300K × 70% = $210K
CAC $45K → payback 1.1 years
```

---

## Side-by-side strategic comparison

| Dimension | DaaS | SaaS | Winner |
|-----------|------|------|--------|
| Gross margin | 45% | 70% | **SaaS** |
| Revenue scalability (ha) | Very high | Moderate | **DaaS** |
| CAC efficiency | Lower per ha at scale | Higher per account | **DaaS** (volume) |
| Pricing power | Commoditizing (Planet, ISRO) | Differentiated (hyperspectral models) | **SaaS** |
| PPP alignment | Required deliverable (ARD) | Upsell path | **Both** |
| FY2026 readiness | Immediate (Firefly data) | Immediate (Aurora live) | **Tie** |

---

## Customer acquisition cost (CAC) analysis

| Channel | Motion | Est. CAC | LTV (3-yr) | LTV:CAC |
|---------|--------|----------|------------|---------|
| PMFBY state tender | RFP via consortium / insurer | $80K | $2.4M (2-yr renew) | **30:1** |
| Enterprise ABM | Pilot → annual SaaS | $45K | $750K | **17:1** |
| Self-serve Aurora | Product-led | $2K | $18K | **9:1** |

*LTV assumptions in A025–A027.*

**Insight:** PMFBY tenders have highest LTV:CAC but longest cycle (9–18 months). Enterprise pilots fund FY2026 opex while tenders mature.

---

## Scalability limits

| Model | Limit | FY2028 ceiling |
|-------|-------|----------------|
| DaaS | Downlink/processing capacity; constellation revisit | ~25M ha/season without national 12-sat constellation |
| SaaS | Customer success headcount; model calibration per crop/region | ~40 enterprise accounts without major CS team expansion |

---

## Recommendation

### Primary model: **SaaS-led hybrid**

| Layer | Role | FY2028 target mix |
|-------|------|-------------------|
| **SaaS (Aurora)** | Primary monetization engine — dashboards, yield models, insurance indices | **55% of India ag revenue** |
| **DaaS (ARD/imagery)** | Land-grab + PPP compliance — bulk feed to insurers, govt, consortium partners | **35%** |
| **Professional services** | Calibration, integration, YES-TECH validation | **10%** |

### Why hybrid beats pure play

| Pure model | Problem | Hybrid fix |
|------------|---------|------------|
| Pure DaaS | Margin compression vs Planet/ISRO; PPP mandates ARD at scale | SaaS layer captures analytics margin |
| Pure SaaS | Misses PMFBY bulk hectare contracts; underutilizes constellation capacity | DaaS wins volume tenders |

### FY2026–28 revenue mix trajectory

| FY | DaaS % | SaaS % | Services % | India ag revenue |
|----|--------|--------|------------|------------------|
| FY2026 | 45% | 45% | 10% | $2.7M |
| FY2027 | 40% | 50% | 10% | $6.7M |
| FY2028 | 35% | 55% | 10% | $12.2M |

---

## Conditions to revisit model

| Trigger | Switch toward |
|---------|---------------|
| Aurora enterprise churn >25% | Increase DaaS bulk; reduce CS-heavy customization |
| PMFBY tenders won but margin <30% | Raise SaaS attach requirement in bids |
| National constellation delayed >12 months | Enterprise SaaS-first; delay B2G scale |
| SatSure partnership fails | Build in-house YES-TECH module or acquire analytics capability |
| Planet undercuts India monitoring 30%+ | Emphasize hyperspectral differentiation; exit commodity multispectral DaaS |

---

## Board recommendation (one sentence)

**Lead with Aurora SaaS for margin and differentiation; use DaaS/ARD as the volume wedge in PMFBY and PPP channels; target 55% SaaS / 35% DaaS revenue mix by FY2028.**
