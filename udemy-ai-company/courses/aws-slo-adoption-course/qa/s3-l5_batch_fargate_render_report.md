# S3-L5 AWS Batch Fargate Render Report

## Target

- Course: aws-slo-adoption-course
- Lecture: s3-l5
- Task ID: TASK-0079
- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01

## AWS Resources

- Stack: `udemy-render-batch-dev`
- Region: `us-east-1`
- Job queue: `udemy-render-queue`
- Job definition: `arn:aws:batch:us-east-1:668602146132:job-definition/udemy-render-worker:1`
- Job ID: `2f7d5b67-508b-4c2a-a0c9-910ff6c10927`
- ECR image: `668602146132.dkr.ecr.us-east-1.amazonaws.com/udemy-render-worker:latest`
- Artifact bucket: `udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc`

## Result

Pass.

## Output

- Video: `s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5/output/s3-l5.mp4`
- Render report: `s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5/output/s3-l5_render_report.md`
- JSON report: `s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5/output/s3-l5_render_report.json`
- Output size: 6,426,415 bytes
- Output duration: 166.657 seconds

## Timing

- Job submitted: 2026-05-11T11:20:38Z
- Worker started: 2026-05-11T11:21:18Z
- Worker ended: 2026-05-11T11:23:07Z
- Worker elapsed: 109.0 seconds
- Batch status: SUCCEEDED
- Container exit code: 0

## Input

- Slides: 8 PNG files
- Audio: 8 WAV files
- Manifest: `s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5/manifest.json`

## Quality Gate

| Check | Result |
| --- | --- |
| AWS Batch Fargate job submitted | Pass |
| ECR image built by CodeBuild | Pass |
| S3 input manifest used | Pass |
| Slide/audio count match | Pass |
| ffmpeg uses `-nostdin` | Pass |
| Segment render success | Pass |
| concat success | Pass |
| faststart applied | Pass |
| decode check success | Pass |
| MP4 uploaded to S3 | Pass |
| Worker != Reviewer | Pass |

## Notes

- This MVP uses existing VOICEVOX WAV files as input.
- VOICEVOX generation itself is not yet moved to Fargate.
- No ECS Service or NAT Gateway is used; Fargate compute cost occurs only while jobs run.
