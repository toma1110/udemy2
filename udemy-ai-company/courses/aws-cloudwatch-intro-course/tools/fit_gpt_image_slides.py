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


def load_font(size: int) -> ImageFont.FreeTypeFont:
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
    label_font = load_font(36)
    for idx, path in enumerate(files):
        thumb = Image.open(path).resize((900, 506), Image.Resampling.LANCZOS)
        x = 35 + (idx % 2) * 940
        y = 70 + (idx // 2) * 590
        draw.text((x, y - 48), path.name, font=label_font, fill=(10, 30, 70))
        sheet.paste(thumb, (x, y))
    sheet.save(out_dir / "contact_sheet.png", "PNG", optimize=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--expected-count", required=True, type=int)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir if args.source_dir.is_absolute() else ROOT / args.source_dir
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    sources = sorted(source_dir.glob("slide_*.png"))
    if len(sources) != args.expected_count:
        raise SystemExit(f"expected {args.expected_count} source slides, found {len(sources)} in {source_dir}")
    for source in sources:
        fit(Image.open(source)).save(out_dir / source.name, "PNG", optimize=True)
    make_contact_sheet(out_dir)
    print(f"fit {len(sources)} GPT-Image2 slides into {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
