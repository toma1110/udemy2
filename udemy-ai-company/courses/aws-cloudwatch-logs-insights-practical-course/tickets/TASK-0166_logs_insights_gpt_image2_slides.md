# Task Summary

Task ID: `TASK-0166`
Title: Logs Insights実践コースGPT-Image2スライド生成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Planned

## Inputs

Input Files:
- `scripts/*_script.json`
- `slides/*_gpt_image_prompts.md`

Dependencies:
- `TASK-0165`

## Deliverables

Expected Output:
- GPT-Image2 source PNG
- 1920x1080 final PNG
- Contact sheets
- Slide generation reports

## Quality Gate

Definition of Done:
- 表示文字はGPT-Image2生成
- ローカル文字合成なし
- Contact sheetで確認できる
- VID-001/VID-002品質を下回らない

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- `TASK-0165`

Notes:
- 完成動画にローカル描画スライドを使わない。
