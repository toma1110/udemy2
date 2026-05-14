# S1-L1 VOICEVOX Generation Report

## Target

- Course: `aws-cloudwatch-intro-course`
- Lecture: `s1-l1`
- Script JSON: `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- Audio directory: `courses/aws-cloudwatch-intro-course/audio/s1-l1/`

## Ownership

- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## Result

- Status: PASS
- Engine: local VOICEVOX Engine
- Speaker ID: 3
- Speed scale: 1.1
- Audio count: 10
- Total duration seconds: 174.859
- gTTS fallback: not used

## Files

| Slide | File | Duration sec |
| ---: | --- | ---: |
| 1 | `slide_001.wav` | 17.376 |
| 2 | `slide_002.wav` | 17.003 |
| 3 | `slide_003.wav` | 15.851 |
| 4 | `slide_004.wav` | 18.432 |
| 5 | `slide_005.wav` | 16.107 |
| 6 | `slide_006.wav` | 17.920 |
| 7 | `slide_007.wav` | 16.107 |
| 8 | `slide_008.wav` | 16.256 |
| 9 | `slide_009.wav` | 20.469 |
| 10 | `slide_010.wav` | 19.339 |

## Verification

```bash
python3 udemy-ai-company/tools/generate_voicevox_audio_local.py \
  udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json \
  udemy-ai-company/courses/aws-cloudwatch-intro-course/audio/s1-l1 \
  --course-id aws-cloudwatch-intro-course \
  --lecture-id s1-l1 \
  --skip-existing
```

Generated reports:

- `audio/s1-l1/voicevox_report.json`
- `audio/s1-l1/voicevox_report.md`

## Notes

- Initial generation produced slides 1-9 before the process exited during slide 10.
- `--skip-existing` was added to the local VOICEVOX script and the 10th WAV was generated without replacing valid existing files.
- All WAV files open successfully and report valid durations.

## Approval

Status: Ready for audio review and video build

Approved By: AI-QA-01

