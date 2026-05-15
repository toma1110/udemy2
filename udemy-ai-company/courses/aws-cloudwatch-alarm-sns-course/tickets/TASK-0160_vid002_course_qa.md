# Task Summary

Task ID: `TASK-0160`
Title: VID-002 course QA

## Ownership

Department: QA
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `scripts/*_script.json`
- `slides/*/contact_sheet.png`
- `video/*/*.mp4`
- `cloudformation/README.md`

Dependencies:
- `TASK-0159`

## Deliverables

Expected Output:
- Course QA report
- AWS execution caveat record

## Quality Gate

Definition of Done:
- course_spec and curriculum are consistent
- Worker and Reviewer are different
- CloudFormation create/update/delete are not executed without CEO approval
- GPT-Image2 and VOICEVOX policy is satisfied

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- None

Notes:
- Static validation can be run; AWS stack mutation cannot.
- `validate.sh` によるCloudFormation validate-templateはPASS。
- AWS stack create/update/deleteはCEO承認対象のため未実行。
