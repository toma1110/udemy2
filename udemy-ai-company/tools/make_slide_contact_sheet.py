#!/usr/bin/env python3
"""Create a contact sheet for slide PNGs in one lecture directory."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lecture_dir", type=Path)
    parser.add_argument("--columns", type=int, default=2)
    parser.add_argument("--thumb-width", type=int, default=920)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    files = sorted(args.lecture_dir.glob("slide_*.png"))
    if not files:
        raise SystemExit(f"No slide_*.png files found in {args.lecture_dir}")

    font = load_font(40)
    columns = args.columns
    rows = (len(files) + columns - 1) // columns
    label_h = 68
    gap = 40
    margin = 24

    thumbs: list[tuple[Path, Image.Image]] = []
    thumb_w = args.thumb_width
    thumb_h = 0
    for path in files:
        image = Image.open(path).convert("RGB")
        h = round(image.height * thumb_w / image.width)
        thumb_h = max(thumb_h, h)
        thumbs.append((path, image.resize((thumb_w, h), Image.Resampling.LANCZOS)))

    sheet_w = margin * 2 + columns * thumb_w + (columns - 1) * gap
    sheet_h = margin * 2 + rows * (label_h + thumb_h) + (rows - 1) * gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), (238, 242, 248))
    draw = ImageDraw.Draw(sheet)

    for i, (path, thumb) in enumerate(thumbs):
        col = i % columns
        row = i // columns
        x = margin + col * (thumb_w + gap)
        y = margin + row * (label_h + thumb_h + gap)
        draw.text((x, y), path.name, font=font, fill=(10, 30, 70))
        sheet.paste(thumb, (x, y + label_h))

    out = args.out or args.lecture_dir / "contact_sheet.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "PNG", compress_level=6)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
