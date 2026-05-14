# AI制作会社 v1

このリポジトリは、AWS/SRE関連のUdemy講座をGitHub Issueベースで半自律的に量産するための「AI制作会社 v1」の運用土台です。

人間はCEOとして最終判断、承認、公開可否判断に集中し、AI社員が企画、実装、教材化、レビュー、進行管理をチケット駆動で進めます。

## ミッション・ビジョン・バリュー

全AI社員の共通判断基準は [docs/MISSION_VISION_VALUES.md](docs/MISSION_VISION_VALUES.md) に定義します。

- ミッション: AWS/SREの実務知識を、初学者がREADME通りに再現できる動画教材へ変換し、現場で使えるクラウド運用力を継続的に届ける
- ビジョン: CEOの最終判断とAI社員の専門分業により、AWS/SRE教育を継続的に生み出す、再現可能なAI教材制作ラインを作る
- バリュー: 受講者の再現性、Source of Truth、チケット透明性、分業品質、検証、コスト安全、初学者へのわかりやすさ、仕組みによる制作品質を重視する

## 目的

- AWS/SRE関連のUdemy講座を継続的に制作する
- `course_spec.md` を唯一の真実として全AIが同じ前提で動く
- 教材ハンズオンではCloudFormationを使い、README通りに再現できる品質で提供する
- 実運用IaCはCDKまたはTerraformを推奨し、教材内でもその位置づけを明記する
- GPT-Image2によるスライドPNG、VOICEVOXによる音声、Google Drive一括アップロードを前提にする
- 完成動画に使う最終スライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示する文字もGPT-Image2生成を必須にする
- VOICEVOXの誤読、空白による不自然な間、英字残存を音声生成前にチェックする
- WorkerとReviewerを分離し、実装AIが自分でレビューしない運用にする
- Publicリポジトリ用の作業コピーは `public_repo/<repo-name>/` に集約する

## 組織構成

| AI社員 | 役割 | 主な成果物 |
| --- | --- | --- |
| AI-Strategy-01 | 企画、講座設計、差別化 | course_spec.md、章立て、チケット案 |
| AI-PM-01 | Issue変更検知、実行可否判定、AIタスク起動 | 自動実行キュー、承認待ち通知、実行指示 |
| AI-Engineer-01 | ハンズオンIaC実装、AWS検証 | template.yamlまたはIaCコード、README、検証レポート |
| AI-Production-01 | 教材化、スライド、台本、音声素材 | slide PNG、script、VOICEVOX素材 |
| AI-QA-01 | 技術レビュー、教材レビュー、整合性レビュー | QAレポート、差戻しコメント |
| AI-Ops-01 | Issue監視、進捗管理、Blocked検知 | Issue更新、ラベル整理、進捗報告 |

## 基本ワークフロー

1. CEOが講座テーマまたは変更方針を決める
2. AI-Strategy-01が `course_spec.md`、`lectures.md`、`course_curriculum.md` と作業チケットを作る
3. AI-PM-01がIssueの変更を検知し、実行可能なチケットをキュー化する
4. 課金影響があるAWS環境構築、CloudFormation stack作成/更新/削除、Fargate/Batch/ECR等の実行はCEO承認後にだけ開始する
5. AI-Engineer-01がハンズオンIaCとREADMEを実装する
6. AI-QA-01が技術レビューとREADME再現確認を行う
7. AI-Production-01がスライド、台本、音声、動画素材を作る
8. AI-QA-01が教材レビューを行う
9. AI-Ops-01がCEO/QA確認用にGoogle Driveへアップロードし、IssueへURLを記録する
10. CEOがDrive URLで確認し、公開可否を判断する
11. AI-Ops-01が公開状態、Google Drive記録、分析レビューを管理する

## CEOの役割

- 講座テーマ、対象者、価格帯、公開可否を決める
- Change Requestの承認または却下を行う
- AWS課金につながる環境構築、デプロイ、stack作成/更新/削除、Fargate/Batch/ECR等の実行可否を承認する
- ブロッカー発生時に優先順位や方針を判断する
- 最終成果物の公開判断を行う

CEOは日々の実装詳細、レビュー詳細、進捗管理を直接担当しません。

## 最初の使い方

1. `courses/sample-aws-sre-course/course_spec.md` をコピーして新講座用の `course_spec.md` を作る
2. `templates/course_curriculum_template.md` をコピーして新講座用の `course_curriculum.md` を作る
3. GitHub Issueの `Task` テンプレートで最初の作業チケットを作る
4. `Owner AI` と `Reviewer AI` を必ず別AIに設定する
5. `docs/QUALITY_GATE.md` を満たすまで `Ready for Publish` に進めない
6. 変更が必要な場合は `Change Request` テンプレートを使い、承認後に実装する
7. 台本を作ったら `python3 tools/narration_checker.py courses/<course>` を実行する
8. GitHub Issue自動検知を使う場合は、初回に `python3 tools/pm_issue_watcher.py --baseline` で現在状態を記録する
9. 自動実行したいIssueには `auto-execute` ラベルを付け、課金影響がある場合はCEO承認後に `ceo-approved` ラベルを付ける

## GitHub Issueベース運用

- すべての作業はIssueから開始する
- 1チケットは1成果物に限定する
- チケットなしの実装、直接修正、口頭だけの変更は禁止する
- `Owner AI` が実装し、`Reviewer AI` がレビューする
- `Worker != Reviewer` を必須条件にする
- 動画制作は `docs/GPT_IMAGE_RULES.md` と `docs/VIDEO_QUALITY_BASELINE.md` に従い、ローカル描画のみ、またはローカル文字合成したスライドを完成動画に使わない
- AI-PM-01は `auto-execute` Issueだけを自動実行対象にし、課金影響があるIssueは `ceo-approved` が付くまで停止する
- BlockedになったIssueはAI-Ops-01が検知し、CEOまたは該当AIへエスカレーションする

詳細は [docs/MISSION_VISION_VALUES.md](docs/MISSION_VISION_VALUES.md)、[docs/WORKFLOW.md](docs/WORKFLOW.md)、[docs/TASK_MANAGEMENT.md](docs/TASK_MANAGEMENT.md)、[docs/PM_AUTOMATION.md](docs/PM_AUTOMATION.md) を参照してください。

## カリキュラム管理

各講座には `course_curriculum.md` を作成し、セクション番号、レクチャー番号、レクチャータイトル、レクチャー完了後に身についていること、ハンズオン有無を記録します。ハンズオンがあるレクチャーではPublicRepo URLを必ず記載します。

詳細は [docs/CURRICULUM_RULES.md](docs/CURRICULUM_RULES.md) を参照してください。

## Publicリポジトリ運用

Publicリポジトリ用のフォルダは必ず `public_repo/<repo-name>/` に作成します。例: `public_repo/sre-slo-introduction-cfn-templates`。

`courses/` には講座のSource of Truth、制作素材、QAレポートを置き、Publicリポジトリそのものは置きません。公開用リポジトリへ反映する場合は、対象Issueにcommit SHA、公開URL、検証結果を記録します。

詳細は [docs/PUBLIC_REPO_RULES.md](docs/PUBLIC_REPO_RULES.md) を参照してください。
