#!/usr/bin/env python3
"""Generate VOICEVOX WAV files for one lecture from an S3 manifest."""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import boto3
import requests


VOICEVOX_URL = "http://127.0.0.1:50021"
DEFAULT_SPEAKER_ID = 3
DEFAULT_SPEED_SCALE = 1.1
MAX_CHUNK_CHARS = 50

READING_FIXES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"閾値"), "しきいち"),
    (re.compile(r"重大度"), "じゅうだいど"),
    (re.compile(r"根本原因"), "こんぽんげんいん"),
    (re.compile(r"発報"), "はっぽう"),
    (re.compile(r"一気通貫"), "いっきつうかん"),
    (re.compile(r"初学者"), "しょがくしゃ"),
    (re.compile(r"そんな方向け"), "そんなかたむけ"),
    (re.compile(r"(目指す|担当している|進めたい)方(?=[です、。])"), r"\1かた"),
    (re.compile(r"CPU"), "シーピーユー"),
    (re.compile(r"SLO"), "エスエルオー"),
    (re.compile(r"SLI"), "エスエルアイ"),
    (re.compile(r"SLA"), "エスエルエー"),
    (re.compile(r"AWS"), "エーダブリューエス"),
    (re.compile(r"CloudWatch"), "クラウドウォッチ"),
    (re.compile(r"CloudFormation"), "クラウドフォーメーション"),
    (re.compile(r"Application Signals"), "アプリケーションシグナルズ"),
    (re.compile(r"Fargate"), "ファーゲート"),
    (re.compile(r"Batch"), "バッチ"),
    (re.compile(r"p99"), "パーセンタイル99"),
    (re.compile(r"p95"), "パーセンタイル95"),
]

SECTION_RE = re.compile(r"^## Slide (\d+)\s*$")


@dataclass(frozen=True)
class S3Uri:
    bucket: str
    key: str


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def parse_s3_uri(uri: str) -> S3Uri:
    parsed = urlparse(uri)
    if parsed.scheme != "s3" or not parsed.netloc:
        raise ValueError(f"Invalid S3 URI: {uri}")
    return S3Uri(bucket=parsed.netloc, key=parsed.path.lstrip("/"))


def download_object(s3: Any, uri: str, destination: Path) -> None:
    parsed = parse_s3_uri(uri)
    destination.parent.mkdir(parents=True, exist_ok=True)
    s3.download_file(parsed.bucket, parsed.key, str(destination))


def upload_object(s3: Any, source: Path, uri: str, content_type: str | None = None) -> None:
    parsed = parse_s3_uri(uri)
    extra_args = {"ContentType": content_type} if content_type else None
    if extra_args:
        s3.upload_file(str(source), parsed.bucket, parsed.key, ExtraArgs=extra_args)
    else:
        s3.upload_file(str(source), parsed.bucket, parsed.key)


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


