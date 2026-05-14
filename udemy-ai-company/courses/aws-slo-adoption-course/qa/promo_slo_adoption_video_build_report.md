# Promo SLO Adoption Video Build Report

## Target

- Course: `aws-slo-adoption-course`
- Asset: `promo_slo_adoption`
- Date: 2026-05-14

## Ownership

- Worker AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: PASS

## Inputs

- Slides: `slides/promo_slo_adoption/slide_001.png` through `slide_007.png`
- Audio: `audio/promo_slo_adoption/slide_001.wav` through `slide_007.wav`
- Script JSON: `scripts/promo_video_script.json`

## VOICEVOX Output

- Report: `audio/promo_slo_adoption/voicevox_report.md`
- Audio count: 7
- Total audio duration seconds: 91.339
- Speaker ID: 3
- Speed scale: 1.1
- gTTS fallback: not used

## Build Output

- Stable MP4: `video/promo_slo_adoption/promo_slo_adoption.mp4`
- Final review MP4: `video/promo_slo_adoption/promo_slo_adoption.30fps.mp4`
- Build report: `video/promo_slo_adoption/build_report.json`
- 30fps report: `video/promo_slo_adoption/build_report_30fps.json`
- Frame check: `video/promo_slo_adoption/frame_check_43s.png`

## Final MP4 Properties

| Property | Value |
| --- | ---: |
| Duration seconds | 91.359206 |
| Size bytes | 5469449 |
| Resolution | 1920x1080 |
| Frame rate | 30 fps |
| Video codec | H.264 |
| Audio codec | AAC |
| Faststart | true |

## Notes

- Dynamic 6fps encoding was attempted first but the local session stopped during segment encoding.
- A stable 1fps slide-video build was completed, then re-encoded to 30fps for review/upload compatibility.
- Decode validation passed for the final 30fps MP4.

## Result

Status: PASS
