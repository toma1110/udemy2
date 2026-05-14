# Task Summary
Task ID: TASK-0093
Title: AWS Batch FargateをVOICEVOX音声生成とffmpeg動画生成の2段ジョブに変更する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/infrastructure/batch-fargate/
- udemy-ai-company/docs/PRODUCTION_CAPACITY.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l5_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l5/
Dependencies:
- TASK-0079 done

# Deliverables
Expected Output:
- VOICEVOX worker image
- VOICEVOX AWS Batch job definition
- `submit_two_stage_jobs.sh`
- 2段job実行レポート

# Quality Gate
Definition of Done:
- VOICEVOX jobがS3上の台本からWAVを生成できる
- render jobがVOICEVOX job成功後に起動する
- render jobが生成されたWAVとPNGからMP4を生成できる
- CloudFormation validateが成功する
- AWS smoke testが成功する
- s3-l5で2段jobの実行結果を記録する
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- CloudFormationを使う
- Terraformは使わない
- 常駐ECS ServiceやNAT Gatewayを作らない

# Blocking
Blocked By:
Notes:
- ユーザー表記は「voicebox」だが、既存運用に合わせてVOICEVOXとして実装する。
- 2026-05-11: CloudFormation update完了。VOICEVOX用ECR、CodeBuild、Batch JobDefinition、CloudWatch Logsを追加。
- 2026-05-11: `WORKER_TYPE=voicevox` でVOICEVOX worker imageをECRへpush済み。
- 2026-05-11: `s3-l5` で2段ジョブを実行し、VOICEVOX job・render jobともにSUCCEEDED。
- 2026-05-11: QAレポート `udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l5_batch_fargate_two_stage_report.md` を作成。
