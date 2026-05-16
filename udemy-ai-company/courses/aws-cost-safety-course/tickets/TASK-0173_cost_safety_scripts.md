# Task Summary

Task ID: `TASK-0173`
Title: AWS課金事故防止入門 台本作成

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
- `handson/README.md`
- `qa/aws_source_verification_report.md`

Dependencies:
- `TASK-0170`
- `TASK-0171`

## Deliverables

Expected Output:
- `scripts/s*_script.md`
- `scripts/s*_script.json`
- ナレーション読み方チェック結果

## Quality Gate

Definition of Done:
- 全12レクチャーの台本が存在する
- 料金や無料枠を断定しない
- AWS公式情報と矛盾しない
- VOICEVOX読み上げルールに従う
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- GPT-Image2前提でスライド内容を設計する

## Blocking

Blocked By:
- TASK-0170
- TASK-0171
