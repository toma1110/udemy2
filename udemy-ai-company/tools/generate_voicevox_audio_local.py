#!/usr/bin/env python3
"""Generate local VOICEVOX WAV files from a lecture script JSON."""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import subprocess
import sys
import time
import wave
from pathlib import Path

import requests


VOICEVOX_URL = "http://127.0.0.1:50021"
DEFAULT_ENGINE = Path("/opt/voicevox_engine/linux-cpu-x64/run")
DEFAULT_SPEAKER_ID = 3
DEFAULT_SPEED_SCALE = 1.1
MAX_CHUNK_CHARS = 50

READING_FIXES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"閾値"), "しきいち"),
    (re.compile(r"重大度"), "じゅうだいど"),
    (re.compile(r"根本原因"), "こんぽんげんいん"),
    (re.compile(r"発報"), "はっぽう"),
    (re.compile(r"初学者"), "しょがくしゃ"),
    (re.compile(r"そんな方向け"), "そんなかたむけ"),
    (re.compile(r"(目指す|担当している|進めたい)方(?=[です、。])"), r"\1かた"),
    (re.compile(r"CPU"), "シーピーユー"),
    (re.compile(r"CDK"), "シーディーケー"),
    (re.compile(r"IaC"), "アイエーシー"),
    (re.compile(r"AWS"), "エーダブリューエス"),
    (re.compile(r"CloudFormation"), "クラウドフォーメーション"),
    (re.compile(r"CloudWatch"), "クラウドウォッチ"),
    (re.compile(r"Terraform"), "テラフォーム"),
]


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def normalize_for_voicevox(text: str) -> str:
    for pattern, replacement in READING_FIXES:
        text = pattern.sub(replacement, text)
    return text


