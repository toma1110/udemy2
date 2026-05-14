# Render Report: aws-slo-adoption-course s7-l3

## Result

- Status: pass
- Started at: 2026-05-12T12:38:05Z
- Ended at: 2026-05-12T12:39:03Z
- Elapsed seconds: 57.872
- Slide count: 8
- Audio count: 8
- Output duration seconds: 135.671
- Output size bytes: 5257427

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.055 | 0 |
| render segment 001 | 6.694 | 0 |
| ffprobe duration slide_002.wav | 0.054 | 0 |
| render segment 002 | 6.963 | 0 |
| ffprobe duration slide_003.wav | 0.054 | 0 |
| render segment 003 | 5.726 | 0 |
| ffprobe duration slide_004.wav | 0.054 | 0 |
| render segment 004 | 5.661 | 0 |
| ffprobe duration slide_005.wav | 0.054 | 0 |
| render segment 005 | 7.005 | 0 |
| ffprobe duration slide_006.wav | 0.054 | 0 |
| render segment 006 | 6.575 | 0 |
| ffprobe duration slide_007.wav | 0.054 | 0 |
| render segment 007 | 6.487 | 0 |
| ffprobe duration slide_008.wav | 0.055 | 0 |
| render segment 008 | 6.678 | 0 |
| concat segments | 0.212 | 0 |
| apply faststart | 0.105 | 0 |
| decode check | 2.969 | 0 |
| ffprobe final video | 0.065 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
