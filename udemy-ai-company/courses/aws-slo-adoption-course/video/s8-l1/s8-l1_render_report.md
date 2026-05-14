# Render Report: aws-slo-adoption-course s8-l1

## Result

- Status: pass
- Started at: 2026-05-12T15:38:40Z
- Ended at: 2026-05-12T15:40:10Z
- Elapsed seconds: 90.576
- Slide count: 8
- Audio count: 8
- Output duration seconds: 138.38
- Output size bytes: 5323988

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.087 | 0 |
| render segment 001 | 10.711 | 0 |
| ffprobe duration slide_002.wav | 0.086 | 0 |
| render segment 002 | 9.504 | 0 |
| ffprobe duration slide_003.wav | 0.086 | 0 |
| render segment 003 | 10.469 | 0 |
| ffprobe duration slide_004.wav | 0.089 | 0 |
| render segment 004 | 9.712 | 0 |
| ffprobe duration slide_005.wav | 0.085 | 0 |
| render segment 005 | 10.483 | 0 |
| ffprobe duration slide_006.wav | 0.085 | 0 |
| render segment 006 | 9.294 | 0 |
| ffprobe duration slide_007.wav | 0.085 | 0 |
| render segment 007 | 9.783 | 0 |
| ffprobe duration slide_008.wav | 0.085 | 0 |
| render segment 008 | 11.173 | 0 |
| concat segments | 0.33 | 0 |
| apply faststart | 0.146 | 0 |
| decode check | 5.785 | 0 |
| ffprobe final video | 0.103 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
