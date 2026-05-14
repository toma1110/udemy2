# S3-L5 Batch Fargate 2段ジョブ QAレポート

## Summary

- Course: aws-slo-adoption-course
- Lecture: s3-l5
- Stack: udemy-render-batch-dev
- Region: us-east-1
- Artifact Bucket: udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc
- Job Queue: udemy-render-queue
- Worker: AI-Ops-01
- Reviewer: AI-QA-01
- Result: pass

## Jobs

| Stage | Job ID | Status | Exit Code |
| --- | --- | --- | ---: |
| VOICEVOX audio generation | cf78a662-a023-4009-b260-6b95fa622ae6 | SUCCEEDED | 0 |
| ffmpeg video render | a76523e7-2c81-4cfd-9397-90ae36633624 | SUCCEEDED | 0 |

## Outputs

- Manifest: s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5-two-stage/manifest.json
- Audio: s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5-two-stage/audio/
- Video: s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5-two-stage/output/s3-l5.mp4
- VOICEVOX report: s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5-two-stage/output/s3-l5_voicevox_report.md
- Render report: s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5-two-stage/output/s3-l5_render_report.md

## VOICEVOX Result

- Started at: 2026-05-11T12:07:57Z
- Ended at: 2026-05-11T12:09:18Z
- Elapsed seconds: 81.585
- Speaker ID: 3
- Speed scale: 1.1
- Audio count: 8
- Total duration seconds: 166.613

## Render Result

- Started at: 2026-05-11T12:10:45Z
- Ended at: 2026-05-11T12:12:33Z
- Elapsed seconds: 108.717
- Slide count: 8
- Audio count: 8
- Output duration seconds: 166.657
- Output size bytes: 6426415
- ffmpeg -nostdin: yes
- Decode check: pass
- Faststart: pass

## Local Verification

`ffprobe` confirmed:

- Video codec: h264
- Audio codec: aac
- Resolution: 1920x1080
- Duration seconds: 166.657000
- Size bytes: 6426415

`ffmpeg -v error -i /tmp/s3-l5-two-stage.mp4 -f null -` completed with exit code 0.

`strings /tmp/s3-l5-two-stage.mp4 | head -n 5` showed `ftyp` followed by `moov`, confirming faststart placement.

## Quality Gate

- CloudFormation validate: pass
- CloudFormation deploy: pass
- AWS smoke test: pass
- VOICEVOX job generated WAV from S3 script: pass
- Render job depended on VOICEVOX job: pass
- Render job generated MP4 from generated WAV and PNG: pass
- Worker != Reviewer: pass
- 常駐ECS Serviceなし: pass
- NAT Gateway追加なし: pass

