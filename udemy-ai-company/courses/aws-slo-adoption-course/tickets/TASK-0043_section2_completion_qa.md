# Task Summary
Task ID: TASK-0043
Title: aws-slo-adoption-course Section 2 の動画完了QAを行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
- udemy-ai-company/courses/aws-slo-adoption-course/lectures.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l1_drive_upload_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l2_drive_upload_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l3_drive_upload_report.md
Dependencies:
- TASK-0030 completed
- TASK-0036 completed
- TASK-0042 completed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section2_completion_report.md
- Section 2 Drive URL list
- Section 3へ進むためのBlocked事項一覧

# Quality Gate
Definition of Done:
- S2-L1、S2-L2、S2-L3のDrive URLがすべて記録されている
- 3本ともDrive fileが `trashed: false` で共有可能である
- 各動画の台本、スライド、音声、動画、Driveレポートが揃っている
- 音声聴取QAの指摘がすべて解消済みである
- `course_spec.md` と `lectures.md` との矛盾がない
- Section 2からSection 3へ進む導線が自然である
- 未解決リスクがある場合はSection 3開始前のIssueとして切り出されている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CEO承認なしにPublished扱いにしない

# Blocking
Blocked By:
Notes:
- Section 2完了後、Section 3の制作チケットを同じ型で切る。
