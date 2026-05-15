# Task Summary
Task ID: TASK-0157
Title: 初回動画レビュー指摘の制作ルール反映状況を監査し、不足分を補強する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `udemy-ai-company/docs/VOICEVOX_RULES.md`
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`
- `udemy-ai-company/docs/PUBLIC_REPO_RULES.md`
- `udemy-ai-company/docs/QUALITY_GATE.md`
- `udemy-ai-company/docs/VIDEO_QUALITY_BASELINE.md`
- `udemy-ai-company/tools/narration_checker.py`
- `udemy-ai-company/tools/generate_voicevox_audio_local.py`
Dependencies:
- 初回動画レビュー指摘
- TASK-0155
- TASK-0156

# Deliverables
Expected Output:
- これまでの指摘がルール化されているかの監査結果
- 不足しているグローバル制作ルールの追記
- 量産時に同じ指摘が再発しないための品質ゲート補強

# Quality Gate
Definition of Done:
- 読み方指摘が `VOICEVOX_RULES.md` と音声生成/チェック系ツールに反映されている
- GPT-Image2由来PNG必須ルールが確認済み
- Public repo補助図解のGitHub表示ルールが明記されている
- Public repoに内部制作向け注意書きを出さないルールが明記されている
- ハンズオン再現性とREADME/CLI/動画手順一致が量産時の重点ゲートとして明記されている
- 過剰な単品磨き込みより量産へ進む判断基準が明記されている

# Constraints
Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- AWS課金リソース作成は行わない

# Blocking
Blocked By:
- none
Notes:
- 本チケットはルール文書の監査・軽微補強のみ。動画、音声、AWS環境の変更は行わない。
- Audit completed:
  - `初学者:しょがくしゃ`、`そんな方向け:そんなかたむけ`、人を指す `方:かた` は `VOICEVOX_RULES.md`、`narration_checker.py`、`generate_voicevox_audio_local.py` に反映済みであることを確認
  - GPT-Image2由来PNG必須、ローカル文字合成禁止、source evidence保存は `GPT_IMAGE_RULES.md`、`QUALITY_GATE.md`、`VIDEO_QUALITY_BASELINE.md` に反映済みであることを確認
  - Google Driveレビュー用アップロードは `GOOGLE_DRIVE_RULES.md` と `WORKFLOW.md` に反映済みであることを確認
- Rule updates completed:
  - `PUBLIC_REPO_RULES.md` に、README/CLI/補助ドキュメントと実テンプレートの整合、不要な手動 `git clone` 手順の禁止、draw.ioのPNG埋め込み、内部制作向け注意書きの非公開ルールを追加
  - `QUALITY_GATE.md` に、受講者レビュー指摘の横展開、Public repo図解/手順整合、量産判断のBlocking基準を追加
  - `VIDEO_QUALITY_BASELINE.md` に、過剰な単品磨き込みを避け、ハンズオン再現性を優先して量産へ進む判断基準を追加
  - `VOICEVOX_RULES.md` に、読み方指摘を個別修正で終わらせず、ルールとツールへ反映する運用を追加
- Verification completed:
  - `git diff --check` PASS
  - 反映キーワード検索で、該当ルールとツールへの記載を確認
