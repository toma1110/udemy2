# Task Summary
Task ID: TASK-0121
Title: Udemy登録情報をSLO導入・運用主語に見直す

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: medium
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-slo-adoption-course/course_infomation.md`
- `courses/aws-slo-adoption-course/course_spec.md`
- `courses/aws-slo-adoption-course/scripts/promo_video_script.md`
- `courses/aws-slo-adoption-course/scripts/promo_video_script.json`
Dependencies:
- CEO feedback: ハンズオンメインではなく、SLO導入できるようになることが分かるタイトルへ寄せる

# Deliverables
Expected Output:
- `courses/aws-slo-adoption-course/course_infomation.md` の登録文言を更新
- `courses/aws-slo-adoption-course/course_spec.md` のタイトルを同期
- `courses/aws-slo-adoption-course/scripts/promo_video_script.*` の旧タイトル表記を更新

# Quality Gate
Definition of Done:
- コースタイトルがハンズオン主語ではなくSLO導入・運用主語になっている
- CloudFormationは教材ハンズオンの再現手段として位置づけられている
- 実運用IaCではCDKまたはTerraformを推奨する文脈と矛盾しない
- SLO導入、SLI設計、エラーバジェット、運用レビューの価値が伝わる
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #157 https://github.com/toma1110/udemy2/issues/157
- 既存動画MP4は自動更新されない。promo動画で旧タイトルが画面表示される場合は、公開前に再レンダリング対象とする。
