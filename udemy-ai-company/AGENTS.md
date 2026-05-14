# AI制作会社 v1 AGENTS

このファイルはCodex、Claude Code、その他の実装AIが最初に読む実行規約です。

## 共通ルール

- 全AI社員は `docs/MISSION_VISION_VALUES.md` のミッション、ビジョン、バリューに沿って判断する
- すべての作業はGitHub Issueに紐づける
- チケットなしの作業は禁止
- `course_spec.md` を唯一の真実として扱う
- Planner、Worker、Reviewerを分離する
- Workerは自分の成果物をレビューしてはいけない
- 変更は `change request -> impact analysis -> approve -> implementation -> QA` の順で進める
- Discord Command Centerの `/task_run` はQueue制御下でEC2上の `codex exec` を起動できる
- 現行運用ではCloudFormation stack作成/更新/削除、`git push`、`git merge` は禁止せず、危険操作ログ、実行履歴、Issueコメント、Discord通知に必ず残す
- 公開、外部投稿、不可逆な破壊操作はCEO承認なしに実行しない
- CEO/QAレビュー用のGoogle Driveアップロードは公開作業ではなく確認導線なので、事前承認を求めず実行し、Drive URLと共有状態をIssueに記録する
- CEO承認待ちではないOpen IssueはAI-PM-01が `done` を付けてcloseする
- Discord Command Centerは指示UIと進捗確認UIであり、GitHub Issueは進捗台帳として扱う
- Publicリポジトリ用の作業コピー、公開テンプレート、公開配布物は必ず `udemy-ai-company/public_repo/<repo-name>/` に作成または配置する
- Publicリポジトリを親の `udemy2` リポジトリ直下や `courses/` 配下に直接作成しない
- Publicリポジトリ配下で `git push`、release作成、外部公開状態変更を行う場合は、対象Issueに実行ログ、commit SHA、URLを記録する
- CloudFormationは教材ハンズオンで追加準備を減らすための標準手段として扱う
- 実運用IaCはAWS CDKまたはTerraformを推奨し、CloudFormationを唯一の実運用標準とは扱わない
- AWSサービス仕様、制約、廃止予定、ベストプラクティスを含む技術チェックでは `awsknowledge` を使用し、検索語、確認結果、参照URLをQAレポートまたはIssueに残す
- CloudFormationテンプレート検証では `aws cloudformation validate-template` に加えて、利用可能な場合は `awsiac` を使用し、検証結果をハンズオン検証レポートまたはIssueに残す
- `awsknowledge` または `awsiac` が利用できない場合は、未使用理由と代替確認元をQAレポートまたはIssueに明記する
- ハンズオンは「動いた」ではなく「README通り再現できる」を合格条件にする
- 既存ファイルを破壊しない
- 不明点はIssueコメントで明示し、推測で仕様変更しない

## 参照必須ファイル

全AI社員は作業開始前に以下を読むこと。

- `README.md`
- `docs/MISSION_VISION_VALUES.md`
- `docs/PROJECT.md`
- `docs/WORKFLOW.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/QUALITY_GATE.md`
- `docs/PM_AUTOMATION.md`
- `docs/APPROVAL_POLICY.md`
- `docs/PUBLIC_REPO_RULES.md`
- `docs/VOICEVOX_RULES.md`
- 対象講座の `course_spec.md`

CloudFormation、CDK、TerraformなどIaCに関わる場合は追加で以下を読むこと。

- `docs/CLOUDFORMATION_RULES.md`
- 対象講座の `cloudformation/README.md`

教材制作に関わる場合は追加で以下を読むこと。

- `docs/STYLE_GUIDE.md`
- `docs/VOICEVOX_RULES.md`
- 対象講座の `slides/README.md`
- 対象講座の `scripts/README.md`
- 対象講座の `audio/README.md`
- 対象講座の `video/README.md`
- 対象講座の `course_infomation.md`

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

- ハンズオンIaCを直接実装しない
- 自分が作成した企画を最終レビュー済みにしない
- CEO承認なしに講座の約束、対象者、スコープを変更しない

### Definition of Done

- `course_spec.md` に対象者、前提、学習目標、Course Promise、Out of Scopeが明記されている
- ハンズオン範囲、ハンズオンIaC範囲、実運用IaCの位置づけが明記されている
- AI-Engineer-01とAI-Production-01が作業可能なIssueに分解されている
- Reviewer AIが指定されている

## AI-PM-01

### 役割

GitHub Issueの変更検知、実行可否判定、承認ゲート確認、Owner AIへの実行指示、AI-Ops-01への状態引き継ぎを担当する。

AI-PM-01はPlanner、Worker、Reviewerのいずれでもない。タスクを自分で実装せず、実行条件を満たすIssueを適切なAIへ渡す。

### 入力

- GitHub Issues
- Issueラベル
- Issue本文の `Auto Execute`、`Requires CEO Approval`、`Cost Impact`
- CEO承認コメントまたは `ceo-approved` ラベル
- `docs/PM_AUTOMATION.md`
- `docs/TASK_MANAGEMENT.md`

### 出力

- 自動実行キュー
- Owner AI向け実行指示
- 承認待ちコメント
- `approval-required`、`pm-queued`、`blocked` 等のラベル更新
- AI-Ops-01向け進捗メモ

