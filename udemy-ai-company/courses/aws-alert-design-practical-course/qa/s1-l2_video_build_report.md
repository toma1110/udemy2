# S1-L2 Video Build Report

## Target

- Course: `aws-alert-design-practical-course`
- Lecture: `s1-l2`
- Script: `scripts/s1-l2_bad_to_good_alerts_script.md`
- Slides: `slides/s1-l2/slide_*.png`
- Audio: `audio/s1-l2/slide_*.wav`
- Output: `video/s1-l2/s1-l2.mp4`

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
| Duration | 353.408s |
| Size | 12820648 bytes |
| Decode check | OK |
| Faststart | true |
| Representative frame check | OK, `video/s1-l2/frame_check_*.png` |

## QA Notes

Worker/Reviewer separation remains required. AI-Production-01 completed generation and mechanical checks; AI-QA-01 or CEO should perform final content approval.
