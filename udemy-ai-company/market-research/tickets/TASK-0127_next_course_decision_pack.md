# Task Summary
Task ID: TASK-0127
Title: 次に作るUdemy講座候補のCEO判断パックを作る

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
- `market-research/udemy_video_idea_scoring_top10.md`
- `market-research/udemy_sellable_video_candidates_50.md`
- `templates/course_spec_template.md`
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0126

# Deliverables
Expected Output:
- `market-research/next_course_decision_pack.md`
- 上位3講座候補
- 各候補のCourse Promise案
- 想定章立て
- ハンズオン範囲
- 低コスト構成案
- CEOへの推奨順位
- CEOが選ぶべき判断ポイント

# Quality Gate
Definition of Done:
- 上位10本から、講座化しやすい候補を3案に絞っている
- 各候補に、対象者、Promise、差別化、ハンズオン範囲、Out of Scopeがある
- 教材ハンズオンをCloudFormationで成立させるか、実運用ではCDK/Terraform推奨にすべきかを明記している
- まだ `course_spec.md` は作成せず、CEO承認待ちの判断資料に留めている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- CEOが最終判断に集中できるよう、調査結果を講座候補へ整理する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 新講座の `course_spec.md` 作成はCEO選定後の別チケットで行う
- AWS課金作業は禁止
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- CEO選定後、別途 `course_spec.md` 作成チケットを起票する
- GitHub Issue: #134 https://github.com/toma1110/udemy2/issues/134
- Output: `market-research/next_course_decision_pack.md`
- Recommended next course: AWS CloudWatch運用監視入門: CloudFormationハンズオン版
- Completed: 2026-05-13
