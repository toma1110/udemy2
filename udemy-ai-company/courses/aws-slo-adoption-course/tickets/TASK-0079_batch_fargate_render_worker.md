# Task Summary
Task ID: TASK-0079
Title: 動画生成の重い処理をAWS Batch on ECS Fargateへ逃がす制作基盤を構築する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/docs/PRODUCTION_CAPACITY.md
- udemy-ai-company/docs/CLOUDFORMATION_RULES.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/
- udemy-ai-company/courses/aws-slo-adoption-course/audio/
Dependencies:
- TASK-0078 done

# Deliverables
Expected Output:
- udemy-ai-company/infrastructure/batch-fargate/template.yaml
- udemy-ai-company/infrastructure/batch-fargate/README.md
- udemy-ai-company/infrastructure/batch-fargate/worker/Dockerfile
- udemy-ai-company/infrastructure/batch-fargate/worker/render_worker.py
- udemy-ai-company/infrastructure/batch-fargate/scripts/*.sh
- udemy-ai-company/infrastructure/batch-fargate/examples/manifest.example.json

# Quality Gate
Definition of Done:
- CloudFormationでAWS Batch Fargate compute environment、job queue、job definition、ECR、S3、CloudWatch Logs、IAMを作成できる
- NAT Gatewayや常駐ECS Serviceを作らず、ジョブ未実行時のcompute課金を避ける
- Fargate jobはpublic subnetで起動し、Security Groupの inbound は開けない
- Job roleは成果物S3 bucketへの必要最小限アクセスに限定する
- workerはS3上のPNG/WAVを入力にし、MP4とQAレポートをS3へ出力できる
- ffmpegは `-nostdin` を使い、segment生成、concat、faststart、decode checkを実行する
- build、deploy、upload、submit、smoke test用スクリプトがある
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- 既存の動画生成プロセスと素材ディレクトリには干渉しない
- CloudFormationを使う
- Terraformは使わない

# Blocking
Blocked By:
Notes:
- MVPは既存WAVを使うrender workerとする。
- VOICEVOXをFargate workerに同梱する構成は、Docker imageサイズと起動時間を実測してから次チケットで判断する。
