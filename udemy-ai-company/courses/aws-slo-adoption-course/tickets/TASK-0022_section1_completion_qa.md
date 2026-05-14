# Task Summary
Task ID: TASK-0022
Title: aws-slo-adoption-course Section 1 の動画完了QAを行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Blocked

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
- udemy-ai-company/courses/aws-slo-adoption-course/lectures.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l1_drive_upload_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l2_drive_upload_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_drive_upload_report.md
Dependencies:
- TASK-0011 completed
- TASK-0015 completed
- TASK-0021 completed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section1_completion_report.md
- Section 1 Drive URL list
- Section 2へ進むためのBlocked事項一覧

# Quality Gate
Definition of Done:
- S1-L1、S1-L2、S1-L3のDrive URLがすべて記録されている
- 3本ともDrive fileが `trashed: false` で共有可能である
- 各動画の台本、スライド、音声、動画、Driveレポートが揃っている
- 音声聴取QAの指摘がすべて解消済みである
- `course_spec.md` と `lectures.md` との矛盾がない
- Section 1からSection 2へ進む導線が自然である
- 未解決リスクがある場合はSection 2開始前のIssueとして切り出されている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CEO承認なしにPublished扱いにしない

# Blocking
Blocked By: TASK-0021
Notes:
- Section 1完了後、Section 2の制作チケットを同じ型で切る。
