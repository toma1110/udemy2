# Task Summary
Task ID: TASK-0081
Title: aws-slo-adoption-course Section 3 修正版動画をGoogle Driveへアップロードする

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l1/s3-l1.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l2/s3-l2.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l3/s3-l3.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l4/s3-l4.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/video/s3-l5/s3-l5.mp4
Dependencies:
- TASK-0080 done

# Deliverables
Expected Output:
- updated Drive URLs for S3-L1 to S3-L5
- updated drive upload QA reports

# Quality Gate
Definition of Done:
- Google Driveへ修正版動画がアップロードされている
- 共有権限が anyone reader である
- Drive URL、ファイルID、サイズが記録されている
- Issue #77 に修正版URLをコメントしている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth

# Blocking
Blocked By:
Notes:
