# Render Report: aws-slo-adoption-course s6-l2

## Result

- Status: pass
- Started at: 2026-05-12T01:56:10Z
- Ended at: 2026-05-12T01:57:38Z
- Elapsed seconds: 87.473
- Slide count: 8
- Audio count: 8
- Output duration seconds: 136.321
- Output size bytes: 4806023

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.089 | 0 |
| render segment 001 | 9.518 | 0 |
| ffprobe duration slide_002.wav | 0.088 | 0 |
| render segment 002 | 10.069 | 0 |
| ffprobe duration slide_003.wav | 0.086 | 0 |
| render segment 003 | 9.138 | 0 |
| ffprobe duration slide_004.wav | 0.087 | 0 |
| render segment 004 | 10.078 | 0 |
| ffprobe duration slide_005.wav | 0.088 | 0 |
| render segment 005 | 9.171 | 0 |
| ffprobe duration slide_006.wav | 0.086 | 0 |
| render segment 006 | 10.628 | 0 |
| ffprobe duration slide_007.wav | 0.087 | 0 |
| render segment 007 | 9.108 | 0 |
| ffprobe duration slide_008.wav | 0.088 | 0 |
| render segment 008 | 10.273 | 0 |
| concat segments | 0.269 | 0 |
| apply faststart | 0.143 | 0 |
| decode check | 6.206 | 0 |
| ffprobe final video | 0.098 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
