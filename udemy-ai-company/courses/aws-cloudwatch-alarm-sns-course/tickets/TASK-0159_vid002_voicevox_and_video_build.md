# Task Summary

Task ID: `TASK-0159`
Title: VID-002追加レクチャーVOICEVOX音声と動画生成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `scripts/*_script.json`
- `slides/<lecture>/slide_*.png`

Dependencies:
- `TASK-0158`

## Deliverables

Expected Output:
- VOICEVOX WAV
- Voice generation reports
- MP4 videos
- Video build reports

## Quality Gate

Definition of Done:
- 音声ファイル数とスライド数が一致する
- MP4が再生可能
- Faststartが付与されている
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- None

Notes:
- ffmpegには `-nostdin` 経路の既存ビルドツールを使う。
- 追加5レクチャーのVOICEVOX音声とMP4生成が完了。
- 全MP4でslides/audios数一致、faststart true、decode validation pass。
