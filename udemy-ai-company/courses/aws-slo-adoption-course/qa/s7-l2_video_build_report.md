# Render Report: aws-slo-adoption-course s7-l2

## Result

- Status: pass
- Started at: 2026-05-12T12:38:11Z
- Ended at: 2026-05-12T12:39:40Z
- Elapsed seconds: 89.515
- Slide count: 8
- Audio count: 8
- Output duration seconds: 133.397
- Output size bytes: 5167215

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.089 | 0 |
| render segment 001 | 9.646 | 0 |
| ffprobe duration slide_002.wav | 0.087 | 0 |
| render segment 002 | 9.298 | 0 |
| ffprobe duration slide_003.wav | 0.088 | 0 |
| render segment 003 | 10.312 | 0 |
| ffprobe duration slide_004.wav | 0.088 | 0 |
| render segment 004 | 10.938 | 0 |
| ffprobe duration slide_005.wav | 0.087 | 0 |
| render segment 005 | 9.618 | 0 |
| ffprobe duration slide_006.wav | 0.087 | 0 |
| render segment 006 | 9.686 | 0 |
| ffprobe duration slide_007.wav | 0.086 | 0 |
| render segment 007 | 9.232 | 0 |
| ffprobe duration slide_008.wav | 0.086 | 0 |
| render segment 008 | 11.165 | 0 |
| concat segments | 0.328 | 0 |
| apply faststart | 0.146 | 0 |
| decode check | 5.857 | 0 |
| ffprobe final video | 0.103 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
