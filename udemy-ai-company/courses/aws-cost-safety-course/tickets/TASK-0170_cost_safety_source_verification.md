# Task Summary

Task ID: `TASK-0170`
Title: AWS課金事故防止入門 AWS公式ソース確認

## Ownership

Department: QA
Owner AI: AI-QA-01
Reviewer AI: AI-Strategy-01

## Execution

Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- AWS Budgets official docs
- Cost Explorer official docs
- Cost Anomaly Detection official docs
- CloudFormation Template Reference

Dependencies:
- `TASK-0169`

## Deliverables

Expected Output:
- `qa/aws_source_verification_report.md` の正式版
- 公開前に再確認が必要な料金、無料枠、UI、API注意点の一覧

## Quality Gate

Definition of Done:
- 料金、無料枠、反映遅延、API課金の表現が公式情報に基づく
- 古いUIや断定的な節約額表現がない
- CloudFormation対象リソースが公式リファレンスと一致している
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- AWS/billing-related execution requires CEO approval
- 数値計算はスクリプトまたは表計算で確認する

## Blocking

Blocked By:
- None