def split_text_chunks(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    def split_long(part: str) -> list[str]:
        if len(part) <= max_chars:
            return [part]
        pieces = re.split(r"(?<=[、。！？])", part)
        chunks: list[str] = []
        buffer = ""
        for piece in pieces:
            if len(piece) > max_chars:
                if buffer:
                    chunks.append(buffer)
                    buffer = ""
                chunks.extend(piece[i : i + max_chars] for i in range(0, len(piece), max_chars))
            elif len(buffer) + len(piece) <= max_chars:
                buffer += piece
            else:
                if buffer:
                    chunks.append(buffer)
                buffer = piece
        if buffer:
            chunks.append(buffer)
        return chunks

    sentences: list[str] = []
    for sentence in re.split(r"(?<=。)", text):
        if sentence:
            sentences.extend(split_long(sentence))

    chunks: list[str] = []
    buffer = ""
    for sentence in sentences:
        if len(buffer) + len(sentence) <= max_chars:
            buffer += sentence
        else:
            if buffer:
                chunks.append(buffer)
            buffer = sentence
    if buffer:
        chunks.append(buffer)
    return chunks or [text]


def concat_wavs(wav_bytes_list: list[bytes]) -> bytes:
    output = io.BytesIO()
    with wave.open(output, "wb") as out_wav:
        for index, wav_bytes in enumerate(wav_bytes_list):
            with wave.open(io.BytesIO(wav_bytes), "rb") as in_wav:
                if index == 0:
                    out_wav.setparams(in_wav.getparams())
                out_wav.writeframes(in_wav.readframes(in_wav.getnframes()))
    return output.getvalue()


def wav_duration(path: Path) -> float:
    with contextlib.closing(wave.open(str(path), "rb")) as wav:
        return wav.getnframes() / float(wav.getframerate())


def engine_is_running() -> bool:
    try:
        return requests.get(f"{VOICEVOX_URL}/version", timeout=2).ok
    except requests.RequestException:
        return False


def start_engine(engine_path: Path) -> subprocess.Popen[str]:
    if not engine_path.exists():
        raise FileNotFoundError(f"VOICEVOX engine not found: {engine_path}")
    process = subprocess.Popen(
        [str(engine_path), "--host", "127.0.0.1", "--port", "50021"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    deadline = time.monotonic() + 180
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"VOICEVOX engine exited early with code {process.returncode}")
        if engine_is_running():
            return process
        time.sleep(3)
    process.terminate()
    raise RuntimeError("VOICEVOX engine did not become ready")


def synthesize_chunk(text: str, speaker_id: int, speed_scale: float) -> bytes:
    query_response = requests.post(
        f"{VOICEVOX_URL}/audio_query",
        params={"text": text, "speaker": speaker_id},
        timeout=60,
    )
    query_response.raise_for_status()
    audio_query = query_response.json()
    audio_query["speedScale"] = speed_scale
    synthesis_response = requests.post(
        f"{VOICEVOX_URL}/synthesis",
        params={"speaker": speaker_id},
        json=audio_query,
        headers={"Content-Type": "application/json"},
        timeout=180,
    )
    synthesis_response.raise_for_status()
    return synthesis_response.content


def generate_wav(text: str, output_path: Path, speaker_id: int, speed_scale: float) -> float:
    chunks = split_text_chunks(normalize_for_voicevox(text))
    wav_parts: list[bytes] = []
    for index, chunk in enumerate(chunks, 1):
        print(f"  chunk {index}/{len(chunks)} -> {output_path.name}", flush=True)
        for attempt in range(1, 4):
            try:
                wav_parts.append(synthesize_chunk(chunk, speaker_id, speed_scale))
                break
            except (requests.ConnectionError, requests.Timeout):
                if attempt == 3:
                    raise
                time.sleep(5 * attempt)
    output_path.write_bytes(concat_wavs(wav_parts) if len(wav_parts) > 1 else wav_parts[0])
    return wav_duration(output_path)


def write_markdown_report(report: dict, path: Path) -> None:
    lines = [
        f"# VOICEVOX Report: {report['course_id']} {report['lecture_id']}",
        "",
        "## Result",
        "",
        f"- Status: {report['status']}",
        f"- Started at: {report['started_at']}",
        f"- Ended at: {report['ended_at']}",
        f"- Speaker ID: {report['speaker_id']}",
        f"- Speed scale: {report['speed_scale']}",
        f"- Audio count: {report['audio_count']}",
        f"- Total duration seconds: {report['total_duration_seconds']}",
        "",
        "## Audio",
        "",
        "| Slide | Duration sec | Size bytes |",
        "| ---: | ---: | ---: |",
    ]
    for item in report["audio"]:
        lines.append(f"| {item['slide_number']} | {item['duration_seconds']} | {item['size_bytes']} |")
    lines.extend(
        [
            "",
            "## Review",
            "",
            "- Engine: local VOICEVOX Engine",
            "- gTTS fallback: not used",
            "- Worker: AI-Production-01",
            "- Reviewer: AI-QA-01",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script_json", type=Path)
    parser.add_argument("audio_dir", type=Path)
    parser.add_argument("--course-id", default="aws-cloudwatch-intro-course")
    parser.add_argument("--lecture-id", default="s1-l1")
    parser.add_argument("--speaker-id", type=int, default=DEFAULT_SPEAKER_ID)
    parser.add_argument("--speed-scale", type=float, default=DEFAULT_SPEED_SCALE)
    parser.add_argument("--engine-path", type=Path, default=DEFAULT_ENGINE)
    parser.add_argument("--slide", type=int, help="Generate only one slide number.")
    parser.add_argument("--skip-existing", action="store_true", help="Reuse existing non-empty WAV files.")
    args = parser.parse_args()

    data = json.loads(args.script_json.read_text(encoding="utf-8"))
    slides = data.get("slides", [])
    if not slides:
        raise SystemExit("No slides found in script JSON")

    engine_process: subprocess.Popen[str] | None = None
    if not engine_is_running():
        engine_process = start_engine(args.engine_path)

    args.audio_dir.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    report = {
        "course_id": args.course_id,
        "lecture_id": args.lecture_id,
        "script_json": str(args.script_json),
        "audio_dir": str(args.audio_dir),
        "started_at": started,
        "ended_at": "",
        "status": "running",
        "speaker_id": args.speaker_id,
        "speed_scale": args.speed_scale,
        "audio": [],
    }
    try:
        total = 0.0
        for slide in slides:
            number = int(slide["slide_number"])
            if args.slide is not None and number != args.slide:
                continue
            narration = str(slide.get("narration", "")).strip()
            if not narration:
                raise ValueError(f"Slide {number} narration is empty")
            output = args.audio_dir / f"slide_{number:03d}.wav"
            if args.skip_existing and output.exists() and output.stat().st_size > 0:
                try:
                    duration = wav_duration(output)
                    print(f"slide {number}/{len(slides)} exists -> {output}", flush=True)
                    total += duration
                    report["audio"].append(
                        {
                            "slide_number": number,
                            "duration_seconds": round(duration, 3),
                            "size_bytes": output.stat().st_size,
                        }
                    )
                    continue
                except wave.Error:
                    output.unlink(missing_ok=True)
            print(f"slide {number}/{len(slides)} -> {output}", flush=True)
            duration = generate_wav(narration, output, args.speaker_id, args.speed_scale)
            total += duration
            report["audio"].append(
                {
                    "slide_number": number,
                    "duration_seconds": round(duration, 3),
                    "size_bytes": output.stat().st_size,
                }
            )
        report["audio_count"] = len(report["audio"])
        report["total_duration_seconds"] = round(total, 3)
        report["status"] = "pass"
        report["ended_at"] = utc_now()
        (args.audio_dir / "voicevox_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        write_markdown_report(report, args.audio_dir / "voicevox_report.md")
        print(json.dumps({k: v for k, v in report.items() if k != "audio"}, ensure_ascii=False, indent=2))
        return 0
    finally:
        if engine_process and engine_process.poll() is None:
            engine_process.terminate()
            try:
                engine_process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                engine_process.kill()


if __name__ == "__main__":
    raise SystemExit(main())
