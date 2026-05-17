# Task Summary

Task ID: `TASK-0222`
Title: 発展監視・APMバンドルを設計し、Application Signals・SLI/SLO Metrics・Lambda Error Rate講座へ接続する
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
- `udemy-ai-company/courses/aws-cloudwatch-application-signals-practical-course/course_spec.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/course_spec.md`
- `udemy-ai-company/courses/aws-lambda-error-rate-monitoring-course/course_spec.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

Dependencies:
- `TASK-0216` Application Signals runtime remediation
- `TASK-0209` Lambda Error Rate full course video generation
- `TASK-0211` SLI/SLO Metrics Intro full course video generation

## Deliverables

Expected Output:
- `BUNDLE-003 発展監視・APMバンドル` の受講順、対象者、到達点
- 3講座の重複範囲と固有成果物の定義
- Application Signalsのハンズオン範囲と、SLI/SLO Metrics/Lambda講座の概念範囲の分離
- バンドル販売文言ドラフト
- 長尺旗艦コースで深掘りするAPM/SLI演習メモ

## Quality Gate

Definition of Done:
- SLI/SLO Metricsはメトリクス候補への入口に集中している
- Lambda Error RateはLambdaのエラー率設計に集中している
- Application Signalsは実アプリ観測、Service Map、SLO画面読解に集中している
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
- `TASK-0216`, `TASK-0209`, and `TASK-0211` video completion

Notes:
- Application Signals is the practical anchor. SLI/SLO Metrics and Lambda Error Rate should remain smaller, sharper modules.
