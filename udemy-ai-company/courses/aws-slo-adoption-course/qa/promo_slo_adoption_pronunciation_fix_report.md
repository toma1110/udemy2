# Promo SLO Adoption Pronunciation Fix Report

## Target

- Course: `aws-slo-adoption-course`
- Asset: `promo_slo_adoption`
- Date: 2026-05-14
- Ticket: `TASK-0124`

## Requested Fix

- `そんな方向け` を `そんなかたむけ` と読ませる
- 対象者を指す `方` を `かた` と読ませる

## Changes

- `scripts/promo_video_script.md`
- `scripts/promo_video_script.json`
- `docs/VOICEVOX_RULES.md`
- `tools/narration_checker.py`
- `tools/generate_voicevox_audio_local.py`
- `infrastructure/batch-fargate/voicevox_worker/voicevox_worker.py`

## Regenerated Assets

- `audio/promo_slo_adoption/slide_001.wav` through `slide_007.wav`
- `video/promo_slo_adoption/promo_slo_adoption.mp4`
- `video/promo_slo_adoption/promo_slo_adoption.30fps.mp4`
- `video/promo_slo_adoption/build_report.json`
- `video/promo_slo_adoption/build_report_30fps.json`
- `video/promo_slo_adoption/drive_upload_pronunciationfix.json`

## Google Drive

- File name: `aws-slo-adoption-promo-slo-adoption-gptimage2-text-pronunciationfix-20260514.mp4`
- File ID: `15dBkmo9Ia1AZcdPy88ETibV6wYZT7Duc`
- Size bytes: 5468104
- Web view link: https://drive.google.com/file/d/15dBkmo9Ia1AZcdPy88ETibV6wYZT7Duc/view?usp=drivesdk

## Verification

| Check | Result |
| --- | --- |
| JSON syntax | PASS |
| VOICEVOX narration checker | PASS |
| Python syntax for touched tools | PASS |
| VOICEVOX WAV regeneration | PASS |
| Stable MP4 build | PASS |
| 30fps MP4 rebuild | PASS |
| 30fps MP4 decode | PASS |
| Faststart | PASS |
| Google Drive upload | PASS |
| Anyone-reader sharing | PASS |

## Remaining Review

- Human/AI-QA listening spot check is still recommended before using the pronunciation-fix upload as the final Udemy upload source.
