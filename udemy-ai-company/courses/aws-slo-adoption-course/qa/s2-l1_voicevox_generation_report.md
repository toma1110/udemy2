# S2-L1 VOICEVOX音声生成レポート

## Ticket

- Task ID: TASK-0027
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- 実施日: 2026-05-10

## Generation Settings

- Engine: VOICEVOX
- Engine version: `0.25.1`
- Speaker ID: `3`
- Speed scale: `1.1`
- gTTS fallback: 未使用

## Pre-check

```text
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l1_script.md --warnings-ok
OK: 1 files checked
```

## Generated Files

| Slide | Duration |
| --- | ---: |
| 1 | 19.733 sec |
| 2 | 19.637 sec |
| 3 | 22.592 sec |
| 4 | 22.016 sec |
| 5 | 21.792 sec |
| 6 | 24.523 sec |
| 7 | 22.293 sec |
| 8 | 22.677 sec |
| 9 | 19.872 sec |

Total duration: 195.136 sec

## Validation

- WAV count: 9
- Script slide count: 9
- WAV decode: pass
- Format: PCM 16-bit mono 24000 Hz
- Git tracking: generated WAV files are ignored by `.gitignore`
