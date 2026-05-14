# Task Summary
Task ID: TASK-0027
Title: aws-slo-adoption-course Section 2 Lecture 1 のVOICEVOX音声を生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l1_script.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
- udemy-ai-company/tools/narration_checker.py
Dependencies:
- TASK-0025 reviewed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/audio/s2-l1/slide_001.wav ... slide_00N.wav
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l1_voicevox_generation_report.md

# Quality Gate
Definition of Done:
- VOICEVOX Engine起動確認済み
- gTTSフォールバックを使っていない
- `narration_checker.py` が成功している
- WAV数が台本スライド数と一致している
- WAVデコード確認が通る
- WAVの形式、長さ、生成条件をQAレポートへ記録している
- 生成メディアはGit追跡しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- VOICEVOX未起動のまま本番音声を生成しない

# Blocking
Blocked By: TASK-0025
Notes:
- 音声生成後、動画生成へ進む前にTASK-0028の聴取QAを必ず通す。
