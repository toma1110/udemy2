# Task Summary
Task ID: TASK-0138
Title: VID-001講座の完成動画MP4を生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Approval Required
Auto Execute: yes
Requires CEO Approval: yes
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/slides/s1-l1/`
- `courses/aws-cloudwatch-intro-course/audio/s1-l1/`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_audio_review_report.md`
Dependencies:
- TASK-0135
- TASK-0137

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/video/s1-l1/s1-l1.mp4`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_video_build_report.md`

# Quality Gate
Definition of Done:
- MP4が1920x1080、16:9、H.264、AACで生成されている
- スライド数と音声数が一致している
- ffmpeg decodeチェックが成功する
- faststartが付与されている
- 動画尺、入力ファイル、検証結果がレポートに残っている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 受講者が見やすく、制作証跡が追跡できる動画にする

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0135
- TASK-0137
- CEO approval to start VID-001 course production
Notes:
- ffmpeg実行では `-nostdin` を使う。
- GitHub Issue: #145 https://github.com/toma1110/udemy2/issues/145
