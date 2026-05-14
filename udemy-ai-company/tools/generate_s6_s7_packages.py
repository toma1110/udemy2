#!/usr/bin/env python3
"""Generate Section 6 and 7 lecture scripts, tickets, and slide PNGs."""

from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "aws-slo-adoption-course"

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

NAVY = (13, 34, 63)
BLUE = (41, 111, 205)
GREEN = (28, 145, 102)
TEAL = (24, 139, 148)
ORANGE = (223, 127, 35)
RED = (218, 70, 62)
MUTED = (89, 105, 128)
BG = (245, 248, 252)
CARD = (255, 255, 255)
LIGHT_BLUE = (232, 243, 255)
LIGHT_GREEN = (235, 250, 242)
LIGHT_ORANGE = (255, 246, 232)
LIGHT_RED = (255, 241, 240)


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for item in FONT_CANDIDATES:
        path = Path(item)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


F_SECTION = load_font(27)
F_TITLE = load_font(58)
F_MESSAGE = load_font(34)
F_CARD_TITLE = load_font(31)
F_BODY = load_font(25)
F_SMALL = load_font(21)
F_BIG = load_font(74)
F_MONO = load_font(28)


def wrap_jp(text: str, limit: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        current += ch
        if ch == "\n":
            lines.append(current.rstrip())
            current = ""
        elif len(current) >= limit:
            lines.append(current)
            current = ""
    if current:
        lines.append(current)
    return lines


def text_center(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, font, fill=NAVY) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - width) // 2
    y = box[1] + (box[3] - box[1] - height) // 2
    draw.text((x, y), text, font=font, fill=fill)


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font, fill, limit: int, line_gap: int) -> int:
    x, y = xy
    for line in wrap_jp(text, limit):
        draw.text((x, y), line, font=font, fill=fill)
        y += line_gap
    return y


@dataclass(frozen=True)
class Slide:
    title: str
    message: str
    narration: str
    visual_notes: list[str]
    layout: str
    cards: list[tuple[str, list[str]]]
    footer: str
    value: float = 0.72
    color: tuple[int, int, int] = GREEN


@dataclass(frozen=True)
class Lecture:
    task_id: str
    issue_number: int | None
    lecture_id: str
    section: int
    lecture_no: int
    title: str
    lecture_type: str
    owner: str
    reviewer: str
    department: str
    slides: list[Slide]


def slide(
    title: str,
    message: str,
    narration: str,
    notes: list[str],
    layout: str,
    cards: list[tuple[str, list[str]]],
    footer: str,
    value: float = 0.72,
    color: tuple[int, int, int] = GREEN,
) -> Slide:
    return Slide(title, message, narration, notes, layout, cards, footer, value, color)


