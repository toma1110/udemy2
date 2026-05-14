#!/usr/bin/env python3
"""Render VID-001 CloudWatch intro slides as 1920x1080 PNG files."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "slides" / "s1-l1"

NAVY = (9, 30, 66)
BLUE = (18, 93, 190)
GREEN = (28, 135, 84)
TEAL = (0, 127, 142)
ORANGE = (224, 117, 28)
RED = (215, 58, 61)
GRAY = (95, 108, 128)
PALE = (246, 250, 254)
LIGHT_BLUE = (232, 243, 255)
LIGHT_GREEN = (235, 249, 241)
LIGHT_TEAL = (231, 248, 250)
LIGHT_ORANGE = (255, 245, 232)
LIGHT_RED = (255, 239, 238)

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in FONT_CANDIDATES:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


F_TITLE = font(66)
F_SUB = font(32)
F_CARD = font(34)
F_BODY = font(27)
F_SMALL = font(22)
F_BADGE = font(25)
F_BIG = font(54)


def wrap(text: str, limit: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        current += ch
        if len(current) >= limit:
            lines.append(current)
            current = ""
    if current:
        lines.append(current)
    return lines


def center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill=NAVY) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - width) // 2
    y = box[1] + (box[3] - box[1] - height) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def base(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (1920, 1080), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 170, 1920, 1080), fill=PALE)
    center(draw, (60, 24, 1860, 88), title, F_TITLE)
    draw.line((95, 112, 960, 112), fill=BLUE, width=5)
    draw.line((960, 112, 1825, 112), fill=GREEN, width=5)
    center(draw, (80, 126, 1840, 162), subtitle, F_SUB, GRAY)
    return img, draw


def footer(draw: ImageDraw.ImageDraw, text: str) -> None:
    draw.rounded_rectangle((115, 995, 1805, 1060), radius=14, outline=BLUE, width=3, fill=(253, 254, 255))
    draw.ellipse((145, 1015, 185, 1055), fill=BLUE)
    center(draw, (145, 1015, 185, 1055), "✓", font(26), "white")
    center(draw, (205, 1005, 1778, 1052), text, F_SMALL, NAVY)


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    color=BLUE,
    fill=(255, 255, 255),
    icon: str = "1",
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=18, outline=color, width=4, fill=fill)
    draw.rounded_rectangle((x1 + 26, y1 - 18, x2 - 26, y1 + 40), radius=12, fill=color)
    center(draw, (x1 + 34, y1 - 14, x2 - 34, y1 + 35), title, F_BADGE, "white")
    draw.ellipse((x1 + 40, y1 + 74, x1 + 118, y1 + 152), outline=color, width=5, fill="white")
    center(draw, (x1 + 40, y1 + 74, x1 + 118, y1 + 152), icon, F_CARD, color)
    y = y1 + 180
    for item in lines:
        for line in wrap(item, 18 if x2 - x1 < 430 else 24):
            draw.text((x1 + 44, y), line, font=F_BODY, fill=NAVY)
            y += 38
        y += 8


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=8)
    if x2 >= x1:
        pts = [(x2, y2), (x2 - 28, y2 - 20), (x2 - 28, y2 + 20)]
    else:
        pts = [(x2, y2), (x2 + 28, y2 - 20), (x2 + 28, y2 + 20)]
    draw.polygon(pts, fill=color)


def metric_chart(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=18, outline=BLUE, width=4, fill="white")
    draw.line((x1 + 70, y2 - 70, x2 - 55, y2 - 70), fill=NAVY, width=4)
    draw.line((x1 + 70, y1 + 55, x1 + 70, y2 - 70), fill=NAVY, width=4)
    values = [0.28, 0.34, 0.42, 0.39, 0.56, 0.65, 0.58, 0.74, 0.68]
    points = []
    width = (x2 - x1 - 150) / (len(values) - 1)
    height = y2 - y1 - 145
    for idx, value in enumerate(values):
        px = x1 + 70 + int(width * idx)
        py = y2 - 70 - int(height * value)
        points.append((px, py))
    draw.line(points, fill=BLUE, width=7)
    for px, py in points:
        draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill=GREEN)
    center(draw, (x1 + 70, y2 - 58, x2 - 55, y2 - 18), "time", F_SMALL, GRAY)
    center(draw, (x1 + 8, y1 + 58, x1 + 70, y2 - 80), "value", F_SMALL, GRAY)


def slide_1() -> None:
    img, draw = base("CloudWatchの地図", "監視の部品を、まず4つに分ける")
    boxes = [(95, 290, 860, 545), (1060, 290, 1825, 545), (95, 680, 860, 935), (1060, 680, 1825, 935)]
    data = [
        ("Metrics", ["数値の時系列", "どれくらいかを見る"], BLUE, LIGHT_BLUE, "1"),
        ("Logs", ["出来事の記録", "何が起きたかを見る"], GREEN, LIGHT_GREEN, "2"),
        ("Alarm", ["条件と状態", "危ないか判断する"], ORANGE, LIGHT_ORANGE, "3"),
        ("Dashboard", ["まとめて見る画面", "表示面として使う"], TEAL, LIGHT_TEAL, "4"),
    ]
    for box, item in zip(boxes, data):
        card(draw, box, item[0], item[1], item[2], item[3], item[4])
    center(draw, (795, 548, 1125, 672), "CloudWatch", F_BIG, NAVY)
    arrow(draw, (920, 605), (860, 515), BLUE)
    arrow(draw, (1000, 605), (1060, 515), GREEN)
    arrow(draw, (920, 630), (860, 710), ORANGE)
    arrow(draw, (1000, 630), (1060, 710), TEAL)
    footer(draw, "最初に4つへ分けると、CloudWatchの画面で迷いにくくなります。")
    save(img, 1)


def slide_2() -> None:
    img, draw = base("Metrics: 数値の時系列", "どれくらいかを、時間ごとの数字で見る")
    metric_chart(draw, (110, 285, 1230, 820))
    card(draw, (1300, 285, 1810, 500), "namespace", ["サービスや用途の棚"], BLUE, LIGHT_BLUE, "棚")
    card(draw, (1300, 570, 1810, 785), "metric", ["棚に入る数値名"], GREEN, LIGHT_GREEN, "数")
    draw.rounded_rectangle((410, 850, 1510, 930), radius=16, fill="white", outline=TEAL, width=4)
    center(draw, (420, 862, 1500, 916), "dimension = どの対象の数字かを決めるラベル", F_SUB, NAVY)
    footer(draw, "メトリクスは、監視対象の変化を数字で追うための基本部品です。")
    save(img, 2)


def slide_3() -> None:
    img, draw = base("Logs: 出来事の記録", "何が起きたかを、文章やイベントで追う")
    draw.rounded_rectangle((130, 285, 1790, 825), radius=20, outline=GREEN, width=4, fill="white")
    rows = [
        ("10:01:02", "request started"),
        ("10:01:05", "database timeout"),
        ("10:01:06", "retry executed"),
        ("10:01:08", "request failed"),
    ]
    y = 345
    for idx, (time_text, body) in enumerate(rows, 1):
        fill = LIGHT_RED if idx == 2 or idx == 4 else (248, 251, 255)
        draw.rounded_rectangle((205, y, 1715, y + 82), radius=12, fill=fill, outline=(205, 216, 230), width=2)
        draw.text((245, y + 24), time_text, font=F_BODY, fill=GRAY)
        draw.text((470, y + 24), body, font=F_BODY, fill=NAVY)
        y += 108
    card(draw, (210, 850, 800, 960), "log group", ["ログのまとまり"], GREEN, LIGHT_GREEN, "G")
    card(draw, (1120, 850, 1710, 960), "log stream", ["まとまり内の流れ"], TEAL, LIGHT_TEAL, "S")
    arrow(draw, (820, 905), (1100, 905), GREEN)
    footer(draw, "ログは、数字だけでは分からない背景を確認するときに使います。")
    save(img, 3)


def slide_4() -> None:
    img, draw = base("Alarm: 条件と状態", "危ないかどうかを、条件で判断する")
    metric_chart(draw, (115, 295, 900, 780))
    draw.line((170, 455, 845, 455), fill=RED, width=7)
    center(draw, (330, 397, 700, 445), "しきいち", F_SUB, RED)
    arrow(draw, (930, 540), (1100, 540), ORANGE)
    card(draw, (1125, 290, 1785, 500), "状態", ["正常", "警告", "データ不足"], ORANGE, LIGHT_ORANGE, "!")
    card(draw, (1125, 610, 1785, 820), "アクション", ["通知", "自動処理", "調査開始"], BLUE, LIGHT_BLUE, "→")
    arrow(draw, (1455, 520), (1455, 590), ORANGE)
    footer(draw, "アラームは、数字を見て行動につなげる入口です。")
    save(img, 4)


def slide_5() -> None:
    img, draw = base("Dashboard: まとめて見る画面", "保存場所ではなく、監視情報の表示面")
    draw.rounded_rectangle((120, 270, 1800, 865), radius=24, outline=TEAL, width=5, fill="white")
    center(draw, (145, 292, 1780, 350), "Dashboard", F_BIG, NAVY)
    panels = [(190, 400, 680, 760), (715, 400, 1205, 760), (1240, 400, 1730, 760)]
    titles = [("Metric Graph", BLUE), ("Alarm State", ORANGE), ("Log Entry", GREEN)]
    for box, (title, color) in zip(panels, titles):
        draw.rounded_rectangle(box, radius=16, outline=color, width=4, fill=(250, 253, 255))
        center(draw, (box[0], box[1] + 18, box[2], box[1] + 62), title, F_BADGE, color)
    metric_chart(draw, (230, 490, 640, 720))
    center(draw, (760, 525, 1160, 625), "ALARM", F_BIG, RED)
    draw.rounded_rectangle((1290, 505, 1680, 555), radius=8, fill=LIGHT_GREEN)
    draw.rounded_rectangle((1290, 585, 1680, 635), radius=8, fill=LIGHT_RED)
    draw.rounded_rectangle((1290, 665, 1680, 715), radius=8, fill=LIGHT_BLUE)
    footer(draw, "ダッシュボードは、情報を保存する場所ではなく、見るための画面です。")
    save(img, 5)


def slide_6() -> None:
    img, draw = base("4つのつながり", "数字、出来事、判断、表示を分ける")
    boxes = [(80, 360, 430, 745), (545, 360, 895, 745), (1010, 360, 1360, 745), (1475, 360, 1825, 745)]
    items = [
        ("Dashboard", ["表示", "全体を見る"], TEAL, LIGHT_TEAL, "1"),
        ("Alarm", ["判断", "入口を見つける"], ORANGE, LIGHT_ORANGE, "2"),
        ("Metrics", ["数字", "変化を追う"], BLUE, LIGHT_BLUE, "3"),
        ("Logs", ["出来事", "背景を掘る"], GREEN, LIGHT_GREEN, "4"),
    ]
    for idx, (box, item) in enumerate(zip(boxes, items)):
        card(draw, box, item[0], item[1], item[2], item[3], item[4])
        if idx < 3:
            arrow(draw, (box[2] + 25, 552), (boxes[idx + 1][0] - 25, 552), item[2])
    footer(draw, "障害調査では、表示、判断、数字、出来事の順で見ると整理しやすくなります。")
    save(img, 6)


def slide_7() -> None:
    img, draw = base("Metricsを探す3つの言葉", "namespace、metric、dimensionで対象を絞る")
    card(draw, (110, 330, 610, 805), "namespace", ["サービスや用途ごとの棚", "例: AWSサービス単位"], BLUE, LIGHT_BLUE, "棚")
    card(draw, (710, 330, 1210, 805), "metric", ["棚に入っている数値名", "例: 利用率や回数"], GREEN, LIGHT_GREEN, "数")
    card(draw, (1310, 330, 1810, 805), "dimension", ["どの対象かを決めるラベル", "例: インスタンスや関数"], TEAL, LIGHT_TEAL, "札")
    arrow(draw, (620, 565), (690, 565), BLUE)
    arrow(draw, (1220, 565), (1290, 565), GREEN)
    footer(draw, "ネームスペース、メトリクス、ディメンションで、見たい数字を絞り込みます。")
    save(img, 7)


def slide_8() -> None:
    img, draw = base("障害時の見始め方", "全体、入口、数字、出来事の順に見る")
    boxes = [(70, 315, 430, 810), (530, 315, 890, 810), (990, 315, 1350, 810), (1450, 315, 1810, 810)]
    items = [
        ("全体", ["ダッシュボード", "どこが変か"], TEAL, LIGHT_TEAL, "1"),
        ("入口", ["アラーム", "どの条件か"], ORANGE, LIGHT_ORANGE, "2"),
        ("数字", ["メトリクス", "いつから変化したか"], BLUE, LIGHT_BLUE, "3"),
        ("出来事", ["ログ", "何が起きたか"], GREEN, LIGHT_GREEN, "4"),
    ]
    for idx, (box, item) in enumerate(zip(boxes, items)):
        card(draw, box, item[0], item[1], item[2], item[3], item[4])
        if idx < 3:
            arrow(draw, (box[2] + 20, 560), (boxes[idx + 1][0] - 20, 560), item[2])
    footer(draw, "順番を決めておくと、CloudWatchの画面で迷う時間を減らせます。")
    save(img, 8)


def slide_9() -> None:
    img, draw = base("ハンズオンと実運用IaC", "CloudFormationは教材内、実運用はCDKまたはTerraform")
    card(draw, (135, 300, 875, 840), "講座ハンズオン", ["追加ツールなしで再現", "README通りに確認", "CloudFormationを使う場合あり"], BLUE, LIGHT_BLUE, "学")
    card(draw, (1045, 300, 1785, 840), "実運用", ["チーム開発で保守", "抽象化と再利用", "CDKまたはTerraform"], GREEN, LIGHT_GREEN, "運")
    arrow(draw, (900, 570), (1020, 570), ORANGE)
    draw.rounded_rectangle((720, 870, 1200, 940), radius=16, outline=ORANGE, width=4, fill=LIGHT_ORANGE)
    center(draw, (735, 882, 1185, 928), "目的で使い分ける", F_SUB, NAVY)
    footer(draw, "本動画ではリソースを作らず、まずCloudWatchの地図を理解します。")
    save(img, 9)


def slide_10() -> None:
    img, draw = base("まとめ", "CloudWatchは4つの部品で地図化できる")
    boxes = [(95, 290, 860, 520), (1060, 290, 1825, 520), (95, 640, 860, 870), (1060, 640, 1825, 870)]
    data = [
        ("Metrics", ["数字を見る"], BLUE, LIGHT_BLUE, "数"),
        ("Logs", ["出来事を見る"], GREEN, LIGHT_GREEN, "記"),
        ("Alarm", ["判断する"], ORANGE, LIGHT_ORANGE, "!"),
        ("Dashboard", ["まとめて表示する"], TEAL, LIGHT_TEAL, "画"),
    ]
    for box, item in zip(boxes, data):
        card(draw, box, item[0], item[1], item[2], item[3], item[4])
    draw.rounded_rectangle((420, 900, 1500, 960), radius=16, fill="white", outline=BLUE, width=4)
    center(draw, (435, 910, 1485, 950), "次へ: アラーム作成、ログ調査、監視ダッシュボード", F_SMALL, NAVY)
    footer(draw, "地図を持っておくと、CloudWatchの次の学習に進みやすくなります。")
    save(img, 10)


def save(img: Image.Image, index: int) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(OUT_DIR / f"slide_{index:03d}.png", "PNG", optimize=True)


def make_contact_sheet() -> None:
    files = sorted(OUT_DIR.glob("slide_*.png"))
    rows = (len(files) + 1) // 2
    sheet = Image.new("RGB", (1920, rows * 590 + 80), (238, 242, 248))
    draw = ImageDraw.Draw(sheet)
    for idx, path in enumerate(files):
        thumb = Image.open(path).resize((900, 506), Image.Resampling.LANCZOS)
        x = 35 + (idx % 2) * 940
        y = 70 + (idx // 2) * 590
        draw.text((x, y - 48), path.name, font=font(36), fill=NAVY)
        sheet.paste(thumb, (x, y))
    sheet.save(OUT_DIR / "contact_sheet.png", "PNG", optimize=True)


def main() -> int:
    for renderer in [slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8, slide_9, slide_10]:
        renderer()
    make_contact_sheet()
    print(f"rendered {len(list(OUT_DIR.glob('slide_*.png')))} slides into {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

