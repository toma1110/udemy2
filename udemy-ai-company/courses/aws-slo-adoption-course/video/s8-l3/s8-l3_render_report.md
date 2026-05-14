# Render Report: aws-slo-adoption-course s8-l3

## Result

- Status: pass
- Started at: 2026-05-12T15:38:39Z
- Ended at: 2026-05-12T15:40:07Z
- Elapsed seconds: 88.446
- Slide count: 8
- Audio count: 8
- Output duration seconds: 136.405
- Output size bytes: 5048849

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.087 | 0 |
| render segment 001 | 9.851 | 0 |
| ffprobe duration slide_002.wav | 0.085 | 0 |
| render segment 002 | 10.619 | 0 |
| ffprobe duration slide_003.wav | 0.085 | 0 |
| render segment 003 | 9.306 | 0 |
| ffprobe duration slide_004.wav | 0.085 | 0 |
| render segment 004 | 9.082 | 0 |
| ffprobe duration slide_005.wav | 0.084 | 0 |
| render segment 005 | 9.403 | 0 |
| ffprobe duration slide_006.wav | 0.086 | 0 |
| render segment 006 | 9.61 | 0 |
| ffprobe duration slide_007.wav | 0.085 | 0 |
| render segment 007 | 10.143 | 0 |
| ffprobe duration slide_008.wav | 0.085 | 0 |
| render segment 008 | 10.826 | 0 |
| concat segments | 0.273 | 0 |
| apply faststart | 0.143 | 0 |
| decode check | 5.383 | 0 |
| ffprobe final video | 0.099 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
