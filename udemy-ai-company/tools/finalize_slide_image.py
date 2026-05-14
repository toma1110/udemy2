#!/usr/bin/env python3
"""Finalize GPT-Image2 slide artwork with exact Japanese title text."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for font_path in FONT_CANDIDATES:
        path = Path(font_path)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit_canvas(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = image.convert("RGB")
    image.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, (248, 251, 255))
    x = (size[0] - image.width) // 2
    y = (size[1] - image.height) // 2
    canvas.paste(image, (x, y))
    return canvas


def wrap_text(text: str, width: int) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False))


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    spacing: int,
) -> int:
    draw.multiline_text(xy, text, font=font, fill=fill, spacing=spacing)
    bbox = draw.multiline_textbbox(xy, text, font=font, spacing=spacing)
    return bbox[3]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--section", required=True)
    args = parser.parse_args()

    if args.source == "latest":
        generated_root = Path.home() / ".codex" / "generated_images"
        source = max(generated_root.rglob("*.png"), key=lambda path: path.stat().st_mtime)
    else:
        source = Path(args.source)

    canvas = fit_canvas(Image.open(source), (1920, 1080))
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    navy = (18, 37, 63)
    blue = (43, 116, 203)
    green = (36, 153, 122)
    muted = (73, 92, 118)

    draw.rectangle((0, 0, 1920, 248), fill=(255, 255, 255, 232))
    draw.rectangle((0, 248, 1920, 252), fill=blue + (230,))
    draw.rectangle((0, 1010, 1920, 1080), fill=(255, 255, 255, 226))
    draw.rectangle((0, 1006, 1920, 1010), fill=green + (220,))

    section_font = load_font(30)
    title_font = load_font(62)
    message_font = load_font(34)

    draw.rounded_rectangle((74, 42, 238, 88), radius=10, fill=blue + (255,))
    draw.text((96, 50), args.section, font=section_font, fill=(255, 255, 255))

    title = wrap_text(args.title, width=25)
    y = draw_multiline(draw, (74, 108), title, title_font, navy, spacing=10)

    message = wrap_text(args.message, width=42)
    draw_multiline(draw, (74, max(190, y + 18)), message, message_font, muted, spacing=8)

    final = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    final.save(args.out, "PNG", optimize=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
