# S1-L1 VOICEVOX Generation Report

## Target

- Course: `aws-cloudwatch-alarm-sns-course`
- Lecture: `s1-l1`
- Date: 2026-05-14

## Ownership

- Worker AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: PASS

## Inputs

- Structured script: `scripts/s1-l1_script.json`
- Audio output directory: `audio/s1-l1/`
- Generator: `tools/generate_voicevox_audio_local.py`

## Result

- Status: PASS
- Speaker ID: 3
- Speed scale: 1.1
- Audio count: 11
- Total duration seconds: 187.381
- gTTS fallback: not used
- Report: `audio/s1-l1/voicevox_report.md`

## Quality Checks

| Check | Result | Notes |
| --- | --- | --- |
| Slide count and audio count match | PASS | 11 slides, 11 WAV files. |
| Narration checker | PASS | `tools/narration_checker.py` passed after reading fixes. |
| VOICEVOX engine used | PASS | Local VOICEVOX output was generated. |
| Missing audio files | PASS | No missing slide audio files. |

## Result

Status: PASS
