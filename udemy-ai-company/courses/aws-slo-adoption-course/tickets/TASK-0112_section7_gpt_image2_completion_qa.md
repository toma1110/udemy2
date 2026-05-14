# Task Summary
Task ID: TASK-0112
Title: Section 7 GPT-Image2版の動画完了QAとCEO確認待ちにする

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Ready for CEO Review

# Inputs
Input Files:
- `scripts/s7-l1_script.md` through `scripts/s7-l3_script.md`
- `slides/s7-l1` through `slides/s7-l3`
- `audio/s7-l1` through `audio/s7-l3`
- `video/s7-l1` through `video/s7-l3`
Dependencies:
- TASK-0109 through TASK-0111

# Deliverables
Expected Output:
- `qa/section7_completion_report.md`
- `qa/s7_gpt_image2_batch_render_report.md`
- Drive URLs for all Section 7 videos
- Quality gate summary

# Quality Gate
Definition of Done:
- Section 7の3動画がMP4 faststart true、decode check OK
- GPT-Image2 slide source is preserved
- Google Drive upload and sharing verified
- VOICEVOX report and render report are recorded
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- S6配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #110
- Completed: 2026-05-12
- Section report: `qa/section7_completion_report.md`
- Batch render report: `qa/s7_gpt_image2_batch_render_report.md`
- Drive URLs: S7-L1, S7-L2, S7-L3 all uploaded and shared as anyone-reader
- QA: Section 7の3動画がfaststart true、decode check OK、代表フレーム確認OK
