# Task Summary

Task ID: `TASK-0191`
Title: CloudWatch introのUdemy登録情報をSLO相当形式に更新し横展開する

## Ownership

Department: production / ops
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Review
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `courses/aws-cloudwatch-intro-course/course_spec.md`
- `courses/aws-cloudwatch-intro-course/course_curriculum.md`
- `courses/aws-cloudwatch-intro-course/course_infomation.md`
- `courses/aws-slo-adoption-course/course_infomation.md`
- `docs/QUALITY_GATE.md`

Dependencies:
- CEO request on 2026-05-17

## Deliverables

Expected Output:
- `courses/aws-cloudwatch-intro-course/course_infomation.md` をSLOコース相当のUdemy登録情報フォーマットへ更新
- Git管理されている公開候補コースの既存 `course_infomation.md` を同フォーマットへ横展開
- `templates/course_infomation_template.md`
- `tools/check_course_information.py`
- `ops/course_information_format_audit_20260517.md`
- Quality Gateの再発防止追記

## Quality Gate

Definition of Done:
- CloudWatch introの `course_infomation.md` がUdemy登録画面の入力項目に沿っている
- `course_spec.md`、ハンズオン範囲、プロモーション動画、VOICEVOX/AI利用表記と矛盾しない
- 横展開対象と残タスクが明記されている
- 再発防止としてテンプレートと機械チェックが追加されている
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- AWSリソース作成や課金影響のある作業は行わない
- 動画、音声、画像生成物は変更しない

## Blocking

Blocked By:
- None

Notes:
- 2026-05-17: CloudWatch introのUdemy登録情報をSLO相当形式へ更新し、テンプレート・チェックツール・横展開監査メモを追加。
- 2026-05-17: Git管理されている公開候補コースへ横展開し、`check_course_information.py` の監査がPASSになった。未追跡の将来コース候補は、コース本体をコミットする別チケットで同テンプレートへ揃える。
