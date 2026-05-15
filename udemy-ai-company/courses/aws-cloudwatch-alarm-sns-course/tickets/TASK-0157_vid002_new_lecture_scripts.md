# Task Summary

Task ID: `TASK-0157`
Title: VID-002追加レクチャー台本作成

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `cloudformation/template.yaml`
- `cloudformation/README.md`

Dependencies:
- `TASK-0156`

## Deliverables

Expected Output:
- `scripts/s1-l2_script.md`
- `scripts/s1-l2_script.json`
- `scripts/s1-l3_script.md`
- `scripts/s1-l3_script.json`
- `scripts/s2-l1_script.md`
- `scripts/s2-l1_script.json`
- `scripts/s2-l2_script.md`
- `scripts/s2-l2_script.json`
- `scripts/s3-l1_script.md`
- `scripts/s3-l1_script.json`
- `slides/*_gpt_image_prompts.md`

## Quality Gate

Definition of Done:
- 台本がVOICEVOXで読みやすい日本語になっている
- READMEと矛盾しない
- stack create/update/deleteをCEO承認後の操作として扱う
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- ローカル文字合成禁止

## Blocking

Blocked By:
- None

Notes:
- AWS公式情報と既存source verificationを前提にする。
- 追加5レクチャーの台本JSONとGPT-Image2プロンプトを作成済み。