LECTURES: list[Lecture] = [
    Lecture(
        "TASK-0100",
        None,
        "s6-l1",
        6,
        1,
        "エラーバジェットの計算",
        "Concept",
        "AI-Production-01",
        "AI-QA-01",
        "production",
        [
            slide(
                "エラーバジェットの計算",
                "信頼性の余白を、時間と失敗数で説明できるようにする",
                "このレクチャーでは、エラーバジェットの計算を扱います。エラーバジェットは、エスエルオーを守るために、どれくらい失敗を許容できるかを表す余白です。計算式そのものは難しくありません。大事なのは、数字を開発と運用の判断に使える形にすることです。",
                ["Section 6の導入", "SLO targetからError Budgetへ変換する流れ", "時間とリクエスト数の2軸"],
                "flow",
                [("SLO", ["守りたい水準", "例: 99.9%"]), ("許容失敗", ["100%との差分", "0.1%"]), ("期間", ["月間", "週次レビュー"]), ("判断材料", ["残量", "消費速度"])],
                "エラーバジェットは、信頼性をどこまで使えるかを示す運用の余白です。",
            ),
            slide(
                "基本式",
                "エラーバジェット = 100% - SLO目標",
                "まず基本式です。エスエルオー目標が九十九点九パーセントなら、許容できる失敗割合は〇点一パーセントです。つまり、全体のうち〇点一パーセントまでなら、目標の範囲内として扱える、という意味になります。",
                ["Formula card", "99.9% SLO -> 0.1% budget", "差分を強調"],
                "formula",
                [("SLO目標", ["99.9%"]), ("差分", ["100% - 99.9%"]), ("予算", ["0.1%"])],
                "まずは、目標との差分を失敗の予算として見るだけです。",
            ),
            slide(
                "時間で見る",
                "月間99.9%なら、約43分の余白",
                "時間で見ると、直感的に理解しやすくなります。月間のエスエルオーが九十九点九パーセントなら、月の〇点一パーセントがエラーバジェットです。三十日で考えると、およそ四十三分です。この四十三分を、障害や劣化でどれだけ使ったかを追います。",
                ["30 days -> 43.2 minutes", "calendar visual", "budget as time tank"],
                "gauge",
                [("43.2分", [""]), ("期間", ["30日", "43,200分"]), ("予算", ["0.1%", "約43分"])],
                "時間換算すると、残り余白をチームで説明しやすくなります。",
                0.72,
                ORANGE,
            ),
            slide(
                "リクエスト数で見る",
                "100万リクエストなら、失敗許容は1000件",
                "リクエストベースで考える場合は、全リクエスト数に許容失敗割合をかけます。たとえば月間百番リクエストで、エスエルオーが九十九点九パーセントなら、許容失敗は千件です。時間ではなく、成功と失敗の件数で管理する見方です。",
                ["1,000,000 requests", "0.1% failure budget", "1,000 failed requests"],
                "formula",
                [("全体", ["1,000,000件"]), ("許容率", ["0.1%"]), ("許容失敗", ["1,000件"])],
                "request-based SLOでは、失敗件数として予算を追えます。",
            ),
            slide(
                "残量を計算する",
                "使った分を引くと、今残っている余白が見える",
                "エラーバジェットは、作って終わりではありません。許容できる失敗から、実際に起きた失敗を引くことで、残量が分かります。残りが多いのか、急速に減っているのかを見ることで、リリース判断や改善優先度の会話ができます。",
                ["Initial budget -> consumed -> remaining", "progress bar", "remaining budget"],
                "flow",
                [("予算", ["許容失敗", "1000件"]), ("消費", ["実際の失敗", "250件"]), ("残量", ["750件", "75%残り"]), ("判断", ["継続", "改善"])],
                "残量を見ることで、信頼性を運用判断に接続できます。",
            ),
            slide(
                "悪い使い方",
                "予算を使い切るまで放置する数字ではない",
                "注意点もあります。エラーバジェットは、使い切るまで何もしなくてよい数字ではありません。短時間で急に消費しているなら、月末にまだ残っていても危険です。そこで次のレクチャーから、消費速度、つまりバーンレートを扱います。",
                ["Do not wait until zero", "burn speed warning", "budget tank draining too fast"],
                "compare",
                [("放置する", ["残りがあるから大丈夫", "急な消費を見落とす"]), ("速度を見る", ["今どれだけ速く減っているか", "早めに手を打てる"])],
                "残量だけでなく、減り方を見ることが次のテーマです。",
            ),
            slide(
                "チームに伝える形",
                "割合、時間、件数を相手に合わせて使い分ける",
                "チームに伝えるときは、割合だけでなく、時間や件数にも変換します。エンジニアには失敗件数、マネジメントには残り割合、オンコールには残り時間が伝わりやすいことがあります。同じ数字でも、相手に合わせて表現を変えます。",
                ["Audience-specific presentation", "engineer/ops/management cards"],
                "three",
                [("エンジニア", ["失敗件数", "対象リクエスト"]), ("オンコール", ["残り時間", "急な消費"]), ("マネジメント", ["残り割合", "判断への影響"])],
                "説明形式を変えると、エラーバジェットが使われる数字になります。",
            ),
            slide(
                "まとめ",
                "エラーバジェットは、SLO目標から計算する信頼性の余白",
                "まとめです。エラーバジェットは、百パーセントとエスエルオー目標の差分です。時間で見れば許容できる劣化時間、リクエスト数で見れば許容できる失敗件数になります。次は、この予算がどれくらいの速さで減っているか、バーンレートを見ていきます。",
                ["Summary cards", "formula/time/requests", "next burn rate"],
                "three",
                [("計算", ["100% - SLO"]), ("見方", ["時間", "失敗件数"]), ("次", ["消費速度", "バーンレート"])],
                "次は、エラーバジェットの消費速度を扱います。",
            ),
        ],
    ),
    Lecture(
        "TASK-0101",
        None,
        "s6-l2",
        6,
        2,
        "バーンレートとは何か",
        "Concept",
        "AI-Production-01",
        "AI-QA-01",
        "production",
        [
            slide(
                "バーンレートとは何か",
                "エラーバジェットを、予定より何倍の速さで使っているか",
                "このレクチャーでは、バーンレートを扱います。バーンレートは、エラーバジェットを予定より何倍の速さで使っているかを表す数字です。残り予算だけではなく、今の消費速度を見ることで、対応の緊急度を判断しやすくなります。",
                ["Burn rate definition", "budget tank with speed meter", "倍速表現"],
                "gauge",
                [("バーンレート", [""]), ("意味", ["消費速度", "予定比で見る"]), ("判断", ["緊急度", "対応タイミング"])],
                "バーンレートは、エラーバジェットの減り方を表す速度計です。",
                0.82,
                ORANGE,
            ),
            slide(
                "1倍の意味",
                "期間ちょうどで予算を使い切るペース",
                "バーンレート一倍は、対象期間が終わるタイミングで、ちょうどエラーバジェットを使い切るペースです。月間予算を一か月で使い切る速度なので、理論上は目標ぴったりです。ただし、常に一倍に張り付いているなら余裕はありません。",
                ["1x burn rate", "month-long budget timeline", "normal pace"],
                "flow",
                [("予算", ["月間分"]), ("速度", ["1倍"]), ("到達", ["月末で使い切り"]), ("状態", ["余裕は小さい"])],
                "一倍は安全というより、余裕なく予定通り使っている状態です。",
            ),
            slide(
                "14倍の意味",
                "月間予算を、約2日で使い切るペース",
                "バーンレート十四倍なら、月間のエラーバジェットを約二日で使い切るペースです。これは、月末まで待つ判断ではありません。短時間で続けば、すぐに目標違反へ近づくため、対応優先度を上げるサインになります。",
                ["14x burn rate", "30 days / 14 = about 2 days", "urgent indicator"],
                "gauge",
                [("14倍", [""]), ("意味", ["約2日で枯渇"]), ("対応", ["早めに確認", "必要なら止血"])],
                "倍数が大きいほど、同じ失敗率でも緊急度は高くなります。",
                0.92,
                RED,
            ),
            slide(
                "失敗率から計算する",
                "実際の失敗率 ÷ 許容失敗率",
                "計算は、実際の失敗率を、エスエルオーで許容した失敗率で割ります。許容失敗率が〇点一パーセントで、今の失敗率が一パーセントなら、バーンレートは十倍です。許容ペースの十倍で予算を使っている、という意味になります。",
                ["actual failure rate / allowed failure rate", "0.1% -> 1.0% = 10x"],
                "formula",
                [("実失敗率", ["1.0%"]), ("許容失敗率", ["0.1%"]), ("結果", ["10倍"])],
                "バーンレートは、失敗率を許容失敗率で割ると計算できます。",
            ),
            slide(
                "残量だけでは遅い",
                "まだ残っていても、急速に減っているなら危険",
                "残量だけを見ると、判断が遅れることがあります。まだ七十パーセント残っていても、今の速度が高ければ、数時間後には大きく減っているかもしれません。バーンレートは、この急な悪化を早く見つけるための指標です。",
                ["Remaining budget vs burn speed", "compare slow drain and fast drain"],
                "compare",
                [("残量だけ", ["まだ70%ある", "急な悪化に気づきにくい"]), ("速度も見る", ["何倍で減っているか", "対応の前倒しができる"])],
                "残量と速度をセットで見ると、判断が早くなります。",
            ),
            slide(
                "バーンレートとアラート",
                "単発の失敗ではなく、予算消費の速さで通知する",
                "バーンレートを使うと、単発エラーではなく、エラーバジェットの消費速度でアラートを設計できます。少しのエラーでも長く続けば問題になりますし、短時間でも強い悪化なら急ぎます。重要なのは、ユーザー体験への影響と緊急度を合わせることです。",
                ["Burn-rate alert flow", "short burst vs sustained issue", "budget-aware alerting"],
                "flow",
                [("失敗率", ["今の悪化"]), ("予算", ["許容範囲"]), ("速度", ["何倍か"]), ("通知", ["緊急度に合わせる"])],
                "バーンレートアラートは、予算消費に基づく通知です。",
            ),
            slide(
                "使いどころ",
                "オンコール、リリース判断、週次レビューで使う",
                "バーンレートは、オンコールだけの数字ではありません。オンコールでは緊急度判断に使い、リリース判断では一時停止や継続の根拠に使います。週次レビューでは、どの時間帯に予算を使ったかを振り返る材料になります。",
                ["Use cases", "on-call/release/review cards"],
                "three",
                [("オンコール", ["緊急度判断", "止血"]), ("リリース判断", ["継続", "一時停止"]), ("レビュー", ["消費要因", "改善計画"])],
                "バーンレートは、検知だけでなく意思決定にも使います。",
            ),
            slide(
                "まとめ",
                "バーンレートは、エラーバジェット消費の速度",
                "まとめです。バーンレートは、実際の失敗率を許容失敗率で割った数字です。一倍なら予定通り、十倍なら許容ペースの十倍で予算を使っています。次は、短期窓と長期窓を組み合わせて、ノイズと見逃しを減らす方法を見ます。",
                ["Summary", "definition/formula/next windows"],
                "three",
                [("定義", ["消費速度"]), ("計算", ["実失敗率 ÷ 許容失敗率"]), ("次", ["短期窓", "長期窓"])],
                "次は、短期窓と長期窓の組み合わせに進みます。",
            ),
        ],
    ),
    Lecture(
        "TASK-0102",
        None,
        "s6-l3",
        6,
        3,
        "短期窓と長期窓の組み合わせ",
        "Concept",
        "AI-Production-01",
        "AI-QA-01",
        "production",
        [
            slide(
                "短期窓と長期窓の組み合わせ",
                "速い検知と、ノイズ抑制を両立する",
                "このレクチャーでは、バーンレートアラートでよく使う、短期窓と長期窓の組み合わせを扱います。短期窓は変化に早く反応します。長期窓は一時的なノイズを抑えます。この二つを組み合わせることで、見逃しと誤報を減らします。",
                ["Short window and long window", "two time-series panels", "noise vs detection"],
                "dashboard",
                [("短期窓", ["早く気づく", "ノイズ多め"]), ("長期窓", ["傾向を見る", "安定する"]), ("組み合わせ", ["両方で判断", "誤報を減らす"])],
                "速さと安定性を、二つの時間窓で分担します。",
            ),
            slide(
                "短期窓",
                "数分の悪化にすばやく反応する",
                "短期窓は、いっぷん、五分、十分のような短い範囲で状態を見ます。急な障害には早く気づけますが、少数のエラーや一時的な揺れにも反応しやすくなります。短期窓だけで通知すると、誤報が増えがちです。",
                ["Short window details", "1m/5m/10m", "fast but noisy"],
                "gauge",
                [("短期", [""]), ("強み", ["早い検知"]), ("弱み", ["ノイズに弱い", "誤報が増える"])],
                "短期窓は、速い代わりに揺れやすい見方です。",
                0.78,
                ORANGE,
            ),
            slide(
                "長期窓",
                "数十分から数時間の傾向を見る",
                "長期窓は、三十分、一時間、六時間のような長い範囲で状態を見ます。一時的なノイズに強く、継続的な悪化を見つけやすい一方で、検知は遅くなります。長期窓だけでは、急な障害への初動が遅れることがあります。",
                ["Long window details", "30m/1h/6h", "stable but slower"],
                "gauge",
                [("長期", [""]), ("強み", ["安定した傾向"]), ("弱み", ["初動が遅い", "短い障害に弱い"])],
                "長期窓は、安定する代わりに反応が遅くなります。",
                0.58,
                BLUE,
            ),
            slide(
                "両方を満たす条件",
                "短期も長期も悪いときに通知する",
                "実運用では、短期窓と長期窓の両方がしきいちを超えたときに通知する設計がよく使われます。短期だけ悪い場合は一時的なノイズかもしれません。長期も悪いなら、継続的にエラーバジェットを使っている可能性が高くなります。",
                ["AND condition", "short window alarm + long window alarm -> page"],
                "flow",
                [("短期", ["急な悪化"]), ("長期", ["継続傾向"]), ("両方", ["信頼度が上がる"]), ("通知", ["対応へ進む"])],
                "短期と長期のAND条件で、誤報を減らします。",
            ),
            slide(
                "高いバーンレート",
                "短い窓でも、強い悪化はすぐ拾う",
                "高いバーンレートは、短時間でも強い悪化を示します。たとえば、十四倍のように高い速度で予算を消費しているなら、短期窓でも早めに拾う価値があります。これは、ユーザー影響が急速に広がるケースへの備えです。",
                ["High burn rate", "urgent lane", "14x threshold"],
                "compare",
                [("低いしきいち", ["小さな悪化", "長く見る"]), ("高いしきいち", ["強い悪化", "早く見る"])],
                "強い悪化ほど、短い窓で早く検知します。",
            ),
            slide(
                "低いバーンレート",
                "弱い悪化は、長い窓で継続性を見る",
                "一方で、低いバーンレートの悪化は、すぐに緊急対応するほどではないかもしれません。その場合は、長い窓で継続しているかを見ます。ゆっくり予算を削っている問題は、週次レビューや計画的改善にもつなげられます。",
                ["Low burn rate", "slow drain over hours", "planned improvement"],
                "flow",
                [("小さな悪化", ["すぐ止血ではない"]), ("長く見る", ["継続性を確認"]), ("レビュー", ["原因を整理"]), ("改善", ["計画に入れる"])],
                "弱い悪化は、長期窓で傾向として扱います。",
            ),
            slide(
                "設計の考え方",
                "通知したい緊急度から逆算する",
                "しきいちや時間窓は、暗記するものではありません。どれくらい速く予算が減ったら、誰を呼びたいのかから逆算します。深夜に起こす通知なのか、営業時間内に見る通知なのかで、短期窓と長期窓の組み合わせは変わります。",
                ["Alert policy design", "who gets notified", "urgency ladder"],
                "three",
                [("誰に", ["オンコール", "担当チーム"]), ("いつ", ["即時", "営業時間"]), ("なぜ", ["予算枯渇リスク", "ユーザー影響"])],
                "時間窓は、通知の緊急度から設計します。",
            ),
            slide(
                "まとめ",
                "短期窓は速さ、長期窓は信頼度を担当する",
                "まとめです。短期窓は早く気づくため、長期窓は一時的なノイズを抑えるために使います。両方を組み合わせることで、必要な通知だけを出しやすくなります。次は、この考え方を使って、バーンレートアラームを設計します。",
                ["Summary", "short=fast, long=confidence, next=alarm design"],
                "three",
                [("短期", ["速い検知"]), ("長期", ["安定した判断"]), ("次", ["アラーム設計"])],
                "次は、バーンレートアラームを設計します。",
            ),
        ],
    ),
    Lecture(
        "TASK-0103",
        None,
        "s6-l4",
        6,
        4,
        "バーンレートAlarmを設計する",
        "Hands-on",
        "AI-Engineer-01",
        "AI-QA-01",
        "engineering / production",
        [
            slide(
                "バーンレートAlarmを設計する",
                "CloudWatchで、予算消費速度に基づく通知へ落とし込む",
                "このレクチャーでは、バーンレートアラームの設計を扱います。実装の細部よりも、何をメトリクスにし、どの時間窓で評価し、どの緊急度で通知するかを整理します。クラウドウォッチアラームに落とし込む前の設計図を作るイメージです。",
                ["Hands-on design intro", "CloudWatch Alarm from burn rate", "design sheet"],
                "flow",
                [("SLI", ["失敗率"]), ("予算", ["許容失敗率"]), ("バーンレート", ["速度を計算"]), ("Alarm", ["通知へ接続"])],
                "まず設計図を作り、それをCloudWatch Alarmへ落とします。",
            ),
            slide(
                "入力を決める",
                "分母、分子、許容失敗率を固定する",
                "最初に、入力を決めます。分母は対象リクエスト、分子は失敗リクエストです。さらに、エスエルオー目標から許容失敗率を決めます。ここが曖昧なままだと、アラームの意味も曖昧になります。",
                ["Input definition", "good/bad/total", "allowed failure rate"],
                "three",
                [("分母", ["対象リクエスト", "全体件数"]), ("分子", ["失敗リクエスト", "5系など"]), ("許容率", ["100% - SLO", "例: 0.1%"])],
                "アラームの前に、分母と分子を固定します。",
            ),
            slide(
                "Metric Mathで速度にする",
                "実失敗率を、許容失敗率で割る",
                "次に、メトリクスマスでバーンレートを計算します。実際の失敗率を許容失敗率で割ることで、何倍の速度で予算を使っているかが出ます。CloudWatchでは、メトリクスを直接見るだけでなく、計算式をアラーム対象にできます。",
                ["Metric Math expression", "failure_rate / allowed_failure_rate", "single time series"],
                "formula",
                [("実失敗率", ["errors / total"]), ("許容率", ["0.1%"]), ("速度", ["burn rate"])],
                "Metric Mathで、失敗率をバーンレートの時系列に変換します。",
            ),
            slide(
                "短期アラーム",
                "急な悪化を拾うための条件",
                "短期アラームは、急な悪化を拾うために使います。たとえば五分間のバーンレートが高い状態を見ます。ここでは、単発の一分だけではなく、数データポイント続いたかを見ることで、ノイズを少し減らします。",
                ["Short-window alarm", "5 minutes", "datapoints to alarm"],
                "gauge",
                [("短期Alarm", [""]), ("期間", ["5分など"]), ("目的", ["急な悪化", "早い検知"])],
                "短期アラームは、強い悪化を早く拾うための条件です。",
                0.86,
                ORANGE,
            ),
            slide(
                "長期アラーム",
                "継続的な悪化を確認する条件",
                "長期アラームは、悪化が続いているかを確認するために使います。三十分や一時間の範囲でバーンレートを見ると、一時的な揺れを抑えられます。短期と長期を組み合わせることで、通知の信頼度を上げます。",
                ["Long-window alarm", "30 minutes or 1 hour", "stability"],
                "gauge",
                [("長期Alarm", [""]), ("期間", ["30分", "1時間"]), ("目的", ["継続確認", "誤報低減"])],
                "長期アラームは、悪化が続いているかを見る条件です。",
                0.62,
                BLUE,
            ),
            slide(
                "Composite Alarmでまとめる",
                "短期と長期をAND条件で扱う",
                "短期と長期の二つのアラームを作ったら、コンポジットアラームでまとめる考え方があります。短期も長期も悪いときだけ通知すれば、単発ノイズを避けやすくなります。ハンズオンでは、構成と考え方をリードミーに沿って確認します。",
                ["Composite Alarm", "short AND long", "single notification"],
                "flow",
                [("短期Alarm", ["早い"]), ("長期Alarm", ["安定"]), ("AND", ["両方悪い"]), ("通知", ["SNSへ"])],
                "Composite Alarmで、通知条件を運用しやすくまとめます。",
            ),
            slide(
                "通知先を分ける",
                "高緊急度と低緊急度を同じ扱いにしない",
                "通知設計では、すべてを同じ宛先に送らないことも重要です。高いバーンレートは即時対応、低いバーンレートはレビューや営業時間内対応に分けられます。通知先は、エスエヌエスやチャット連携に接続する前に、緊急度で整理します。",
                ["Severity routing", "high/low urgency", "SNS topic routing"],
                "compare",
                [("高緊急度", ["強い悪化", "即時確認", "オンコール"]), ("低緊急度", ["ゆっくり消費", "営業時間", "週次レビュー"])],
                "通知先は、バーンレートの緊急度に合わせて分けます。",
            ),
            slide(
                "まとめ",
                "入力、計算、時間窓、通知先を順番に決める",
                "まとめです。バーンレートアラームは、分母と分子を決め、失敗率を計算し、許容失敗率で割り、短期窓と長期窓で評価します。最後に、緊急度に合わせて通知先を決めます。次のセクションでは、これらを見せるダッシュボードへ進みます。",
                ["Summary checklist", "input/math/windows/routing", "next dashboard"],
                "three",
                [("入力", ["分母", "分子"]), ("評価", ["短期窓", "長期窓"]), ("通知", ["緊急度", "宛先"])],
                "次は、SLOダッシュボードを作ります。",
            ),
        ],
    ),
    Lecture(
        "TASK-0104",
        None,
        "s7-l1",
        7,
        1,
        "見るべき指標と見せるべき指標",
        "Concept",
        "AI-Production-01",
        "AI-QA-01",
        "production",
        [
            slide(
                "見るべき指標と見せるべき指標",
                "運用担当とマネジメントでは、必要な粒度が違う",
                "このセクションでは、エスエルオーダッシュボードを作ります。最初に大事なのは、見るべき指標と見せるべき指標を分けることです。運用担当は原因調査のために細かい情報が必要です。一方で、マネジメントには判断に必要な要約が必要です。",
                ["Section 7 intro", "operator vs management dashboards", "different granularity"],
                "compare",
                [("見るべき指標", ["運用担当向け", "原因調査", "細かい粒度"]), ("見せるべき指標", ["意思決定向け", "状態要約", "影響と判断"])],
                "同じSLOでも、見る相手によって粒度を変えます。",
            ),
            slide(
                "運用担当が見るもの",
                "悪化に気づき、原因にたどるための指標",
                "運用担当向けには、悪化を見つけて原因にたどる情報が必要です。現在のエスエルアイ、エスエルオー達成率、バーンレート、失敗件数、関連する内部メトリクスを並べます。目的は、次の調査行動に進めることです。",
                ["Operator dashboard", "SLI/SLO/burn/internal metrics", "diagnosis path"],
                "dashboard",
                [("SLI", ["成功率", "待ち時間"]), ("Burn", ["速度", "しきいち"]), ("原因候補", ["CPU", "DB", "Queue"])],
                "運用担当向けは、次の調査行動につながる配置にします。",
            ),
            slide(
                "マネジメントが見るもの",
                "状態、リスク、判断を短く伝える",
                "マネジメント向けには、細かいメトリクスよりも、状態、リスク、判断材料が重要です。今月の達成状況、残りエラーバジェット、主な消費理由、リリース判断への影響を短くまとめます。数字は、意思決定のために使います。",
                ["Management report", "status/risk/decision", "simple summary"],
                "three",
                [("状態", ["達成中か", "違反リスク"]), ("リスク", ["残り予算", "消費理由"]), ("判断", ["継続", "改善優先"])],
                "見せる指標は、意思決定につながる要約にします。",
            ),
            slide(
                "分けないと起きる問題",
                "細かすぎると伝わらず、粗すぎると調査できない",
                "一枚のダッシュボードにすべてを詰め込むと、どちらにも使いにくくなります。細かすぎると意思決定者には伝わりません。粗すぎると運用担当は原因を調べられません。用途ごとに画面を分けるほうが、結果的に使われます。",
                ["Overloaded dashboard problem", "too detailed vs too summary"],
                "compare",
                [("細かすぎる", ["数字が多すぎる", "判断に使えない"]), ("粗すぎる", ["原因が分からない", "対応に進めない"])],
                "用途を分けることで、ダッシュボードが使われるようになります。",
            ),
            slide(
                "共通で必要な3つ",
                "SLO達成率、残り予算、バーンレート",
                "どの相手にも共通して必要なのは、エスエルオー達成率、残りエラーバジェット、バーンレートの三つです。達成率は今の状態、残り予算は余裕、バーンレートは悪化の速度を表します。この三つを起点に、粒度を変えて表示します。",
                ["Common metrics", "attainment/remaining/burn rate"],
                "three",
                [("達成率", ["今の状態"]), ("残り予算", ["余裕"]), ("バーンレート", ["悪化速度"])],
                "共通指標を起点に、相手ごとに粒度を変えます。",
            ),
            slide(
                "表示の順番",
                "結論、詳細、原因候補の順に置く",
                "画面の並びも重要です。最初に結論として、正常か危険かを見せます。次に、達成率や残り予算を置きます。最後に、原因候補となる内部メトリクスへ進めるようにします。上から下へ、判断から調査へ流れる構成です。",
                ["Dashboard hierarchy", "status -> details -> diagnosis"],
                "flow",
                [("結論", ["正常", "注意", "危険"]), ("詳細", ["達成率", "残り予算"]), ("原因候補", ["内部指標"]), ("行動", ["調査", "報告"])],
                "判断から調査へ進む順番で配置します。",
            ),
            slide(
                "更新頻度も分ける",
                "即時対応とレビューでは、見る時間軸が違う",
                "更新頻度も相手によって変わります。オンコールは今の数分を見ます。週次レビューでは、数日から一週間の傾向を見ます。月次報告では、期間全体の達成状況を見ます。時間軸を分けることで、同じ数字の意味が整理されます。",
                ["Time horizons", "on-call weekly monthly"],
                "three",
                [("オンコール", ["数分", "即時対応"]), ("週次", ["数日", "改善確認"]), ("月次", ["1か月", "報告と判断"])],
                "時間軸を分けると、見るべき指標が整理されます。",
            ),
            slide(
                "まとめ",
                "運用向けと意思決定向けを分けて設計する",
                "まとめです。エスエルオーダッシュボードは、一枚ですべてを解決しようとしないことが大切です。運用担当には調査できる粒度を、マネジメントには判断できる要約を用意します。次は、運用担当向けダッシュボードを具体化します。",
                ["Summary", "operator vs decision dashboard", "next hands-on"],
                "three",
                [("運用向け", ["調査できる"]), ("意思決定向け", ["判断できる"]), ("次", ["運用担当向け"])],
                "次は、運用担当向けダッシュボードを作ります。",
            ),
        ],
    ),
    Lecture(
        "TASK-0105",
        None,
        "s7-l2",
        7,
        2,
        "運用担当向けダッシュボード",
        "Hands-on",
        "AI-Engineer-01",
        "AI-QA-01",
        "engineering / production",
        [
            slide(
                "運用担当向けダッシュボード",
                "異常検知から原因調査までを一画面で進める",
                "このレクチャーでは、運用担当向けのエスエルオーダッシュボードを設計します。目的は、異常に気づき、状況を把握し、原因候補へ進むことです。きれいなレポートではなく、対応中に使える画面を作ります。",
                ["Operator dashboard hands-on", "detect -> understand -> diagnose"],
                "flow",
                [("検知", ["SLO状態"]), ("把握", ["残り予算", "速度"]), ("調査", ["原因候補"]), ("対応", ["Runbookへ"])],
                "運用担当向けは、対応中に使える画面にします。",
            ),
            slide(
                "上段: 状態を置く",
                "正常、注意、危険がすぐ分かるようにする",
                "上段には、今の状態を置きます。エスエルオー達成率、残りエラーバジェット、現在のバーンレートを並べると、まず危険度が分かります。対応中の人が最初に見る場所なので、結論を大きく表示します。",
                ["Top row status", "SLO attainment, remaining budget, burn rate"],
                "dashboard",
                [("達成率", ["99.92%", "目標内"]), ("残り予算", ["62%", "余裕"]), ("Burn", ["1.8x", "注意"])],
                "最初に、今危険なのかどうかを見せます。",
            ),
            slide(
                "中段: 時系列を見る",
                "悪化がいつ始まり、続いているかを確認する",
                "中段には時系列グラフを置きます。成功率、レイテンシ、エラー率、バーンレートを時間で見ると、いつ悪化したか、続いているか、回復しているかが分かります。ここで、対応の緊急度と影響範囲を確認します。",
                ["Middle row time series", "success/latency/error/burn"],
                "dashboard",
                [("成功率", ["低下開始", "回復傾向"]), ("待ち時間", ["p95", "p99"]), ("Burn", ["短期", "長期"])],
                "時系列で、悪化の開始、継続、回復を確認します。",
            ),
            slide(
                "下段: 原因候補へ進む",
                "内部メトリクスは、体験悪化の後に見る",
                "下段には原因候補を置きます。シーピーユー、メモリ、データベース待ち、キューの長さ、外部依存の失敗などです。ここで大事なのは、内部メトリクスを主役にしないことです。まず体験悪化を見てから、原因候補として使います。",
                ["Bottom row diagnostic metrics", "CPU/DB/Queue/external dependency"],
                "three",
                [("基盤", ["CPU", "メモリ"]), ("依存先", ["DB待ち", "外部API"]), ("処理待ち", ["Queue", "再試行"])],
                "内部メトリクスは、原因調査の入口として使います。",
            ),
            slide(
                "Alarm状態も置く",
                "通知が出ている理由を、その場で確認できるようにする",
                "運用中は、なぜ通知が出ているのかをすぐ確認できることが重要です。クラウドウォッチアラームの状態や、短期窓、長期窓のどちらが発火しているかを表示します。通知とダッシュボードをつなげると、初動が速くなります。",
                ["Alarm status panel", "short/long burn alarm states"],
                "flow",
                [("通知", ["SNS", "Chat"]), ("Alarm状態", ["短期", "長期"]), ("理由", ["しきいち超過"]), ("初動", ["確認が速い"])],
                "通知の理由を、ダッシュボード上で確認できるようにします。",
            ),
            slide(
                "Runbookへの導線",
                "次に何をするかまで置いておく",
                "ダッシュボードは見るだけでは不十分です。異常を見つけたら、次に何をするかへ進める必要があります。ランブックやリードミーへのリンク、確認コマンド、担当チーム、関連サービスを置くと、対応の迷いを減らせます。",
                ["Runbook links", "next action panel", "owner/team/service"],
                "three",
                [("Runbook", ["初動手順", "切り分け"]), ("README", ["再現手順", "削除手順"]), ("担当", ["Owner", "連絡先"])],
                "画面から次の行動へ進めるようにします。",
            ),
            slide(
                "コストと整理",
                "増やしすぎず、使われる画面に絞る",
                "クラウドウォッチダッシュボードは便利ですが、増やしすぎると管理されなくなります。講座では低コストを前提に、必要なウィジェットに絞ります。サービス単位、重要操作単位など、使う人が迷わない単位で整理します。",
                ["Cost and dashboard hygiene", "focused widgets", "low cost"],
                "compare",
                [("増やしすぎ", ["誰も見ない", "コストと管理が増える"]), ("絞る", ["重要操作", "対応に使う", "低コスト"])],
                "必要な画面に絞ることも、運用品質の一部です。",
            ),
            slide(
                "まとめ",
                "状態、時系列、原因候補、行動を一画面に置く",
                "まとめです。運用担当向けダッシュボードでは、上段に状態、中段に時系列、下段に原因候補を置きます。さらにアラーム状態とランブックへの導線を入れると、対応に使える画面になります。次は、マネジメント向けのレポートに変換します。",
                ["Summary", "status/timeline/diagnosis/action"],
                "three",
                [("状態", ["達成率", "残り予算"]), ("調査", ["時系列", "原因候補"]), ("行動", ["Alarm", "Runbook"])],
                "次は、マネジメント向けSLOレポートを作ります。",
            ),
        ],
    ),
    Lecture(
        "TASK-0106",
        None,
        "s7-l3",
        7,
        3,
        "マネジメント向けSLOレポート",
        "Work",
        "AI-Production-01",
        "AI-QA-01",
        "production",
        [
            slide(
                "マネジメント向けSLOレポート",
                "細かいメトリクスを、判断できる文章と数字に変換する",
                "このレクチャーでは、マネジメント向けのエスエルオーレポートを扱います。運用ダッシュボードの細かい数字を、そのまま渡しても判断には使いにくいです。状態、影響、原因、次の判断を短くまとめる形へ変換します。",
                ["Management SLO report", "metrics to decision summary"],
                "flow",
                [("メトリクス", ["細かい"]), ("要約", ["状態", "影響"]), ("判断", ["継続", "改善"]), ("報告", ["短く伝える"])],
                "レポートは、数字を意思決定に変換するための成果物です。",
            ),
            slide(
                "1ページで伝える",
                "今どうなのか、何が必要なのかを先に書く",
                "マネジメント向けレポートでは、最初に結論を書きます。今月のエスエルオーは達成中なのか、違反リスクがあるのか。エラーバジェットはどれくらい残っているのか。追加対応が必要なのか。この順番で伝えると、読む側が判断しやすくなります。",
                ["One-page report", "status first", "decision summary"],
                "three",
                [("状態", ["達成中", "注意", "危険"]), ("余白", ["残り予算", "消費速度"]), ("判断", ["継続", "改善投資"])],
                "最初に結論を置くと、読み手が判断しやすくなります。",
            ),
            slide(
                "残り予算を見せる",
                "何パーセント残っているか、何日分の余裕か",
                "残りエラーバジェットは、マネジメントに伝わりやすい指標です。何パーセント残っているか、今のペースなら何日で枯渇しそうかを示します。単なる障害件数ではなく、目標に対する余白として説明します。",
                ["Remaining budget", "percent and days remaining", "risk gauge"],
                "gauge",
                [("残り62%", [""]), ("意味", ["まだ余裕あり"]), ("注意", ["消費速度も確認"])],
                "残り予算は、信頼性リスクを説明する要約指標です。",
                0.62,
                GREEN,
            ),
            slide(
                "消費理由を書く",
                "予算を使った主要イベントを3つまでに絞る",
                "レポートには、エラーバジェットを消費した理由も書きます。ただし、すべての細かいエラーを並べる必要はありません。主要イベントを三つまでに絞り、いつ、何が起き、どれくらい予算を使ったかを書きます。",
                ["Top budget consumers", "three event cards"],
                "three",
                [("いつ", ["日時", "時間帯"]), ("何が", ["障害", "劣化"]), ("影響", ["消費量", "ユーザー影響"])],
                "消費理由は、主要イベントに絞って伝えます。",
            ),
            slide(
                "判断につなげる",
                "リリース継続、改善優先、監視強化を提案する",
                "マネジメント向けレポートは、報告で終わらせません。エラーバジェットが十分ならリリース継続、急速に減っているなら改善優先、原因が不明なら監視強化のように、次の判断案を添えます。数字は、判断に使って初めて価値があります。",
                ["Decision options", "continue/improve/observe"],
                "flow",
                [("余裕あり", ["継続"]), ("消費速い", ["改善優先"]), ("原因不明", ["監視強化"]), ("合意", ["次の行動"])],
                "数字に判断案を添えると、SLOが組織で使われます。",
            ),
            slide(
                "言い方を変える",
                "技術用語を、事業影響の言葉に置き換える",
                "報告では、技術用語をそのまま並べすぎないことも大切です。バーンレート十四倍という数字は、月間予算を約二日で使い切るペースです、のように言い換えます。エスエルオー違反リスクを、事業影響と判断の言葉に変換します。",
                ["Translate technical terms", "burn rate -> days to exhaustion"],
                "compare",
                [("技術用語だけ", ["バーンレート14倍", "p99悪化"]), ("判断の言葉", ["約2日で枯渇", "重要操作が遅い"])],
                "相手が判断できる言葉へ変換します。",
            ),
            slide(
                "テンプレート",
                "状態、予算、原因、判断、次回確認",
                "レポートテンプレートはシンプルで構いません。状態、残り予算、主な消費理由、判断案、次回確認の五つを入れます。毎回同じ型で出すと、過去との比較もしやすくなり、月次レビューに組み込みやすくなります。",
                ["Report template", "status/budget/reasons/decision/next review"],
                "flow",
                [("状態", ["達成中か"]), ("予算", ["残り"]), ("原因", ["主な消費"]), ("判断", ["次の行動"])],
                "同じ型で出すと、SLOレビューが続けやすくなります。",
            ),
            slide(
                "まとめ",
                "SLOレポートは、信頼性の状況を判断へつなげる",
                "まとめです。マネジメント向けエスエルオーレポートでは、細かいメトリクスではなく、状態、残り予算、消費理由、判断案を短く伝えます。これで、エスエルオーが運用チームだけの数字ではなく、組織の意思決定に使える数字になります。",
                ["Summary", "status/budget/reason/decision", "bridge to organization rollout"],
                "three",
                [("状態", ["今どうか"]), ("理由", ["なぜそうなったか"]), ("判断", ["次に何をするか"])],
                "次のセクションでは、SLOを組織に導入する話へ進みます。",
            ),
        ],
    ),
]


