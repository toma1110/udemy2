# PM_AUTOMATION

AI-PM-01はGitHub Issueの変更を検知し、実行可能なチケットだけをOwner AIへ渡す。

PMは実装者でもレビュアーでもない。実行可否、承認ゲート、キュー投入、状態通知を担当する。

## 目的

- GitHub Issueの更新を定期的に検知する
- `auto-execute` ラベル付きIssueだけを自動実行対象にする
- Owner AIとReviewer AIの分離を確認する
- AWS課金につながる作業をCEO承認なしに実行しない
- CEO承認待ちではないOpen Issueを自動クローズする
- 実行指示を `.pm_queue/` に残し、必要に応じてAI実行コマンドへ渡す
- AI-Ops-01が仕組みルールの整合性を定期監査できる状態にする

## 役割分担

| 領域 | 担当 |
| --- | --- |
| Issue変更検知 | AI-PM-01 |
| 実行可否判定 | AI-PM-01 |
| 課金承認判断 | CEO |
| 成果物の実装 | Owner AI |
| 成果物のレビュー | Reviewer AI |
| 進捗・Blocked管理 | AI-Ops-01 |
| 仕組みルール監査 | AI-Ops-01 |

## Issue自動クローズ方針

AI-PM-01は、Open Issueを「CEO承認待ち」と「それ以外」に分ける。

以下のいずれかに該当し、まだCEO承認済みではないIssueだけをOpenのまま残す。

- `approval-required` ラベルがある
- `Requires CEO Approval:` が `yes` である
- `CEO Approval:` 欄があり、未承認である
- AWS課金、CloudFormation stack作成/更新/削除、Fargate/Batch/ECR等の課金影響がある
- タイトルまたは本文に `CEO承認待ち`、`CEO確認待ち`、`公開承認待ち`、`Ready for Publish` 等がある

上記以外のOpen Issueは、AI-PM-01が `done` ラベルを付けてcloseする。

CEO承認済みのIssueは「承認待ち」ではないため、Openに残さずcloseする。承認後に作業が必要な場合は、承認済みの内容をもとに新しいTask Issueを作る。

## 自動実行対象

以下をすべて満たすIssueだけを自動実行する。

- Open Issueである
- `auto-execute` ラベルがある、または本文の `Auto Execute:` が `yes` である
- コメントに `/auto-execute` または `/pm-run` がある
- `blocked`、`done`、`pm-queued`、`in-progress` が付いていない
- Owner AIとReviewer AIが設定されている
- Owner AIとReviewer AIが同一ではない
- `course_spec.md` と矛盾する明確な記述がない
- 課金影響がある場合はCEO承認済みである

## CEO承認が必要な作業

以下に該当するIssueは、AI-PM-01が自動実行を止める。

- AWS環境構築
- CloudFormation stackのcreate、update、delete
- `aws cloudformation deploy`
- AWS Batch、Fargate、ECS、ECR、Lambda、VPC、RDS等の作成または更新
- S3、CloudWatch、SNS、IAM等のリソース作成または長時間利用
- コスト見積もりを超える可能性がある検証

承認する場合は、Issueに `ceo-approved` ラベルを付ける。コメントで承認する場合は `/approve-cost` を含める。

## コメントコマンド

CEOはIssue本文の細かい項目をすべて埋めなくてもよい。PMがIssueタイトル、本文、コメントから担当AIを推定する。

- `/auto-execute`: 自動実行対象にする
- `/pm-run`: 自動実行対象にする
- `/pm-breakdown`: 大きい依頼を子チケットへ分解する
- `/breakdown`: 大きい依頼を子チケットへ分解する
- `/approve-cost`: AWS課金影響がある作業を承認する

担当AIの推定ルール:

- 動画、スライド、VOICEVOX、GPT-Image2、台本、音声: `AI-Production-01` -> `AI-QA-01`
- CloudFormation、AWS Batch、Fargate、ECR、ハンズオン、環境構築: `AI-Engineer-01` -> `AI-QA-01`
- QA、レビュー、確認待ち、品質: `AI-QA-01` -> `AI-Ops-01`
- course_spec、企画、章立て、学習目標: `AI-Strategy-01` -> `AI-QA-01`

## ラベル

- `pm`: PM管理対象
- `rule-audit`: AI-Ops-01による仕組みルール監査
- `auto-execute`: AI-PM-01による自動実行対象
- `pm-parent`: PMが子チケットへ分解した親Issue
- `pm-child`: PMが親Issueから作成した子Issue
- `needs-breakdown`: 分解に必要な情報が不足
- `feedback`: CEOフィードバック対応
- `approval-required`: CEO承認が必要
- `ceo-approved`: CEO承認済み
- `pm-queued`: PMが実行キューへ投入済み
- `in-progress`: 作業中
- `blocked`: 実行停止中

ラベルは以下で作成または更新する。

```bash
./scripts/create_github_labels.sh
```

## ウォッチャー

Issue監視は `tools/pm_issue_watcher.py` を使う。

