# Task Summary

Task ID: `TASK-0176`
Title: AWS課金事故防止入門 コースQA

## Ownership

Department: QA
Owner AI: AI-QA-01
Reviewer AI: AI-Strategy-01

## Execution

Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `handson/README.md`
- `qa/aws_source_verification_report.md`
- `scripts/`
- `slides/`
- `audio/`
- `video/`

Dependencies:
- `TASK-0175`

## Deliverables

Expected Output:
- course QA report
- source consistency report
- audio/video spot check notes
- Drive upload summary

## Quality Gate

Definition of Done:
- AWS公式情報と矛盾しない
- 課金防止を過剰に保証していない
- 料金、無料枠、反映遅延、API課金の注意が明記されている
- GPT-Image2/VOICEVOXルールを満たす
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- AWS/billing-related execution requires CEO approval

## Blocking

Blocked By:
- TASK-0175