def header(draw: ImageDraw.ImageDraw, lecture: Lecture, slide_data: Slide) -> None:
    draw.rectangle((0, 0, 1920, 232), fill=(255, 255, 255))
    draw.rounded_rectangle((78, 36, 230, 82), radius=10, fill=BLUE)
    draw.text((102, 45), f"S{lecture.section}-L{lecture.lecture_no}", font=F_SECTION, fill=(255, 255, 255))
    draw.text((78, 110), slide_data.title, font=F_TITLE, fill=NAVY)
    draw.text((82, 188), slide_data.message, font=F_MESSAGE, fill=MUTED)
    draw.rectangle((0, 230, 1920, 236), fill=BLUE)
    draw.rectangle((960, 230, 1920, 236), fill=GREEN)


def footer(draw: ImageDraw.ImageDraw, text: str) -> None:
    draw.rounded_rectangle((96, 1000, 1824, 1062), radius=15, fill=(255, 255, 255), outline=(204, 216, 231), width=2)
    draw.ellipse((126, 1015, 166, 1055), fill=GREEN)
    text_center(draw, (126, 1015, 166, 1055), "✓", load_font(26), (255, 255, 255))
    draw.text((188, 1019), text, font=F_SMALL, fill=NAVY)


def draw_card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: list[str], color, fill, icon: str) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=color, width=3)
    draw.rounded_rectangle((x1 + 24, y1 - 18, x2 - 24, y1 + 38), radius=12, fill=color)
    text_center(draw, (x1 + 36, y1 - 12, x2 - 36, y1 + 34), title, F_SMALL, (255, 255, 255))
    draw.ellipse((x1 + 38, y1 + 72, x1 + 118, y1 + 152), fill=(255, 255, 255), outline=color, width=5)
    text_center(draw, (x1 + 38, y1 + 72, x1 + 118, y1 + 152), icon, F_CARD_TITLE, color)
    y = y1 + 180
    for item in body:
        for line in wrap_jp(item, 18 if x2 - x1 < 430 else 23):
            draw.text((x1 + 42, y), line, font=F_BODY, fill=NAVY)
            y += 37
        y += 7


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=BLUE) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=8)
    draw.polygon([(x2, y2), (x2 - 26, y2 - 18), (x2 - 26, y2 + 18)], fill=color)