初回は既存Issueを一斉実行しないため、ベースラインだけを作る。

```bash
python3 tools/pm_issue_watcher.py --baseline
```

1回だけ検知して、実行可能Issueをキュー化する。

```bash
python3 tools/pm_issue_watcher.py --apply
```

CEO承認待ち以外のOpen Issueも同時にクローズする。

```bash
python3 tools/pm_issue_watcher.py --apply --close-non-approval
```

60秒ごとに監視する。

```bash
python3 tools/pm_issue_watcher.py --apply --close-non-approval --poll-seconds 60
```

AI実行コマンドへ渡す場合は、標準入力でプロンプトを受け取れるコマンドを指定する。

```bash
python3 tools/pm_issue_watcher.py --apply --close-non-approval --execute --executor "codex exec"
```

`scripts/run_pm_watcher.sh` から起動する場合、`PM_WATCHER_CLOSE_NON_APPROVAL` はデフォルトで有効である。無効化する場合だけ `PM_WATCHER_CLOSE_NON_APPROVAL=0` を指定する。

## systemd自動起動

サーバー再起動時に監視を自動起動する場合は、systemdサービスを使う。

```bash
sudo install -m 0644 infrastructure/systemd/udemy-ai-pm-watcher.service /etc/systemd/system/udemy-ai-pm-watcher.service
sudo systemctl daemon-reload
sudo systemctl enable --now udemy-ai-pm-watcher.service
```

状態確認:

```bash
systemctl status udemy-ai-pm-watcher.service
journalctl -u udemy-ai-pm-watcher.service -n 100 --no-pager
```

## 実行キュー

AI-PM-01は実行可能Issueごとに `.pm_queue/issue-<number>.md` を作る。

このファイルには以下を含める。

- Issue番号
- Issue URL
- Owner AI
- Reviewer AI
- 入力ファイル
- 成果物
- Definition of Done
- 承認状態
- 実行時の注意

`.pm_queue/` と `.pm_state/` はローカル運用状態であり、Git管理対象にしない。

## 仕組みルール監査

AI-Ops-01は `tools/rule_auditor.py` を使い、Issue運用とドキュメントの整合性を定期チェックする。

監査対象:

- Owner AI / Reviewer AI の存在と分離
- Definition of Done と Mission/Vision/Values Alignment の記入
- 課金影響IssueのCEO承認ゲート
- CEO承認待ち以外のOpen Issueが残っていないか
- Blocked Issueの理由記録
- `AGENTS.md`、`PM_AUTOMATION.md`、Taskテンプレートの必須ルール参照

監査は報告と軽修正に限定する。`pm` ラベル不足、CEO承認待ちIssueの `approval-required` / `blocked` 不足だけを自動補正し、Issue close、実行開始、CEO承認、成果物変更は行わない。

dry-run:

```bash
python3 tools/rule_auditor.py --repo toma1110/udemy2
```

GitHub上の単一監査Issueへ記録し、低リスクなラベル補正を行う:

```bash
python3 tools/rule_auditor.py --repo toma1110/udemy2 --apply
```

標準起動スクリプト:

```bash
./scripts/run_rule_auditor.sh
```

`scripts/run_rule_auditor.sh` は `RULE_AUDITOR_APPLY=1` をデフォルトとし、監査Issue `AI-Ops Rule Audit` に結果をコメントする。dry-runだけ行う場合は `RULE_AUDITOR_APPLY=0` を指定する。

## 大きい依頼の分解

AI-PM-01は、`s6動画作成`、`Section 7の動画をまとめて作成` のような大きい依頼を検知した場合、親Issueを直接executorへ渡さず、子チケットを作成する。

標準分解:

- 各Lectureの動画制作チケット
- Section全体の完了QAチケット

親Issueには `pm-parent` と `pm-queued` を付け、子Issueには `pm-child` を付ける。課金承認済みの親Issueから作成した子Issueには `ceo-approved` を引き継ぐ。

Section番号を特定できない場合は `needs-breakdown` と `blocked` を付ける。CEOは `s6`、`Section 6` のように追記すればよい。

## レビューIssueのコメント対応

`review` ラベル付きIssueでは、CEOコメントに次のような語が含まれる場合、PMがフィードバック対応チケットを作成する。

- お願いします
- 修正
- 追加
- 作り直し
- 気になる
- 読み方
- ルール

`クローズしてください` または `/close` が含まれる場合は、PMがIssueを `done` にしてcloseする。

## 失敗時の扱い

AI-PM-01は以下の場合に自動実行しない。

- GitHub CLIが未認証
- Issue本文からOwner AIまたはReviewer AIを判定できない
- Owner AIとReviewer AIが同じ
- 課金影響があるがCEO承認がない
- `blocked`、`done`、`pm-queued`、`in-progress` ラベルがある

実行しない理由はIssueコメントまたは標準出力に残す。

`--close-non-approval` が有効な場合、上記の実行可否判定より前にOpen Issueの整理を行う。CEO承認待ちではないIssueは実行キューへ送らず、`done` を付けてcloseする。
