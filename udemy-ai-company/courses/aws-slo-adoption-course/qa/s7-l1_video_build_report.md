# Render Report: aws-slo-adoption-course s7-l1

## Result

- Status: pass
- Started at: 2026-05-12T12:38:09Z
- Ended at: 2026-05-12T12:39:41Z
- Elapsed seconds: 92.17
- Slide count: 8
- Audio count: 8
- Output duration seconds: 142.134
- Output size bytes: 5498098

## Stages

| Stage | Elapsed sec | Exit code |
| --- | ---: | ---: |
| ffprobe duration slide_001.wav | 0.087 | 0 |
| render segment 001 | 10.316 | 0 |
| ffprobe duration slide_002.wav | 0.085 | 0 |
| render segment 002 | 10.388 | 0 |
| ffprobe duration slide_003.wav | 0.085 | 0 |
| render segment 003 | 10.935 | 0 |
| ffprobe duration slide_004.wav | 0.086 | 0 |
| render segment 004 | 9.451 | 0 |
| ffprobe duration slide_005.wav | 0.085 | 0 |
| render segment 005 | 10.784 | 0 |
| ffprobe duration slide_006.wav | 0.086 | 0 |
| render segment 006 | 10.682 | 0 |
| ffprobe duration slide_007.wav | 0.085 | 0 |
| render segment 007 | 10.38 | 0 |
| ffprobe duration slide_008.wav | 0.084 | 0 |
| render segment 008 | 9.762 | 0 |
| concat segments | 0.299 | 0 |
| apply faststart | 0.142 | 0 |
| decode check | 5.814 | 0 |
| ffprobe final video | 0.097 | 0 |

## Review

- Worker: AWS Batch Fargate render worker
- Reviewer: AI-QA-01
- ffmpeg -nostdin: yes
- Decode check: yes
