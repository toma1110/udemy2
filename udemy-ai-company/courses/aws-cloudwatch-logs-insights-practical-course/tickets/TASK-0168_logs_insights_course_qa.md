# Task Summary

Task ID: `TASK-0168`
Title: Logs Insights実践コースQA

## Ownership

Department: QA
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

## Execution

Priority: high
Status: Planned

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `handson/README.md`
- `scripts/*_script.json`
- `qa/*`

Dependencies:
- `TASK-0167`

## Deliverables

Expected Output:
- Course QA report
- Drive URL summary

## Quality Gate

Definition of Done:
- AWS公式仕様と矛盾しない
- クエリ料金注意が明確
- 標準ハンズオンでAWSリソース作成なし
- GPT-Image2/VOICEVOXポリシーを満たす
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- `TASK-0167`

Notes:
- 人間の最終視聴レビューはUdemy公開前に実施する。
