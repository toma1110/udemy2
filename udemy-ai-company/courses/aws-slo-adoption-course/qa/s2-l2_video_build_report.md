# S2-L2 動画生成レポート

## Ticket

- Task ID: TASK-0035
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- 実施日: 2026-05-10

## Output

- Final video: `udemy-ai-company/courses/aws-slo-adoption-course/video/s2-l2/s2-l2.mp4`
- Segments: `video/s2-l2/segments/segment_001.mp4` ... `segment_009.mp4`
- Representative frame: `video/s2-l2/frame_check_90s.png`

## Validation

| Check | Result | Notes |
| --- | --- | --- |
| Slide count | Pass | 9 PNG files |
| Audio count | Pass | 9 WAV files |
| Segment count | Pass | 9 MP4 files |
| Segment audio spec | Pass | all AAC mono 44100 Hz |
| Final video stream | Pass | H.264 1920x1080, 30 fps |
| Final audio stream | Pass | AAC mono 44100 Hz |
| Duration | Pass | 188.789 sec |
| File size | Pass | 18,771,215 bytes |
| Decode | Pass | ffmpeg decode check success |
| Faststart | Pass | `moov` at byte 36, before `mdat` at byte 161517 |
| Representative frame | Pass | non-empty 1920x1080 PNG |

## Notes

- 途中で破損した `segment_007.mp4` は上書き再生成し、decode checkで確認済み。
- 音声の最終自然さ確認は `s2-l2_audio_review_report.md` のCEOスポット聴取ポイントを使う。
