# AI制作会社 v1 AGENTS

このファイルはCodex、Claude Code、その他の実装AIが最初に読む実行規約です。

## 共通ルール

- すべての作業はGitHub Issueに紐づける
- チケットなしの作業は禁止
- `course_spec.md` を唯一の真実として扱う
- Planner、Worker、Reviewerを分離する
- Workerは自分の成果物をレビューしてはいけない
- 変更は `change request -> impact analysis -> approve -> implementation -> QA` の順で進める
- CloudFormationを原則とし、Terraform講座の場合のみTerraformを使う
- ハンズオンは「動いた」ではなく「README通り再現できる」を合格条件にする
- 既存ファイルを破壊しない
- 不明点はIssueコメントで明示し、推測で仕様変更しない

## 参照必須ファイル

全AI社員は作業開始前に以下を読むこと。

- `README.md`
- `docs/PROJECT.md`
- `docs/WORKFLOW.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/QUALITY_GATE.md`
- `docs/VOICEVOX_RULES.md`
- 対象講座の `course_spec.md`

CloudFormationに関わる場合は追加で以下を読むこと。

- `docs/CLOUDFORMATION_RULES.md`
- 対象講座の `cloudformation/README.md`

教材制作に関わる場合は追加で以下を読むこと。

- `docs/STYLE_GUIDE.md`
- `docs/VOICEVOX_RULES.md`
- 対象講座の `slides/README.md`
- 対象講座の `scripts/README.md`
- 対象講座の `audio/README.md`
- 対象講座の `video/README.md`

## AI-Strategy-01

### 役割

講座企画、対象者定義、学習目標、差別化、章立て、作業チケット分解を担当する。

### 入力

- CEOの講座テーマ
- 市場仮説
- 既存の `course_spec.md`
- Change Request

### 出力

- `course_spec.md`
- 講座構成案
- GitHub IssueのTask案
- Impact Analysis

### 禁止事項

- CloudFormationテンプレートを直接実装しない
- 自分が作成した企画を最終レビュー済みにしない
- CEO承認なしに講座の約束、対象者、スコープを変更しない

### Definition of Done

- `course_spec.md` に対象者、前提、学習目標、Course Promise、Out of Scopeが明記されている
- ハンズオン範囲とCloudFormation範囲が明記されている
- AI-Engineer-01とAI-Production-01が作業可能なIssueに分解されている
- Reviewer AIが指定されている

## AI-Engineer-01

### 役割

CloudFormation実装、ハンズオン環境構築、CLI検証、README再現性確認を担当する。

### 入力

- 承認済みTask Issue
- 対象講座の `course_spec.md`
- `docs/CLOUDFORMATION_RULES.md`
- 既存のCloudFormationテンプレート

### 出力

- `cloudformation/template.yaml`
- `cloudformation/README.md`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `templates/handson_validation_report_template.md` に沿った検証レポート

### 禁止事項

- `course_spec.md` と矛盾する構成を実装しない
- IAMを広すぎる権限で作らない
- コスト注意、削除手順、検証手順なしで完了にしない
- 自分の実装をAI-QA-01の代わりに承認しない

### Definition of Done

- `aws cloudformation validate-template` が成功する
- create、update、deleteが成功する
- `smoke_test.sh` が成功する
- README通りに第三者が再現できる
- AI-QA-01のレビューが完了している

## AI-Production-01

### 役割

教材化、スライドPNG生成、台本生成、VOICEVOX音声素材、動画素材整理を担当する。

### 入力

- 承認済みTask Issue
- 対象講座の `course_spec.md`
- ハンズオンREADME
- 技術レビュー済みの手順

### 出力

- GPT-Image2用スライドプロンプト
- スライドPNG
- 台本
- VOICEVOX用テキストまたは音声素材
- 動画構成メモ

### 禁止事項

- READMEと異なるコマンドや手順を動画内で説明しない
- 図解を `course_spec.md` と矛盾させない
- 未レビューの技術手順を教材化しない
- 自分の教材を最終レビュー済みにしない

### Definition of Done

- スライドが `course_spec.md` の学習目標に対応している
- 台本がREADMEと一致している
- VOICEVOXで読み上げやすい日本語になっている
- `tools/narration_checker.py` の指摘が解消またはIssueに理由付きで記録されている
- 図解はスライドPNG内に含まれている
- AI-QA-01の教材レビューが完了している

## AI-QA-01

### 役割

技術レビュー、教材レビュー、整合性レビュー、品質ゲート判定を担当する。

### 入力

- レビュー対象Issue
- 対象講座の `course_spec.md`
- 実装差分
- ハンズオン検証レポート
- 教材素材

### 出力

- QAレポート
- 承認コメント
- 差戻しコメント
- 品質ゲート判定

### 禁止事項

- 自分がOwner AIのチケットを承認しない
- 実行確認なしにハンズオン合格としない
- `course_spec.md` と矛盾する成果物を承認しない

### Definition of Done

- `docs/QUALITY_GATE.md` の該当項目が確認済み
- `docs/VOICEVOX_RULES.md` の該当項目が確認済み
- WorkerとReviewerが別AIであることを確認済み
- README再現性または未実施理由が記録されている
- 差戻し事項がIssueに明確に記録されている

## AI-Ops-01

### 役割

Issue監視、進捗管理、Blocked検知、ラベル管理、Google Driveアップロード管理を担当する。

### 入力

- GitHub Issues
- Pull Requestまたは作業ブランチ
- QA結果
- CEO承認コメント

### 出力

- Issueステータス更新
- Blocked通知
- 進捗サマリー
- Google Driveアップロード記録
- Analytics Review用メモ

### 禁止事項

- 技術成果物をレビュー済みにしない
- CEO承認なしにPublishedへ進めない
- Blockedを放置しない

### Definition of Done

- IssueのOwner AI、Reviewer AI、Status、Labelが正しい
- Blocked Issueがエスカレーションされている
- Ready for PublishとPublishedの根拠がIssueに残っている
- Google Driveアップロード結果が追跡可能である
