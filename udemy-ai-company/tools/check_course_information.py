#!/usr/bin/env python3
"""Validate Udemy course information drafts against the standard format."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


COMPANY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_COURSES_ROOT = COMPANY_ROOT / "courses"

REQUIRED_SECTIONS = (
    "# udemy登録情報",
    "## 想定する学習者",
    "### コースで受講生は何を学びますか？",
    "### コースを受講するための要件や前提条件は何ですか?",
    "### 誰に向けたコースですか?",
    "## コース紹介ページ",
    "### コースタイトル",
    "### コースのサブタイトル",
    "### コースの説明",
    "## コース画像",
    "## コースメッセージ",
    "### 歓迎のメッセージ",
    "### お祝いのメッセージ",
)

REQUIRED_TERMS = (
    "VOICEVOX",
    "GPT-Image2",
)

INSTRUCTION_PREFIXES = (
    "※",
    "TODO",
    "コースを受講する学習者に求められる",
    "そのような要件がない場合は",
    "コースの内容が必ず役に立つ",
    "そうすることで、最適な学習者に",
)


@dataclass
class CheckResult:
    path: Path
    ok: bool
    findings: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check course_infomation.md files.")
    parser.add_argument("paths", nargs="*", type=Path, help="Specific course_infomation.md files to check.")
    parser.add_argument(
        "--courses-root",
        type=Path,
        default=DEFAULT_COURSES_ROOT,
        help="Course root used when no explicit paths are passed.",
    )
    return parser.parse_args()


def non_template_lines(text: str, start_heading: str) -> list[str]:
    pattern = re.compile(
        rf"^{re.escape(start_heading)}\s*\n(?P<body>.*?)(?=^### |\n## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return []
    lines: list[str] = []
    for raw_line in match.group("body").splitlines():
        line = raw_line.strip()
        if not line or line.startswith(INSTRUCTION_PREFIXES):
            continue
        lines.append(line)
    return lines


def check_file(path: Path) -> CheckResult:
    findings: list[str] = []
    if not path.exists():
        return CheckResult(path, False, ["file does not exist"])

    text = path.read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            findings.append(f"missing section: {section}")
    for term in REQUIRED_TERMS:
        if term not in text:
            findings.append(f"missing required term: {term}")

    learning_outcomes = non_template_lines(text, "### コースで受講生は何を学びますか？")
    if len(learning_outcomes) < 4:
        findings.append("learning outcomes must contain at least 4 concrete lines")

    prerequisites = non_template_lines(text, "### コースを受講するための要件や前提条件は何ですか?")
    if not prerequisites:
        findings.append("prerequisites section has no concrete content")

    audience = non_template_lines(text, "### 誰に向けたコースですか?")
    if not audience:
        findings.append("target audience section has no concrete content")

    if "TODO" in text:
        findings.append("TODO remains in course information")

    return CheckResult(path, not findings, findings)


def discover_files(courses_root: Path) -> list[Path]:
    course_dirs = sorted(path.parent for path in courses_root.glob("*/course_spec.md"))
    if course_dirs:
        return [course_dir / "course_infomation.md" for course_dir in course_dirs]
    return sorted(courses_root.glob("*/course_infomation.md"))


def main() -> int:
    args = parse_args()
    paths = args.paths or discover_files(args.courses_root)
    if not paths:
        print("FAIL: no course_infomation.md files found")
        return 1

    results = [check_file(path) for path in paths]
    for result in results:
        status = "PASS" if result.ok else "FAIL"
        print(f"{status}: {result.path}")
        for finding in result.findings:
            print(f"  - {finding}")

    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
