# Task Summary

Task ID: `TASK-0172`
Title: AWS課金事故防止 optional CloudFormationテンプレート検討

## Ownership

Department: Engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

## Execution

Priority: medium
Status: Backlog
Auto Execute: no
Requires CEO Approval: yes
Cost Impact: possible

## Inputs

Input Files:
- `course_spec.md`
- `cloudformation/README.md`
- `qa/aws_source_verification_report.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/06-cost-alerts.yaml`

Dependencies:
- `TASK-0170`
- `TASK-0171`

## Deliverables

Expected Output:
- optional CloudFormationテンプレート案
- validate手順
- stack create/update/delete手順
- smoke test案
- CEO承認前に実行しない操作一覧

## Quality Gate

Definition of Done:
- CloudFormationは教材ハンズオン用途に限定されている
- 実運用IaCはCDKまたはTerraform推奨である
- `AWS::Budgets::Budget`、`AWS::CE::AnomalyMonitor`、`AWS::CE::AnomalySubscription` の仕様と整合している
- Budget Actionsなど危険な自動制御を標準テンプレートに含めない
- AWS stack操作はCEO承認後にだけ実行する
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- AWS/billing-related execution requires CEO approval
- 課金影響があるAWS作業は実行しない

## Blocking

Blocked By:
- TASK-0170
- CEO approval for any AWS execution
