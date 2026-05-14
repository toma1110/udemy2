# Task Summary
Task ID: TASK-0015
Title: aws-slo-adoption-course Section 1 Lecture 2 の動画を生成し、読み修正版をDrive更新する

# Ownership
Department: production / ops
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s1-l2/slide_001.png ... slide_009.png
- udemy-ai-company/courses/aws-slo-adoption-course/audio/s1-l2/slide_001.wav ... slide_009.wav
- udemy-ai-company/docs/VOICEVOX_RULES.md
Dependencies:
- TASK-0012 production complete
- TASK-0013 production complete
- TASK-0014 production complete
- CEO auditory review feedback reflected

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l2/s1-l2.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l2_script_review_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l2_voicevox_asset_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l2_video_build_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l2_drive_upload_report.md
- Google Drive URL: https://drive.google.com/file/d/1bAF6MrXm6I2d2e3hH12ZcrtURCeSuzCO/view?usp=drivesdk

# Quality Gate
Definition of Done:
- Slide 1 の `触れる` が `さわれる` と読まれるよう修正されている
- Slide 5 の `そうした方が` が `そうしたかたが` と読まれるよう修正されている
- VOICEVOXで該当スライドの音声を再生成している
- 全セグメントを同一音声仕様 AAC mono 44100 Hz で再生成している
- ffmpeg decode check が成功している
- faststart が適用されている
- Drive上の既存 `s1-l2.mp4` が同じURLのまま更新されている
- Drive file が `trashed: false` である
- 生成メディアはGit追跡しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 音声レビュー指摘は動画再生成前に台本へ反映する

# Blocking
Blocked By:
Notes:
- CEO確認により動画品質はOK。
- 音声レビューで発見した読み分けは `docs/VOICEVOX_RULES.md` と `tools/narration_checker.py` に反映済み。
