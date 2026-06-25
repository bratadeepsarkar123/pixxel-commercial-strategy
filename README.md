# Pixxel Commercial Strategy (India)

Independent commercial-strategy case on **Pixxel Space Technologies** — India's hyperspectral earth-observation startup — covering market sizing, vertical prioritization, and monetization for FY2026–28.

**Author:** [Bratadeep Sarkar](https://github.com/bratadeepsarkar123) · B.Tech EE, IIT Kanpur  
**Deck:** [`deliverables/Pixxel_Commercial_Strategy_Deck.pdf`](deliverables/Pixxel_Commercial_Strategy_Deck.pdf) (5 pages) · [`.pptx`](deliverables/Pixxel_Commercial_Strategy_Deck.pptx)

---

## Three recommendations

| # | Recommendation | FY2028 anchor |
|---|----------------|---------------|
| 1 | India satellite precision-ag analytics TAM **$102M** (base) | PMFBY **$72M (71%)** · Enterprise **$30M (29%)** |
| 2 | **PMFBY crop insurance first** (weighted score **3.90 vs 3.55**) | Enterprise precision ag from FY2027 |
| 3 | **SaaS-led hybrid** monetization | Pixxel India ag revenue **$12.2M**; **~58%** blended gross margin |

---

## Repository map

| Path | Contents |
|------|----------|
| [`final.md`](final.md) | Master narrative + deck outline |
| [`analysis/`](analysis/) | Issue tree, TAM model, segment matrix, unit economics |
| [`research/sources.md`](research/sources.md) | 38 primary/secondary citations |
| [`assumptions-log.md`](assumptions-log.md) | Every number tagged (verified or assumption) |
| [`deliverables/`](deliverables/) | Board deck PDF/PPTX + slide PNGs |

---

## How to read this case

1. Start with **`deliverables/Pixxel_Commercial_Strategy_Deck.pdf`** (~5 min).
2. Drill into **`final.md`** for full argumentation.
3. Trace any number via **`assumptions-log.md`** → **`research/sources.md`**.

---

## Methodology

- MECE issue tree + hypothesis-driven prioritization  
- Bottom-up TAM (139M ha → 55% addressable → 12% adoption × $11.10/ha) triangulated against industry reports  
- Weighted segment scorecard (market size, willingness-to-pay, competition, regulation)  
- DaaS vs SaaS unit economics → hybrid revenue-mix recommendation  

All estimates marked `[ASSUMPTION]` in `assumptions-log.md` are planning assumptions, not Pixxel disclosures.

---

## Rebuild deck (optional)

```bash
pip install -r requirements.txt
python scripts/build_deck.py
```

Assembles `deliverables/slides/*.png` into PDF and PPTX. See [`deliverables/README.md`](deliverables/README.md).

---

## Contact

[LinkedIn](https://linkedin.com/in/bratadeep-sarkar-iitk) · [GitHub](https://github.com/bratadeepsarkar123)

---

## License

Analysis and deck © Bratadeep Sarkar. Pixxel Space Technologies is a third-party company; this repository is an independent academic case study.
