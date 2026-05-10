#!/usr/bin/env python3
"""Check narration text for VOICEVOX pronunciation risks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Issue:
    path: Path
    location: str
    rule: str
    severity: str
    message: str
    suggestion: str


JP_READING_FIXES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(\d+(?:\.\d+)?)\s*GB"), r"\1ギガバイト"),
    (re.compile(r"(\d+(?:\.\d+)?)\s*MB"), r"\1メガバイト"),
    (re.compile(r"(\d+(?:\.\d+)?)\s*ms"), r"\1ミリ秒"),
    (re.compile(r"CPU(\d+)"), r"シーピーユー\1"),
    (re.compile(r"閾値"), "しきいち"),
    (re.compile(r"\bt(\d+)\.micro\b"), r"ティー\1ドットマイクロ"),
    (re.compile(r"\bm(\d+)i\b"), r"エム\1アイ"),
    (re.compile(r"\bm(\d+)\b"), r"エム\1"),
    (re.compile(r"(?<![a-zA-Z0-9])STEP\s+(\d+)(?![a-zA-Z0-9])"), r"ステップ\1"),
    (re.compile(r"(?<![a-zA-Z0-9])Step\s+(\d+)(?![a-zA-Z0-9])"), r"ステップ\1"),
    (re.compile(r"(?<![a-zA-Z0-9])step\s+(\d+)(?![a-zA-Z0-9])"), r"ステップ\1"),
    (re.compile(r"ステップ\s+(\d+)"), r"ステップ\1"),
    (re.compile(r"重大度"), "じゅうだいど"),
    (re.compile(r"根本原因"), "こんぽんげんいん"),
    (re.compile(r"発報"), "はっぽう"),
    (re.compile(r"一気通貫"), "いっきつうかん"),
    (re.compile(r"一気貫通"), "いっきかんつう"),
    (re.compile(r"今リリース"), "いまりりーす"),
    (re.compile(r"右上"), "みぎうえ"),
    (re.compile(r"上で"), "うえで"),
    (re.compile(r"(?<=[ぁ-んァ-ヶー])値(?=[をがにのは、。へとも])"), "あたい"),
]


EN_TO_KANA: list[tuple[str, str]] = [
    ("Cost Anomaly Detection", "コストアノマリーディテクション"),
    ("Simple Notification Service", "シンプルノティフィケーションサービス"),
    ("AWS Systems Manager", "エーダブリューエスシステムズマネージャー"),
    ("AWS Incident Manager", "エーダブリューエスインシデントマネージャー"),
    ("CloudWatch Metrics", "クラウドウォッチメトリクス"),
    ("CloudWatch Alarms", "クラウドウォッチアラームズ"),
    ("CloudWatch Alarm", "クラウドウォッチアラーム"),
    ("CloudWatch Agent", "クラウドウォッチエージェント"),
    ("CloudWatch Logs", "クラウドウォッチログス"),
    ("Logs Insights", "ログスインサイツ"),
    ("AWS Budgets", "エーダブリューエスバジェッツ"),
    ("AWS Chatbot", "エーダブリューエスチャットボット"),
    ("SNS Topics", "エスエヌエストピックス"),
    ("SNS Topic", "エスエヌエストピック"),
    ("AWS CLI", "エーダブリューエスシーエルアイ"),
    ("aws cli", "エーダブリューエスシーエルアイ"),
    ("CloudFormation", "クラウドフォーメーション"),
    ("CloudWatch", "クラウドウォッチ"),
    ("CloudTrail", "クラウドトレイル"),
    ("CloudShell", "クラウドシェル"),
    ("CloudFront", "クラウドフロント"),
    ("EventBridge", "イベントブリッジ"),
    ("OpenTelemetry", "オープンテレメトリー"),
    ("OpenSearch", "オープンサーチ"),
    ("Multi-AZ", "マルチエーゼット"),
    ("Dashboard", "ダッシュボード"),
    ("Dashboards", "ダッシュボード"),
    ("Namespace", "ネームスペース"),
    ("Parameter", "パラメーター"),
    ("Parameters", "パラメーターズ"),
    ("Outputs", "アウトプッツ"),
    ("Terraform", "テラフォーム"),
    ("Kubernetes", "クバネティス"),
    ("Grafana", "グラファナ"),
    ("Prometheus", "プロメテウス"),
    ("PagerDuty", "ページャーデューティー"),
    ("Blameless", "ブレームレス"),
    ("Section", "セクション"),
    ("API", "エーピーアイ"),
    ("api", "エーピーアイ"),
    ("EC2", "イーシーツー"),
    ("ec2", "イーシーツー"),
    ("SNS", "エスエヌエス"),
    ("SRE", "エスアールイー"),
    ("AWS", "エーダブリューエス"),
    ("IAM", "アイアム"),
]


RISKY_JP_TERMS: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"重大度"), "じゅうだいど", "VOICEVOXが「じゅうたいど」と読みやすい"),
    (re.compile(r"根本原因"), "こんぽんげんいん", "「ねもとげんいん」と読まれやすい"),
    (re.compile(r"発報"), "はっぽう", "読みが崩れやすい"),
    (re.compile(r"一気貫通"), "いっきかんつう", "読みが安定しない"),
    (re.compile(r"今リリース"), "いまりりーす", "「こんリリース」と読まれやすい"),
    (re.compile(r"右上"), "みぎうえ", "「みぎじょう」と読まれやすい"),
    (re.compile(r"上で"), "うえで", "「じょうで」と読まれやすい"),
    (re.compile(r"閾値"), "しきいち", "読みが揺れやすい"),
    (re.compile(r"(?<=[ぁ-んァ-ヶー])値(?=[をがにのは、。へとも])"), "あたい", "「ね」と読まれやすい"),
]


CHECKS: list[tuple[str, str, re.Pattern[str], str, str]] = [
    (
        "B",
        "warn",
        re.compile(r"[A-Za-z][A-Za-z0-9_./:+-]*"),
        "ナレーションにアルファベットが残っています",
        "読み上げ用のカタカナ表記にしてください",
    ),
    (
        "C",
        "error",
        re.compile(r"[一-龯ぁ-んァ-ヶA-Za-z0-9]+（[ぁ-んァ-ヶーA-Za-z0-9]+）"),
        "カッコによるふりがな併記があります",
        "VOICEVOXは両方読むため、読み上げたい表記だけにしてください",
    ),
    (
        "D",
        "error",
        re.compile(r"〇〇|×{2,}|＊{2,}|\*{2,}"),
        "伏字記号があります",
        "「あるチーム」「とあるエンジニア」など自然な表現にしてください",
    ),
    (
        "E",
        "warn",
        re.compile(r"[A-Za-z][A-Za-z0-9-]+(?:\s+[A-Za-z][A-Za-z0-9-]+)+"),
        "英語フレーズに空白が残っています",
        "多語サービス名はカタカナで一語化してください",
    ),
    (
        "E",
        "warn",
        re.compile(r"(?:STEP|Step|step)\s+\d+|ステップ\s+\d+"),
        "ステップ番号の前に空白があります",
        "「ステップ5」のように詰めてください",
    ),
    (
        "F",
        "warn",
        re.compile(r"\d+(?:ms|GB|MB|xx|XX)\b"),
        "数値と英略語単位が連結しています",
        "「ミリ秒」「ギガバイト」「5系のエラー」など読み下してください",
    ),
]


def normalize_for_voicevox(text: str) -> str:
    for pattern, replacement in JP_READING_FIXES:
        text = pattern.sub(replacement, text)
    for source, replacement in EN_TO_KANA:
        text = re.sub(re.escape(source), replacement, text)
    return text


def iter_target_files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_dir():
            yield from path.rglob("script.json")
            yield from path.rglob("*_script.md")
            yield from path.rglob("lesson_*.md")
        elif path.name == "script.json" or (
            path.suffix.lower() == ".md" and (path.name.endswith("_script.md") or path.name.startswith("lesson_"))
        ):
            yield path


def extract_texts(path: Path) -> list[tuple[str, str]]:
    if path.name == "script.json":
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        texts: list[tuple[str, str]] = []
        for index, slide in enumerate(data.get("slides", []), start=1):
            narration = slide.get("narration")
            location = f"slide {slide.get('slide_number', index)}"
            texts.append((location, narration if isinstance(narration, str) else ""))
        return texts

    return [("markdown", path.read_text(encoding="utf-8"))]


def check_text(text: str, path: Path, location: str) -> list[Issue]:
    issues: list[Issue] = []

    if not text.strip():
        return [
            Issue(path, location, "N", "error", "ナレーションが空です", "読み上げ文を追加してください")
        ]

    for pattern, replacement, reason in RISKY_JP_TERMS:
        if pattern.search(text):
            issues.append(Issue(path, location, "A", "warn", reason, f"「{replacement}」に書き換えてください"))

    for rule, severity, pattern, message, suggestion in CHECKS:
        if pattern.search(text):
            issues.append(Issue(path, location, rule, severity, message, suggestion))

    normalized = normalize_for_voicevox(text)
    leftovers = sorted(set(re.findall(r"[A-Za-z][A-Za-z0-9_./:+-]*", normalized)))
    if leftovers:
        issues.append(
            Issue(
                path,
                location,
                "R",
                "error",
                "正規化後もアルファベットが残ります: " + ", ".join(leftovers[:8]),
                "読み替えテーブルに追加するか、本文をカタカナ化してください",
            )
        )

    for sentence in re.split(r"(?<=。)", text):
        if len(sentence) > 80 and not re.search(r"[、。！？]", sentence[:80]):
            issues.append(
                Issue(
                    path,
                    location,
                    "H",
                    "warn",
                    "長い文の前半に句読点が少なく、息継ぎが不自然になりやすいです",
                    "30〜50文字を目安に読点か句点を入れてください",
                )
            )

    return issues


def format_issue(issue: Issue) -> str:
    return (
        f"{issue.severity.upper()} {issue.path}:{issue.location} "
        f"[rule {issue.rule}] {issue.message} -> {issue.suggestion}"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="VOICEVOX向けナレーション品質チェック")
    parser.add_argument("paths", nargs="+", type=Path, help="script.json、Markdown、またはディレクトリ")
    parser.add_argument("--warnings-ok", action="store_true", help="警告だけなら終了コード0にする")
    args = parser.parse_args(argv)

    files = sorted(set(iter_target_files(args.paths)))
    if not files:
        print("対象ファイルが見つかりません", file=sys.stderr)
        return 2

    issues: list[Issue] = []
    for path in files:
        try:
            for location, text in extract_texts(path):
                issues.extend(check_text(text, path, location))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            issues.append(Issue(path, "file", "P", "error", f"ファイルを読めません: {exc}", "形式を確認してください"))

    if issues:
        for issue in issues:
            print(format_issue(issue))
        if args.warnings_ok and all(issue.severity == "warn" for issue in issues):
            return 0
        return 1

    print(f"OK: {len(files)} files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
