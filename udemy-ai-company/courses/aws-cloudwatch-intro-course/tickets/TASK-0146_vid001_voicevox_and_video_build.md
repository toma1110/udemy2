# Task Summary

Task ID: `TASK-0146`
Title: `VID-001追加レクチャーのVOICEVOX音声とMP4動画を生成する`

## Ownership

Department: Production
Owner AI: `AI-Production-01`
Reviewer AI: `AI-QA-01`

## Execution

Priority: high
Status: done

## Inputs

Input Files:

- `scripts/*_script.json`
- `slides/<lecture>/slide_*.png`
- `udemy-ai-company/tools/generate_voicevox_audio_local.py`
- `udemy-ai-company/tools/build_slide_audio_video.py`

Dependencies:

- `TASK-0145`

## Deliverables

Expected Output:

- VOICEVOX WAV files under `audio/<lecture>/`
- MP4 files under `video/<lecture>/`
- audio/video build reports

## Quality Gate

Definition of Done:

- Slide count equals audio count
- MP4 validates with ffmpeg decode
- Build report states GPT-Image2-derived slides were used
- Worker and reviewer are separated

## Constraints

Rules:

- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
Notes:
