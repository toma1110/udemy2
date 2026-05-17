# Course Production QA Report

## Result

- Status: pass for local remediated video artifacts
- Course ID: `aws-cloudwatch-logs-insights-practical-course`
- Course Title: AWS CloudWatch Logs Insights実践: 障害調査クエリ集
- Original production date: 2026-05-15
- Runtime remediation date: 2026-05-17
- Current lecture video runtime: 2058.560 sec (34.31 min)
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## Deliverables

| Area | Result |
| --- | --- |
| Lecture scripts | 8 Markdown files and 8 JSON files updated for 4〜5 minute lectures |
| GPT-Image2 prompts | 8 prompt Markdown files preserved |
| GPT-Image2 source PNG | 48 source PNG files preserved |
| Final slide PNG | 48 fitted 1920x1080 PNG files reused for final videos |
| VOICEVOX WAV | 48 WAV files regenerated on 2026-05-17 |
| MP4 video | 8 final MP4 files regenerated on 2026-05-17 |
| Drive upload | 8 remediated videos uploaded in `TASK-0222` with anyone-reader sharing |

## Quality Gate

- pass: `course_spec.md` is the source of truth.
- pass: CEO approved curriculum before video generation.
- pass: AWS official documentation verification report exists.
- pass: No standard AWS resource creation is required for the hands-on.
- pass: GPT-Image2-derived slide PNGs are used for final videos.
- pass: No local text overlay was added to final slides.
- pass: VOICEVOX audio reports are present for all lectures.
- pass: MP4 build reports are present, faststart is true for all lectures.
- pass: Total main lecture runtime is over 30 minutes.
- pass: Worker and Reviewer are separated in tickets and reports.

## Residual Risk

- Google Drive upload for the remediated 2026-05-17 MP4 files was completed in `TASK-0222`; transcoding status may complete asynchronously on Drive.
- GPT-Image2-generated small text may contain minor visual imperfections; the primary title/subtitle and diagram intent are usable for review.
