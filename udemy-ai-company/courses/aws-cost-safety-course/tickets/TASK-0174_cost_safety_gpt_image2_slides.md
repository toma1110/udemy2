# Task Summary

Task ID: `TASK-0174`
Title: AWS課金事故防止入門 GPT-Image2スライド作成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `scripts/`
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`
- `udemy-ai-company/docs/VIDEO_QUALITY_BASELINE.md`

Dependencies:
- `TASK-0173`

## Deliverables

Expected Output:
- GPT-Image2 prompts
- GPT-Image2 source PNG
- final slide PNG
- contact sheets
- slide generation QA report

## Quality Gate

Definition of Done:
- 完成動画スライドはGPT-Image2由来PNGのみ
- 表示文字もGPT-Image2で生成されている
- 料金や無料枠の断定表示がない
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- ローカル文字合成スライドを完成動画に使わない

## Blocking

Blocked By:
- TASK-0173
