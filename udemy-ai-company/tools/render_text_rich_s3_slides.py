#!/usr/bin/env python3
"""Render Section 3 slides in the text-rich style used by Section 2."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1] / "courses" / "aws-slo-adoption-course"
OUT_ROOT = ROOT / "slides"

NAVY = (10, 30, 70)
BLUE = (20, 92, 190)
GREEN = (20, 136, 70)
TEAL = (0, 125, 135)
ORANGE = (230, 120, 20)
RED = (220, 55, 50)
LIGHT_BLUE = (235, 245, 255)
LIGHT_GREEN = (238, 250, 241)
LIGHT_RED = (255, 242, 240)
GRAY = (92, 104, 120)
PALE = (247, 250, 254)


FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]


def font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        p = Path(path)
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


F_TITLE = font(64)
F_SUB = font(31)
F_CARD_TITLE = font(36)
F_BODY = font(25)
F_SMALL = font(21)
F_BADGE = font(24)
F_BIG = font(58)


def wrap(text: str, limit: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        if ch == "\n":
            lines.append(current)
            current = ""
            continue
        current += ch
        if len(current) >= limit:
            lines.append(current)
            current = ""
    if current:
        lines.append(current)
    return lines


def center_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fnt, fill) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = box[0] + (box[2] - box[0] - (bbox[2] - bbox[0])) // 2
    y = box[1] + (box[3] - box[1] - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.rectangle((0, 0, 1920, 170), fill="white")
    center_text(draw, (50, 20, 1870, 88), title, F_TITLE, NAVY)
    draw.line((90, 108, 960, 108), fill=BLUE, width=5)
    draw.line((960, 108, 1830, 108), fill=GREEN, width=5)
    center_text(draw, (80, 118, 1840, 160), subtitle, F_SUB, NAVY)


def footer(draw: ImageDraw.ImageDraw, text: str) -> None:
    draw.rounded_rectangle((110, 1002, 1810, 1062), radius=14, outline=BLUE, width=3, fill=(252, 254, 255))
    draw.ellipse((136, 1016, 176, 1056), fill=BLUE)
    center_text(draw, (136, 1016, 176, 1056), "✓", font(28), "white")
    center_text(draw, (190, 1008, 1780, 1056), text, F_SMALL, NAVY)


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: list[str],
    color=BLUE,
    fill=(255, 255, 255),
    icon: str = "✓",
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=16, outline=color, width=3, fill=fill)
    draw.rounded_rectangle((x1 + 18, y1 - 18, x2 - 18, y1 + 34), radius=10, fill=color)
    center_text(draw, (x1 + 26, y1 - 16, x2 - 26, y1 + 32), title, F_BADGE, "white")
    draw.ellipse((x1 + 34, y1 + 70, x1 + 116, y1 + 152), outline=color, width=5, fill=(248, 252, 255))
    center_text(draw, (x1 + 34, y1 + 70, x1 + 116, y1 + 152), icon, F_CARD_TITLE, color)
    y = y1 + 178
    for item in body:
        for line in wrap(item, 18 if (x2 - x1) < 390 else 24):
            draw.text((x1 + 42, y), line, font=F_BODY, fill=NAVY)
            y += 36
        y += 10


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=8)
    if x2 >= x1:
        pts = [(x2, y2), (x2 - 26, y2 - 18), (x2 - 26, y2 + 18)]
    else:
        pts = [(x2, y2), (x2 + 26, y2 - 18), (x2 + 26, y2 + 18)]
    draw.polygon(pts, fill=color)


def draw_gauge(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int, value: float, label: str, color=GREEN) -> None:
    x, y = center
    box = (x - radius, y - radius, x + radius, y + radius)
    draw.arc(box, 180, 360, fill=(210, 218, 232), width=22)
    draw.arc(box, 180, 180 + int(180 * value), fill=color, width=22)
    angle = 180 + int(180 * value)
    import math

    ex = x + int((radius - 22) * math.cos(math.radians(angle)))
    ey = y + int((radius - 22) * math.sin(math.radians(angle)))
    draw.line((x, y, ex, ey), fill=NAVY, width=8)
    draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=NAVY)
    center_text(draw, (x - radius, y + 48, x + radius, y + 100), label, F_BODY, NAVY)


def draw_chart(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color=BLUE) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=14, outline=color, width=3, fill="white")
    draw.line((x1 + 42, y2 - 42, x2 - 32, y2 - 42), fill=NAVY, width=3)
    draw.line((x1 + 42, y1 + 32, x1 + 42, y2 - 42), fill=NAVY, width=3)
    pts = []
    values = [0.32, 0.45, 0.39, 0.58, 0.52, 0.68, 0.60, 0.76]
    w = (x2 - x1 - 95) / (len(values) - 1)
    h = y2 - y1 - 90
    for i, v in enumerate(values):
        pts.append((x1 + 42 + int(i * w), y2 - 42 - int(v * h)))
    draw.line(pts, fill=color, width=5)
    for p in pts:
        draw.ellipse((p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6), fill=color)


def layout_three_cards(draw, slide):
    cards = slide["cards"]
    xs = [(70, 260, 610, 845), (690, 260, 1230, 845), (1310, 260, 1850, 845)]
    colors = [BLUE, GREEN, TEAL]
    fills = [LIGHT_BLUE, LIGHT_GREEN, (238, 250, 250)]
    icons = ["✓", "2", "3"]
    for i, item in enumerate(cards[:3]):
        card(draw, xs[i], item[0], item[1], colors[i], fills[i], icons[i])
    footer(draw, slide["footer"])


def layout_flow(draw, slide):
    cards = slide["cards"]
    xs = [(70, 310, 440, 810), (530, 310, 900, 810), (990, 310, 1360, 810), (1450, 310, 1820, 810)]
    colors = [BLUE, GREEN, BLUE, GREEN]
    icons = ["1", "2", "3", "✓"]
    for i, item in enumerate(cards[:4]):
        card(draw, xs[i], item[0], item[1], colors[i], (255, 255, 255), icons[i])
        if i < min(3, len(cards) - 1):
            arrow(draw, (xs[i][2] + 18, 560), (xs[i + 1][0] - 18, 560), colors[i])
    footer(draw, slide["footer"])


def layout_compare(draw, slide):
    left, right = slide["cards"][0], slide["cards"][1]
    card(draw, (95, 290, 850, 840), left[0], left[1], RED, LIGHT_RED, "!")
    draw.line((960, 255, 960, 865), fill=(170, 185, 205), width=4)
    card(draw, (1070, 290, 1825, 840), right[0], right[1], GREEN, LIGHT_GREEN, "✓")
    arrow(draw, (880, 570), (1040, 570), BLUE)
    footer(draw, slide["footer"])


def layout_dashboard(draw, slide):
    for x in [85, 675, 1265]:
        draw.rounded_rectangle((x, 265, x + 505, 835), radius=18, outline=BLUE, width=3, fill="white")
    labels = slide["cards"]
    for i, x in enumerate([85, 675, 1265]):
        title, body = labels[i]
        draw.rounded_rectangle((x + 25, 285, x + 480, 340), radius=10, fill=[BLUE, GREEN, ORANGE][i])
        center_text(draw, (x + 35, 288, x + 470, 337), title, F_BADGE, "white")
        if i == 0:
            draw_gauge(draw, (x + 252, 500), 135, 0.78, "成功率", GREEN)
        elif i == 1:
            draw_chart(draw, (x + 78, 405, x + 430, 655), BLUE)
            center_text(draw, (x + 80, 680, x + 430, 735), "待ち時間", F_BODY, NAVY)
        else:
            draw_gauge(draw, (x + 252, 500), 135, 0.35, "エラー率", RED)
        y = 735
        for item in body[:2]:
            draw.text((x + 52, y), "✓ " + item, font=F_SMALL, fill=NAVY)
            y += 42
    footer(draw, slide["footer"])


def layout_big_gauge(draw, slide):
    title, body = slide["cards"][0]
    draw_gauge(draw, (960, 500), 240, slide.get("value", 0.72), title, slide.get("color", GREEN))
    left = slide["cards"][1]
    right = slide["cards"][2]
    card(draw, (80, 330, 520, 760), left[0], left[1], BLUE, LIGHT_BLUE, "→")
    card(draw, (1400, 330, 1840, 760), right[0], right[1], GREEN, LIGHT_GREEN, "✓")
    arrow(draw, (540, 535), (690, 535), BLUE)
    arrow(draw, (1230, 535), (1380, 535), GREEN)
    footer(draw, slide["footer"])


def render_slide(lecture: str, index: int, slide: dict) -> None:
    img = Image.new("RGB", (1920, 1080), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 170, 1920, 1080), fill=PALE)
    header(draw, slide["title"], slide["subtitle"])
    layout = slide.get("layout", "three")
    if layout == "flow":
        layout_flow(draw, slide)
    elif layout == "compare":
        layout_compare(draw, slide)
    elif layout == "dashboard":
        layout_dashboard(draw, slide)
    elif layout == "gauge":
        layout_big_gauge(draw, slide)
    else:
        layout_three_cards(draw, slide)
    out = OUT_ROOT / lecture / f"slide_{index:03d}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)


SLIDES = {
    "s3-l1": [
        {"title": "良いSLIの3条件", "subtitle": "ユーザー体験、計測可能性、改善行動の3つで選ぶ", "layout": "three", "footer": "この3条件を満たす指標を、SLOの土台にします。", "cards": [("1. 体験に近い", ["ユーザーが困ったかを説明できる", "成功、待ち時間、失敗に近い"]), ("2. 継続して測れる", ["CloudWatchやログから集められる", "毎日同じ定義で見られる"]), ("3. 行動につながる", ["悪化した時に調査先が分かる", "改善後に効果を確認できる"])]},
        {"title": "条件1: ユーザー体験に近い", "subtitle": "ユーザーが困ったかどうかを説明できる指標にする", "layout": "flow", "footer": "内部状態ではなく、ユーザー操作が成功したかを起点にします。", "cards": [("ユーザー操作", ["ログイン", "検索", "決済"]), ("体験", ["使えたか", "待たされたか"]), ("SLI候補", ["成功率", "レイテンシ"]), ("判断", ["困りごとを説明できる"])]},
        {"title": "条件2: 継続して計測できる", "subtitle": "毎日同じ定義で集められることが重要", "layout": "flow", "footer": "測れない指標は、SLOにもレビューにも使えません。", "cards": [("データ源", ["メトリクス", "ログ"]), ("集計", ["同じ分母", "同じ期間"]), ("保存", ["ダッシュボード", "履歴"]), ("運用", ["毎週レビューできる"])]},
        {"title": "条件3: 改善行動につながる", "subtitle": "悪化したときに、次の打ち手を考えられる指標にする", "layout": "flow", "footer": "SLIは、悪化を検知して改善へ進むための入口です。", "cards": [("悪化を検知", ["成功率低下", "待ち時間増加"]), ("原因を見る", ["経路", "依存先", "エラー種別"]), ("改善する", ["修正", "容量調整"]), ("効果を見る", ["SLIが戻ったか確認"])]},
        {"title": "悪いSLI: 内部都合だけを見る", "subtitle": "CPU使用率だけでは、ユーザー体験を説明しにくい", "layout": "compare", "footer": "CPUは重要ですが、ユーザーの困りごとの代表にはしません。", "cards": [("内部指標だけ", ["CPUが高い", "メモリが多い", "でもユーザー影響は不明"]), ("体験指標を主役にする", ["リクエスト成功率", "応答時間", "エラー率"])]},
        {"title": "良いSLI: 体験を測る", "subtitle": "成功率、待ち時間、エラー率から始める", "layout": "dashboard", "footer": "まずは3つの基本指標から候補を作ると、会話が進みます。", "cards": [("成功率", ["使えたか", "主要操作ごとに見る"]), ("待ち時間", ["待たされたか", "分布で見る"]), ("エラー率", ["失敗したか", "分母を決める"])]},
        {"title": "最初は1つでよい", "subtitle": "完璧な指標セットより、運用で使える1つを選ぶ", "layout": "flow", "footer": "小さく始めて、レビューしながら指標を育てます。", "cards": [("1サービス", ["対象を絞る"]), ("1操作", ["重要体験を選ぶ"]), ("1指標", ["成功率から開始"]), ("育てる", ["レイテンシを追加"])]},
        {"title": "まとめ: 良いSLIは説明できる", "subtitle": "ユーザー体験、計測、改善行動を満たすか確認する", "layout": "three", "footer": "次は、可用性、レイテンシ、エラー率を設計します。", "cards": [("体験", ["ユーザーが困ることに近い"]), ("計測", ["継続して同じ定義で測れる"]), ("改善", ["悪化時に次の行動へ進める"])]},
    ],
    "s3-l2": [
        {"title": "可用性、レイテンシ、エラー率を設計する", "subtitle": "3つの指標で、ユーザー体験を分解する", "layout": "dashboard", "footer": "使えたか、待たされたか、失敗したかを分けて設計します。", "cards": [("可用性", ["使えたか", "成功率で見る"]), ("レイテンシ", ["待たされたか", "分布で見る"]), ("エラー率", ["失敗したか", "分母を決める"])]},
        {"title": "可用性: 使えたか", "subtitle": "成功したリクエストの割合で考える", "layout": "gauge", "value": 0.82, "color": GREEN, "footer": "サーバー起動中ではなく、ユーザー操作が成功したかを見ます。", "cards": [("成功率", [""]), ("分母", ["対象リクエスト", "主要操作"]), ("分子", ["成功した操作", "期待どおりの応答"])]},
        {"title": "レイテンシ: 待たされたか", "subtitle": "応答時間は平均ではなく分布で見る", "layout": "dashboard", "footer": "一部の遅い体験は、平均だけでは見えにくくなります。", "cards": [("平均", ["全体を丸める"]), ("p95", ["日常的な遅さ"]), ("p99", ["深刻な遅さ"])]},
        {"title": "エラー率: 失敗したか", "subtitle": "どの失敗をエラーとして数えるかを決める", "layout": "compare", "footer": "分母と分子の定義がずれると、チームごとに違う数字になります。", "cards": [("数える失敗", ["5系エラー", "タイムアウト", "重要操作の失敗"]), ("分けて扱うもの", ["入力ミス", "権限不足", "ヘルスチェック"])]},
        {"title": "分母を先に決める", "subtitle": "どのリクエストを対象にするかで意味が変わる", "layout": "flow", "footer": "対象にする操作を決めてから、成功と失敗を定義します。", "cards": [("全リクエスト", ["管理画面", "ヘルスチェック"]), ("対象を選ぶ", ["主要操作", "ユーザー影響"]), ("分母", ["測る対象"]), ("SLI", ["意味が揃う"])]},
        {"title": "目標水準を置く", "subtitle": "指標だけでなく、どこまで許容するかを決める", "layout": "three", "footer": "SLIに目標水準を置くと、SLOとして判断できます。", "cards": [("可用性", ["月間成功率", "99.9%など"]), ("レイテンシ", ["p95", "300ミリ秒以内など"]), ("エラー率", ["失敗率", "許容範囲を決める"])]},
        {"title": "組み合わせて見る", "subtitle": "1つの指標だけで、体験全体は説明できない", "layout": "dashboard", "footer": "成功率が高くても、待ち時間が長ければ体験は悪くなります。", "cards": [("成功率", ["正常に見える"]), ("待ち時間", ["悪化を検知"]), ("重要操作", ["一部だけ失敗"])]},
        {"title": "まとめ: 体験を3つに分ける", "subtitle": "使えたか、待たされたか、失敗したかを定義する", "layout": "three", "footer": "次は、レイテンシをパーセンタイルで見る理由を扱います。", "cards": [("使えたか", ["可用性"]), ("待たされたか", ["レイテンシ"]), ("失敗したか", ["エラー率"])]},
    ],
    "s3-l3": [
        {"title": "p95/p99を使う理由", "subtitle": "平均では見えない、遅いユーザー体験を見る", "layout": "dashboard", "footer": "レイテンシSLIでは、分布の後ろ側を見ることが重要です。", "cards": [("平均", ["全体を丸める"]), ("p95", ["95%が収まる"]), ("p99", ["より遅い体験を拾う"])]},
        {"title": "平均は体験を丸める", "subtitle": "一部の遅さが、全体の中に隠れる", "layout": "compare", "footer": "遅いリクエストに当たったユーザーの体験は、平均では説明しきれません。", "cards": [("平均だけ", ["多くが速いと良く見える", "遅い少数が隠れる"]), ("分布を見る", ["遅いユーザーを拾う", "体験悪化を説明できる"])]},
        {"title": "パーセンタイルとは", "subtitle": "速い側から何番目かを見る", "layout": "flow", "footer": "p95は95%がその時間以内、p99は99%がその時間以内という意味です。", "cards": [("並べる", ["応答時間を速い順にする"]), ("位置を見る", ["95番目", "99番目"]), ("後ろ側", ["遅い体験を確認"]), ("判断", ["SLO目標に使う"])]},
        {"title": "p95は日常的な遅さを見る", "subtitle": "多くのユーザーに影響する遅さを把握しやすい", "layout": "gauge", "value": 0.68, "color": BLUE, "footer": "最初のレイテンシSLIは、p95から始めると会話しやすくなります。", "cards": [("p95", [""]), ("特徴", ["極端な揺れを受けにくい", "日常的な遅さを見る"]), ("使いどころ", ["一般的な操作", "最初の目標設定"])]},
        {"title": "p99は深刻な遅さを見る", "subtitle": "少数でも痛みが大きい体験を拾う", "layout": "gauge", "value": 0.9, "color": ORANGE, "footer": "決済や認証など、痛みが大きい操作ではp99も見ます。", "cards": [("p99", [""]), ("特徴", ["分布のかなり後ろを見る", "少数の強い不満を拾う"]), ("注意", ["少量データでは揺れやすい"])]},
        {"title": "どちらを使うか", "subtitle": "重要度とノイズの大きさで選ぶ", "layout": "three", "footer": "重要操作ほど後ろ側を見る一方、少量データでは期間や指標を調整します。", "cards": [("p95から開始", ["トラフィックが少ない", "日常の遅さを把握"]), ("p99も見る", ["重要操作", "離脱影響が大きい"]), ("期間を調整", ["短すぎると揺れる", "長すぎると遅れる"])]},
        {"title": "CloudWatchでは期間も見る", "subtitle": "集計期間が短すぎると、判断が不安定になる", "layout": "flow", "footer": "期間設計は、後半のSLOとバーンレート設計につながります。", "cards": [("短い期間", ["変化に早い", "揺れやすい"]), ("長い期間", ["安定する", "気づきが遅い"]), ("目的", ["検知", "レビュー"]), ("設計", ["窓を使い分ける"])]},
        {"title": "まとめ: 平均ではなく分布を見る", "subtitle": "遅いユーザー体験を、パーセンタイルで拾う", "layout": "three", "footer": "次は、AWSサービス別にSLI候補を整理します。", "cards": [("平均", ["全体を丸める"]), ("p95", ["日常的な遅さ"]), ("p99", ["深刻な遅さ"])]},
    ],
    "s3-l4": [
        {"title": "AWSサービス別SLI選定ガイド", "subtitle": "サービス名からではなく、ユーザー体験から逆算する", "layout": "flow", "footer": "まずユーザー操作を決め、そこからAWSメトリクスを選びます。", "cards": [("ユーザー操作", ["ログイン", "検索", "決済"]), ("体験", ["成功", "待ち時間"]), ("AWS部品", ["ALB", "API Gateway"]), ("メトリクス", ["SLI候補にする"])]},
        {"title": "ALB: 入口の成功と遅さ", "subtitle": "外部リクエストの成功率と応答時間を見る", "layout": "three", "footer": "入口に近いので、サービス全体のユーザー影響をつかみやすいです。", "cards": [("成功率", ["2系応答", "期待した応答"]), ("失敗", ["5系エラー", "ターゲット失敗"]), ("応答時間", ["TargetResponseTime", "遅さを把握"])]},
        {"title": "API Gateway: API利用者の体験", "subtitle": "成功、失敗、レイテンシをエンドポイント単位で見る", "layout": "flow", "footer": "重要なエンドポイントを分けると、悪化を見逃しにくくなります。", "cards": [("API全体", ["まとめすぎ注意"]), ("主要操作", ["ログイン", "決済"]), ("エンドポイント", ["単位を分ける"]), ("SLI", ["成功率と遅さ"])]},
        {"title": "ECSとLambda: 実行基盤だけで判断しない", "subtitle": "基盤メトリクスは補助、体験メトリクスを主役にする", "layout": "compare", "footer": "実行基盤の状態は、体験指標と組み合わせて判断します。", "cards": [("基盤だけ", ["CPU", "実行時間", "失敗回数"]), ("体験と組み合わせる", ["入口の成功率", "主要操作の遅さ", "エラー率"])]},
        {"title": "RDS: 直接のSLIではなく原因分析に使う", "subtitle": "データベース状態は、体験悪化の調査に使う", "layout": "compare", "footer": "DBメトリクスは、ユーザー体験が悪化した後の原因分析で力を発揮します。", "cards": [("体験SLI", ["画面が遅い", "エラーが増えた"]), ("RDS指標", ["接続数", "待ち時間", "CPU", "ストレージ"])]},
        {"title": "Application Signals: 体験に近い入口", "subtitle": "サービスレベルの可用性とレイテンシを扱いやすい", "layout": "three", "footer": "考えかたと、実アプリ計装やデータ期間の制約を分けて扱います。", "cards": [("可用性", ["サービス単位で見る"]), ("レイテンシ", ["体験に近い遅さ"]), ("制約", ["計装が必要", "データ期間が必要"])]},
        {"title": "サービス別ではなく操作別に整理する", "subtitle": "ログイン、検索、決済などの主要操作を軸にする", "layout": "flow", "footer": "AWSサービスは、ユーザー操作を支える部品として整理します。", "cards": [("ログイン", ["認証", "API"]), ("検索", ["API", "DB"]), ("決済", ["外部依存", "DB"]), ("SLI候補", ["操作ごとに選ぶ"])]},
        {"title": "まとめ: 体験からメトリクスへ", "subtitle": "ユーザー操作を決めてから、AWSメトリクスを選ぶ", "layout": "three", "footer": "次は、CPU使用率をSLIにしない理由を扱います。", "cards": [("操作を決める", ["誰の何を守るか"]), ("体験を分解", ["成功", "待ち時間", "失敗"]), ("メトリクスを選ぶ", ["入口を主役", "内部は補助"])]},
    ],
    "s3-l5": [
        {"title": "CPU使用率をSLIにしない理由", "subtitle": "内部状態とユーザー体験を混同しない", "layout": "compare", "footer": "CPUは重要ですが、ユーザー体験そのものではありません。", "cards": [("内部状態", ["CPU使用率", "メモリ", "キュー"]), ("ユーザー体験", ["成功したか", "待たされたか", "失敗したか"])]},
        {"title": "CPUは内部状態", "subtitle": "ユーザーが見ているのは、成功と待ち時間", "layout": "three", "footer": "内部状態がよく見えても、ユーザー体験が悪いことはあります。", "cards": [("ユーザー", ["画面が開くか", "操作が完了するか"]), ("体験SLI", ["成功率", "レイテンシ"]), ("内部指標", ["CPU", "メモリ", "DB"])]},
        {"title": "高いCPUが悪いとは限らない", "subtitle": "負荷に応じて効率よく使えている場合もある", "layout": "gauge", "value": 0.86, "color": ORANGE, "footer": "成功率と待ち時間が守られているなら、緊急度は変わります。", "cards": [("高CPU", [""]), ("問題が小さい例", ["成功率が維持", "待ち時間も正常"]), ("確認するもの", ["スケール", "ユーザー影響"])]},
        {"title": "低いCPUでも体験は悪化する", "subtitle": "待ち時間の原因はCPU以外にもある", "layout": "three", "footer": "CPUだけを見ていると、外部依存やDB待ちを見逃します。", "cards": [("DB待ち", ["接続枯渇", "クエリ遅延"]), ("外部依存", ["API待ち", "タイムアウト"]), ("ネットワーク", ["遅延", "再送"])]},
        {"title": "SLIは外側、原因分析は内側", "subtitle": "まず体験を見て、次に内部メトリクスで調べる", "layout": "flow", "footer": "体験指標で検知し、内部指標で原因を探します。", "cards": [("外側", ["成功率", "待ち時間"]), ("悪化検知", ["SLO違反", "アラート"]), ("内側", ["CPU", "DB", "Queue"]), ("改善", ["原因に手を打つ"])]},
        {"title": "アラートの主語を変える", "subtitle": "「CPUが高い」より「ユーザー体験が悪い」を優先する", "layout": "compare", "footer": "重要アラートは、ユーザー影響を中心に設計します。", "cards": [("CPUが高い", ["原因候補", "補助アラート"]), ("体験が悪い", ["重要アラート", "対応判断に使える"])]},
        {"title": "CPUは捨てない", "subtitle": "SLIではなく、診断と容量計画に使う", "layout": "three", "footer": "指標の目的を分けることで、監視とSLOが整理されます。", "cards": [("原因分析", ["どこが詰まったか"]), ("容量計画", ["増強タイミング"]), ("コスト最適化", ["使いすぎ", "余りすぎ"])]},
        {"title": "まとめ: ユーザー体験を先に置く", "subtitle": "CPU使用率は補助指標として活かす", "layout": "three", "footer": "Section 4では、AWSでSLOをどう計測するかに進みます。", "cards": [("SLI", ["成功率", "待ち時間", "エラー率"]), ("補助指標", ["CPU", "DB", "メモリ"]), ("判断", ["体験から運用へつなぐ"])]},
    ],
}


def make_contact_sheet(lecture: str) -> None:
    files = sorted((OUT_ROOT / lecture).glob("slide_*.png"))
    sheet = Image.new("RGB", (1920, 4 * 620), (238, 242, 248))
    draw = ImageDraw.Draw(sheet)
    label_font = font(40)
    for i, path in enumerate(files):
        thumb = Image.open(path).resize((920, 518), Image.Resampling.LANCZOS)
        x = 20 + (i % 2) * 960
        y = 76 + (i // 2) * 620
        draw.text((x, y - 60), path.name, font=label_font, fill=NAVY)
        sheet.paste(thumb, (x, y))
    sheet.save(OUT_ROOT / lecture / "contact_sheet.png", "PNG", optimize=True)


def main() -> int:
    for lecture, slides in SLIDES.items():
        for i, slide in enumerate(slides, 1):
            render_slide(lecture, i, slide)
        make_contact_sheet(lecture)
        print(f"{lecture}: {len(slides)} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
