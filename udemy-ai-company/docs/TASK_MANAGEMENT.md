# TASK_MANAGEMENT

## 目的

GitHub Issueを制作会社の業務台帳として扱い、AIが半自律的に作業しても全体崩壊しない状態を保つ。

## 基本ルール

- すべての作業はIssueから開始する
- 1チケット1成果物にする
- `docs/MISSION_VISION_VALUES.md` と矛盾するチケットは開始しない
- Owner AIを必須にする
- Reviewer AIを必須にする
- Owner AIとReviewer AIは別AIにする
- `course_spec.md` と矛盾するチケットは開始しない
- 変更はChange Requestから開始する
- 自動実行したいIssueには `auto-execute` ラベルを付ける
- AWS課金につながる作業は `approval-required` とし、CEO承認後に `ceo-approved` を付ける
- AI-PM-01は `auto-execute` と承認状態を見て実行キューへ送る
- AI-PM-01はCEO承認待ち以外のOpen Issueを `done` にしてcloseする
- AI-Ops-01は定期監査でルール違反を検知し、監査Issueへ報告する
- AI-Ops-01は `pm`、`approval-required`、`blocked` の不足など低リスクなラベル補正だけ自動実行できる

## 1チケット1成果物

良い例:

- CloudFormationテンプレートを作成する
- ハンズオンREADMEを作成する
- 第1章スライドPNGを生成する
- 第1章台本を作成する

悪い例:

- 講座全体を完成させる
- AWS監視講座を全部作る
- いい感じに修正する

## Owner AI

Owner AIは成果物を作る責任を持つ。

Owner AIは以下を行う。

- 入力ファイルを確認する
- 成果物を作成する
- Definition of Doneを満たす証跡を残す
- Reviewer AIへレビュー依頼する

## AI-PM-01

AI-PM-01はIssue変更を検知し、実行してよいタスクだけをOwner AIへ渡す責任を持つ。

AI-PM-01は以下を行う。

- `auto-execute` ラベル付きIssueの更新を検知する
- Owner AIとReviewer AIが設定され、同一AIでないことを確認する
- `course_spec.md` と矛盾する可能性があるIssueをBlockedにする
- 課金影響があるIssueはCEO承認の有無を確認する
- 実行可能Issueを `.pm_queue/` にキュー化し、必要に応じてAI実行コマンドへ渡す
- 実行不可理由をIssueコメントに残す

AI-PM-01は実装担当でもレビュー担当でもない。成果物の作成はOwner AI、承認はReviewer AIが行う。

## Reviewer AI

Reviewer AIは成果物を承認または差戻しする責任を持つ。

Reviewer AIは以下を行う。

- `course_spec.md` との整合性を確認する
- 品質ゲートを確認する
- 実行確認または未実施理由を記録する
- 差戻し理由を具体的に書く

## AI-Ops-01 ルール監査

AI-Ops-01は `tools/rule_auditor.py` で、Issue運用が会社ルールに沿っているかを定期確認する。

監査で確認する項目:

- Owner AI と Reviewer AI が設定され、同一でない
- Definition of Done が記入されている
- Mission/Vision/Values Alignment が記入されている
- 講座成果物に関わるIssueが `course_spec.md` を参照している
- 課金影響があるIssueがCEO承認ゲートを通っている
- CEO承認待ち以外のOpen Issueが残っていない
- Blocked Issueに理由が記録されている

監査結果は `AI-Ops Rule Audit` Issueへコメントとして残す。AI-Ops-01は監査で検知した違反を勝手に実装、close、承認、公開しない。

## Blocked時の対応

IssueがBlockedになったら、AI-Ops-01が以下を記録する。

- Blocked理由
- 必要な判断者
- 影響範囲
- 次の確認期限

CEO判断が必要な場合は、Issueコメントで明確に依頼する。

CEO承認待ちとしてOpenに残すIssueには、`approval-required` と `blocked` を付ける。CEO承認待ちではないBlocked Issueは放置せず、AI-PM-01が自動クローズする。

## stale issue対応

7日以上更新がないIssueはAI-Ops-01が確認する。

- 継続する
- Blockedにする
- Closeする
- 別Issueに分割する

判断結果をIssueコメントに残す。

## GitHub labels案

部署:

- `strategy`
- `engineering`
- `production`
- `qa`
- `ops`

優先度:

- `high`
- `medium`
- `low`

状態:

- `blocked`
- `review`
- `ready`
- `done`

自動化:

- `pm`
- `rule-audit`
- `auto-execute`
- `approval-required`
- `ceo-approved`
- `pm-queued`
- `in-progress`

ラベル作成はGitHub CLIが使える環境で以下を実行する。

```bash
./scripts/create_github_labels.sh
```

## Issue本文の必須項目

- Task ID
- Title
- Department
- Owner AI
- Reviewer AI
- Priority
- Status
- Input Files
- Dependencies
- Expected Output
- Definition of Done
- Mission/Vision/Values Alignment
- Auto Execute
- Requires CEO Approval
- Cost Impact
- Blocked By

## 課金承認ルール

以下を含むIssueは、`ceo-approved` ラベルまたはIssue本文/コメントに明確なCEO承認があるまでAI-PM-01が自動実行しない。

- AWS環境構築
- CloudFormation stackのcreate、update、delete
- `aws cloudformation deploy`
- AWS Batch、Fargate、ECS、ECR、Lambda、VPC、RDS等の作成または更新
- S3、CloudWatch、SNS、IAM等のリソース作成または長時間利用
- コスト見積もりを超える可能性がある検証

承認待ちのIssueは `approval-required` と `blocked` を付け、CEOに判断を依頼する。

CEO承認済みになったIssueは承認待ちではないため、Openに残さない。承認内容を実行する場合は、別のTask Issueとして作成する。
