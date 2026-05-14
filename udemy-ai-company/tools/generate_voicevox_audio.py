#!/usr/bin/env python3
"""Generate VOICEVOX WAV files from a lecture script.json into a target audio directory."""

from __future__ import annotations

import argparse
import contextlib
import json
import sys
import wave
from pathlib import Path


UDemy_SRC = Path("/home/ubuntu/workspace/udemy")
sys.path.insert(0, str(UDemy_SRC))

from src.voice_generator import check_voicevox_running, generate_voice_for_slide, normalize_for_voicevox


def wav_duration(path: Path) -> float:
    with contextlib.closing(wave.open(str(path), "rb")) as wav:
        frames = wav.getnframes()
        rate = wav.getframerate()
        return frames / float(rate)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script_json", type=Path)
    parser.add_argument("audio_dir", type=Path)
    parser.add_argument("--slide", type=int)
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    if not check_voicevox_running():
        raise SystemExit("VOICEVOX is not running on http://localhost:50021")

    data = json.loads(args.script_json.read_text(encoding="utf-8"))
    args.audio_dir.mkdir(parents=True, exist_ok=True)
    audio_info = []
    slides = data["slides"]
    for slide in slides:
        number = int(slide["slide_number"])
        if args.slide is not None and number != args.slide:
            continue
        wav_path = args.audio_dir / f"slide_{number:03d}.wav"
        if args.skip_existing and wav_path.exists() and wav_path.stat().st_size > 0:
            print(f"slide {number}/{len(slides)} exists -> {wav_path}", flush=True)
            audio_info.append(
                {
                    "slide_number": number,
                    "wav_path": str(wav_path),
                    "duration_sec": wav_duration(wav_path),
                }
            )
            continue
        narration = normalize_for_voicevox(slide["narration"])
        print(f"slide {number}/{len(slides)} -> {wav_path}", flush=True)
        duration = generate_voice_for_slide(narration, str(wav_path))
        print(f"  {duration:.2f}s", flush=True)
        audio_info.append(
            {
                "slide_number": number,
                "wav_path": str(wav_path),
                "duration_sec": duration,
            }
        )

    report = {
        "script_json": str(args.script_json),
        "audio_dir": str(args.audio_dir),
        "slides": len(audio_info),
        "duration": sum(item["duration_sec"] for item in audio_info),
        "audio": audio_info,
    }
    (args.audio_dir / "voicevox_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({k: v for k, v in report.items() if k != "audio"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
