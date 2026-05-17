# S1-L2 Video Build Report

## Target

- Course: `aws-runbook-first-response-course`
- Lecture: `s1-l2`
- Script: `scripts/s1-l2_playbook_vs_runbook_script.md`
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
| Slide PNG | 8 |
| Audio WAV | 8 |
| Segments | 8 |

## Output Validation

| Check | Result |
| --- | --- |
| MP4 generated | OK |
| Duration | 315.188s |
| Size | 12236141 bytes |
| Decode check | OK |
| Faststart | true |
| Representative frame check | OK, `video/s1-l2/frame_check_*.png` |

## QA Notes

Worker/Reviewer separation remains required. AI-Production-01 completed generation and mechanical checks; AI-QA-01 or CEO should perform final content approval.
