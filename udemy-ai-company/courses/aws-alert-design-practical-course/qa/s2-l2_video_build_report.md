# S2-L2 Video Build Report

## Target

- Course: `aws-alert-design-practical-course`
- Lecture: `s2-l2`
- Script: `scripts/s2-l2_owner_runbook_escalation_script.md`
- Slides: `slides/s2-l2/slide_*.png`
- Audio: `audio/s2-l2/slide_*.wav`
- Output: `video/s2-l2/s2-l2.mp4`

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
| Duration | 328.736s |
| Size | 11930140 bytes |
| Decode check | OK |
| Faststart | true |
| Representative frame check | OK, `video/s2-l2/frame_check_*.png` |

## QA Notes

Worker/Reviewer separation remains required. AI-Production-01 completed generation and mechanical checks; AI-QA-01 or CEO should perform final content approval.
