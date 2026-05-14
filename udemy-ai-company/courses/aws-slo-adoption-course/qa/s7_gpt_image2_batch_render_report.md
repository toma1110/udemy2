# Section 7 GPT-Image2 Batch Render Report

## Result

Pass.

## Scope

- Course: AWS SLO Adoption Course
- Section: S7 ダッシュボードとレポート
- Slides: GPT-Image2 generated PNGs
- Audio: existing VOICEVOX WAV files
- Renderer: AWS Batch Fargate render worker
- Date: 2026-05-12

## Batch Jobs

| Lecture | Job ID | Status | Duration | Size |
| --- | --- | --- | ---: | ---: |
| S7-L1 | `8c6ebde5-c852-4801-b4ca-6d1383c1b230` | SUCCEEDED | 142.134s | 5498098 bytes |
| S7-L2 | `64991790-f03c-4f80-9bc9-1da33431496e` | SUCCEEDED | 133.397s | 5167215 bytes |
| S7-L3 | `22c15399-95dd-432f-8a02-1fd913aacc31` | SUCCEEDED | 135.671s | 5257427 bytes |

## Assets

| Lecture | Slides | Audio | Contact Sheet | Video |
| --- | ---: | ---: | --- | --- |
| S7-L1 | 8 | 8 | `slides/s7-l1/contact_sheet.png` | `video/s7-l1/s7-l1.mp4` |
| S7-L2 | 8 | 8 | `slides/s7-l2/contact_sheet.png` | `video/s7-l2/s7-l2.mp4` |
| S7-L3 | 8 | 8 | `slides/s7-l3/contact_sheet.png` | `video/s7-l3/s7-l3.mp4` |

## Verification

- GPT-Image2 source preserved: OK
- Slide/audio count match: OK
- ffprobe video/audio streams: OK
- Resolution: 1920x1080 for all MP4s
- MP4 faststart: OK for all 3 videos
- ffmpeg decode check: OK for all 3 videos
- Representative frame extraction at 90s: OK for all 3 videos
- Google Drive upload: OK
- Google Drive sharing: anyone reader true

## Drive URLs

- S7-L1: https://drive.google.com/file/d/1TePcU6JE22ZwOmzVs62trVtUSInJTOqO/view?usp=drivesdk
- S7-L2: https://drive.google.com/file/d/1SbLZbKnKUUDqEQqnacgrnjsH_fPvQUkQ/view?usp=drivesdk
- S7-L3: https://drive.google.com/file/d/1ZB9hzbo6KDTgj1ZPgQJZ2MrbvuGaHJlk/view?usp=drivesdk

## Review

- Worker: AI-Production-01
- Reviewer: AI-QA-01
- CEO review status: Ready for CEO Review
