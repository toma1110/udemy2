# Task Summary

Task ID: `TASK-0195`
Title: Application Signals実践コースの通常レクチャー台本を作成する

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Review
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `scripts/lectures.md`
- `cloudformation/README.md`
- `handson/README.md`
- `qa/aws_source_verification_report.md`

Dependencies:
- `TASK-0192`
- `TASK-0193`

## Deliverables

Expected Output:
- `scripts/s1-l1_script.md`
- `scripts/s1-l1_script.json`
- `scripts/s1-l2_script.md`
- `scripts/s1-l2_script.json`
- `scripts/s2-l1_script.md`
- `scripts/s2-l1_script.json`
- `scripts/s2-l2_script.md`
- `scripts/s2-l2_script.json`
- `scripts/s2-l3_script.md`
- `scripts/s2-l3_script.json`
- `scripts/s3-l1_script.md`
- `scripts/s3-l1_script.json`
- `scripts/s3-l2_script.md`
- `scripts/s3-l2_script.json`
- `scripts/s3-l3_script.md`
- `scripts/s3-l3_script.json`
- `scripts/s4-l1_script.md`
- `scripts/s4-l1_script.json`
- `scripts/s4-l2_script.md`
- `scripts/s4-l2_script.json`
- `scripts/s4-l3_script.md`
- `scripts/s4-l3_script.json`

## Quality Gate

Definition of Done:
- 各レクチャーが `course_curriculum.md` のLearning Goalに対応している
- ナレーションがVOICEVOX向けにチェック済み
- AWSリソース作成の説明はCEO承認後の検証結果と矛盾しない
- Application Signals SLOはメトリクス到達後に作る説明になっている
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- ローカル描画スライドを完成動画に使わない

## Blocking

Blocked By:
- `TASK-0193` QA review findings
- CEO-approved lifecycle validation if actual console screenshots or exact timings are required

Notes:
- まずS1とプロモーション動画を優先し、ハンズオン実演レクチャーは検証結果に合わせて調整する。
- 2026-05-16: `s1-l1` と `s1-l2` のMarkdown台本、JSON台本、GPT-Image2プロンプトを作成済み。
- 2026-05-16: `tools/narration_checker.py` でプロモーション動画、`s1-l1`、`s1-l2` のナレーションチェック済み。
- 2026-05-16: `s2-l1` から `s4-l3` までのMarkdown台本、JSON台本、GPT-Image2プロンプトを作成済み。
- 2026-05-16: `scripts/` 配下の全台本に対してJSON妥当性確認と `tools/narration_checker.py --warnings-ok` を実行済み。
- Reviewer AIによる内容QAは未実施。
