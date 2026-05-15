# Course Production QA Report

## Result

- Status: pass
- Course ID: `aws-cloudwatch-logs-insights-practical-course`
- Course Title: AWS CloudWatch Logs Insights実践: 障害調査クエリ集
- Production date: 2026-05-15
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## Deliverables

| Area | Result |
| --- | --- |
| Lecture scripts | 8 Markdown files and 8 JSON files |
| GPT-Image2 prompts | 8 prompt Markdown files |
| GPT-Image2 source PNG | 48 source PNG files |
| Final slide PNG | 48 fitted 1920x1080 PNG files |
| VOICEVOX WAV | 48 WAV files |
| MP4 video | 8 final MP4 files |
| Drive upload | 8 uploaded review files |

## Quality Gate

- pass: `course_spec.md` is the source of truth.
- pass: AWS official documentation verification report exists.
- pass: No standard AWS resource creation is required for the hands-on.
- pass: GPT-Image2-derived slide PNGs are used for final videos.
- pass: No local text overlay was added to final slides.
- pass: VOICEVOX audio reports are present for all lectures.
- pass: MP4 build reports are present, faststart is true for all lectures.
- pass: Drive metadata confirms public reader permission for all uploaded files.
- pass: Worker and Reviewer are separated in tickets and reports.

## Residual Risk

- GPT-Image2-generated small text may contain minor visual imperfections; the primary title/subtitle and diagram intent are usable for review.
- Google Drive transcoding status is outside the local build pipeline and may complete after upload.
