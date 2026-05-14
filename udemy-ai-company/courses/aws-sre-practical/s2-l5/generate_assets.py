from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


W = 1600
H = 760
OUT_DIR = Path(__file__).resolve().parent / "assets"

BG_TOP = (18, 24, 46)
BG_BOTTOM = (9, 13, 29)
CARD_BG = (24, 31, 56)
CARD_ALT = (29, 38, 68)
TEXT = (235, 239, 245)
MUTED = (158, 171, 195)
ORANGE = (255, 153, 0)
BLUE = (88, 166, 255)
LBLUE = (121, 199, 227)
GREEN = (86, 211, 100)
RED = (255, 107, 107)
PURPLE = (147, 112, 219)
GRID = (42, 50, 83)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    raise FileNotFoundError("font not found")


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def fit_font(draw: ImageDraw.ImageDraw, text: str, size: int, max_width: int, min_size: int = 13) -> ImageFont.FreeTypeFont:
    for font_size in range(size, min_size - 1, -1):
        font = get_font(font_size)
        if text_width(draw, text, font) <= max_width:
            return font
    return get_font(min_size)


def split_long_token(draw: ImageDraw.ImageDraw, token: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    parts: list[str] = []
    current = ""
    for ch in token:
        candidate = current + ch
        if current and text_width(draw, candidate, font) > max_width:
            parts.append(current)
            current = ch
        else:
            current = candidate
    if current:
        parts.append(current)
    return parts


def wrap_line(draw: ImageDraw.ImageDraw, line: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    if not line or text_width(draw, line, font) <= max_width:
        return [line]

    words = line.split(" ")
    if len(words) == 1:
        return split_long_token(draw, line, font, max_width)

    lines: list[str] = []
    current = ""
    for word in words:
        candidates = split_long_token(draw, word, font, max_width)
        for part in candidates:
            candidate = part if not current else f"{current} {part}"
            if current and text_width(draw, candidate, font) > max_width:
                lines.append(current)
                current = part
            else:
                current = candidate
    if current:
        lines.append(current)
    return lines


def draw_fit_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    max_width: int,
    size: int,
    fill: tuple[int, int, int],
    min_size: int = 13,
) -> None:
    font = fit_font(draw, text, size, max_width, min_size=min_size)
    draw.text(xy, text, font=font, fill=fill)


def draw_fit_text_with_visible_underscores(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    max_width: int,
    size: int,
    fill: tuple[int, int, int],
    min_size: int = 13,
) -> None:
    font = fit_font(draw, text, size, max_width, min_size=min_size)
    draw.text(xy, text, font=font, fill=fill)

    marker = "CLI_COMMANDS.md"
    start = 0
    while True:
        idx = text.find(marker, start)
        if idx == -1:
            break
        prefix = text[:idx]
        ux1 = xy[0] + text_width(draw, prefix + "CLI", font)
        ux2 = xy[0] + text_width(draw, prefix + "CLI_", font)
        line_y = xy[1] + font.size + 1
        draw.line((ux1 + 1, line_y, ux2 - 1, line_y), fill=fill, width=2)
        start = idx + len(marker)


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    max_width: int,
    size: int,
    fill: tuple[int, int, int],
    max_lines: int | None = None,
    min_size: int = 13,
    line_gap: int = 5,
) -> None:
    chosen_font = get_font(min_size)
    chosen_lines: list[str] = []
    for font_size in range(size, min_size - 1, -1):
        font = get_font(font_size)
        lines: list[str] = []
        for raw in text.splitlines():
            lines.extend(wrap_line(draw, raw, font, max_width))
        if max_lines is None or len(lines) <= max_lines:
            chosen_font = font
            chosen_lines = lines
            break
        chosen_font = font
        chosen_lines = lines

    if max_lines is not None:
        chosen_lines = chosen_lines[:max_lines]

    x, y = xy
    line_height = chosen_font.size + line_gap
    for idx, line in enumerate(chosen_lines):
        draw.text((x, y + idx * line_height), line, font=chosen_font, fill=fill)


def canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG_BOTTOM)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / max(H - 1, 1)
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        draw.line((0, y, W, y), fill=(r, g, b))

    for x in range(0, W, 48):
        draw.line((x, 0, x, H), fill=(20, 26, 46))
    for y in range(0, H, 48):
        draw.line((0, y, W, y), fill=(20, 26, 46))

    draw.rounded_rectangle((28, 28, W - 28, H - 28), radius=30, outline=(36, 46, 80), width=2)
    draw.rectangle((40, 40, 48, H - 40), fill=ORANGE)
    return img, draw