def parse_markdown_script(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = value_after_heading(lines, "Title") or path.stem
    slide_starts: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = SECTION_RE.match(line)
        if match:
            slide_starts.append((int(match.group(1)), index))

    slides: list[dict[str, Any]] = []
    for pos, (slide_number, start) in enumerate(slide_starts):
        end = slide_starts[pos + 1][1] if pos + 1 < len(slide_starts) else len(lines)
        block = lines[start:end]
        slides.append(
            {
                "slide_number": slide_number,
                "title": value_after_heading(block, "Slide Title"),
                "narration": value_after_heading(block, "Narration"),
            }
        )
    return {"title": title, "slides": slides}


def load_script(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return parse_markdown_script(path)


def normalize_for_voicevox(text: str) -> str:
    for pattern, replacement in READING_FIXES:
        text = pattern.sub(replacement, text)
    return text


def split_text_chunks(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    def split_long(part: str) -> list[str]:
        if len(part) <= max_chars:
            return [part]
        pieces = re.split(r"(?<=[、？」！」])", part)
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
    with wave.open(str(path), "rb") as wav:
        return wav.getnframes() / float(wav.getframerate())


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
    for chunk in chunks:
        for attempt in range(1, 4):
            try:
                wav_parts.append(synthesize_chunk(chunk, speaker_id, speed_scale))
                break
            except (requests.ConnectionError, requests.Timeout):
                if attempt == 3:
                    raise
                time.sleep(5 * attempt)

    combined = concat_wavs(wav_parts) if len(wav_parts) > 1 else wav_parts[0]
    output_path.write_bytes(combined)
    return wav_duration(output_path)


def engine_candidates() -> list[tuple[list[str], Path | None]]:
    env_command = os.environ.get("VOICEVOX_ENGINE_COMMAND")
    candidates: list[tuple[list[str], Path | None]] = []
    if env_command:
        candidates.append((env_command.split(), None))
    candidates.extend(
        [
            (
                [
                    "gosu",
                    "user",
                    "/opt/voicevox_engine/run",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    "50021",
                    "--output_log_utf8",
                ],
                None,
            ),
            (
                [
                    "/opt/voicevox_engine/run",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    "50021",
                    "--output_log_utf8",
                ],
                None,
            ),
            (["/opt/voicevox_engine/linux-cpu-x64/run", "--host", "127.0.0.1", "--port", "50021"], None),
        ]
    )
    return candidates


def wait_for_engine(process: subprocess.Popen[str]) -> None:
    deadline = time.monotonic() + 180
    last_error = ""
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"VOICEVOX engine exited early with code {process.returncode}")
        try:
            response = requests.get(f"{VOICEVOX_URL}/version", timeout=5)
            if response.ok:
                print(f"VOICEVOX engine ready: {response.text}", flush=True)
                return
            last_error = f"status={response.status_code}"
        except requests.RequestException as exc:
            last_error = str(exc)
        time.sleep(3)
    raise RuntimeError(f"VOICEVOX engine did not become ready: {last_error}")


def start_voicevox_engine() -> subprocess.Popen[str]:
    failures: list[str] = []
    for command, cwd in engine_candidates():
        process: subprocess.Popen[str] | None = None
        if cwd is not None and not cwd.exists():
            failures.append(f"missing cwd for {' '.join(command)}: {cwd}")
            continue
        try:
            print(f"starting VOICEVOX engine: {' '.join(command)}", flush=True)
            process = subprocess.Popen(
                command,
                cwd=str(cwd) if cwd else None,
                stdout=sys.stdout,
                stderr=sys.stderr,
                text=True,
            )
            wait_for_engine(process)
            return process
        except Exception as exc:
            failures.append(f"{' '.join(command)} -> {exc}")
            try:
                if process is not None and process.poll() is None:
                    process.terminate()
            except Exception:
                pass
    raise RuntimeError("Unable to start VOICEVOX engine:\n" + "\n".join(failures))


def write_report(report: dict[str, Any], path: Path) -> None:
    lines = [
        f"# VOICEVOX Report: {report['course_id']} {report['lecture_id']}",
        "",
        "## Result",
        "",
        f"- Status: {report['status']}",
        f"- Started at: {report['started_at']}",
        f"- Ended at: {report.get('ended_at', '')}",
        f"- Elapsed seconds: {report.get('elapsed_seconds', '')}",
        f"- Speaker ID: {report.get('speaker_id', '')}",
        f"- Speed scale: {report.get('speed_scale', '')}",
        f"- Audio count: {report.get('audio_count', '')}",
        f"- Total duration seconds: {report.get('total_duration_seconds', '')}",
        "",
        "## Audio",
        "",
        "| Slide | Duration sec | Size bytes |",
        "| ---: | ---: | ---: |",
    ]
    for item in report.get("audio", []):
        lines.append(f"| {item['slide_number']} | {item['duration_seconds']} | {item['size_bytes']} |")
    lines.extend(
        [
            "",
            "## Review",
            "",
            "- Worker: AWS Batch Fargate VOICEVOX worker",
            "- Reviewer: AI-QA-01",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest-s3-uri", required=True)
    args = parser.parse_args()

    started = time.monotonic()
    s3 = boto3.client("s3")
    work_dir = Path(os.environ.get("VOICEVOX_WORK_DIR", "/tmp/voicevox-work"))
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    manifest_path = work_dir / "manifest.json"
    download_object(s3, args.manifest_s3_uri, manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    course_id = manifest["course_id"]
    lecture_id = manifest["lecture_id"]
    audio_s3_uri = manifest["audio_s3_uri"].rstrip("/")
    output_s3_uri = manifest["output_s3_uri"].rstrip("/")
    speaker_id = int(manifest.get("voicevox", {}).get("speaker_id", DEFAULT_SPEAKER_ID))
    speed_scale = float(manifest.get("voicevox", {}).get("speed_scale", DEFAULT_SPEED_SCALE))

    report: dict[str, Any] = {
        "course_id": course_id,
        "lecture_id": lecture_id,
        "manifest_s3_uri": args.manifest_s3_uri,
        "started_at": utc_now(),
        "status": "running",
        "speaker_id": speaker_id,
        "speed_scale": speed_scale,
        "audio": [],
    }
    engine_process: subprocess.Popen[str] | None = None
    try:
        script_uri = manifest.get("script_s3_uri")
        if not script_uri:
            raise ValueError("manifest.script_s3_uri is required for VOICEVOX job")

        script_path = work_dir / Path(parse_s3_uri(script_uri).key).name
        download_object(s3, script_uri, script_path)
        script = load_script(script_path)
        slides = script.get("slides", [])
        if not slides:
            raise ValueError("No slides were found in script")

        engine_process = start_voicevox_engine()
        audio_dir = work_dir / "audio"
        audio_dir.mkdir(parents=True)

        total_duration = 0.0
        for slide in slides:
            slide_number = int(slide["slide_number"])
            narration = str(slide.get("narration", "")).strip()
            if not narration:
                raise ValueError(f"Slide {slide_number} has empty narration")
            wav_path = audio_dir / f"slide_{slide_number:03d}.wav"
            print(f"generating slide {slide_number}: {wav_path}", flush=True)
            duration = generate_wav(narration, wav_path, speaker_id, speed_scale)
            total_duration += duration
            upload_object(s3, wav_path, f"{audio_s3_uri}/slide_{slide_number:03d}.wav", "audio/wav")
            report["audio"].append(
                {
                    "slide_number": slide_number,
                    "duration_seconds": round(duration, 3),
                    "size_bytes": wav_path.stat().st_size,
                }
            )

        report["audio_count"] = len(report["audio"])
        report["total_duration_seconds"] = round(total_duration, 3)
        report["status"] = "pass"
        report["ended_at"] = utc_now()
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)

        json_report = work_dir / f"{lecture_id}_voicevox_report.json"
        markdown_report = work_dir / f"{lecture_id}_voicevox_report.md"
        json_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_report(report, markdown_report)
        upload_object(s3, json_report, f"{output_s3_uri}/{lecture_id}_voicevox_report.json", "application/json")
        upload_object(s3, markdown_report, f"{output_s3_uri}/{lecture_id}_voicevox_report.md", "text/markdown")
        return 0
    except Exception as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
        report["ended_at"] = utc_now()
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        failure_report = work_dir / f"{lecture_id}_voicevox_report.failed.json"
        failure_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        try:
            upload_object(s3, failure_report, f"{output_s3_uri}/{lecture_id}_voicevox_report.failed.json", "application/json")
        except Exception as upload_exc:
            print(f"failed to upload failure report: {upload_exc}", file=sys.stderr, flush=True)
        print(f"VOICEVOX job failed: {exc}", file=sys.stderr, flush=True)
        return 1
    finally:
        if engine_process and engine_process.poll() is None:
            engine_process.terminate()


if __name__ == "__main__":
    raise SystemExit(main())
