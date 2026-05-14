# Task Summary
Task ID: TASK-0078
Title: 動画制作パイプラインの速度、並列度、安定性の運用基準を定義する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/docs/WORKFLOW.md
- udemy-ai-company/docs/TASK_MANAGEMENT.md
- udemy-ai-company/docs/QUALITY_GATE.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/*_video_build_report.md
Dependencies:
- 既存の動画制作チケット運用が成立していること

# Deliverables
Expected Output:
- udemy-ai-company/docs/PRODUCTION_CAPACITY.md
- udemy-ai-company/templates/production_capacity_report_template.md
- udemy-ai-company/tools/production_capacity_check.sh

# Quality Gate
Definition of Done:
- CPU、メモリ、ディスク、VOICEVOX、ffmpegを考慮した並列実行基準がある
- 現行の2 vCPU環境で安全な同時実行数が明記されている
- 速度計測に必要な記録項目が定義されている
- 安定化のための停止条件、再試行条件、ロック方針が明記されている
- read-onlyで実行できる容量診断ツールがある
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- 生成中の動画、音声、スライド素材には干渉しない
- 診断ツールは既存プロセスを停止しない

# Blocking
Blocked By:
Notes:
- 2026-05-10 read-only確認では、ホストは2 vCPU、約1.9GiB RAM、swap使用あり。
- CPU系の新規並列化は、VOICEVOXとffmpegを同時に走らせない基準から始める。
