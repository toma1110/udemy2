# Task Summary

Task ID: `TASK-0223`
Title: AWS学習安全・トラブルシュートバンドルを設計し、Cost Safety・CloudFormation Rollback・IAM AccessDenied講座へ接続する
GitHub Issue: TBD

## Ownership

Department: strategy / production
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

## Execution

Priority: medium
Status: Ready
Auto Execute: planning and documentation only
Requires CEO Approval: yes, before publishing bundle or changing Udemy course configuration
Cost Impact: none

## Inputs

Input Files:
- `udemy-ai-company/docs/BUNDLE_STRATEGY.md`
- `udemy-ai-company/courses/aws-cost-safety-course/course_spec.md`
- `udemy-ai-company/courses/aws-cloudformation-rollback-troubleshooting-course/course_spec.md`
- `udemy-ai-company/courses/aws-iam-accessdenied-troubleshooting-course/course_spec.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

Dependencies:
- `TASK-0219` Cost Safety video completion
- `TASK-0207` CloudFormation Rollback full course video generation
- `TASK-0208` IAM AccessDenied full course video generation

## Deliverables

Expected Output:
- `BUNDLE-004 AWS学習安全・トラブルシュートバンドル` の受講順、対象者、到達点
- 3講座の重複範囲と固有成果物の定義
- 課金安全、CloudFormation失敗、IAM権限エラーの切り分け順を整理
- バンドル販売文言ドラフト
- 長尺旗艦コースで深掘りする安全運用演習メモ

## Quality Gate

Definition of Done:
- Cost Safetyは課金事故予防と削除チェックに集中している
- CloudFormation RollbackはStack Eventsとsafe retryに集中している
- IAM AccessDeniedは権限エラー読解と最小権限変更フローに集中している
- 各単品講座は5レクチャー以上、講義本編30分以上で成立する
- 同じMP4の大量使い回しを前提にしていない
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- No Udemy publishing mutation in this ticket
- No Google Drive mutation in this ticket
- No AWS execution in this ticket

## Blocking

Blocked By:
- `TASK-0219`, `TASK-0207`, and `TASK-0208` video completion

Notes:
- This bundle is positioned as the safety layer before AWS hands-on heavy courses.
