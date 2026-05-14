# Task Summary
Task ID: TASK-0062
Title: aws-slo-adoption-course Section 3 Lecture 3 の動画を生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- course_spec.md
- lectures.md
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
Dependencies:
- TASK-0061 done

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l3/s3-l3.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l3_video_build_report.md

# Quality Gate
Definition of Done:
- スライドPNGとVOICEVOX音声からMP4を生成している
- H.264、1920x1080、30fps、AAC音声である
- faststartが付与されている
- ffmpeg decodeチェックが成功する
- 動画尺とスライド数がレポートに記録されている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- ナレーション本文に英字略語を残さない

# Blocking
Blocked By:
Notes:
- 2026-05-10 ユーザーから「s3も作成開始してください！」と制作開始承認済み。
