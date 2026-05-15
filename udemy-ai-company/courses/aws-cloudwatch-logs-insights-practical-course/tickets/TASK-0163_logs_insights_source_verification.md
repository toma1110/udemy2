# Task Summary

Task ID: `TASK-0163`
Title: Logs Insights AWS公式仕様確認

## Ownership

Department: Strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- AWS CloudWatch Logs Insights official documentation

Dependencies:
- `TASK-0162`

## Deliverables

Expected Output:
- `qa/aws_source_verification_report.md`

## Quality Gate

Definition of Done:
- 基本構文が公式ドキュメントに基づく
- JOIN/subquery/SOURCE/pattern/anomalyの扱いが公式情報に基づく
- コスト注意が公式情報に基づく
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
- AWS docs MCPとaws-observability skillを使用。
