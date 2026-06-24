# Pixxel Commercial Strategy Case — Agent Handoff

## Who You Are Working For

**Bratadeep Sarkar**, 2nd-year B.Tech Electrical Engineering, IIT Kanpur (CPI 7.22). Building an independent consulting case study for resume and interview defense. Target firms: McKinsey, BCG, and IIT Kanpur SPO consulting-track companies.

## Why This Project Exists

Bratadeep needs a **second pure strategy consulting project** on his resume (first is ShARE × SIIC GTM win for healthcare AI). This case analyzes **Pixxel Space Technologies** — a real, $95M-funded Indian hyperspectral satellite company — and produces a board-ready commercial strategy. The problem statement comes from ICG Section B Task 1 ("Pix and Profit") but must be framed on the resume as an **independent Self Project**, never as "ICG recruitment."

**Resume goal (after completion):** 3 bullets covering TAM sizing, vertical prioritization, and DaaS vs SaaS recommendation — only verified numbers.

## What You Must Deliver

| Deliverable | Path | Requirement |
|-------------|------|-------------|
| Issue tree + hypothesis | `analysis/01-issue-tree.md` | MECE, 3 layers, stated hypothesis |
| TAM model | `analysis/02-tam-model.md` (+ optional Excel) | Bottom-up, every assumption documented |
| Segment comparison | `analysis/03-segment-comparison.md` | Ag analytics vs PMFBY on 4 criteria |
| Monetization analysis | `analysis/04-daas-vs-saas.md` | Unit economics, clear recommendation |
| Assumptions log | `assumptions-log.md` | Every number traceable to source |
| Research notes | `research/sources.md` | Primary sources only where possible |
| **Final deck** | `deliverables/Pixxel_Commercial_Strategy_Deck.pdf` | **5 pages**, board format |

## Case Brief (From ICG PS — Section B Task 1)

**Client:** Pixxel Space Technologies (hyperspectral EO, Aurora analytics platform, 12-satellite PPP with Indian govt, $95M raised).

**Problem:** World-class infrastructure but no dominant monetization strategy. Must transition from hardware-centric startup to profitable data/analytics enterprise.

**Your mandate:** 3-year commercial plan (FY2026–FY2028) covering:

1. **Market Sizing** — TAM for satellite-based precision agriculture analytics in India. Explicit methodology, step-by-step calculations, documented assumptions.

2. **Vertical Prioritization** — Compare two segments:
   - Precision Agriculture Analytics (direct-to-enterprise agribusiness)
   - Crop Insurance / PMFBY Index Underwriting (B2B/B2G for insurers/govt)
   Score on: market size, willingness-to-pay, competition, regulatory framework. Recommend primary vertical + expansion sequence.

3. **Monetization Strategy** — DaaS (raw/standardized imagery) vs SaaS (Aurora subscription analytics). Evaluate unit economics, scalability, CAC. Recommend model or justified hybrid.

**Output:** 5-page PDF deck, data-driven, actionable, board-ready.

**Full PS text:** Read `C:\Users\brata\Downloads\resumes\CONSULT PROJECTS\secy recruitment '26.md` — Section B, Task 1 (Pages 6–8).

## How to Proceed — McKinsey-Style Workflow

### Phase 0: Learn (1–2 hours — DO THIS FIRST)

Before writing any analysis, review these resources to internalize consulting methodology:

1. Watch: [Victor Cheng Case Interview Workshop Part 1](https://www.youtube.com/watch?v=fBwUxnTpTBo)
2. Watch: [Crafting Cases Market Sizing Breakdown](https://www.youtube.com/watch?v=N5SLtfVoZAM)
3. Read: [Issue Trees Guide](https://www.hackingthecaseinterview.com/pages/issue-trees) — focus on MECE and 80/20
4. Read: [Market Sizing 6-Step Method](https://strategycase.com/market-sizing-case-interviews/)
5. Skim: McKinsey interviewing page — [mckinsey.com/careers/interviewing](http://www.mckinsey.com/careers/interviewing)

Document key takeaways in `research/methodology-notes.md`.

### Phase 1: Clarify + Hypothesize (30 min)

Create `analysis/01-issue-tree.md`:

- Restate the client problem in one sentence
- State a **testable hypothesis** (e.g., "PMFBY underwriting is the faster revenue path because…")
- Build MECE issue tree with 3–4 top-level branches:
  - Market Attractiveness (size, growth, margins)
  - Competitive Landscape (Planet Labs, ISRO, domestic players)
  - Monetization & Unit Economics (DaaS vs SaaS)
  - Go-to-Market & Regulatory (data policy, PMFBY mechanics)
- Mark 80/20 priority branches

### Phase 2: Research (2–4 hours)

Populate `research/sources.md` with primary sources:

- Pixxel website, press releases, funding announcements
- IN-SPACe / Indian space economy reports
- PMFBY scheme documentation (govt sources)
- Planet Labs public filings (competitive benchmark)
- Precision ag market reports (cite source for every stat)

**Rule:** Never invent metrics. If a number is estimated, label it `[ASSUMPTION]` in `assumptions-log.md` with rationale.

### Phase 3: Analysis (4–6 hours)

**TAM (`analysis/02-tam-model.md`):**

- Use bottom-up: e.g., Total farmable hectares → addressable % → adoption rate → annual price/hectare
- Show 3-scenario sensitivity (conservative / base / optimistic)
- Sanity-check against top-down estimate (Indian ag GDP × analytics spend %)
- State strategic "so-what"

**Segments (`analysis/03-segment-comparison.md`):**

- Weighted scoring matrix (4–5 criteria, explicit weights)
- Winner + rationale
- Sequenced expansion roadmap FY2026–28

**Monetization (`analysis/04-daas-vs-saas.md`):**

- Side-by-side unit economics table
- CAC, gross margin, scalability, customer concentration risk
- Clear recommendation with conditions under which you'd switch models

### Phase 4: Deck (2–3 hours)

5-page PDF structure (Pyramid Principle — answer first on each page):

| Page | Title (Action Headline) | Content |
|------|-------------------------|---------|
| 1 | Executive Summary | Problem, hypothesis, 3 recommendations |
| 2 | India Precision Ag TAM is $X M by FY2028 | TAM exhibit + key assumptions |
| 3 | [Primary Segment] Should Lead Market Entry | Segment comparison matrix + recommendation |
| 4 | [DaaS/SaaS/Hybrid] Maximizes FY2026–28 Profitability | Unit economics + revenue trajectory |
| 5 | FY2026–28 Roadmap & Next Steps | Phased GTM, risks, metrics to track |

Use charts from `charts/` folder. Professional, minimal, black text suitable for printing.

### Phase 5: Verification Gate

Before marking done, verify:

- [ ] Every number in deck appears in `assumptions-log.md` with source
- [ ] No overlap with ShARE resume bullets (different industry, different frameworks emphasized)
- [ ] Bratadeep can defend TAM math on a whiteboard in 10 minutes
- [ ] Deck is exactly 5 pages
- [ ] Project labeled "Self Project" in any resume draft — NOT "ICG recruitment"

## Non-Negotiable Rules

- **Never invent facts** — see `RESUME_RULES.md` in workspace
- **Primary sources first** — company pages, govt docs, not prep sites
- **Resume is separate** — do NOT edit resume files until user approves deck
- **Folder only** — all work product stays under `pixxel-commercial-strategy/`
- **No GitHub push** unless user confirms

## Resume Integration (ONLY After User Approval)

When deck is approved, add to master resume as:

**Pixxel Space Technologies — Commercial Strategy Analysis | Self Project | [Month Year]**

Three bullets (one per pillar — use verified numbers only):

1. TAM sizing bullet
2. Vertical prioritization bullet
3. Monetization recommendation bullet

Then swap **Servota** out of `Bratadeep_Sarkar_Product.tex` for this project. Recompile PDF using **ITConfer / Squarepoint layout** per `SPO_AGENT_RULE_SNIPPET.md` and `Bratadeep_Sarkar_Squarepoint.tex`.

## Reference Files

- Case PS: `CONSULT PROJECTS/secy recruitment '26.md`
- SPO layout rules: `SPO_AGENT_RULE_SNIPPET.md`, `SPO_DEFAULT_FORMAT.md`
- Gold LaTeX master: `Bratadeep_Sarkar_Squarepoint.tex`
- Master resume: `spo_master_resume.tex` (AntiGravity brain copy)
- Consulting one-pager: `Bratadeep_Sarkar_Product.tex`
