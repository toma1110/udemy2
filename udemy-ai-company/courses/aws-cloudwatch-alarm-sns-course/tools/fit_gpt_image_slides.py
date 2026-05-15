#!/usr/bin/env python3
"""Fit GPT-Image2 source slides to 1920x1080 without adding text."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH = 1920
HEIGHT = 1080

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in FONT_CANDIDATES:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    scale = min(WIDTH / image.width, HEIGHT / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (WIDTH, HEIGHT), (246, 250, 254))
    x = (WIDTH - resized.width) // 2
    y = (HEIGHT - resized.height) // 2
    canvas.paste(resized, (x, y))
    return canvas


def make_contact_sheet(out_dir: Path) -> None:
    files = sorted(out_dir.glob("slide_*.png"))
    rows = (len(files) + 1) // 2
    sheet = Image.new("RGB", (1920, rows * 590 + 80), (238, 242, 248))
    draw = ImageDraw.Draw(sheet)
    label_font = font(36)
    for idx, path in enumerate(files):
        thumb = Image.open(path).resize((900, 506), Image.Resampling.LANCZOS)
        x = 35 + (idx % 2) * 940
        y = 70 + (idx // 2) * 590
        draw.text((x, y - 48), path.name, font=label_font, fill=(10, 30, 70))
        sheet.paste(thumb, (x, y))
    sheet.save(out_dir / "contact_sheet.png", "PNG")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lecture_id")
    parser.add_argument("--expected", type=int, required=True)
    args = parser.parse_args()

    section = args.lecture_id.split("-")[0]
    source_dir = ROOT / "slides" / f"{section}-gpt-image2-sources" / args.lecture_id
    out_dir = ROOT / "slides" / args.lecture_id
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = sorted(source_dir.glob("slide_*.png"))
    if len(sources) != args.expected:
        raise SystemExit(f"expected {args.expected} source slides, found {len(sources)} in {source_dir}")
    for source in sources:
        fit(Image.open(source)).save(out_dir / source.name, "PNG")
    make_contact_sheet(out_dir)
    print(f"fit {len(sources)} GPT-Image2 slides into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
