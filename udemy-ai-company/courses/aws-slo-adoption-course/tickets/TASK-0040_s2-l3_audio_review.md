# Task Summary
Task ID: TASK-0040
Title: aws-slo-adoption-course Section 2 Lecture 3 の音声聴取QAと読み修正を行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/audio/s2-l3/slide_001.wav ... slide_00N.wav
- udemy-ai-company/docs/VOICEVOX_RULES.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l3_voicevox_generation_report.md
Dependencies:
- TASK-0039 completed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l3_audio_review_report.md
- 必要に応じた `s2-l3_script.md` 読み修正
- 必要に応じた `VOICEVOX_RULES.md` / `narration_checker.py` 更新
- 必要に応じた該当WAV再生成

# Quality Gate
Definition of Done:
- 全WAVを通しで聴取している
- `SLO`、`SLI`、`サービス責任者`、`メトリクス`、`障害対応`、`リリース判断` の読みが自然である
- チェックリスト表現が単調すぎず、受講者が聞き取りやすい
- 不自然な空白、文末切れ、長すぎる無音、異常ノイズがない
- 指摘がある場合は、台本修正、音声再生成、再聴取まで完了している
- 人間CEOが最低1回スポット聴取するための確認ポイントがレポートにまとまっている
- このチケットが完了するまで動画生成チケットをReadyにしない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- QA担当は制作成果物を承認するが、未修正の誤読を許容しない

# Blocking
Blocked By: TASK-0039
Notes:
