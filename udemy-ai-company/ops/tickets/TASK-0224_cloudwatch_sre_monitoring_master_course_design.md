# Task Summary

Task ID: TASK-0224
Title: CloudWatch/SRE監視実践マスター長尺コース設計

## Ownership

Department: Strategy / Production
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Review

## Inputs

Input Files:

- `udemy-ai-company/docs/BUNDLE_STRATEGY.md`
- `udemy-ai-company/templates/course_spec_template.md`
- `udemy-ai-company/templates/course_infomation_template.md`
- `udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md`
- `udemy-ai-company/courses/aws-slo-adoption-course/course_curriculum.md`
- `udemy-ai-company/courses/aws-slo-adoption-course/course_infomation.md`

Dependencies:

- `BUNDLE-001 CloudWatch監視入門バンドル`
- `BUNDLE-002 SRE運用入門バンドル`
- `BUNDLE-003 発展監視・APMバンドル`
- `BUNDLE-004 AWS学習安全・トラブルシュートバンドル`

## Deliverables

Expected Output:

- `udemy-ai-company/courses/aws-cloudwatch-sre-monitoring-master-course/README.md`
- `udemy-ai-company/courses/aws-cloudwatch-sre-monitoring-master-course/course_spec.md`
- `udemy-ai-company/courses/aws-cloudwatch-sre-monitoring-master-course/course_curriculum.md`
- `udemy-ai-company/courses/aws-cloudwatch-sre-monitoring-master-course/course_infomation.md`
- 制作ディレクトリREADME一式
- `udemy-ai-company/docs/BUNDLE_STRATEGY.md` の長尺旗艦コース方針更新

## Quality Gate

Definition of Done:

- 10〜12時間級の長尺コースとして成立する章立てがある
- 既存短尺講座の単純連結ではなく、統合演習、章末演習、設計レビュー、運用判断が含まれる
- バンドル戦略との関係が明記されている
- CloudFormationは教材ハンズオン用途に限定されている
- 実運用IaCはCDKまたはTerraform推奨になっている
- GPT-Image2とVOICEVOX前提が明記されている
- AWSリソース作成、更新、削除を伴う検証はCEO承認後であることが明記されている
- WorkerとReviewerが分離されている
- Udemy登録用 `course_infomation.md` が標準チェックを通過する

## Constraints

Rules:

- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- AWS課金影響がある操作はCEO承認後のみ実行
- 完成動画にはGPT-Image2由来PNGのみ使用
- ナレーションはVOICEVOXを前提にする

## Blocking

Blocked By:

- AI-QA-01による企画レビュー
- 長尺版を先に制作するか、短尺バンドル検証後に制作するかのCEO判断

Notes:

- 本タスクは設計のみ。動画生成、AWSリソース作成、PublicRepo作成、Google Driveアップロードは別チケットで実施する。
