# Render Report: aws-slo-adoption-course s6-l4

## Result

- Status: pass
- Started at: 2026-05-12T01:56:14Z
- Ended at: 2026-05-12T01:57:40Z
- Elapsed seconds: 86.574
- Slide count: 8
- Audio count: 8
- Output duration seconds: 133.643
- Output size bytes: 5033075

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.088 | 0 |
| render segment 001 | 10.107 | 0 |
| ffprobe duration slide_002.wav | 0.086 | 0 |
| render segment 002 | 8.768 | 0 |
| ffprobe duration slide_003.wav | 0.089 | 0 |
| render segment 003 | 9.995 | 0 |
| ffprobe duration slide_004.wav | 0.086 | 0 |
| render segment 004 | 8.757 | 0 |
| ffprobe duration slide_005.wav | 0.088 | 0 |
| render segment 005 | 8.695 | 0 |
| ffprobe duration slide_006.wav | 0.087 | 0 |
| render segment 006 | 9.597 | 0 |
| ffprobe duration slide_007.wav | 0.086 | 0 |
| render segment 007 | 10.689 | 0 |
| ffprobe duration slide_008.wav | 0.086 | 0 |
| render segment 008 | 11.015 | 0 |
| concat segments | 0.293 | 0 |
| apply faststart | 0.147 | 0 |
| decode check | 5.478 | 0 |
| ffprobe final video | 0.102 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
