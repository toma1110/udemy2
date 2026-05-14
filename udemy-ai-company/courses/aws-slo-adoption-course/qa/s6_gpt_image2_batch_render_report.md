# S6 GPT-Image2 Batch Render Report

## Result

Pass.

## Scope

- Section: 6
- Lectures: S6-L1 through S6-L4
- Slide generation: GPT-Image2
- Render pipeline: AWS Batch Fargate render worker
- Audio source: existing VOICEVOX WAV assets
- S3 input prefix pattern: `s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s6-l*-gpt-image2-20260512/`

## Batch Jobs

| Lecture | Job name | Job ID | Status | Runtime seconds |
| --- | --- | --- | --- | ---: |
| S6-L1 | `render-aws-slo-s6-l1-gpt-image2-20260512` | `f41e3657-3c44-463b-90dd-a20410c16e25` | SUCCEEDED | 120.7 |
| S6-L2 | `render-aws-slo-s6-l2-gpt-image2-20260512` | `c510c717-c7bc-42ac-8a04-139578d47c64` | SUCCEEDED | 117.0 |
| S6-L3 | `render-aws-slo-s6-l3-gpt-image2-20260512` | `ecc57d5c-d59f-4a14-9907-642e79924c8c` | SUCCEEDED | 115.2 |
| S6-L4 | `render-aws-slo-s6-l4-gpt-image2-20260512` | `a8098a20-f6e6-4bf7-9878-49d727e9fda4` | SUCCEEDED | 115.2 |

## Validation

- Render reports: `video/s6-l*/build_report.json`
- Video build reports: `qa/s6-l*_video_build_report.md`
- `ffmpeg` decode check: OK for all 4 videos
- MP4 faststart: OK for all 4 videos
- Resolution: 1920x1080
- Audio: AAC mono, 24000 Hz

## Notes

- This pass replaces the earlier Section 6 local-renderer slide pass.
- The original GPT-Image2 PNGs are preserved under `slides/s6-gpt-image2-sources/`.
- Worker: AI-Production-01
- Reviewer: AI-QA-01
