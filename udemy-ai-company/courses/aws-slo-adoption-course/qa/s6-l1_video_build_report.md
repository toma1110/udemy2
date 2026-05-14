# Render Report: aws-slo-adoption-course s6-l1

## Result

- Status: pass
- Started at: 2026-05-12T01:56:49Z
- Ended at: 2026-05-12T01:58:19Z
- Elapsed seconds: 90.894
- Slide count: 8
- Audio count: 8
- Output duration seconds: 143.03
- Output size bytes: 5199466

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.089 | 0 |
| render segment 001 | 10.977 | 0 |
| ffprobe duration slide_002.wav | 0.087 | 0 |
| render segment 002 | 9.246 | 0 |
| ffprobe duration slide_003.wav | 0.087 | 0 |
| render segment 003 | 10.956 | 0 |
| ffprobe duration slide_004.wav | 0.087 | 0 |
| render segment 004 | 10.387 | 0 |
| ffprobe duration slide_005.wav | 0.087 | 0 |
| render segment 005 | 9.474 | 0 |
| ffprobe duration slide_006.wav | 0.087 | 0 |
| render segment 006 | 9.866 | 0 |
| ffprobe duration slide_007.wav | 0.088 | 0 |
| render segment 007 | 10.058 | 0 |
| ffprobe duration slide_008.wav | 0.088 | 0 |
| render segment 008 | 10.331 | 0 |
| concat segments | 0.287 | 0 |
| apply faststart | 0.141 | 0 |
| decode check | 6.289 | 0 |
| ffprobe final video | 0.098 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
