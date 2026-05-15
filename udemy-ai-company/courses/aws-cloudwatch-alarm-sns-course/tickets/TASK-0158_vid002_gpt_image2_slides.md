# Task Summary

Task ID: `TASK-0158`
Title: VID-002追加レクチャーGPT-Image2スライド生成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `slides/*_gpt_image_prompts.md`
- `scripts/*_script.json`

Dependencies:
- `TASK-0157`

## Deliverables

Expected Output:
- GPT-Image2 source PNG
- 1920x1080 fitted PNG
- Contact sheets
- Slide generation report

## Quality Gate

Definition of Done:
- 表示文字はGPT-Image2生成
- ローカル文字合成なし
- Contact sheetで全スライドを確認できる
- VID-001基準を下回らない

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- None

Notes:
- Source PNGは `slides/s*-gpt-image2-sources/<lecture>/` に置く。
- 追加5レクチャー、合計38枚のGPT-Image2 source PNGを生成済み。
- すべて1920x1080へフィットし、contact sheetを作成済み。