def draw_gauge(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int, value: float, label: str, color) -> None:
    x, y = center
    draw.arc((x - radius, y - radius, x + radius, y + radius), 180, 360, fill=(205, 216, 231), width=24)
    draw.arc((x - radius, y - radius, x + radius, y + radius), 180, 180 + int(180 * value), fill=color, width=24)
    import math

    angle = 180 + int(180 * value)
    ex = x + int((radius - 32) * math.cos(math.radians(angle)))
    ey = y + int((radius - 32) * math.sin(math.radians(angle)))
    draw.line((x, y, ex, ey), fill=NAVY, width=9)
    draw.ellipse((x - 13, y - 13, x + 13, y + 13), fill=NAVY)
    text_center(draw, (x - radius, y + 58, x + radius, y + 118), label, F_CARD_TITLE, NAVY)


def draw_chart(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color=BLUE) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=14, fill=(255, 255, 255), outline=(207, 218, 232), width=2)
    draw.line((x1 + 46, y2 - 42, x2 - 34, y2 - 42), fill=NAVY, width=3)
    draw.line((x1 + 46, y1 + 34, x1 + 46, y2 - 42), fill=NAVY, width=3)
    values = [0.34, 0.38, 0.42, 0.37, 0.56, 0.68, 0.58, 0.74]
    pts = []
    for idx, val in enumerate(values):
        x = x1 + 46 + int(idx * ((x2 - x1 - 94) / (len(values) - 1)))
        y = y2 - 42 - int(val * (y2 - y1 - 92))
        pts.append((x, y))
    draw.line(pts, fill=color, width=5)
    for x, y in pts:
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=color)


def layout_three(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    boxes = [(86, 320, 600, 850), (704, 320, 1218, 850), (1322, 320, 1836, 850)]
    colors = [BLUE, GREEN, TEAL]
    fills = [LIGHT_BLUE, LIGHT_GREEN, (234, 250, 251)]
    icons = ["1", "2", "3"]
    for idx, item in enumerate(slide_data.cards[:3]):
        draw_card(draw, boxes[idx], item[0], item[1], colors[idx], fills[idx], icons[idx])


def layout_flow(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    boxes = [(72, 360, 430, 810), (540, 360, 898, 810), (1008, 360, 1366, 810), (1476, 360, 1834, 810)]
    colors = [BLUE, GREEN, ORANGE, TEAL]
    for idx, item in enumerate(slide_data.cards[:4]):
        draw_card(draw, boxes[idx], item[0], item[1], colors[idx], (255, 255, 255), str(idx + 1))
        if idx < 3:
            arrow(draw, (boxes[idx][2] + 24, 590), (boxes[idx + 1][0] - 24, 590), colors[idx])


def layout_compare(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    left, right = slide_data.cards[:2]
    draw_card(draw, (120, 340, 860, 835), left[0], left[1], RED, LIGHT_RED, "!")
    draw_card(draw, (1060, 340, 1800, 835), right[0], right[1], GREEN, LIGHT_GREEN, "✓")
    arrow(draw, (898, 590), (1020, 590), BLUE)


def layout_formula(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    draw.rounded_rectangle((155, 350, 1765, 780), radius=24, fill=(255, 255, 255), outline=BLUE, width=4)
    labels = slide_data.cards[:3]
    x_positions = [265, 760, 1255]
    signs = ["-", "=", ""]
    colors = [BLUE, ORANGE, GREEN]
    for idx, (title, body) in enumerate(labels):
        draw.rounded_rectangle((x_positions[idx], 442, x_positions[idx] + 330, 620), radius=18, fill=[LIGHT_BLUE, LIGHT_ORANGE, LIGHT_GREEN][idx], outline=colors[idx], width=3)
        text_center(draw, (x_positions[idx], 468, x_positions[idx] + 330, 510), title, F_CARD_TITLE, colors[idx])
        text_center(draw, (x_positions[idx], 535, x_positions[idx] + 330, 600), " / ".join(body), F_MONO, NAVY)
        if signs[idx]:
            text_center(draw, (x_positions[idx] + 360, 495, x_positions[idx] + 450, 590), signs[idx], F_BIG, NAVY)


def layout_gauge(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    draw_gauge(draw, (960, 555), 240, slide_data.value, slide_data.cards[0][0], slide_data.color)
    draw_card(draw, (110, 380, 545, 800), slide_data.cards[1][0], slide_data.cards[1][1], BLUE, LIGHT_BLUE, "→")
    draw_card(draw, (1375, 380, 1810, 800), slide_data.cards[2][0], slide_data.cards[2][1], GREEN, LIGHT_GREEN, "✓")
    arrow(draw, (575, 585), (690, 585), BLUE)
    arrow(draw, (1230, 585), (1345, 585), GREEN)


def layout_dashboard(draw: ImageDraw.ImageDraw, slide_data: Slide) -> None:
    boxes = [(90, 330, 590, 830), (710, 330, 1210, 830), (1330, 330, 1830, 830)]
    colors = [BLUE, GREEN, ORANGE]
    for idx, (title, body) in enumerate(slide_data.cards[:3]):
        x1, y1, x2, y2 = boxes[idx]
        draw.rounded_rectangle((x1, y1, x2, y2), radius=20, fill=(255, 255, 255), outline=colors[idx], width=3)
        draw.rounded_rectangle((x1 + 28, y1 + 28, x2 - 28, y1 + 84), radius=12, fill=colors[idx])
        text_center(draw, (x1 + 38, y1 + 31, x2 - 38, y1 + 80), title, F_SMALL, (255, 255, 255))
        if idx == 1:
            draw_chart(draw, (x1 + 62, y1 + 132, x2 - 62, y1 + 332), colors[idx])
        else:
            draw_gauge(draw, ((x1 + x2) // 2, y1 + 245), 130, 0.72 if idx == 0 else 0.47, title, colors[idx])
        y = y1 + 385
        for item in body[:2]:
            draw.text((x1 + 52, y), "✓ " + item, font=F_SMALL, fill=NAVY)
            y += 42


LAYOUTS = {
    "three": layout_three,
    "flow": layout_flow,
    "compare": layout_compare,
    "formula": layout_formula,
    "gauge": layout_gauge,
    "dashboard": layout_dashboard,
}


def render_slide(lecture: Lecture, slide_number: int, slide_data: Slide) -> None:
    image = Image.new("RGB", (1920, 1080), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 236, 1920, 1080), fill=BG)
    for x in range(-220, 2050, 360):
        draw.rounded_rectangle((x, 275, x + 260, 960), radius=34, fill=(241, 245, 250))
    header(draw, lecture, slide_data)
    LAYOUTS[slide_data.layout](draw, slide_data)
    footer(draw, slide_data.footer)
    out = COURSE / "slides" / lecture.lecture_id / f"slide_{slide_number:03d}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out, "PNG", optimize=True)


def make_contact_sheet(lecture: Lecture) -> None:
    files = sorted((COURSE / "slides" / lecture.lecture_id).glob("slide_*.png"))
    rows = (len(files) + 1) // 2
    sheet = Image.new("RGB", (1920, max(1, rows) * 600 + 80), (235, 240, 248))
    draw = ImageDraw.Draw(sheet)
    for idx, path in enumerate(files):
        thumb = Image.open(path).resize((900, 506), Image.Resampling.LANCZOS)
        x = 40 + (idx % 2) * 940
        y = 70 + (idx // 2) * 600
        draw.text((x, y - 44), path.name, font=F_SMALL, fill=NAVY)
        sheet.paste(thumb, (x, y))
    sheet.save(COURSE / "slides" / lecture.lecture_id / "contact_sheet.png", "PNG", optimize=True)


def script_markdown(lecture: Lecture) -> str:
    lines = [
        f"# Section {lecture.section} Lecture {lecture.lecture_no} 台本",
        "",
        "## Title",
        "",
        lecture.title,
        "",
        "## Source",
        "",
        "- `course_spec.md`",
        "- `lectures.md`",
        "- `docs/VOICEVOX_RULES.md`",
        "- Google SRE Workbook: Implementing SLOs",
        "- Amazon CloudWatch SLO / Alarm / Dashboard documentation",
        "",
    ]
    for idx, item in enumerate(lecture.slides, 1):
        lines.extend(
            [
                f"## Slide {idx}",
                "",
                "### Slide Title",
                "",
                item.title,
                "",
                "### Slide Message",
                "",
                item.message,
                "",
                "### Narration",
                "",
                item.narration,
                "",
                "### Visual Notes",
                "",
            ]
        )
        lines.extend(f"- {note}" for note in item.visual_notes)
        lines.append("")
    lines.extend(
        [
            "## QA Notes",
            "",
            f"- `lectures.md` の Lecture {lecture.section}-{lecture.lecture_no}「{lecture.title}」に合わせて構成",
            "- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる",
            "- CloudWatch はナレーション内ではクラウドウォッチに寄せる",
            "- バーンレート、エラーバジェットは日本語表記で統一",
            "- 8枚構成",
            "",
        ]
    )
    return "\n".join(lines)


def script_json(lecture: Lecture) -> dict:
    return {
        "title": lecture.title,
        "slides": [
            {
                "slide_number": idx,
                "title": item.title,
                "message": item.message,
                "narration": item.narration,
                "visual_notes": item.visual_notes,
            }
            for idx, item in enumerate(lecture.slides, 1)
        ],
    }


def ticket_text(lecture: Lecture) -> str:
    issue = "#TBD" if lecture.issue_number is None else f"#{lecture.issue_number}"
    return f"""# Task Summary
Task ID: {lecture.task_id}
Title: Section {lecture.section} Lecture {lecture.lecture_no} の完成動画を制作しDriveへアップロードする

# Ownership
Department: {lecture.department}
Owner AI: {lecture.owner}
Reviewer AI: {lecture.reviewer}

# Execution
Priority: high
Status: Production

# Inputs
Input Files:
- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
Dependencies:
- Section 5 production is running in another chat; do not modify s5 assets

# Deliverables
Expected Output:
- `scripts/{lecture.lecture_id}_script.md`
- `scripts/{lecture.lecture_id}_script.json`
- `slides/{lecture.lecture_id}/slide_*.png`
- `audio/{lecture.lecture_id}/slide_*.wav`
- `video/{lecture.lecture_id}/{lecture.lecture_id}.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- `course_spec.md` と `lectures.md` に整合している
- VOICEVOXナレーションチェックを通過している
- AWS Batch Fargate 2段ジョブでVOICEVOX音声とMP4を生成している
- MP4 faststart true、decode check OK
- Drive metadataと共有設定を確認している
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- s5配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: {issue}
"""


def write_files() -> None:
    for lecture in LECTURES:
        (COURSE / "scripts" / f"{lecture.lecture_id}_script.md").write_text(script_markdown(lecture), encoding="utf-8")
        (COURSE / "scripts" / f"{lecture.lecture_id}_script.json").write_text(
            json.dumps(script_json(lecture), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        ticket_name = f"{lecture.task_id}_{lecture.lecture_id}_lecture_package.md"
        (COURSE / "tickets" / ticket_name).write_text(ticket_text(lecture), encoding="utf-8")
        for idx, item in enumerate(lecture.slides, 1):
            render_slide(lecture, idx, item)
        make_contact_sheet(lecture)
        print(f"{lecture.lecture_id}: scripts, ticket, and {len(lecture.slides)} slides generated")


def main() -> int:
    write_files()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
