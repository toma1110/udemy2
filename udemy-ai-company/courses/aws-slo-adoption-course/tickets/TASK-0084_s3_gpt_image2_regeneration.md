# Task Summary
Task ID: TASK-0084
Title: aws-slo-adoption-course Section 3 スライドをGPT-Image2で再生成し動画を再作成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l4_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l5_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s2-l*/contact_sheet.png
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3_slide_generation_root_cause_report.md
Dependencies:
- TASK-0083 done
- CEO approval to regenerate S3 with GPT-Image2

# Deliverables
Expected Output:
- GPT-Image2-generated S3 slide PNGs for S3-L1 to S3-L5
- Updated contact sheets
- Updated slide generation reports with Generation Mode and GPT-Image2 source evidence
- Rebuilt S3 videos using approved existing VOICEVOX audio
- Updated video build reports
- Updated Google Drive upload reports and URLs
- Updated section3 completion report

# Quality Gate
Definition of Done:
- Final slide PNGs are GPT-Image2-derived
- `*_slide_generation_report.md` records Generation Mode, GPT-Image2 source files, prompt summary, post-processing, and contact sheet comparison
- S2 approved contact sheets are used as visual quality reference
- Slide text density and visual richness are comparable to S2
- Worker and Reviewer are separated
- Existing approved audio is reused unless a separate audio change request is approved
- Videos pass ffprobe, faststart, decode check, and Drive sharing checks

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- ローカル描画だけで最終スライドを作らない
- 例外採用はCEO承認が必要

# Blocking
Blocked By:
Notes:
- GitHub Issue: #84
- 2026-05-11 CEOがGPT-Image2での動画再生成を承認。Blocked解除し制作開始。
- 2026-05-11 S3-L1〜S3-L5 のGPT-Image2スライド再生成、動画再ビルド、Google Drive再アップロード、Driveメタデータ確認まで完了。
