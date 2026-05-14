#!/usr/bin/env python3
"""Build a lecture MP4 from matching slide PNGs and VOICEVOX WAV files."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ffmpeg_args(*args: str) -> list[str]:
    return ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", *args]


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(json.loads(result.stdout)["format"]["duration"])


def moov_before_mdat(path: Path) -> bool:
    data = path.read_bytes()
    moov = data.find(b"moov")
    mdat = data.find(b"mdat")
    return moov != -1 and mdat != -1 and moov < mdat


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lecture", required=True)
    parser.add_argument("--course-root", type=Path, default=Path("udemy-ai-company/courses/aws-slo-adoption-course"))
    parser.add_argument("--dynamic", action="store_true", help="Apply a subtle zoom motion to each slide.")
    parser.add_argument("--fps", type=int, default=1)
    args = parser.parse_args()

    lecture = args.lecture
    root = args.course_root
    slide_dir = root / "slides" / lecture
    audio_dir = root / "audio" / lecture
    video_dir = root / "video" / lecture
    segment_dir = video_dir / "segments"

    slides = sorted(slide_dir.glob("slide_*.png"))
    audios = sorted(audio_dir.glob("slide_*.wav"))
    if len(slides) != len(audios):
        raise SystemExit(f"slide/audio count mismatch: {len(slides)} slides, {len(audios)} audios")
    if not slides:
        raise SystemExit(f"no slides found: {slide_dir}")

    shutil.rmtree(segment_dir, ignore_errors=True)
    segment_dir.mkdir(parents=True, exist_ok=True)
    video_dir.mkdir(parents=True, exist_ok=True)

    segment_paths: list[Path] = []
    for index, (slide, audio) in enumerate(zip(slides, audios), 1):
        print(f"{lecture}: encoding segment {index}/{len(slides)}", flush=True)
        segment = segment_dir / f"segment_{index:03d}.mp4"
        segment_paths.append(segment)
        if args.dynamic:
            fps = max(1, args.fps)
            duration = probe_duration(audio)
            frames = max(1, math.ceil(duration * fps))
            vf = (
                "scale=2000:1125,"
                f"zoompan=z='min(1.03,1+0.03*on/{frames})':"
                "x='iw/2-(iw/zoom/2)':"
                "y='ih/2-(ih/zoom/2)':"
                f"d={frames}:s=1920x1080:fps={fps},"
                "setsar=1"
            )
        else:
            fps = max(1, args.fps)
            duration = None
            vf = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1"

        cmd = ffmpeg_args(
                "-y",
                "-framerate",
                "1",
                "-loop",
                "1",
                "-i",
                str(slide),
                "-i",
                str(audio),
                "-vf",
                vf,
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-tune",
                "stillimage",
                "-pix_fmt",
                "yuv420p",
                "-r",
                str(fps),
                "-c:a",
                "aac",
                "-ac",
                "2",
                "-ar",
                "44100",
                "-b:a",
                "256k",
                "-shortest",
        )
        if duration is not None:
            cmd.extend(["-t", f"{duration:.3f}"])
        cmd.append(str(segment))
        run(cmd)

    concat = video_dir / "concat.txt"
    concat.write_text(
        "".join(f"file '{segment.resolve()}'\n" for segment in segment_paths),
        encoding="utf-8",
    )

    raw = video_dir / f"{lecture}.raw.mp4"
    final = video_dir / f"{lecture}.mp4"
    print(f"{lecture}: concatenating segments", flush=True)
    run(
        ffmpeg_args(
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat),
            "-c",
            "copy",
            str(raw),
        )
    )
    print(f"{lecture}: applying faststart", flush=True)
    run(
        ffmpeg_args(
            "-y",
            "-i",
            str(raw),
            "-c",
            "copy",
            "-movflags",
            "+faststart",
            str(final),
        )
    )
    raw.unlink(missing_ok=True)

    print(f"{lecture}: validating decode", flush=True)
    run(ffmpeg_args("-i", str(final), "-f", "null", "-"))

    duration = probe_duration(final)
    report = {
        "lecture": lecture,
        "slides": len(slides),
        "audios": len(audios),
        "duration": duration,
        "size": final.stat().st_size,
        "faststart": moov_before_mdat(final),
        "output": str(final),
        "dynamic": args.dynamic,
        "fps": args.fps,
    }
    (video_dir / "build_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))

    frame_time = min(90.0, max(1.0, duration / 2))
    frame = video_dir / f"frame_check_{int(frame_time)}s.png"
    print(f"{lecture}: extracting frame check", flush=True)
    run(ffmpeg_args("-y", "-ss", f"{frame_time:.3f}", "-i", str(final), "-frames:v", "1", str(frame)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
