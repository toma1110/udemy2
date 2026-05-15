#!/usr/bin/env python3
"""Generate GPT-Image2 prompt files from lecture script JSON files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

STYLE = (
    "Use a premium AWS/SRE educational visual style. 16:9 slide, clean log-analysis "
    "and incident-investigation aesthetic, white and pale blue background, navy, teal, "
    "green, amber, and restrained red accents, readable Japanese text generated directly "
    "inside the image, no logos, no watermark, no local text overlay."
)


def prompt_for_slide(slide: dict) -> str:
    title = str(slide.get("slide_title") or slide["title"]).strip()
    message = str(slide.get("slide_message") or slide["message"]).strip()
    raw_notes = slide.get("visual_notes", "")
    if isinstance(raw_notes, list):
        notes = "; ".join(str(note).strip() for note in raw_notes if str(note).strip())
    else:
        notes = str(raw_notes).strip().replace("\n", " ")
    return (
        "Create a Japanese course slide. "
        f"Large title: `{title}`. "
        f"Subtitle: `{message}`. "
        f"Visual: {notes}. "
        "Use large readable Japanese text, a clear operations diagram or query card layout, "
        "and leave generous margins. Do not add extra marketing copy, logos, or watermarks."
    )


def write_prompts(script_json: Path, out_dir: Path) -> Path:
    data = json.loads(script_json.read_text(encoding="utf-8"))
    lecture_id = script_json.stem.replace("_script", "")
    slides = data.get("slides", [])
    if not slides:
        raise ValueError(f"no slides in {script_json}")

    lines = [
        f"# GPT-Image2 Prompts: {lecture_id}",
        "",
        STYLE,
        "",
        "## Production Rules",
        "",
        "- All visible text must be generated directly by GPT-Image2.",
        "- Do not use local text overlay.",
        "- Keep one clear message per slide.",
        "- Prefer diagrams, query cards, timelines, and troubleshooting flows over decorative art.",
        "",
    ]
    for slide in slides:
        number = int(slide["slide_number"])
        lines.extend(
            [
                f"## slide_{number:03d}.png",
                "",
                prompt_for_slide(slide),
                "",
            ]
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    output = out_dir / f"{lecture_id}_gpt_image_prompts.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=ROOT / "scripts",
        help="Directory containing *_script.json files.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "slides",
        help="Directory where *_gpt_image_prompts.md files are written.",
    )
    args = parser.parse_args()

    files = sorted(args.scripts_dir.glob("s*-l*_script.json"))
    if not files:
        raise SystemExit(f"no script JSON files found in {args.scripts_dir}")
    for script_json in files:
        output = write_prompts(script_json, args.out_dir)
        print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
