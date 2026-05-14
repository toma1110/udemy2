# S1-L1 Video Build Report

## Target

- Course: `aws-cloudwatch-alarm-sns-course`
- Lecture: `s1-l1`
- Video ID: `VID-002`
- Date: 2026-05-14

## Ownership

- Worker AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: PASS

## Inputs

- Slides: `slides/s1-l1/slide_001.png` through `slide_011.png`
- Audio: `audio/s1-l1/slide_001.wav` through `slide_011.wav`
- Build script: `tools/build_slide_audio_video.py`

## Build Output

- Video: `video/s1-l1/s1-l1.mp4`
- Build report: `video/s1-l1/build_report.json`
- Frame check: `video/s1-l1/frame_check_90s.png`

## Build Properties

| Property | Value |
| --- | ---: |
| Slides | 11 |
| Audio files | 11 |
| Duration seconds | 187.252245 |
| Size bytes | 10513350 |
| FPS | 1 |
| Faststart | true |
| Dynamic video | false |

## Pronunciation Fix

- `初学者` は `しょがくしゃ` に変更
- Existing GPT-Image2 slide PNG files were reused without regeneration.

## Decode Checks

| Check | Result | Notes |
| --- | --- | --- |
| MP4 exists | PASS | `s1-l1.mp4` exists and is non-zero. |
| ffprobe stream check | PASS | H.264 1920x1080 video and AAC audio detected. |
| Faststart | PASS | `build_report.json` reports `faststart: true`. |
| Frame extraction | PASS | `frame_check_90s.png` generated and reviewed. |
| GPT-Image2 slide source | PASS | Final video uses GPT-Image2-derived slides. |

## Result

Status: PASS
