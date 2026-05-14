# S6/S7 Batch Parallel Run Report

## Result

Pass.

## Scope

- Section 6: 4 lectures
- Section 7: 3 lectures
- Pipeline: AWS Batch Fargate two-stage jobs
- Stage 1: VOICEVOX audio generation
- Stage 2: slide/audio render

## Timing

- Wall clock from first container start to last render completion: 572.1 seconds
- Wall clock: about 9 minutes 32 seconds
- Max vCPUs configured for this run: 16
- Effective concurrency: about 4 active 4-vCPU jobs

## Job Durations

| Job | Status | Runtime seconds |
| --- | --- | ---: |
| render-aws-slo-s6-l1-two-stage-voicevox | SUCCEEDED | 119.3 |
| render-aws-slo-s6-l1-two-stage-render | SUCCEEDED | 111.5 |
| render-aws-slo-s6-l2-two-stage-voicevox | SUCCEEDED | 101.5 |
| render-aws-slo-s6-l2-two-stage-render | SUCCEEDED | 98.0 |
| render-aws-slo-s6-l3-two-stage-voicevox | SUCCEEDED | 98.2 |
| render-aws-slo-s6-l3-two-stage-render | SUCCEEDED | 103.3 |
| render-aws-slo-s6-l4-two-stage-voicevox | SUCCEEDED | 96.7 |
| render-aws-slo-s6-l4-two-stage-render | SUCCEEDED | 73.0 |
| render-aws-slo-s7-l1-two-stage-voicevox | SUCCEEDED | 112.9 |
| render-aws-slo-s7-l1-two-stage-render | SUCCEEDED | 101.5 |
| render-aws-slo-s7-l2-two-stage-voicevox | SUCCEEDED | 109.0 |
| render-aws-slo-s7-l2-two-stage-render | SUCCEEDED | 96.0 |
| render-aws-slo-s7-l3-two-stage-voicevox | SUCCEEDED | 95.6 |
| render-aws-slo-s7-l3-two-stage-render | SUCCEEDED | 84.7 |

## Notes

- All AWS Batch jobs exited with code 0.
- Local MP4 validation passed for all seven videos.
- Google Drive upload passed for all seven videos.
- Worker: AI-Ops-01
- Reviewer: AI-QA-01
