# Task Summary

Task ID: `TASK-0220`
Title: CloudWatch監視入門バンドルを直近目標として定義し、既存是正チケットへ接続する
GitHub Issue: TBD

## Ownership

Department: strategy / production
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Ready
Auto Execute: planning and documentation only
Requires CEO Approval: yes, before publishing bundle or changing Udemy course configuration
Cost Impact: none

## Inputs

Input Files:
- `udemy-ai-company/docs/BUNDLE_STRATEGY.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`
- `udemy-ai-company/courses/aws-cloudwatch-intro-course/course_spec.md`
- `udemy-ai-company/courses/aws-cloudwatch-logs-insights-practical-course/course_spec.md`
- `udemy-ai-company/courses/aws-cloudwatch-alarm-sns-course/course_spec.md`
- `udemy-ai-company/courses/*/course_infomation.md`
- Udemy Course Bundles instructor help

Dependencies:
- `TASK-0213` Logs Insights runtime remediation
- `TASK-0214` CloudWatch intro runtime remediation
- `TASK-0215` Alarm/SNS runtime remediation

## Deliverables

Expected Output:
- `BUNDLE-001 CloudWatch監視入門バンドル` の構成確定
- 各講座の `course_spec.md` / `course_curriculum.md` / `course_infomation.md` にバンドル内の役割を反映
- 各講座の重複範囲と固有成果物を明記
- バンドル販売ページで使うタイトル、説明、受講順、対象者のドラフト
- 将来の長尺旗艦コースへ統合する深掘り範囲のメモ

## Quality Gate

Definition of Done:
- `BUNDLE-001` は2〜3講座のUdemy Course Bundleとして説明できる
- 各単品講座は5レクチャー以上、講義本編30分以上で成立する計画になっている
- `aws-cloudwatch-intro-course` はCloudWatch全体像に集中している
- `aws-cloudwatch-logs-insights-practical-course` は障害調査クエリ集に集中している
- `aws-cloudwatch-alarm-sns-course` はAlarm/SNS通知設計に集中している
- 同じMP4の大量使い回しを前提にしていない
- 将来の長尺旗艦コースは単品講座の連結ではなく、統合演習と深掘りを追加する方針になっている
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- No Udemy publishing mutation in this ticket
- No Google Drive mutation in this ticket
- No AWS execution in this ticket
- Video generation remains gated by each course remediation ticket and CEO approval

## Blocking

Blocked By:
- CEO confirmation of bundle strategy

Notes:
- Existing remediation tickets `TASK-0213` through `TASK-0215` remain valid. This ticket adds bundle intent above them instead of replacing them.
- `aws-slo-adoption-course` is not part of `BUNDLE-001`; it is a candidate for `BUNDLE-002 SRE運用入門バンドル`.
