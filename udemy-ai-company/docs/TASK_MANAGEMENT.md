# TASK_MANAGEMENT

## 目的

GitHub Issueを制作会社の業務台帳として扱い、AIが半自律的に作業しても全体崩壊しない状態を保つ。

## 基本ルール

- すべての作業はIssueから開始する
- 1チケット1成果物にする
- Owner AIを必須にする
- Reviewer AIを必須にする
- Owner AIとReviewer AIは別AIにする
- `course_spec.md` と矛盾するチケットは開始しない
- 変更はChange Requestから開始する

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

## Reviewer AI

Reviewer AIは成果物を承認または差戻しする責任を持つ。

Reviewer AIは以下を行う。

- `course_spec.md` との整合性を確認する
- 品質ゲートを確認する
- 実行確認または未実施理由を記録する
- 差戻し理由を具体的に書く

## Blocked時の対応

IssueがBlockedになったら、AI-Ops-01が以下を記録する。

- Blocked理由
- 必要な判断者
- 影響範囲
- 次の確認期限

CEO判断が必要な場合は、Issueコメントで明確に依頼する。

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
- Blocked By