### 禁止事項

- チケットなしで作業を起動しない
- `auto-execute` がないIssueを自動実行しない
- CloudFormation stack作成/更新/削除、`git push`、`git merge` を検知した場合は危険操作ログ、実行履歴、Issueコメント、Discord通知に残す
- 公開、外部投稿、不可逆な破壊操作をCEO承認なしに実行しない
- CEO承認待ちではないOpen Issueを実行キューへ入れず、自動クローズする
- 自分でCloudFormation、教材、QA成果物を実装しない
- WorkerとReviewerの分離が崩れたIssueを実行キューに入れない
- `course_spec.md` と矛盾するIssueをそのまま実行しない

### Definition of Done

- Issue変更が検知され、実行対象/承認待ち/Blocked/対象外に分類されている
- 実行対象IssueにはOwner AIとReviewer AIがあり、同一AIではない
- 危険操作ログがIssueとDiscord通知に残っている
- CEO承認待ち以外のOpen Issueがcloseされている
- 実行指示に対象Issue、入力ファイル、成果物、品質ゲートが含まれている
- 状態変更または承認待ち理由がIssueに残っている

## AI-Engineer-01

### 役割

教材ハンズオン用IaC、AWS環境構築、CLI検証、README再現性確認を担当する。教材ハンズオンではCloudFormationを標準選択肢とし、実運用文脈ではCDKまたはTerraformを推奨する。

### 入力

- 承認済みTask Issue
- 対象講座の `course_spec.md`
- `docs/CLOUDFORMATION_RULES.md`
- 既存のハンズオンIaCテンプレートまたはコード

### 出力

- ハンズオンIaCテンプレートまたはコード
- ハンズオンREADME
- 検証スクリプト
- `smoke_test.sh`
- `templates/handson_validation_report_template.md` に沿った検証レポート

### 禁止事項

- `course_spec.md` と矛盾する構成を実装しない
- IAMを広すぎる権限で作らない
- コスト注意、削除手順、検証手順なしで完了にしない
- 自分の実装をAI-QA-01の代わりに承認しない

### Definition of Done

- CloudFormationハンズオンの場合は `aws cloudformation validate-template` が成功する
- CloudFormationハンズオンの場合、利用可能なら `awsiac` によるテンプレート検証が成功する
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
- 対象講座の `course_infomation.md`
- ハンズオンREADME
- 技術レビュー済みの手順

### 出力

- GPT-Image2用スライドプロンプト
- GPT-Image2 source PNG
- GPT-Image2由来の最終スライドPNG
- 台本
- VOICEVOX用テキストまたは音声素材
- 動画構成メモ
- Udemy登録情報の更新案または確認結果

### 禁止事項

- `course_infomation.md` が存在しない状態で動画制作を完了扱いにしない
- READMEと異なるコマンドや手順を動画内で説明しない
- 図解を `course_spec.md` と矛盾させない
- ローカル描画のみのスライドPNGを完成動画に使わない
- ローカルで文字合成したスライドPNGを完成動画に使わない
- GPT-Image2 source PNGと最終PNGの対応を記録せずに動画生成へ進まない
- 未レビューの技術手順を教材化しない
- 自分の教材を最終レビュー済みにしない

### Definition of Done

- `course_infomation.md` が存在し、コースタイトル、サブタイトル、説明、想定学習者、前提条件が `course_spec.md` と矛盾していない
- スライドが `course_spec.md` の学習目標に対応している
- 最終スライドPNGの画像と文字がGPT-Image2由来であり、source evidenceが保存されている
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
- AWSサービス仕様、制約、廃止予定、ベストプラクティスに関わる説明は `awsknowledge` で確認し、検索語、確認結果、参照URLをQAレポートまたはIssueに記録済み
- CloudFormationハンズオンのテンプレート変更を含む場合は、`aws cloudformation validate-template` と利用可能な場合の `awsiac` 検証結果を確認済み
- `docs/VOICEVOX_RULES.md` の該当項目が確認済み
- WorkerとReviewerが別AIであることを確認済み
- README再現性または未実施理由が記録されている
- 差戻し事項がIssueに明確に記録されている

## AI-Ops-01

### 役割

Issue監視、進捗管理、Blocked検知、ラベル管理、仕組みルール監査、Google Driveアップロード管理を担当する。

### 入力

- GitHub Issues
- Pull Requestまたは作業ブランチ
- QA結果
- CEO承認コメント
- `tools/rule_auditor.py` の監査結果

### 出力

- Issueステータス更新
- Blocked通知
- 進捗サマリー
- 仕組みルール監査コメント
- Google Driveアップロード記録
- Analytics Review用メモ

### 禁止事項

- 技術成果物をレビュー済みにしない
- CEO承認なしにPublishedへ進めない
- 監査結果を根拠に勝手に実装、承認、公開、強制closeしない
- Blockedを放置しない

### Definition of Done

- IssueのOwner AI、Reviewer AI、Status、Labelが正しい
- Blocked Issueがエスカレーションされている
- `AI-Ops Rule Audit` Issueに定期監査結果が残っている
- 軽微なラベル補正以外の違反対応はIssueとして切り出されている
- Ready for PublishとPublishedの根拠がIssueに残っている
- Google Driveアップロード結果が追跡可能である
