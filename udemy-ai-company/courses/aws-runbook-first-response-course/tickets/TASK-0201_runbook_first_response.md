# TASK-0201: AWS障害対応Runbookを作る動画を制作する

## Task Summary

Task ID: TASK-0201
Title: AWS障害対応Runbookを作る動画を制作する
GitHub Issue: #173

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Engineering/Production draft started
Auto Execute: yes
Requires CEO Approval: no for content drafting
Cost Impact: none for standard scope

## Inputs

- `udemy-ai-company/market-research/udemy_sellable_video_candidates_50.md`
- `udemy-ai-company/courses/aws-alert-design-practical-course/`
- `udemy-ai-company/courses/aws-slo-adoption-course/scripts/s7-l2_script.md`
- AWS Well-Architected runbook/playbook documentation

## Deliverables

- `course_spec.md`
- `course_curriculum.md`
- `course_infomation.md`
- `handson/runbook_template.md`
- `scripts/s1-l1_runbook_map_script.md`
- `scripts/s1-l1_runbook_map_script.json`
- `slides/s1-l1_gpt_image2_prompts.md`
- `qa/aws_source_verification_report.md`
- `qa/production_qa_plan.md`

## Quality Gate

- Runbook includes trigger, owner, severity, first checks, escalation, rollback/mitigation, communication, and postmortem link
- No real AWS execution is required for standard lesson
- Worker != Reviewer

## Notes

The first production slice is `s1-l1`. Subsequent lectures can expand into first checks, escalation timeline, and communication/postmortem linkage.
