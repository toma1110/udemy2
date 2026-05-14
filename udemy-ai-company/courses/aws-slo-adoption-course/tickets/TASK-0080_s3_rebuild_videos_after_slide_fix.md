# Task Summary
Task ID: TASK-0080
Title: aws-slo-adoption-course Section 3 スライド修正版で動画を再生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l*/slide_*.png
- udemy-ai-company/courses/aws-slo-adoption-course/audio/s3-l*/slide_*.wav
Dependencies:
- TASK-0079 done

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l1/s3-l1.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l2/s3-l2.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l3/s3-l3.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l4/s3-l4.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l5/s3-l5.mp4
- updated video build QA reports

# Quality Gate
Definition of Done:
- 修正版スライドと既存VOICEVOX音声で動画を再生成している
- H.264、1920x1080、AAC mono、44100Hzである
- faststartが付与されている
- ffmpeg decode checkが成功する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 音声に問題なしのためWAVは再生成しない

# Blocking
Blocked By:
Notes:
