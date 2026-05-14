# S3-L1 Video Build Report

## Target

- Lecture: Section 3 Lecture 1「良いSLIの3条件」
- Video: `video/s3-l1/s3-l1.mp4`

## Result

Pass.

## Output

- Size: 5,920,621 bytes
- Duration: 167.59 seconds
- Video: H.264, 1920x1080 static-slide encode
- Audio: AAC, mono, 44100 Hz
- Faststart: true
- Decode check: OK
- Frame check: `video/s3-l1/frame_check_90s.png`
- Build metadata: `video/s3-l1/build_report.json`

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
