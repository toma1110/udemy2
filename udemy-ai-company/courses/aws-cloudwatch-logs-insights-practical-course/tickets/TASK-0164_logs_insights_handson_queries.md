# Task Summary

Task ID: `TASK-0164`
Title: Logs Insightsハンズオンとクエリ集作成

## Ownership

Department: Engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `course_spec.md`
- `qa/aws_source_verification_report.md`

Dependencies:
- `TASK-0163`

## Deliverables

Expected Output:
- `handson/README.md`
- `handson/queries/*.sql`
- `handson/sample_logs/*`

## Quality Gate

Definition of Done:
- 標準手順でAWSリソース作成が不要
- 既存ロググループで任意実行できる
- クエリ料金注意がある
- クエリが公式構文に沿う
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- AWS resource creation requires CEO approval

## Blocking

Blocked By:
- None

Notes:
- サンプルログは読解用。CloudWatch Logsへ投入する標準手順は含めない。
