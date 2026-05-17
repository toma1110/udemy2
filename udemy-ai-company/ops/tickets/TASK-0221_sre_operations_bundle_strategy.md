# Task Summary

Task ID: `TASK-0221`
Title: SRE運用入門バンドルを設計し、Alert Design・Runbook・SLO講座へ接続する
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
- `udemy-ai-company/courses/aws-alert-design-practical-course/course_spec.md`
- `udemy-ai-company/courses/aws-runbook-first-response-course/course_spec.md`
- `udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

Dependencies:
- `TASK-0217` Alert Design video completion
- `TASK-0218` Runbook First Response video completion
- SLO course QA remains acceptable for bundle inclusion

## Deliverables

Expected Output:
- `BUNDLE-002 SRE運用入門バンドル` の受講順、対象者、到達点
- 3講座の重複範囲と固有成果物の定義
- 各講座の `course_spec.md` / `course_curriculum.md` / `course_infomation.md` へのbundle role反映
- バンドル販売文言ドラフト
- 長尺旗艦コースで深掘りするSRE運用演習メモ

## Quality Gate

Definition of Done:
- Alert Designはアラート判断基準に集中している
- Runbookは初動対応手順に集中している
- SLOは信頼性指標、エラーバジェット、レビュー運用に集中している
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
- `TASK-0217` and `TASK-0218` course video completion

Notes:
- `aws-slo-adoption-course` is already long enough by current inventory, but still needs bundle-level positioning review.
