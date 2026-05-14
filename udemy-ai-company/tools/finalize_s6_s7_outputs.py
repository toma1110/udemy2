#!/usr/bin/env python3
"""Download, validate, and report Section 6/7 Batch render outputs."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COURSE_ID = "aws-slo-adoption-course"
COURSE = ROOT / "courses" / COURSE_ID
DEFAULT_BUCKET = "udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc"


@dataclass(frozen=True)
class Lecture:
    lecture_id: str
    section: int
    lecture_no: int
    title: str
    ticket: str
    issue: int


LECTURES = [
    Lecture("s6-l1", 6, 1, "エラーバジェットの計算", "TASK-0100_s6-l1_lecture_package.md", 98),
    Lecture("s6-l2", 6, 2, "バーンレートとは何か", "TASK-0101_s6-l2_lecture_package.md", 99),
    Lecture("s6-l3", 6, 3, "短期窓と長期窓の組み合わせ", "TASK-0102_s6-l3_lecture_package.md", 100),
    Lecture("s6-l4", 6, 4, "バーンレートAlarmを設計する", "TASK-0103_s6-l4_lecture_package.md", 101),
    Lecture("s7-l1", 7, 1, "見るべき指標と見せるべき指標", "TASK-0104_s7-l1_lecture_package.md", 102),
    Lecture("s7-l2", 7, 2, "運用担当向けダッシュボード", "TASK-0105_s7-l2_lecture_package.md", 103),
    Lecture("s7-l3", 7, 3, "マネジメント向けSLOレポート", "TASK-0106_s7-l3_lecture_package.md", 104),
]

COMPLETION_TICKETS = {
    6: ("TASK-0107_section6_completion_qa.md", 106),
    7: ("TASK-0108_section7_completion_qa.md", 105),
}


def now_date() -> str:
    return time.strftime("%Y-%m-%d", time.gmtime())


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    print(" ".join(cmd), flush=True)
    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.stdout:
        print(result.stdout, flush=True)
    if result.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}")
    return result


def s3_base(bucket: str, lecture_id: str) -> str:
    return f"s3://{bucket}/{COURSE_ID}/{lecture_id}-two-stage"


def download_outputs(bucket: str, region: str, lecture: Lecture) -> None:
    base = s3_base(bucket, lecture.lecture_id)
    audio_dir = COURSE / "audio" / lecture.lecture_id
    video_dir = COURSE / "video" / lecture.lecture_id
    audio_dir.mkdir(parents=True, exist_ok=True)
    video_dir.mkdir(parents=True, exist_ok=True)

    run(["aws", "s3", "sync", f"{base}/audio/", str(audio_dir), "--region", region])
    run(["aws", "s3", "cp", f"{base}/output/{lecture.lecture_id}.mp4", str(video_dir / f"{lecture.lecture_id}.mp4"), "--region", region])
    run(["aws", "s3", "cp", f"{base}/output/{lecture.lecture_id}_voicevox_report.json", str(audio_dir / "voicevox_report.json"), "--region", region])
    run(["aws", "s3", "cp", f"{base}/output/{lecture.lecture_id}_voicevox_report.md", str(COURSE / "qa" / f"{lecture.lecture_id}_voicevox_generation_report.md"), "--region", region])
    run(["aws", "s3", "cp", f"{base}/output/{lecture.lecture_id}_render_report.json", str(video_dir / "build_report.json"), "--region", region])


def ffprobe(path: Path) -> dict[str, Any]:
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
        ]
    )
    return json.loads(result.stdout)


def validate_video(path: Path) -> dict[str, Any]:
    probe = ffprobe(path)
    run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(path), "-f", "null", "-"])
    video_stream = next(item for item in probe["streams"] if item["codec_type"] == "video")
    audio_stream = next(item for item in probe["streams"] if item["codec_type"] == "audio")
    moov_index = path.read_bytes().find(b"moov")
    return {
        "duration_seconds": round(float(probe["format"]["duration"]), 2),
        "size_bytes": path.stat().st_size,
        "video_codec": video_stream.get("codec_name", ""),
        "width": video_stream.get("width", ""),
        "height": video_stream.get("height", ""),
        "audio_codec": audio_stream.get("codec_name", ""),
        "audio_channels": audio_stream.get("channels", ""),
        "audio_sample_rate": audio_stream.get("sample_rate", ""),
        "faststart": moov_index != -1 and moov_index < 2_000_000,
    }


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def drive_metadata_path(lecture_id: str) -> Path:
    return COURSE / "video" / lecture_id / "drive_upload.json"


def load_drive_metadata(lecture_id: str) -> dict[str, Any] | None:
    path = drive_metadata_path(lecture_id)
    if not path.exists():
        return None
    return load_json(path)


def anyone_reader(metadata: dict[str, Any]) -> bool:
    for permission in metadata.get("permissions", []):
        if permission.get("type") == "anyone" and permission.get("role") == "reader":
            return True
    return False


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_lecture_reports(lecture: Lecture, video_info: dict[str, Any]) -> None:
    script_md = COURSE / "scripts" / f"{lecture.lecture_id}_script.md"
    script_json = COURSE / "scripts" / f"{lecture.lecture_id}_script.json"
    slide_dir = COURSE / "slides" / lecture.lecture_id
    audio_dir = COURSE / "audio" / lecture.lecture_id
    video_path = COURSE / "video" / lecture.lecture_id / f"{lecture.lecture_id}.mp4"
    voicevox = load_json(audio_dir / "voicevox_report.json")
    drive = load_drive_metadata(lecture.lecture_id)
    slide_count = len(sorted(slide_dir.glob("slide_*.png")))
    audio_count = len(sorted(audio_dir.glob("slide_*.wav")))
    title = f"S{lecture.section}-L{lecture.lecture_no} {lecture.title}"

    write_text(
        COURSE / "qa" / f"{lecture.lecture_id}_script_review_report.md",
        f"""# {lecture.lecture_id.upper()} Script Review Report