def title(draw: ImageDraw.ImageDraw, main: str, sub: str) -> None:
    font_main = get_font(42)
    font_sub = get_font(24)
    draw.text((84, 56), main, font=font_main, fill=TEXT)
    draw.text((86, 112), sub, font=font_sub, fill=MUTED)


def card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], label: str, sub: str, color: tuple[int, int, int]) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=24, fill=CARD_BG, outline=(51, 62, 101), width=2)
    draw.rounded_rectangle((x1 + 18, y1 + 18, x1 + 112, y1 + 94), radius=18, fill=color)
    icon_font = get_font(28)
    draw.text((x1 + 46, y1 + 41), label[:2], font=icon_font, fill=(10, 15, 28))
    text_x = x1 + 138
    max_width = max(80, x2 - text_x - 24)
    draw_fit_text(draw, (text_x, y1 + 34), label, max_width, 28, TEXT, min_size=18)
    draw_wrapped_text(draw, (text_x, y1 + 76), sub, max_width, 18, MUTED, max_lines=2, min_size=13, line_gap=5)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: tuple[int, int, int], label: str = "") -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=8)
    draw.polygon(
        [
            (x2, y2),
            (x2 - 28, y2 - 16),
            (x2 - 28, y2 + 16),
        ],
        fill=color,
    )
    if label:
        font = get_font(18)
        tw = draw.textbbox((0, 0), label, font=font)[2]
        lx = (x1 + x2 - tw) // 2
        ly = min(y1, y2) - 30
        draw.rounded_rectangle((lx - 10, ly - 4, lx + tw + 10, ly + 28), radius=12, fill=(20, 26, 48))
        draw.text((lx, ly), label, font=font, fill=color)


def terminal(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], lines: list[str], accent: tuple[int, int, int] = BLUE) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=18, fill=(12, 16, 30), outline=(54, 68, 110), width=2)
    draw.rectangle((x1, y1, x2, y1 + 36), fill=(24, 30, 53))
    for i, c in enumerate((RED, ORANGE, GREEN)):
        cx = x1 + 18 + i * 22
        draw.ellipse((cx, y1 + 11, cx + 12, y1 + 23), fill=c)
    font = get_font(18)
    draw.text((x1 + 110, y1 + 8), "terminal", font=font, fill=MUTED)

    inner_width = x2 - x1 - 36
    content_height = y2 - (y1 + 52) - 12
    mono = get_font(14)
    line_height = 22
    for size in range(20, 13, -1):
        candidate = get_font(size)
        candidate_line_height = size + 8
        widths_fit = all(text_width(draw, line, candidate) <= inner_width for line in lines)
        heights_fit = len(lines) * candidate_line_height <= content_height
        if widths_fit and heights_fit:
            mono = candidate
            line_height = candidate_line_height
            break

    cy = y1 + 52
    for line in lines:
        fill = accent if line.startswith("$") else TEXT
        draw.text((x1 + 18, cy), line, font=mono, fill=fill)
        cy += line_height


def checklist(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], items: list[tuple[str, bool]]) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=24, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((x1 + 28, y1 + 22), "Verification Checklist", font=get_font(26), fill=TEXT)
    cy = y1 + 76
    for label, ok in items:
        fill = GREEN if ok else ORANGE
        draw.rounded_rectangle((x1 + 28, cy - 2, x1 + 58, cy + 28), radius=10, fill=fill)
        draw.text((x1 + 35, cy + 1), "OK" if ok else "!", font=get_font(16), fill=(12, 18, 30))
        draw.text((x1 + 78, cy), label, font=get_font(22), fill=TEXT)
        cy += 52


def badge(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, color: tuple[int, int, int]) -> None:
    x, y = xy
    font = get_font(18)
    tw = draw.textbbox((0, 0), text, font=font)[2]
    draw.rounded_rectangle((x, y, x + tw + 24, y + 34), radius=17, fill=color)
    draw.text((x + 12, y + 7), text, font=font, fill=(12, 18, 30))


def resource_note(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, width: int = 760) -> None:
    x, y = xy
    draw.rounded_rectangle((x, y, x + width, y + 46), radius=16, fill=(20, 26, 48), outline=(54, 66, 106), width=2)
    badge(draw, (x + 14, y + 6), "GitHubリソース", BLUE)
    draw_fit_text_with_visible_underscores(draw, (x + 190, y + 12), text, width - 212, 20, TEXT, min_size=15)


