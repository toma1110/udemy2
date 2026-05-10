# AI制作会社 v1

このリポジトリは、AWS/SRE関連のUdemy講座をGitHub Issueベースで半自律的に量産するための「AI制作会社 v1」の運用土台です。

人間はCEOとして最終判断、承認、公開可否判断に集中し、AI社員が企画、実装、教材化、レビュー、進行管理をチケット駆動で進めます。

## 目的

- AWS/SRE関連のUdemy講座を継続的に制作する
- `course_spec.md` を唯一の真実として全AIが同じ前提で動く
- CloudFormationハンズオンをREADME通りに再現できる品質で提供する
- GPT-Image2によるスライドPNG、VOICEVOXによる音声、Google Drive一括アップロードを前提にする
- VOICEVOXの誤読、空白による不自然な間、英字残存を音声生成前にチェックする
- WorkerとReviewerを分離し、実装AIが自分でレビューしない運用にする

## 組織構成

| AI社員 | 役割 | 主な成果物 |
| --- | --- | --- |
| AI-Strategy-01 | 企画、講座設計、差別化 | course_spec.md、章立て、チケット案 |
| AI-Engineer-01 | CloudFormation実装、ハンズオン検証 | template.yaml、README、検証レポート |
| AI-Production-01 | 教材化、スライド、台本、音声素材 | slide PNG、script、VOICEVOX素材 |
| AI-QA-01 | 技術レビュー、教材レビュー、整合性レビュー | QAレポート、差戻しコメント |
| AI-Ops-01 | Issue監視、進捗管理、Blocked検知 | Issue更新、ラベル整理、進捗報告 |

## 基本ワークフロー

1. CEOが講座テーマまたは変更方針を決める
2. AI-Strategy-01が `course_spec.md` と作業チケットを作る
3. AI-Engineer-01がCloudFormationとハンズオンREADMEを実装する
4. AI-QA-01が技術レビューとREADME再現確認を行う
5. AI-Production-01がスライド、台本、音声、動画素材を作る
6. AI-QA-01が教材レビューを行う
7. CEOが公開承認する
8. AI-Ops-01がGoogle Driveアップロード、公開状態、分析レビューを管理する

## CEOの役割

- 講座テーマ、対象者、価格帯、公開可否を決める
- Change Requestの承認または却下を行う
- ブロッカー発生時に優先順位や方針を判断する
- 最終成果物の公開判断を行う

CEOは日々の実装詳細、レビュー詳細、進捗管理を直接担当しません。

## 最初の使い方

1. `courses/sample-aws-sre-course/course_spec.md` をコピーして新講座用の `course_spec.md` を作る
2. GitHub Issueの `Task` テンプレートで最初の作業チケットを作る
3. `Owner AI` と `Reviewer AI` を必ず別AIに設定する
4. `docs/QUALITY_GATE.md` を満たすまで `Ready for Publish` に進めない
5. 変更が必要な場合は `Change Request` テンプレートを使い、承認後に実装する
6. 台本を作ったら `python3 tools/narration_checker.py courses/<course>` を実行する

## GitHub Issueベース運用

- すべての作業はIssueから開始する
- 1チケットは1成果物に限定する
- チケットなしの実装、直接修正、口頭だけの変更は禁止する
- `Owner AI` が実装し、`Reviewer AI` がレビューする
- `Worker != Reviewer` を必須条件にする
- BlockedになったIssueはAI-Ops-01が検知し、CEOまたは該当AIへエスカレーションする

詳細は [docs/WORKFLOW.md](docs/WORKFLOW.md) と [docs/TASK_MANAGEMENT.md](docs/TASK_MANAGEMENT.md) を参照してください。