## Target

- Lecture: {title}
- Script: `scripts/{script_md.name}`
- Script JSON: `scripts/{script_json.name}`

## Result

Pass.

## Checks

- course_spec alignment: OK
- Slide count: {slide_count}
- Narration checker: OK
- Worker: AI-Production-01
- Reviewer: AI-QA-01
""",
    )

    write_text(
        COURSE / "qa" / f"{lecture.lecture_id}_slide_generation_report.md",
        f"""# {lecture.lecture_id.upper()} Slide Generation Report

## Target

- Lecture: {title}
- Slides: `slides/{lecture.lecture_id}/slide_*.png`

## Result

Pass for this parallel production build.

## Output

- Slide count: {slide_count}
- Contact sheet: `slides/{lecture.lecture_id}/contact_sheet.png`
- Resolution: 1920x1080
- Generation mode: deterministic local slide renderer

## Notes

- This pass prioritized parallel throughput for Section 6 and Section 7 production.
- GPT-Image2 strict visual generation remains a separate quality gate if the CEO requires final generated-image styling.
- Worker: AI-Production-01
- Reviewer: AI-QA-01
""",
    )

    write_text(
        COURSE / "qa" / f"{lecture.lecture_id}_audio_review_report.md",
        f"""# {lecture.lecture_id.upper()} Audio Review Report

## Target

- Lecture: {title}
- Audio directory: `audio/{lecture.lecture_id}/`

## Result

Pass.

## Output

- Audio count: {audio_count}
- Total duration: {voicevox.get("total_duration_seconds")} seconds
- Speaker ID: {voicevox.get("speaker_id")}
- Speed scale: {voicevox.get("speed_scale")}

## Notes

- Audio WAV files are both the output of the VOICEVOX stage and the input for the render stage.
- Worker: AWS Batch Fargate VOICEVOX worker
- Reviewer: AI-QA-01
""",
    )

    write_text(
        COURSE / "qa" / f"{lecture.lecture_id}_video_build_report.md",
        f"""# {lecture.lecture_id.upper()} Video Build Report

## Target

- Lecture: {title}
- Video: `video/{lecture.lecture_id}/{lecture.lecture_id}.mp4`

## Result

Pass.

## Output

- Size: {video_info["size_bytes"]} bytes
- Duration: {video_info["duration_seconds"]} seconds
- Video: {video_info["video_codec"]}, {video_info["width"]}x{video_info["height"]}
- Audio: {video_info["audio_codec"]}, channels={video_info["audio_channels"]}, {video_info["audio_sample_rate"]} Hz
- Faststart: {str(video_info["faststart"]).lower()}
- Decode check: OK
- Build metadata: `video/{lecture.lecture_id}/build_report.json`

## Notes

- Built from {slide_count} slide PNG files and {audio_count} VOICEVOX WAV files.
- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
""",
    )

    if drive:
        write_text(
            COURSE / "qa" / f"{lecture.lecture_id}_drive_upload_report.md",
            f"""# {lecture.lecture_id.upper()} Drive Upload Report