def save(img: Image.Image, name: str) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    img.save(OUT_DIR / name)


def make_title_overview() -> None:
    img, draw = canvas()
    title(draw, "ハンズオン全体像", "三層構成のデプロイから可観測性の設定、最後の確認までを一気に進める")

    card(draw, (80, 180, 360, 320), "ALB", "入口", ORANGE)
    card(draw, (400, 180, 680, 320), "EC2", "Flask App", BLUE)
    card(draw, (720, 180, 1000, 320), "RDS", "MySQL", GREEN)
    arrow(draw, (360, 250), (400, 250), ORANGE, "HTTP")
    arrow(draw, (680, 250), (720, 250), GREEN, "SQL")

    card(draw, (1100, 120, 1480, 220), "CW", "Metrics / Logs", LBLUE)
    card(draw, (1100, 250, 1480, 350), "XR", "Trace", PURPLE)
    card(draw, (1100, 365, 1480, 465), "S3", "ALB Access Logs", GREEN)
    arrow(draw, (840, 320), (1100, 170), LBLUE)
    arrow(draw, (840, 320), (1100, 300), PURPLE)
    arrow(draw, (220, 320), (1100, 430), GREEN)

    draw.text((84, 470), "進めるステップ", font=get_font(28), fill=TEXT)
    steps = [
        ("1", "Cloud\nFormation", ORANGE),
        ("2", "Flask\nDeploy", BLUE),
        ("3", "CWAgent", LBLUE),
        ("4", "CW Logs", BLUE),
        ("5", "X-Ray", PURPLE),
        ("6", "ALB Logs", GREEN),
    ]
    x = 84
    for idx, (num, label, color) in enumerate(steps):
        draw.rounded_rectangle((x, 520, x + 210, 620), radius=20, fill=CARD_ALT, outline=(56, 68, 108), width=2)
        draw.rounded_rectangle((x + 18, 546, x + 66, 594), radius=16, fill=color)
        draw.text((x + 33, 557), num, font=get_font(22), fill=(10, 15, 28))
        draw_wrapped_text(draw, (x + 82, 543), label, 108, 19, TEXT, max_lines=2, min_size=15, line_gap=2)
        if idx < len(steps) - 1:
            arrow(draw, (x + 210, 570), (x + 240, 570), color)
        x += 250

    badge(draw, (84, 650), "deploy", ORANGE)
    badge(draw, (194, 650), "observe", LBLUE)
    badge(draw, (320, 650), "verify", GREEN)
    save(img, "slide_001_handson_overview.png")


def make_cloudformation() -> None:
    img, draw = canvas()
    title(draw, "STEP 1: CloudFormationで環境を自動構築", "テンプレートを一度アップロードすれば、本番想定の基盤をまとめて作成")
    terminal(draw, (90, 180, 620, 480), [
        "$ aws cloudformation create-stack",
        "  --stack-name sre-handson",
        "  --template-body file://sre-handson-base.yml",
        "",
        "CREATE_IN_PROGRESS ...",
        "CREATE_COMPLETE",
    ], ORANGE)
    card(draw, (760, 180, 1110, 330), "VPC", "ネットワーク基盤", BLUE)
    card(draw, (1160, 180, 1510, 330), "ALB", "入口のロードバランサー", ORANGE)
    card(draw, (760, 390, 1110, 540), "EC2", "Flaskアプリ実行環境", BLUE)
    card(draw, (1160, 390, 1510, 540), "RDS", "MySQLデータベース", GREEN)
    arrow(draw, (620, 250), (740, 250), ORANGE, "stack create")
    arrow(draw, (620, 430), (740, 430), LBLUE, "resource provisioning")
    badge(draw, (90, 520), "5-8 min", ORANGE)
    badge(draw, (220, 520), "reproducible", BLUE)
    badge(draw, (384, 520), "IaC", GREEN)
    resource_note(draw, (760, 612), "CloudFormationテンプレートとCLI_COMMANDS.mdを同じリポジトリに配置", width=720)
    save(img, "slide_005_cloudformation.png")


