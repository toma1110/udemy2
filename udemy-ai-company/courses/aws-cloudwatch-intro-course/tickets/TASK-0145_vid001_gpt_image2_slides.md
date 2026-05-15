# Task Summary

Task ID: `TASK-0145`
Title: `VID-001追加レクチャーのGPT-Image2スライドを制作する`

## Ownership

Department: Production
Owner AI: `AI-Production-01`
Reviewer AI: `AI-QA-01`

## Execution

Priority: high
Status: done

## Inputs

Input Files:

- `scripts/*_script.json`
- `slides/*_gpt_image_prompts.md`
- `docs/GPT_IMAGE_RULES.md`
- `docs/VIDEO_QUALITY_BASELINE.md`

Dependencies:

- `TASK-0144`

## Deliverables

Expected Output:

- GPT-Image2 source PNGs under `slides/<section>-gpt-image2-sources/<lecture>/`
- final PNGs under `slides/<lecture>/`
- contact sheets
- slide generation QA reports

## Quality Gate

Definition of Done:

- Final PNGs are GPT-Image2-derived
- Local text overlay is absent
- Contact sheet exists
- Visual quality does not fall below `s1-l1` baseline

## Constraints

Rules:

- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Final videos must not use local-only slides

## Blocking

Blocked By:
Notes:
