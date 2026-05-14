# Task Summary
Task ID: TASK-0020
Title: aws-slo-adoption-course Section 1 Lecture 3 の動画を生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Blocked

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s1-l3/slide_001.png ... slide_00N.png
- udemy-ai-company/courses/aws-slo-adoption-course/audio/s1-l3/slide_001.wav ... slide_00N.wav
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_audio_review_report.md
Dependencies:
- TASK-0017 reviewed
- TASK-0018 completed
- TASK-0019 approved

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l3/s1-l3.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_video_build_report.md

# Quality Gate
Definition of Done:
- スライド数と音声数が一致している
- 全セグメントを同一音声仕様 AAC mono 44100 Hz で生成している
- 生成MP4がH.264 1920x1080 30fpsである
- ffprobeでduration、video stream、audio streamを確認している
- ffmpeg decode checkが成功している
- faststartが適用されている
- 代表フレームが非空で、台本内容と一致している
- 生成メディアはGit追跡しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 音声聴取QAが終わるまで動画生成しない

# Blocking
Blocked By: TASK-0017, TASK-0018, TASK-0019
Notes:
