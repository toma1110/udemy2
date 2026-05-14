#!/usr/bin/env python3
"""Compose GPT Image2 promo backgrounds with exact Japanese slide text."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1920
HEIGHT = 1080
NAVY = (9, 24, 52)
WHITE = (255, 255, 255)
CYAN = (56, 189, 248)
GREEN = (52, 211, 153)
AMBER = (251, 191, 36)
MUTED = (226, 232, 240)
PANEL = (8, 19, 42, 205)

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in FONT_CANDIDATES:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


F_BADGE = font(26)
F_TITLE = font(86)
F_TITLE_SMALL = font(72)
F_MESSAGE = font(42)
F_BODY = font(31)
F_FOOT = font(24)


def cover(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    scale = max(WIDTH / image.width, HEIGHT / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    x = (resized.width - WIDTH) // 2
    y = (resized.height - HEIGHT) // 2
    return resized.crop((x, y, x + WIDTH, y + HEIGHT))


def rounded_alpha(size: tuple[int, int], radius: int, fill: tuple[int, int, int, int]) -> Image.Image:
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=fill)
    return layer


def text_lines(text: str, width: int) -> list[str]:
    return textwrap.wrap(text, width=width, break_long_words=True, replace_whitespace=False)


def tokenized(text: str) -> list[str]:
    tokens: list[str] = []
    current = ""
    ascii_mode = False
    for ch in text:
        is_ascii = ch.isascii() and (ch.isalnum() or ch in "-_/.,%+")
        if current and is_ascii == ascii_mode:
            current += ch
        else:
            if current:
                tokens.append(current)
            current = ch
            ascii_mode = is_ascii
    if current:
        tokens.append(current)
    return tokens


def wrap_pixels(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    line = ""
    for token in tokenized(text):
        candidate = line + token
        box = draw.textbbox((0, 0), candidate, font=fnt)
        if line and box[2] - box[0] > max_width:
            lines.append(line.rstrip())
            line = token.lstrip()
        else:
            line = candidate
    if line:
        lines.append(line.rstrip())
    return lines


def font_fit(draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int, minimum: int) -> ImageFont.FreeTypeFont:
    size = start
    while size >= minimum:
        fnt = font(size)
        box = draw.textbbox((0, 0), text, font=fnt)
        if box[2] - box[0] <= max_width:
            return fnt
        size -= 4
    return font(minimum)


NOTE_LABELS = {
    1: ["講座の約束", "監視を運用判断へ", "AWSとSREを実践へ"],
    2: ["監視の迷子", "判断基準の不足"],
    3: ["設計から説明まで", "SLI・SLO・バーンレート"],
    4: ["IaCで作る", "作成・更新・削除まで"],
    5: ["現在形のAWS", "使いどころと制約"],
    6: ["SRE・インフラ・運用改善", "AWS CLIの基本操作"],
    7: ["最初のSLO設計", "自分のサービスへ持ち帰る"],
}


def draw_panel(base: Image.Image, slide: dict, index: int) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, WIDTH, HEIGHT), fill=(3, 7, 18, 70))
    od.rectangle((0, 0, 1040, HEIGHT), fill=(3, 7, 18, 105))
    od.polygon([(920, 0), (1205, 0), (1015, HEIGHT), (760, HEIGHT)], fill=(3, 7, 18, 45))
    base.alpha_composite(overlay)

    panel = rounded_alpha((850, 650), 34, PANEL)
    shadow = Image.new("RGBA", panel.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((20, 22, 830, 628), radius=34, fill=(0, 0, 0, 115))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    base.alpha_composite(shadow, (86, 204))
    base.alpha_composite(panel, (106, 186))

    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((150, 230, 390, 282), radius=24, fill=(15, 23, 42, 225), outline=(148, 163, 184, 150), width=2)
    draw.text((176, 244), "AWS SRE / SLO", font=F_BADGE, fill=CYAN)

    title_font = font_fit(draw, slide["title"], 735, 86, 58)
    y = 330
    for line in wrap_pixels(draw, slide["title"], title_font, 735):
        draw.text((150, y), line, font=title_font, fill=WHITE)
        y += title_font.size + 18

    y += 24
    message_font = font_fit(draw, slide["message"], 735, 42, 32)
    for line in wrap_pixels(draw, slide["message"], message_font, 735):
        draw.text((154, y), line, font=message_font, fill=GREEN)
        y += message_font.size + 14

    y += 36
    notes = NOTE_LABELS.get(index, slide.get("visual_notes", [])[:3])
    for note in notes:
        draw.rounded_rectangle((156, y + 4, 186, y + 34), radius=15, fill=CYAN)
        draw.text((206, y), str(note), font=F_BODY, fill=MUTED)
        y += 48

    draw.line((150, 900, 875, 900), fill=(148, 163, 184, 160), width=2)
    draw.text((150, 928), "AWS SRE入門: SLO導入とCloudFormationハンズオン", font=F_FOOT, fill=(203, 213, 225))
    draw.rounded_rectangle((812, 920, 898, 968), radius=20, fill=(15, 23, 42, 230), outline=(148, 163, 184, 120), width=2)
    draw.text((836, 932), f"{index}/7", font=F_FOOT, fill=WHITE)


def render(script_json: Path, source_dir: Path, out_dir: Path) -> None:
    data = json.loads(script_json.read_text(encoding="utf-8"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for slide in data["slides"]:
        index = int(slide["slide_number"])
        source = source_dir / f"slide_{index:03d}_source.png"
        if not source.exists():
            raise FileNotFoundError(source)
        base = cover(Image.open(source)).convert("RGBA")
        draw_panel(base, slide, index)
        base.convert("RGB").save(out_dir / f"slide_{index:03d}.png", "PNG", compress_level=6)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--script-json", type=Path, default=Path("udemy-ai-company/courses/aws-slo-adoption-course/scripts/promo_video_script.json"))
    parser.add_argument("--source-dir", type=Path, default=Path("udemy-ai-company/courses/aws-slo-adoption-course/slides/promo_gpt_image2_sources"))
    parser.add_argument("--out-dir", type=Path, default=Path("udemy-ai-company/courses/aws-slo-adoption-course/slides/promo_gpt_image2"))
    args = parser.parse_args()
    render(args.script_json, args.source_dir, args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
