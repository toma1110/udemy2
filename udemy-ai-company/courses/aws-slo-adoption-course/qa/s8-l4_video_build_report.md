# Render Report: aws-slo-adoption-course s8-l4

## Result

- Status: pass
- Started at: 2026-05-12T15:38:31Z
- Ended at: 2026-05-12T15:39:58Z
- Elapsed seconds: 86.907
- Slide count: 8
- Audio count: 8
- Output duration seconds: 132.149
- Output size bytes: 4831141

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.088 | 0 |
| render segment 001 | 9.551 | 0 |
| ffprobe duration slide_002.wav | 0.086 | 0 |
| render segment 002 | 9.825 | 0 |
| ffprobe duration slide_003.wav | 0.086 | 0 |
| render segment 003 | 9.723 | 0 |
| ffprobe duration slide_004.wav | 0.087 | 0 |
| render segment 004 | 8.93 | 0 |
| ffprobe duration slide_005.wav | 0.087 | 0 |
| render segment 005 | 9.858 | 0 |
| ffprobe duration slide_006.wav | 0.088 | 0 |
| render segment 006 | 10.473 | 0 |
| ffprobe duration slide_007.wav | 0.088 | 0 |
| render segment 007 | 8.225 | 0 |
| ffprobe duration slide_008.wav | 0.088 | 0 |
| render segment 008 | 10.892 | 0 |
| concat segments | 0.277 | 0 |
| apply faststart | 0.137 | 0 |
| decode check | 5.905 | 0 |
| ffprobe final video | 0.098 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
