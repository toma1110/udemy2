#!/usr/bin/env python3
"""Render promotional video slides for the AWS SLO adoption course."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1920
HEIGHT = 1080

NAVY = (16, 32, 64)
INK = (30, 41, 59)
BLUE = (34, 103, 230)
CYAN = (16, 148, 180)
GREEN = (28, 150, 94)
ORANGE = (232, 130, 38)
RED = (220, 65, 58)
PALE = (246, 249, 253)
LINE = (202, 213, 226)
WHITE = (255, 255, 255)

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        candidate = Path(path)
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


F_TITLE = font(82)
F_SUBTITLE = font(40)
F_CARD_TITLE = font(38)
F_BODY = font(31)
F_SMALL = font(25)
F_MONO = font(28)
F_HERO = font(96)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill=INK) -> None:
    tw, th = text_size(draw, text, fnt)
    x = box[0] + (box[2] - box[0] - tw) // 2
    y = box[1] + (box[3] - box[1] - th) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def wrap(text: str, max_chars: int) -> list[str]:
    rows: list[str] = []
    row = ""
    for ch in text:
        if ch == "\n":
            rows.append(row)
            row = ""
            continue
        row += ch
        if len(row) >= max_chars:
            rows.append(row)
            row = ""
    if row:
        rows.append(row)
    return rows


def draw_header(draw: ImageDraw.ImageDraw, title: str, message: str) -> None:
    draw.rectangle((0, 0, WIDTH, 172), fill=WHITE)
    draw.text((92, 46), title, font=F_TITLE, fill=NAVY)
    draw.text((96, 128), message, font=F_SMALL, fill=(71, 85, 105))
    draw.rounded_rectangle((1540, 48, 1828, 108), radius=18, fill=(235, 244, 255), outline=(190, 215, 255), width=2)
    center(draw, (1540, 48, 1828, 108), "AWS SRE / SLO", F_SMALL, BLUE)
    draw.line((92, 164, 1828, 164), fill=LINE, width=3)


def rounded_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill=WHITE, outline=LINE) -> None:
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=3)


def metric_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    value: str,
    caption: str,
    color: tuple[int, int, int],
) -> None:
    rounded_panel(draw, box)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle((x1 + 26, y1 + 26, x1 + 88, y1 + 88), radius=16, fill=color)
    center(draw, (x1 + 26, y1 + 26, x1 + 88, y1 + 88), "✓", F_CARD_TITLE, WHITE)
    draw.text((x1 + 112, y1 + 24), title, font=F_CARD_TITLE, fill=NAVY)
    draw.text((x1 + 42, y1 + 122), value, font=F_HERO, fill=color)
    for i, row in enumerate(wrap(caption, 20)):
        draw.text((x1 + 48, y1 + 246 + i * 42), row, font=F_BODY, fill=INK)


def draw_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE) -> None:
    draw.line((*start, *end), fill=color, width=8)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    head = 26
    points = [
        end,
        (int(end[0] - head * math.cos(angle - 0.55)), int(end[1] - head * math.sin(angle - 0.55))),
        (int(end[0] - head * math.cos(angle + 0.55)), int(end[1] - head * math.sin(angle + 0.55))),
    ]
    draw.polygon(points, fill=color)


def footer(draw: ImageDraw.ImageDraw, number: int) -> None:
    draw.text((96, 1012), "AWS SRE入門: SLO導入とCloudFormationハンズオン", font=F_SMALL, fill=(71, 85, 105))
    center(draw, (1720, 992, 1828, 1046), f"{number}/7", F_SMALL, (71, 85, 105))


def hero(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(241, 247, 255))
    draw.rounded_rectangle((118, 114, 1802, 252), radius=30, fill=WHITE, outline=(200, 220, 245), width=3)
    center(draw, (118, 114, 1802, 252), slide["title"], F_HERO, NAVY)
    center(draw, (120, 282, 1800, 360), slide["message"], F_SUBTITLE, BLUE)
    for i, (label, value, color) in enumerate(
        [
            ("SLI", "測る", BLUE),
            ("SLO", "決める", GREEN),
            ("Error Budget", "使う", ORANGE),
            ("Burn Rate", "気づく", RED),
        ]
    ):
        x = 150 + i * 430
        rounded_panel(draw, (x, 450, x + 350, 760), WHITE, (190, 210, 230))
        center(draw, (x, 500, x + 350, 575), label, F_CARD_TITLE, NAVY)
        center(draw, (x, 610, x + 350, 690), value, F_TITLE, color)
    center(draw, (200, 842, 1720, 908), "監視の数字を、信頼性の判断に変える", F_SUBTITLE, INK)


def problem(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw_header(draw, slide["title"], slide["message"])
    items = [
        ("アラームはある", "ただし、何を守るかが曖昧"),
        ("用語が混ざる", "SLI / SLO / SLA / エラーバジェット"),
        ("判断に使えない", "リリース停止や改善優先度に結びつかない"),
    ]
    for i, (title, body) in enumerate(items):
        y = 270 + i * 210
        rounded_panel(draw, (154, y, 1766, y + 150), WHITE, (220, 95, 90) if i == 0 else LINE)
        draw.rounded_rectangle((194, y + 36, 266, y + 108), radius=18, fill=[RED, ORANGE, BLUE][i])
        center(draw, (194, y + 36, 266, y + 108), str(i + 1), F_CARD_TITLE, WHITE)
        draw.text((316, y + 30), title, font=F_CARD_TITLE, fill=NAVY)
        draw.text((316, y + 88), body, font=F_BODY, fill=INK)


def value(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw_header(draw, slide["title"], slide["message"])
    steps = [("設計", BLUE), ("計測", CYAN), ("可視化", GREEN), ("通知", ORANGE), ("説明", RED)]
    for i, (label, color) in enumerate(steps):
        x = 110 + i * 350
        draw.rounded_rectangle((x, 390, x + 250, 600), radius=26, fill=WHITE, outline=color, width=4)
        center(draw, (x, 420, x + 250, 505), label, F_CARD_TITLE, color)
        center(draw, (x, 520, x + 250, 580), str(i + 1), F_TITLE, NAVY)
        if i < len(steps) - 1:
            draw_arrow(draw, (x + 260, 495), (x + 330, 495), color)
    metric_card(draw, (150, 720, 565, 950), "SLI", "成功率", "ユーザー体験に近い指標を選ぶ", BLUE)
    metric_card(draw, (752, 720, 1167, 950), "SLO", "99.9%", "どこまで守るかを決める", GREEN)
    metric_card(draw, (1354, 720, 1769, 950), "Burn Rate", "14x", "消費速度で早く気づく", ORANGE)


def handson(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw_header(draw, slide["title"], slide["message"])
    blocks = [
        ("CloudFormation", "template.yaml", BLUE),
        ("CloudWatch", "Metrics / Alarm", GREEN),
        ("SNS", "Notification", ORANGE),
        ("Dashboard", "SLO view", CYAN),
    ]
    for i, (title, body, color) in enumerate(blocks):
        x = 100 + i * 440
        rounded_panel(draw, (x, 305, x + 340, 555), WHITE, color)
        center(draw, (x, 338, x + 340, 410), title, F_CARD_TITLE, color)
        center(draw, (x, 452, x + 340, 510), body, F_MONO, NAVY)
        if i < len(blocks) - 1:
            draw_arrow(draw, (x + 350, 430), (x + 420, 430), BLUE)
    commands = ["validate", "create", "put-metrics", "smoke", "update", "delete"]
    for i, command in enumerate(commands):
        x = 132 + i * 280
        draw.rounded_rectangle((x, 720, x + 220, 815), radius=18, fill=(235, 244, 255), outline=(180, 210, 245), width=2)
        center(draw, (x, 720, x + 220, 815), command, F_SMALL, NAVY)
    center(draw, (160, 866, 1760, 926), "README通りに再現でき、最後に削除まで確認する", F_BODY, INK)


def aws(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw_header(draw, slide["title"], slide["message"])
    metric_card(draw, (130, 306, 650, 740), "Custom Metrics", "低コスト", "実アプリなしでSLOの形を練習する", BLUE)
    metric_card(draw, (700, 306, 1220, 740), "Application Signals", "Optional", "計装やデータ期間が必要な機能は分けて扱う", GREEN)
    metric_card(draw, (1270, 306, 1790, 740), "Course Policy", "安全", "課金や制約を明示して進める", ORANGE)
    center(draw, (180, 844, 1740, 912), "古い自作監視だけでなく、AWSの現在形も押さえる", F_SUBTITLE, INK)


def audience(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw_header(draw, slide["title"], slide["message"])
    people = [
        ("SRE志向", "信頼性を説明できるようにしたい"),
        ("インフラ担当", "CloudWatch監視をSLOに接続したい"),
        ("バックエンド担当", "ユーザー体験を指標化したい"),
        ("運用改善", "アラート疲れを減らしたい"),
    ]
    for i, (title, body) in enumerate(people):
        x = 130 + (i % 2) * 850
        y = 285 + (i // 2) * 300
        rounded_panel(draw, (x, y, x + 720, y + 220), WHITE, [BLUE, GREEN, CYAN, ORANGE][i])
        draw.ellipse((x + 42, y + 60, x + 122, y + 140), fill=[BLUE, GREEN, CYAN, ORANGE][i])
        center(draw, (x + 42, y + 60, x + 122, y + 140), "✓", F_CARD_TITLE, WHITE)
        draw.text((x + 160, y + 48), title, font=F_CARD_TITLE, fill=NAVY)
        draw.text((x + 160, y + 112), body, font=F_BODY, fill=INK)
    center(draw, (160, 910, 1760, 970), "前提: AWS CLIの基本操作ができること", F_BODY, BLUE)


def close(draw: ImageDraw.ImageDraw, slide: dict) -> None:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(244, 250, 247))
    center(draw, (120, 108, 1800, 210), slide["title"], F_TITLE, NAVY)
    center(draw, (150, 226, 1770, 292), slide["message"], F_SUBTITLE, GREEN)
    outcomes = [
        ("選ぶ", "サービスに合うSLI"),
        ("決める", "SLOとエラーバジェット"),
        ("作る", "CloudWatch基盤"),
        ("説明する", "判断と次アクション"),
    ]
    for i, (title, body) in enumerate(outcomes):
        x = 125 + i * 430
        rounded_panel(draw, (x, 410, x + 350, 720), WHITE, [BLUE, GREEN, ORANGE, RED][i])
        center(draw, (x, 448, x + 350, 535), title, F_TITLE, [BLUE, GREEN, ORANGE, RED][i])
        center(draw, (x + 20, 590, x + 330, 662), body, F_BODY, INK)
    center(draw, (150, 836, 1770, 910), "最初のSLOを、自分のサービスに持ち帰る", F_SUBTITLE, NAVY)


LAYOUTS = {
    "hero": hero,
    "problem": problem,
    "value": value,
    "handson": handson,
    "aws": aws,
    "audience": audience,
    "close": close,
}


def render(script_json: Path, output_dir: Path) -> None:
    data = json.loads(script_json.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    for slide in data["slides"]:
        image = Image.new("RGB", (WIDTH, HEIGHT), PALE)
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 172, WIDTH, HEIGHT), fill=PALE)
        layout = LAYOUTS[slide.get("layout", "hero")]
        layout(draw, slide)
        footer(draw, int(slide["slide_number"]))
        output = output_dir / f"slide_{int(slide['slide_number']):03d}.png"
        image.save(output, "PNG", optimize=True)
        print(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--script-json",
        type=Path,
        default=Path("courses/aws-slo-adoption-course/scripts/promo_video_script.json"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("courses/aws-slo-adoption-course/slides/promo"),
    )
    args = parser.parse_args()
    render(args.script_json, args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
