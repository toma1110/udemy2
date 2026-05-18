# Task Summary
Task ID: TASK-0245
Title: CloudWatch入門コース画像を生成しGoogle Driveへアップロードする

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/course_infomation.md`
- `courses/aws-cloudwatch-intro-course/course_spec.md`
Dependencies:
- CEO request on 2026-05-18

# Deliverables
Expected Output:
- `course_image_gpt_image2_source.png`
- `course_image.png`
- `qa/course_image_generation_report.md`
- `qa/course_image_drive_metadata.json`
- `qa/course_image_drive_upload_report.md`

# Quality Gate
Definition of Done:
- Udemy target image exists and is 750x422 PNG
- GPT-Image2 source is preserved
- Drive upload has `mimeType: image/png`
- Drive upload has `trashed: false`
- Drive upload has anyone-reader permission
- Worker != Reviewer

# Constraints
Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- final course image must be GPT-Image2-derived PNG
- course image must not contain text, official AWS logos, or official UI copies
- follow `docs/GOOGLE_DRIVE_RULES.md`

# Blocking
Blocked By:
- none
Notes:
- Uploaded file: `aws-cloudwatch-intro-course-image-20260518.png`
- Drive URL: https://drive.google.com/file/d/12Q8yIvHA86DKeNuy2VLs-jg9SXIN9hjC/view?usp=drivesdk
