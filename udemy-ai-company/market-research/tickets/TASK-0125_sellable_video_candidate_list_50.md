# Task Summary
Task ID: TASK-0125
Title: Udemyで売れる可能性がある動画テーマ候補を50本以上作る

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- `market-research/udemy_keyword_demand_scan.md`
- `market-research/learner_pain_review_scan.md`
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0121
- TASK-0122
- TASK-0123
- TASK-0124

# Deliverables
Expected Output:
- `market-research/udemy_sellable_video_candidates_50.md`
- 50本以上の動画テーマ候補
- 各候補の想定受講者
- 各候補の学習Promise
- 市場シグナル
- 競合との差別化
- ハンズオン化可否
- GPT-Image2スライド化のしやすさ
- VOICEVOX台本化の注意点

# Quality Gate
Definition of Done:
- 動画テーマ候補が50件以上ある
- 各候補に、タイトル案、対象者、学習Promise、市場根拠、差別化、制作難易度、優先度がある
- AWS/SRE関連に寄せている
- 既存講座 `aws-slo-adoption-course` と重複する場合は、重複理由と差別化案を明記している
- 「売れる」と断定せず、仮説スコアとして扱っている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 量産候補を根拠付きで揃え、CEOが次の講座テーマを判断できる状態にする

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 既存講座の `course_spec.md` は変更しない
- 新講座の制作着手はCEO選定後の別チケットで行う
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- 50本は講座全体ではなく、動画単位または小講座単位のテーマ候補として扱う
- GitHub Issue: #132 https://github.com/toma1110/udemy2/issues/132
- Output: `market-research/udemy_sellable_video_candidates_50.md`
- Candidate count: 52
- Completed: 2026-05-13
