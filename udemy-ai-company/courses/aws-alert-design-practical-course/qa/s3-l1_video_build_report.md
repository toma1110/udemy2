# S3-L1 Video Build Report

## Target

- Course: `aws-alert-design-practical-course`
- Lecture: `s3-l1`
- Script: `scripts/s3-l1_cloudwatch_alarm_evaluation_script.md`
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
| Slide PNG | 7 |
| Audio WAV | 7 |
| Segments | 7 |

## Output Validation

| Check | Result |
| --- | --- |
| MP4 generated | OK |
| Duration | 305.856s |
| Size | 11450998 bytes |
| Decode check | OK |
| Faststart | true |
| Representative frame check | OK, `video/s3-l1/frame_check_*.png` |

## QA Notes

Worker/Reviewer separation remains required. AI-Production-01 completed generation and mechanical checks; AI-QA-01 or CEO should perform final content approval.
