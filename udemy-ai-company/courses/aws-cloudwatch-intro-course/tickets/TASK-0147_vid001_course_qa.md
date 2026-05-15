# Task Summary

Task ID: `TASK-0147`
Title: `VID-001拡張コースの教材QAを実施する`

## Ownership

Department: QA
Owner AI: `AI-QA-01`
Reviewer AI: `AI-Ops-01`

## Execution

Priority: high
Status: done

## Inputs

Input Files:

- `course_spec.md`
- `course_curriculum.md`
- `handson/README.md`
- `scripts/*_script.md`
- `slides/*/contact_sheet.png`
- `video/*/*.mp4`

Dependencies:

- `TASK-0146`

## Deliverables

Expected Output:

- per-lecture QA reports
- final course QA report

## Quality Gate

Definition of Done:

- Course follows Source of Truth
- Logs Insights content is source-aligned
- Hands-on remains no-resource-create by default
- GPT-Image2 and VOICEVOX requirements are satisfied
- Worker != Reviewer

## Constraints

Rules:

- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
Notes:
