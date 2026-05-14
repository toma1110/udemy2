# Render Report: aws-slo-adoption-course s8-l2

## Result

- Status: pass
- Started at: 2026-05-12T15:38:31Z
- Ended at: 2026-05-12T15:40:01Z
- Elapsed seconds: 89.738
- Slide count: 8
- Audio count: 8
- Output duration seconds: 137.772
- Output size bytes: 5023268

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.088 | 0 |
| render segment 001 | 9.691 | 0 |
| ffprobe duration slide_002.wav | 0.087 | 0 |
| render segment 002 | 9.437 | 0 |
| ffprobe duration slide_003.wav | 0.088 | 0 |
| render segment 003 | 11.057 | 0 |
| ffprobe duration slide_004.wav | 0.088 | 0 |
| render segment 004 | 9.819 | 0 |
| ffprobe duration slide_005.wav | 0.087 | 0 |
| render segment 005 | 9.434 | 0 |
| ffprobe duration slide_006.wav | 0.087 | 0 |
| render segment 006 | 8.939 | 0 |
| ffprobe duration slide_007.wav | 0.088 | 0 |
| render segment 007 | 10.915 | 0 |
| ffprobe duration slide_008.wav | 0.088 | 0 |
| render segment 008 | 10.645 | 0 |
| concat segments | 0.291 | 0 |
| apply faststart | 0.14 | 0 |
| decode check | 6.092 | 0 |
| ffprobe final video | 0.099 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
