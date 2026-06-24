"""Assemble Pixxel deck from Gamma PNG exports → PDF + PPTX (watermark removed)."""

from __future__ import annotations

import zipfile
from pathlib import Path

from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.util import Inches
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
PPT_V3_DIR = ROOT / "PPT_V3"
PPT_V3_ZIP = ROOT / "PPT_V3.zip"
DELIVERABLES = ROOT / "deliverables"
SLIDES_DIR = DELIVERABLES / "slides"

# PPT_V3.zip: 6 exports; file 2 is a duplicate TAM variant — use 1,3,4,5,6 for 5-page deck.
PPT_V3_SOURCES = [
    "1_58percent-blended-gross-margin.png",
    "3_Indias-satellite-based-precision-ag-analytics-market-reaches-dollar102M-by-FY2028-driven-by-PMFBY-ma.png",
    "4_PMFBY-index-underwriting-outscores-enterprise-precision-ag-390-vs-355-weighted-on-market-size-and-re.png",
    "5_SaaS-led-hybrid-55percent-Aurora-35percent-DaaS-10percent-services-maximizes-blended-margin-pure-Daa.png",
    "6_Execute-3-phase-roadmap-Prove-FY2026-Scale-FY2027-Margins-FY2028-targeting-dollar122M-India-ag-reven.png",
]

SLIDE_NAMES = [
    "01_executive_summary.png",
    "02_tam_sizing.png",
    "03_segment_selection.png",
    "04_monetization_model.png",
    "05_roadmap_next_steps.png",
]


def ensure_ppt_v3_extracted() -> None:
    if PPT_V3_DIR.is_dir() and any(PPT_V3_DIR.glob("*.png")):
        return
    if not PPT_V3_ZIP.exists():
        raise FileNotFoundError(f"Missing {PPT_V3_ZIP}")
    PPT_V3_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(PPT_V3_ZIP, "r") as zf:
        zf.extractall(PPT_V3_DIR)


def _watermark_fill_color(img: Image.Image) -> tuple[int, int, int]:
    """Sample local background along the bottom row, left of the Gamma badge."""
    w, h = img.size
    samples: list[tuple[int, int, int]] = []
    for y in (h - 10, h - 18, h - 26, h - 34):
        if y < 0:
            continue
        for x_frac in (0.55, 0.62, 0.68, 0.74, 0.80):
            x = int(w * x_frac)
            if x >= int(w * 0.835):
                continue
            samples.append(img.getpixel((x, y))[:3])

    if not samples:
        return img.getpixel((int(w * 0.06), h - 18))[:3]

    r = sum(p[0] for p in samples) // len(samples)
    g = sum(p[1] for p in samples) // len(samples)
    b = sum(p[2] for p in samples) // len(samples)
    return (r, g, b)


def remove_gamma_watermark(img: Image.Image) -> Image.Image:
    """Mask bottom-right Gamma pill badge."""
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    fill = _watermark_fill_color(img)

    # Pill badge + logo — cover generous bottom-right region.
    left = int(w * 0.825)
    top = int(h * 0.928)
    draw.rectangle([left, top, w, h], fill=fill)

    # Feather edge: narrow strip to blend any residual anti-aliasing.
    edge_left = int(w * 0.815)
    edge_right = left
    for x in range(edge_left, edge_right):
        t = (x - edge_left) / max(edge_right - edge_left, 1)
        px = img.getpixel((x, h - 16))[:3]
        blend = tuple(int(px[i] * (1 - t) + fill[i] * t) for i in range(3))
        draw.line([(x, top), (x, h)], fill=blend, width=1)

    return img


def process_slide(src: Path) -> Image.Image:
    return remove_gamma_watermark(Image.open(src))


def build_slides() -> list[Path]:
    ensure_ppt_v3_extracted()
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    for src_name, out_name in zip(PPT_V3_SOURCES, SLIDE_NAMES):
        src = PPT_V3_DIR / src_name
        if not src.exists():
            raise FileNotFoundError(f"Missing slide in PPT_V3: {src_name}")
        dst = SLIDES_DIR / out_name
        process_slide(src).save(dst, format="PNG", optimize=True)
        outputs.append(dst)

    return outputs


def build_pdf(slide_paths: list[Path], pdf_path: Path) -> None:
    first = Image.open(slide_paths[0])
    page_w, page_h = first.size
    first.close()

    c = canvas.Canvas(str(pdf_path), pagesize=(page_w, page_h))
    for slide in slide_paths:
        c.drawImage(ImageReader(str(slide)), 0, 0, width=page_w, height=page_h)
        c.showPage()
    c.save()


def build_pptx(slide_paths: list[Path], pptx_path: Path) -> None:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    for slide_path in slide_paths:
        slide = prs.slides.add_slide(blank)
        slide.shapes.add_picture(
            str(slide_path), 0, 0, width=prs.slide_width, height=prs.slide_height
        )

    prs.save(str(pptx_path))


def main() -> None:
    DELIVERABLES.mkdir(parents=True, exist_ok=True)
    slides = build_slides()

    pdf_path = DELIVERABLES / "Pixxel_Commercial_Strategy_Deck.pdf"
    pptx_path = DELIVERABLES / "Pixxel_Commercial_Strategy_Deck.pptx"

    build_pdf(slides, pdf_path)
    build_pptx(slides, pptx_path)

    print(f"Source: {PPT_V3_DIR} (from PPT_V3.zip)")
    print(f"Slides: {SLIDES_DIR}")
    for s in slides:
        print(f"  - {s.name}")
    print(f"PDF:  {pdf_path}")
    print(f"PPTX: {pptx_path}")
    print("Note: skipped PPT_V3 file 2 (duplicate TAM variant)")


if __name__ == "__main__":
    main()
