# Task Summary
Task ID: TASK-0117
Title: Section 9 の動画完了QAとCEO確認待ちにする

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: CEO Review

# Inputs
Input Files:
- `scripts/s9-l1_script.md` through `scripts/s9-l4_script.md`
- `slides/s9-l1` through `slides/s9-l4`
- `audio/s9-l1` through `audio/s9-l4`
- `video/s9-l1` through `video/s9-l4`
Dependencies:
- TASK-0113 through TASK-0116

# Deliverables
Expected Output:
- `qa/section9_completion_report.md`
- `qa/s9_gpt_image2_batch_render_report.md`
- Drive URLs for all Section 9 videos
- Quality gate summary

# Quality Gate
Definition of Done:
- Section 9の4動画がMP4 faststart true、decode check OK
- GPT-Image2 slide source is preserved
- Google Drive upload and sharing verified
- VOICEVOX report and render report are recorded
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- S7配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #125
