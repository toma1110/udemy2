# S3-L3 Video Build Report

## Target

- Lecture: Section 3 Lecture 3「p95/p99を使う理由」
- Video: `video/s3-l3/s3-l3.mp4`

## Result

Pass.

## Output

- Size: 6,169,889 bytes
- Duration: 167.03 seconds
- Video: H.264, 1920x1080 static-slide encode
- Audio: AAC, mono, 44100 Hz
- Faststart: true
- Decode check: OK
- Frame check: `video/s3-l3/frame_check_90s.png`
- Build metadata: `video/s3-l3/build_report.json`

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
