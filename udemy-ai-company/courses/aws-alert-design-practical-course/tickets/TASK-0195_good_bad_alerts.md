# TASK-0195: VID-005 良いアラートと悪いアラートを制作する

## Task Summary

Task ID: TASK-0195
Title: VID-005 良いアラートと悪いアラートを制作する
GitHub Issue: #169

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

- `udemy-ai-company/market-research/udemy_video_idea_scoring_top10.md`
- `udemy-ai-company/market-research/udemy_sellable_video_candidates_50.md`
- `udemy-ai-company/courses/aws-sre-practical/s5-l1/script.json`
- AWS CloudWatch alarm documentation

## Deliverables

- `course_spec.md`
- `course_curriculum.md`
- `course_infomation.md`
- `scripts/s1-l1_good_bad_alerts_script.md`
- `scripts/s1-l1_good_bad_alerts_script.json`
- `slides/s1-l1_gpt_image2_prompts.md`
- `qa/aws_source_verification_report.md`
- `qa/production_qa_plan.md`

## Quality Gate

- Alert fatigue, actionability, severity, owner, threshold, and runbook connection are explained
- CloudWatch alarm evaluation settings are sourced from AWS docs
- Standard content requires no AWS execution
- Worker != Reviewer

## Notes

The first production slice is `s1-l1`. Subsequent lectures can expand into M out of N, missing data, Composite Alarm, and Runbook connection.
