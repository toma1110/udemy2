# Task Summary

Task ID: `TASK-0165`
Title: Logs Insights実践コース台本作成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `handson/README.md`
- `handson/queries/*.sql`

Dependencies:
- `TASK-0164`

## Deliverables

Expected Output:
- `scripts/s1-l1_script.md`
- `scripts/s1-l1_script.json`
- `scripts/s1-l2_script.md`
- `scripts/s1-l2_script.json`
- `scripts/s1-l3_script.md`
- `scripts/s1-l3_script.json`
- `scripts/s2-l1_script.md`
- `scripts/s2-l1_script.json`
- `scripts/s2-l2_script.md`
- `scripts/s2-l2_script.json`
- `scripts/s2-l3_script.md`
- `scripts/s2-l3_script.json`
- `scripts/s3-l1_script.md`
- `scripts/s3-l1_script.json`
- `scripts/s3-l2_script.md`
- `scripts/s3-l2_script.json`

## Quality Gate

Definition of Done:
- 台本がVOICEVOXで読みやすい日本語になっている
- クエリとハンズオンREADMEに矛盾しない
- AWSリソース作成を標準手順にしない
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- ローカル文字合成禁止

## Blocking

Blocked By:
- None

Notes:
- 2026-05-15: 8レクチャー、各6スライド構成で台本MarkdownとJSONを作成済み。
