# S3-L2 Video Build Report

## Target

- Lecture: Section 3 Lecture 2「可用性、レイテンシ、エラー率を設計する」
- Video: `video/s3-l2/s3-l2.mp4`

## Result

Pass.

## Output

- Size: 6,066,670 bytes
- Duration: 166.34 seconds
- Video: H.264, 1920x1080 static-slide encode
- Audio: AAC, mono, 44100 Hz
- Faststart: true
- Decode check: OK
- Frame check: `video/s3-l2/frame_check_90s.png`
- Build metadata: `video/s3-l2/build_report.json`

## Notes

- Built from 8 GPT-Image2 PNG slides and 8 existing approved VOICEVOX WAV files.
- Encoding used 1fps static-slide input to avoid long ffmpeg process termination while preserving slide-video behavior.
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## Revision 2026-05-11

- Trigger: Issue #84 GPT-Image2 regeneration request.
- Rebuilt video from GPT-Image2 regenerated slides. Existing approved VOICEVOX audio was reused.
- Faststart: true
- Decode check: OK
