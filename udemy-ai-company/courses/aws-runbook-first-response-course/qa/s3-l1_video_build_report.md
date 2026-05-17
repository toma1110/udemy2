# S3-L1 Video Build Report

## Target

- Course: `aws-runbook-first-response-course`
- Lecture: `s3-l1`
- Script: `scripts/s3-l1_mitigation_rollback_escalation_script.md`
- Slides: `slides/s3-l1/slide_*.png`
- Audio: `audio/s3-l1/slide_*.wav`
- Output: `video/s3-l1/s3-l1.mp4`

## Build Method

The lecture was built from matching GPT-Image2-derived slide PNGs and VOICEVOX WAV files.

- Video: H.264, 1920x1080, 1fps static slide video
- Audio: AAC, stereo, 44100 Hz
- Dynamic subtle zoom: disabled
- `-nostdin` used for ffmpeg
- `-movflags +faststart` applied

## Inputs

| Type | Count |
| --- | ---: |
| Slide PNG | 9 |
| Audio WAV | 9 |
| Segments | 9 |

## Output Validation

| Check | Result |
| --- | --- |
| MP4 generated | OK |
| Duration | 357.439s |
| Size | 14121244 bytes |
| Decode check | OK |
| Faststart | true |
| Representative frame check | OK, `video/s3-l1/frame_check_*.png` |

## QA Notes

Worker/Reviewer separation remains required. AI-Production-01 completed generation and mechanical checks; AI-QA-01 or CEO should perform final content approval.
