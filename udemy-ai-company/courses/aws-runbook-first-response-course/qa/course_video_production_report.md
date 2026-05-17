# Course Video Production Report

## Target

- Course: `aws-runbook-first-response-course`
- Task: `TASK-0218`
- GitHub Issue: #192
- Production date: 2026-05-17
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01

## Summary

- Status: Completed locally and uploaded to Google Drive
- Lecture count: 6
- Total main lecture runtime: 1961.926s (32.70 minutes)
- Udemy runtime gate: PASS, over 30 minutes
- AWS resource execution: none
- Slide rule: GPT-Image2-derived PNGs only, no local text overlay
- Audio rule: VOICEVOX WAV generation

## Lecture Results

| Lecture | Title | Slides | Duration seconds | Faststart | Drive anyone-reader |
| --- | --- | ---: | ---: | --- | --- |
| `s1-l1` | Runbookに何を書くか | 8 | 258.474 | true | true |
| `s1-l2` | PlaybookとRunbookの違い | 8 | 315.188 | true | true |
| `s2-l1` | CloudWatch Alarmから5分で確認すること | 9 | 339.434 | true | true |
| `s2-l2` | Dashboard、Logs、Recent deploy、AWS Healthを見る | 9 | 332.564 | true | true |
| `s3-l1` | Mitigation、Rollback、Escalationを決める | 9 | 357.439 | true | true |
| `s3-l2` | CommunicationとPostmortemへつなげる | 9 | 358.826 | true | true |

## QA Artifacts

- Course contact sheet: `qa/course_slide_contact_sheet.png`
- AWS source verification: `qa/aws_source_verification_report.md`
- Per-lecture production QA: `qa/*_production_qa_report.md`
- Per-lecture build metadata: `qa/*_video_build_report.json`
- Per-lecture Drive metadata: `qa/*_drive_metadata.json`

## Notes

The final MP4 files remain local and are excluded from Git by `.gitignore`; Google Drive URLs are the delivery artifact.
