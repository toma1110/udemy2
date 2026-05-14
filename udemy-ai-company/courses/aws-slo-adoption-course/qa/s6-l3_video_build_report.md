# Render Report: aws-slo-adoption-course s6-l3

## Result

- Status: pass
- Started at: 2026-05-12T01:56:18Z
- Ended at: 2026-05-12T01:57:43Z
- Elapsed seconds: 86.171
- Slide count: 8
- Audio count: 8
- Output duration seconds: 134.368
- Output size bytes: 4877850

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.088 | 0 |
| render segment 001 | 9.548 | 0 |
| ffprobe duration slide_002.wav | 0.087 | 0 |
| render segment 002 | 9.249 | 0 |
| ffprobe duration slide_003.wav | 0.087 | 0 |
| render segment 003 | 10.237 | 0 |
| ffprobe duration slide_004.wav | 0.086 | 0 |
| render segment 004 | 9.701 | 0 |
| ffprobe duration slide_005.wav | 0.086 | 0 |
| render segment 005 | 9.718 | 0 |
| ffprobe duration slide_006.wav | 0.086 | 0 |
| render segment 006 | 9.124 | 0 |
| ffprobe duration slide_007.wav | 0.087 | 0 |
| render segment 007 | 9.474 | 0 |
| ffprobe duration slide_008.wav | 0.087 | 0 |
| render segment 008 | 9.795 | 0 |
| concat segments | 0.277 | 0 |
| apply faststart | 0.138 | 0 |
| decode check | 5.923 | 0 |
| ffprobe final video | 0.098 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
