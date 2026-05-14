#!/usr/bin/env python3
"""Render one Udemy lecture from S3 slide PNGs and WAV audio files."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import boto3


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


def run(cmd: list[str], stage: str, report: dict[str, Any]) -> subprocess.CompletedProcess[str]:
    start = time.monotonic()
    started_at = utc_now()
    print(f"[{started_at}] {stage}: {' '.join(cmd)}", flush=True)
    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elapsed = round(time.monotonic() - start, 3)
    report.setdefault("stages", []).append(
        {
            "stage": stage,
            "started_at": started_at,
            "ended_at": utc_now(),
            "elapsed_seconds": elapsed,
            "exit_code": result.returncode,
            "command": cmd,
        }
    )
    if result.stdout:
        print(result.stdout, flush=True)
    if result.returncode != 0:
        raise RuntimeError(f"{stage} failed with exit code {result.returncode}")
    return result


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


def list_prefix(s3: Any, uri: str) -> list[dict[str, Any]]:
    parsed = parse_s3_uri(uri)
    paginator = s3.get_paginator("list_objects_v2")
    objects: list[dict[str, Any]] = []
    for page in paginator.paginate(Bucket=parsed.bucket, Prefix=parsed.key):
        objects.extend(page.get("Contents", []))
    return objects


def download_prefix(s3: Any, uri: str, destination: Path, suffixes: tuple[str, ...]) -> list[Path]:
    parsed = parse_s3_uri(uri)
    destination.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []
    for item in list_prefix(s3, uri):
        key = item["Key"]
        if key.endswith("/") or not key.lower().endswith(suffixes):
            continue
        relative_name = Path(key).name
        local_path = destination / relative_name
        s3.download_file(parsed.bucket, key, str(local_path))
        downloaded.append(local_path)
    return sorted(downloaded)


def ffprobe_duration(path: Path, report: dict[str, Any]) -> float:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        f"ffprobe duration {path.name}",
        report,
    )
    return float(result.stdout.strip())


def ffprobe_json(path: Path, report: dict[str, Any]) -> dict[str, Any]:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ],
        "ffprobe final video",
        report,
    )
    return json.loads(result.stdout)


def render_segments(
    slides: list[Path],
    audio_files: list[Path],
    work_dir: Path,
    video_config: dict[str, Any],
    report: dict[str, Any],
) -> list[Path]:
    width = int(video_config.get("width", 1920))
    height = int(video_config.get("height", 1080))
    fps = int(video_config.get("fps", 30))
    crf = str(video_config.get("crf", 23))
    preset = str(video_config.get("preset", "veryfast"))
    audio_bitrate = str(video_config.get("audio_bitrate", "192k"))
    tail_padding_seconds = float(video_config.get("tail_padding_seconds", 0.2))
    vf = (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,"
        "format=yuv420p"
    )
    segments_dir = work_dir / "segments"
    segments_dir.mkdir(parents=True, exist_ok=True)
    segments: list[Path] = []

    for index, (slide, audio) in enumerate(zip(slides, audio_files, strict=True), start=1):
        duration = ffprobe_duration(audio, report) + tail_padding_seconds
        segment = segments_dir / f"segment_{index:03d}.mp4"
        run(
            [
                "ffmpeg",
                "-nostdin",
                "-y",
                "-loop",
                "1",
                "-framerate",
                str(fps),
                "-i",
                str(slide),
                "-i",
                str(audio),
                "-t",
                f"{duration:.3f}",
                "-vf",
                vf,
                "-c:v",
                "libx264",
                "-preset",
                preset,
                "-crf",
                crf,
                "-tune",
                "stillimage",
                "-c:a",
                "aac",
                "-b:a",
                audio_bitrate,
                "-shortest",
                str(segment),
            ],
            f"render segment {index:03d}",
            report,
        )
        segments.append(segment)

    return segments


def concat_segments(segments: list[Path], work_dir: Path, lecture_id: str, report: dict[str, Any]) -> Path:
    concat_file = work_dir / "concat.txt"
    concat_file.write_text(
        "".join(f"file '{segment.as_posix()}'\n" for segment in segments),
        encoding="utf-8",
    )
    concat_output = work_dir / f"{lecture_id}.concat.mp4"
    final_output = work_dir / f"{lecture_id}.mp4"

    run(
        [
            "ffmpeg",
            "-nostdin",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-c",
            "copy",
            str(concat_output),
        ],
        "concat segments",
        report,
    )
    run(
        [
            "ffmpeg",
            "-nostdin",
            "-y",
            "-i",
            str(concat_output),
            "-c",
            "copy",
            "-movflags",
            "+faststart",
            str(final_output),
        ],
        "apply faststart",
        report,
    )
    run(
        [
            "ffmpeg",
            "-nostdin",
            "-v",
            "error",
            "-i",
            str(final_output),
            "-f",
            "null",
            "-",
        ],
        "decode check",
        report,
    )
    return final_output


def write_markdown_report(report: dict[str, Any], path: Path) -> None:
    lines = [
        f"# Render Report: {report['course_id']} {report['lecture_id']}",
        "",
        "## Result",
        "",
        f"- Status: {report['status']}",
        f"- Started at: {report['started_at']}",
        f"- Ended at: {report.get('ended_at', '')}",
        f"- Elapsed seconds: {report.get('elapsed_seconds', '')}",
        f"- Slide count: {report.get('slide_count', '')}",
        f"- Audio count: {report.get('audio_count', '')}",
        f"- Output duration seconds: {report.get('output_duration_seconds', '')}",
        f"- Output size bytes: {report.get('output_size_bytes', '')}",
        "",
        "## Stages",
        "",
        "| Stage | Elapsed sec | Exit code |",
        "| --- | ---: | ---: |",
    ]
    for stage in report.get("stages", []):
        lines.append(
            f"| {stage['stage']} | {stage['elapsed_seconds']} | {stage['exit_code']} |"
        )
    lines.extend(
        [
            "",
            "## Review",
            "",
            "- Worker: AWS Batch Fargate render worker",
            "- Reviewer: AI-QA-01",
            "- ffmpeg -nostdin: yes",
            "- Decode check: yes",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Udemy lecture video from an S3 manifest.")
    parser.add_argument("--manifest-s3-uri", required=True)
    args = parser.parse_args()

    started_monotonic = time.monotonic()
    s3 = boto3.client("s3")
    work_dir = Path(os.environ.get("RENDER_WORK_DIR", "/tmp/render-work"))
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    manifest_path = work_dir / "manifest.json"
    download_object(s3, args.manifest_s3_uri, manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    course_id = manifest["course_id"]
    lecture_id = manifest["lecture_id"]
    output_s3_uri = manifest["output_s3_uri"].rstrip("/")
    report: dict[str, Any] = {
        "course_id": course_id,
        "lecture_id": lecture_id,
        "manifest_s3_uri": args.manifest_s3_uri,
        "started_at": utc_now(),
        "status": "running",
        "stages": [],
    }

    try:
        slides = download_prefix(s3, manifest["slides_s3_uri"], work_dir / "slides", (".png",))
        audio_files = download_prefix(s3, manifest["audio_s3_uri"], work_dir / "audio", (".wav",))
        report["slide_count"] = len(slides)
        report["audio_count"] = len(audio_files)

        if not slides:
            raise ValueError("No slide PNG files were found.")
        if len(slides) != len(audio_files):
            raise ValueError(f"Slide/audio count mismatch: slides={len(slides)} audio={len(audio_files)}")

        segments = render_segments(slides, audio_files, work_dir, manifest.get("video", {}), report)
        final_video = concat_segments(segments, work_dir, lecture_id, report)
        probe = ffprobe_json(final_video, report)
        duration = float(probe["format"]["duration"])

        report["output_duration_seconds"] = round(duration, 3)
        report["output_size_bytes"] = final_video.stat().st_size
        report["ffprobe"] = probe
        report["status"] = "pass"
        report["ended_at"] = utc_now()
        report["elapsed_seconds"] = round(time.monotonic() - started_monotonic, 3)

        json_report_path = work_dir / f"{lecture_id}_render_report.json"
        markdown_report_path = work_dir / f"{lecture_id}_render_report.md"
        json_report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_markdown_report(report, markdown_report_path)

        upload_object(s3, final_video, f"{output_s3_uri}/{lecture_id}.mp4", "video/mp4")
        upload_object(s3, json_report_path, f"{output_s3_uri}/{lecture_id}_render_report.json", "application/json")
        upload_object(s3, markdown_report_path, f"{output_s3_uri}/{lecture_id}_render_report.md", "text/markdown")
        print(f"[{utc_now()}] render completed: s3 output={output_s3_uri}", flush=True)
        return 0
    except Exception as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
        report["ended_at"] = utc_now()
        report["elapsed_seconds"] = round(time.monotonic() - started_monotonic, 3)
        failure_report_path = work_dir / f"{lecture_id}_render_report.failed.json"
        failure_report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        try:
            upload_object(s3, failure_report_path, f"{output_s3_uri}/{lecture_id}_render_report.failed.json", "application/json")
        except Exception as upload_exc:
            print(f"failed to upload failure report: {upload_exc}", file=sys.stderr, flush=True)
        print(f"render failed: {exc}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