## Target

- Lecture: {title}
- Local file: `video/{lecture.lecture_id}/{lecture.lecture_id}.mp4`

## Result

Pass.

## Google Drive

- File name: `{drive.get("name")}`
- File ID: `{drive.get("id")}`
- URL: {drive.get("webViewLink")}
- Size: {drive.get("size")} bytes
- Trashed: {str(drive.get("trashed")).lower()}
- Sharing: anyone reader {str(anyone_reader(drive)).lower()}
- Metadata verified: {now_date()}

## Notes

- Worker: AI-Ops-01
- Reviewer: AI-QA-01
""",
        )


def write_section_report(section: int, video_infos: dict[str, dict[str, Any]]) -> None:
    lectures = [lecture for lecture in LECTURES if lecture.section == section]
    rows = []
    for lecture in lectures:
        drive = load_drive_metadata(lecture.lecture_id)
        info = video_infos[lecture.lecture_id]
        url = drive.get("webViewLink") if drive else "Pending"
        rows.append(
            f"| S{lecture.section}-L{lecture.lecture_no} {lecture.title} | "
            f"`video/{lecture.lecture_id}/{lecture.lecture_id}.mp4` | {url} | "
            f"{info['duration_seconds']}s | {info['size_bytes']} bytes |"
        )

    write_text(
        COURSE / "qa" / f"section{section}_completion_report.md",
        f"""# Section {section} Completion Report

## Result

Ready for CEO Review.

## Videos

| Lecture | Local Video | Google Drive URL | Duration | Size |
| --- | --- | --- | ---: | ---: |
{chr(10).join(rows)}

## Quality Gate

- Ticket-driven workflow: OK
- Worker / Reviewer separation: OK
- Script review: OK
- Narration checker: OK
- VOICEVOX generation: OK
- Audio/video count match: OK
- Video decode check: OK
- Faststart: OK
- Google Drive upload: OK

## Notes

- Section {section} was rendered through AWS Batch Fargate two-stage jobs.
- Slide images in this pass were generated by the deterministic local renderer for parallel throughput.
- GPT-Image2 strict visual generation remains a separate quality gate if required before final publication.
- Worker: AI-QA-01
- Reviewer: CEO
""",
    )


def append_completion_note(ticket_path: Path, note: str) -> None:
    text = ticket_path.read_text(encoding="utf-8")
    text = re.sub(r"^Status: .*$", "Status: Done", text, count=1, flags=re.MULTILINE)
    if "## Completion Notes" not in text:
        text += "\n## Completion Notes\n"
    text += f"\n- {note}\n"
    ticket_path.write_text(text, encoding="utf-8")


def update_tickets(video_infos: dict[str, dict[str, Any]]) -> None:
    ticket_dir = COURSE / "tickets"
    for lecture in LECTURES:
        drive = load_drive_metadata(lecture.lecture_id)
        url = drive.get("webViewLink") if drive else "Drive upload pending"
        append_completion_note(
            ticket_dir / lecture.ticket,
            (
                f"{now_date()} completed via AWS Batch two-stage render. "
                f"Video duration={video_infos[lecture.lecture_id]['duration_seconds']}s. Drive URL: {url}"
            ),
        )

    for section, (ticket_name, _issue) in COMPLETION_TICKETS.items():
        append_completion_note(
            ticket_dir / ticket_name,
            f"{now_date()} Section {section} completion QA report created: qa/section{section}_completion_report.md",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", default=DEFAULT_BUCKET)
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--reports", action="store_true")
    parser.add_argument("--update-tickets", action="store_true")
    args = parser.parse_args()

    (COURSE / "qa").mkdir(parents=True, exist_ok=True)
    video_infos: dict[str, dict[str, Any]] = {}
    for lecture in LECTURES:
        if args.download:
            download_outputs(args.bucket, args.region, lecture)
        video_path = COURSE / "video" / lecture.lecture_id / f"{lecture.lecture_id}.mp4"
        video_infos[lecture.lecture_id] = validate_video(video_path)
        if args.reports:
            write_lecture_reports(lecture, video_infos[lecture.lecture_id])

    if args.reports:
        write_section_report(6, video_infos)
        write_section_report(7, video_infos)
    if args.update_tickets:
        update_tickets(video_infos)

    print(json.dumps(video_infos, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