def make_production_extension() -> None:
    img, draw = canvas()
    title(draw, "補足: この構成は学習用の最小構成", "本番運用では、可用性・セキュリティ・運用性を段階的に強化する")

    draw.rounded_rectangle((90, 170, 740, 610), radius=26, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((126, 202), "このハンズオンで学ぶ土台", font=get_font(30), fill=TEXT)
    lab_items = [
        ("ALB + EC2 + RDS", "三層構成の基本"),
        ("CloudWatch Logs / Metrics", "調査の入口"),
        ("X-Ray / Trace", "リクエストの流れ"),
        ("S3 ALB Logs", "アクセス分析の材料"),
    ]
    cy = 266
    for label, sub in lab_items:
        draw.rounded_rectangle((126, cy, 700, cy + 58), radius=18, fill=(18, 24, 44))
        draw.rounded_rectangle((146, cy + 14, 172, cy + 40), radius=8, fill=BLUE)
        draw.text((194, cy + 10), label, font=get_font(22), fill=TEXT)
        draw.text((472, cy + 13), sub, font=get_font(18), fill=MUTED)
        cy += 74

    draw.rounded_rectangle((860, 170, 1510, 610), radius=26, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((896, 202), "実案件で追加するベストプラクティス", font=get_font(30), fill=TEXT)
    prod_items = [
        ("Multi-AZ / Auto Scaling", "単一障害点を減らす", ORANGE),
        ("Private Subnet / Session Manager", "直接SSHを避ける", LBLUE),
        ("RDS Backup / Encryption / Multi-AZ", "データを守る", GREEN),
        ("ACM HTTPS / Secrets Manager", "通信と認証情報を守る", PURPLE),
        ("Alarms / Dashboard / OTel", "検知と分析を強化", RED),
    ]
    cy = 258
    for label, sub, color in prod_items:
        draw.rounded_rectangle((896, cy, 1470, cy + 54), radius=18, fill=(18, 24, 44))
        draw.rounded_rectangle((916, cy + 13, 942, cy + 39), radius=8, fill=color)
        draw_fit_text(draw, (964, cy + 8), label, 290, 21, TEXT, min_size=15)
        draw_fit_text(draw, (1268, cy + 11), sub, 178, 17, MUTED, min_size=13)
        cy += 64

    arrow(draw, (740, 390), (860, 390), ORANGE, "extend")
    draw.rounded_rectangle((250, 642, 1350, 694), radius=22, fill=(18, 24, 44), outline=(54, 66, 106), width=2)
    draw.text((284, 657), "まず最小構成で運用データの見方を理解し、必要に応じて本番レベルへ拡張します。", font=get_font(24), fill=TEXT)
    save(img, "slide_003_production_extension.png")


def make_deploy() -> None:
    img, draw = canvas()
    title(draw, "STEP 2: FlaskアプリをEC2へデプロイ", "GitHubから取得したTODOアプリをEC2上で起動し、RDSへ接続")
    terminal(draw, (80, 180, 720, 560), [
        "$ git clone https://github.com/.../sre-todo-app.git",
        "$ cd sre-todo-app",
        "$ pip3 install -r requirements.txt",
        '$ export DB_HOST="rds-endpoint"',
        '$ export DB_PASSWORD="******"',
        "$ python3 app.py",
        "Running on http://0.0.0.0:5000",
    ], BLUE)
    card(draw, (820, 210, 1120, 360), "EC2", "Flask App / Gunicorn候補", BLUE)
    card(draw, (1180, 210, 1490, 360), "RDS", "todo_items テーブル", GREEN)
    arrow(draw, (1120, 285), (1180, 285), GREEN, "SQL")
    draw.rounded_rectangle((820, 430, 1490, 620), radius=24, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((848, 454), "TODO App Preview", font=get_font(30), fill=TEXT)
    draw.rounded_rectangle((850, 500, 1450, 560), radius=16, fill=(245, 247, 250))
    draw_fit_text(draw, (878, 516), "ALB DNS -> /  [Deploy] [Metrics] [Traces]", 540, 22, (28, 34, 50), min_size=16)
    draw.rounded_rectangle((850, 576, 1450, 604), radius=14, fill=(226, 233, 244))
    badge(draw, (820, 150), "SSH", ORANGE)
    badge(draw, (920, 150), "Flask", BLUE)
    badge(draw, (1038, 150), "MySQL", GREEN)
    save(img, "slide_006_flask_deploy.png")


def make_metrics() -> None:
    img, draw = canvas()
    title(draw, "STEP 3: CloudWatch Agentでメトリクスを収集", "CPUだけでなく、メモリとディスク使用率もEC2から送信")
    card(draw, (120, 240, 520, 420), "EC2", "CW Agent installed\nmem / disk metrics", BLUE)
    card(draw, (1040, 240, 1460, 420), "CW", "CloudWatch Metrics\nCWAgent namespace", LBLUE)
    arrow(draw, (520, 330), (1040, 330), LBLUE, "push metrics")
    draw.rounded_rectangle((560, 220, 1000, 450), radius=24, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((592, 248), "amazon-cloudwatch-agent.json", font=get_font(28), fill=TEXT)
    terminal(draw, (588, 286, 972, 436), [
        '"metrics_collected": {',
        '  "mem": {},',
        '  "disk": { "resources": ["/"] }',
        '}',
    ], GREEN)
    draw.rounded_rectangle((200, 500, 1380, 640), radius=26, fill=(18, 24, 44), outline=(54, 66, 106), width=2)
    draw.text((236, 532), "CWAgent Dashboard", font=get_font(30), fill=TEXT)
    for idx, (label, value, color) in enumerate([
        ("CPU", "21%", ORANGE),
        ("Memory", "63%", BLUE),
        ("Disk", "48%", GREEN),
    ]):
        x = 260 + idx * 360
        draw.rounded_rectangle((x, 566, x + 280, 616), radius=18, fill=CARD_BG)
        draw.text((x + 22, 580), label, font=get_font(20), fill=MUTED)
        draw.text((x + 190, 576), value, font=get_font(24), fill=color)
    resource_note(draw, (560, 660), "CloudWatch Agentの設定・確認コマンドはCLI_COMMANDS.mdを参照", width=820)
    save(img, "slide_007_cwagent_metrics.png")


def make_logs() -> None:
    img, draw = canvas()
    title(draw, "STEP 4: CloudWatch Logsへアプリログを転送", "EC2上の app.log を一箇所へ集約し、調査をしやすくする")
    card(draw, (100, 220, 470, 400), "APP", "/home/ec2-user/...\napp.log", BLUE)
    card(draw, (1110, 220, 1490, 400), "LOG", "/sre-handson/app\ninstance_id stream", ORANGE)
    arrow(draw, (470, 310), (1110, 310), ORANGE, "collect_list")
    terminal(draw, (540, 190, 1020, 430), [
        '{',
        '  "file_path": "/home/.../app.log",',
        '  "log_group_name": "/sre-handson/app",',
        '  "log_stream_name": "{instance_id}"',
        '}',
    ], ORANGE)
    draw.rounded_rectangle((180, 490, 1420, 650), radius=26, fill=(14, 18, 32), outline=(54, 66, 106), width=2)
    draw.text((218, 520), "Recent log events", font=get_font(28), fill=TEXT)
    sample = [
        "2026-04-30T07:32:10Z INFO GET / health=200 latency=18ms",
        "2026-04-30T07:32:16Z INFO POST /todos user=demo status=201",
        "2026-04-30T07:32:24Z WARN db retry count=1 endpoint=rds-endpoint",
    ]
    cy = 566
    for line in sample:
        draw.text((220, cy), line, font=get_font(20), fill=LBLUE)
        cy += 30
    save(img, "slide_008_cloudwatch_logs.png")


def make_xray() -> None:
    img, draw = canvas()
    title(draw, "STEP 5: X-Rayでリクエストの流れを見える化", "Flaskアプリに数行追加し、サービスマップとトレースを取得")
    terminal(draw, (80, 200, 720, 520), [
        "from aws_xray_sdk.core import xray_recorder",
        "from aws_xray_sdk.ext.flask.middleware import XRayMiddleware",
        "",
        "xray_recorder.configure(service='sre-todo-app')",
        "XRayMiddleware(app, xray_recorder)",
        "$ sudo systemctl start xray",
    ], PURPLE)
    card(draw, (860, 210, 1130, 360), "ALB", "entry point", ORANGE)
    card(draw, (1160, 210, 1430, 360), "APP", "Flask handler", BLUE)
    card(draw, (1010, 430, 1280, 580), "DB", "MySQL query", GREEN)
    arrow(draw, (1130, 285), (1160, 285), ORANGE, "HTTP")
    arrow(draw, (1295, 360), (1160, 430), LBLUE, "subsegment")
    draw.rounded_rectangle((820, 140, 1480, 620), radius=28, outline=(111, 93, 156), width=3)
    draw.text((858, 160), "X-Ray Service Map", font=get_font(30), fill=TEXT)
    badge(draw, (820, 646), "trace latency", PURPLE)
    badge(draw, (970, 646), "error hotspot", RED)
    badge(draw, (1130, 646), "dependency view", BLUE)
    resource_note(draw, (80, 646), "X-Ray SDK / IAM / 確認コマンドはCLI_COMMANDS.mdを参照", width=720)
    save(img, "slide_009_xray_trace.png")


def make_alb_logs() -> None:
    img, draw = canvas()
    title(draw, "STEP 6: ALBアクセスログをS3へ保存", "レスポンスタイムやHTTPステータスを後から分析できるようにする")
    card(draw, (140, 240, 500, 420), "ALB", "access log enabled", ORANGE)
    card(draw, (1120, 240, 1460, 420), "S3", "sre-handson-alb-logs\n<account-id>", GREEN)
    arrow(draw, (500, 330), (1120, 330), GREEN, "gzip log objects")
    draw.rounded_rectangle((570, 190, 1050, 470), radius=24, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((600, 220), "Captured fields", font=get_font(28), fill=TEXT)
    items = [
        "client_ip",
        "target_processing_time",
        "elb_status_code",
        "target_status_code",
        "request_uri",
    ]
    cy = 268
    for item in items:
        draw.text((612, cy), f"• {item}", font=get_font(22), fill=LBLUE)
        cy += 38
    terminal(draw, (250, 520, 1360, 660), [
        'h2 2026-04-30T07:35:02Z app/sre-handson-alb 203.0.113.10:443 ... "GET / HTTP/1.1" 200 200',
        'h2 2026-04-30T07:35:06Z app/sre-handson-alb 203.0.113.10:443 ... "POST /todos HTTP/1.1" 302 302',
    ], GREEN)
    save(img, "slide_010_alb_s3_logs.png")


def make_verify() -> None:
    img, draw = canvas()
    title(draw, "動作確認: すべてつながっているか確認", "ブラウザ・メトリクス・ログ・トレース・アクセスログの5点を横断チェック")
    checklist(draw, (90, 190, 770, 610), [
        ("ALB DNSでTODOアプリが表示される", True),
        ("CWAgent namespaceにメモリ/ディスクが届く", True),
        ("/sre-handson/app にログが届く", True),
        ("X-Rayサービスマップにトレースが出る", True),
        ("S3にALBログオブジェクトが作成される", True),
    ])
    draw.rounded_rectangle((860, 190, 1490, 610), radius=24, fill=CARD_ALT, outline=(60, 72, 112), width=2)
    draw.text((896, 218), "Observability Snapshot", font=get_font(28), fill=TEXT)
    for idx, (label, color) in enumerate([
        ("Browser", ORANGE),
        ("Metrics", BLUE),
        ("Logs", LBLUE),
        ("Trace", PURPLE),
        ("S3", GREEN),
    ]):
        y = 270 + idx * 62
        draw.rounded_rectangle((900, y, 1450, y + 42), radius=16, fill=(18, 24, 44))
        draw.rounded_rectangle((916, y + 10, 936, y + 30), radius=8, fill=color)
        draw.text((954, y + 8), label, font=get_font(22), fill=TEXT)
        draw.text((1240, y + 8), "healthy", font=get_font(20), fill=color)
    badge(draw, (90, 642), "ready for section 3", GREEN)
    save(img, "slide_011_verification.png")


def make_shutdown() -> None:
    img, draw = canvas()
    title(draw, "作業後はEC2・RDSを必ず停止", "ハンズオン後の無駄な課金を防ぎ、RDSの7日自動再起動も意識する")
    card(draw, (120, 220, 520, 420), "EC2", "Instance state -> Stop", ORANGE)
    card(draw, (620, 220, 1020, 420), "RDS", "Actions -> Stop\n7 days later auto-start", RED)
    card(draw, (1120, 220, 1480, 420), "$", "monthly cost guard", GREEN)
    arrow(draw, (320, 450), (320, 610), ORANGE, "stop after lab")
    arrow(draw, (820, 450), (820, 610), RED, "remember 7-day limit")
    draw.rounded_rectangle((120, 610, 1480, 680), radius=22, fill=(53, 24, 28), outline=(140, 54, 60), width=2)
    draw.text((154, 632), "Long break? Take an RDS snapshot first, then delete unused resources to avoid surprise charges.", font=get_font(24), fill=(255, 214, 214))
    badge(draw, (120, 160), "cost control", GREEN)
    badge(draw, (264, 160), "stop > delete when idle", ORANGE)
    save(img, "slide_012_shutdown.png")


def main() -> None:
    make_title_overview()
    make_production_extension()
    make_cloudformation()
    make_deploy()
    make_metrics()
    make_logs()
    make_xray()
    make_alb_logs()
    make_verify()
    make_shutdown()


if __name__ == "__main__":
    main()
