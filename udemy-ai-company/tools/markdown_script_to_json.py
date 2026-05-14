#!/usr/bin/env python3
"""Convert a course markdown script into the script.json shape used by VOICEVOX tools."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SECTION_RE = re.compile(r"^## Slide (\d+)\s*$")


def value_after_heading(lines: list[str], heading: str) -> str:
    target = f"### {heading}"
    for index, line in enumerate(lines):
        if line.strip() == target:
            values: list[str] = []
            for body_line in lines[index + 1 :]:
                if body_line.startswith("### ") or body_line.startswith("## "):
                    break
                if body_line.strip():
                    values.append(body_line.rstrip())
            return "\n".join(values).strip()
    return ""


def parse_script(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = value_after_heading(lines, "Title") or path.stem

    slide_starts: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = SECTION_RE.match(line)
        if match:
            slide_starts.append((int(match.group(1)), index))

    slides = []
    for pos, (slide_number, start) in enumerate(slide_starts):
        end = slide_starts[pos + 1][1] if pos + 1 < len(slide_starts) else len(lines)
        block = lines[start:end]
        visual_notes = value_after_heading(block, "Visual Notes")
        notes = [
            note.removeprefix("-").strip()
            for note in visual_notes.splitlines()
            if note.strip()
        ]
        slides.append(
            {
                "slide_number": slide_number,
                "title": value_after_heading(block, "Slide Title"),
                "message": value_after_heading(block, "Slide Message"),
                "narration": value_after_heading(block, "Narration"),
                "visual_notes": notes,
            }
        )

    return {"title": title, "slides": slides}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    data = parse_script(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {args.output} ({len(data['slides'])} slides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
