# Deliverables — Pixxel Commercial Strategy Deck

## Files

| File | Description |
|------|-------------|
| `Pixxel_Commercial_Strategy_Deck.pdf` | **5-page board deck** (print-ready) |
| `Pixxel_Commercial_Strategy_Deck.pptx` | Same 5 slides as editable PowerPoint |
| `slides/01_executive_summary.png` | Slide 1 — Executive summary |
| `slides/02_tam_sizing.png` | Slide 2 — TAM waterfall + scenarios |
| `slides/03_segment_selection.png` | Slide 3 — PMFBY vs enterprise (SatSure paradox filled) |
| `slides/04_monetization_model.png` | Slide 4 — Unit economics + hybrid model |
| `slides/05_roadmap_next_steps.png` | Slide 5 — Roadmap, KPIs, risks, 90-day actions |

## Rebuild

From repo root:

```bash
python scripts/build_deck.py
```

Sources **PPT_V3.zip** (extracts to `PPT_V3/`). Uses slides 1, 3, 4, 5, 6 (skips file 2 — duplicate dark TAM variant). Gamma watermark is masked on export.

## Gamma reference

See `pixxel_gamma_prompts.md` for per-slide prompts and design settings.

## Source of truth

All numbers: `final.md` + `assumptions-log.md`
