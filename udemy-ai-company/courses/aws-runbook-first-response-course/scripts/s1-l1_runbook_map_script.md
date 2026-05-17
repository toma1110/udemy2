# s1-l1 Script: Runbookに何を書くか

Course: `aws-runbook-first-response-course`
Lecture: `s1-l1`
Target length: 8-10 minutes

## Slide 1

### Slide Title

障害対応Runbook入門

### Slide Message

アラートから初動対応へ

### Narration

このレクチャーでは、障害対応ランブックに何を書くべきかを整理します。アラートが鳴ったあと、何を見るか、誰が動くか、いつエスカレーションするか。この三つが曖昧だと、対応は担当者の記憶に依存します。ランブックは、その迷いを減らすための手順書です。

### Visual Notes

- CloudWatch alert leading into a runbook workflow
- On-call engineer with clear steps

## Slide 2

### Slide Title

Runbookとは

### Slide Message

特定の結果へ進む手順

### Narration

ランブックは、特定の結果を得るための手順です。たとえば、注文エーピーアイのエラー率が上がったとき、影響を確認し、ログを見て、必要なら切り戻し準備をして、関係者へ連絡する。誰が実行しても、だいたい同じ結果へ進めることが目的です。

### Visual Notes

- Step-by-step operational procedure
- Desired outcome at the end

## Slide 3

### Slide Title

最初に書く5項目

### Slide Message

Trigger / Owner / Severity / Scope / Goal

### Narration

まず書くべき項目は五つです。トリガー、オーナー、セベリティ、スコープ、ゴールです。何が起きたら使うのか。誰が担当するのか。どれくらい急ぐのか。どのサービスやユーザーに影響するのか。最終的にどの状態へ戻したいのか。ここが未記入だと、手順を読んでも動けません。

### Visual Notes

- Five fields on a runbook header card
- Missing fields highlighted as risk

## Slide 4

### Slide Title

初動確認

### Slide Message

5分以内に見るものを絞る

### Narration

次に、初動確認を短く書きます。アラームの発火時刻、ユーザー影響、ダッシュボードの傾向、直近デプロイ、関連ログ、エーダブリューエスヘルス。ここで大切なのは、全部を調べようとしないことです。最初の5分で見るものだけに絞ると、焦っているときでも手順を追えます。

### Visual Notes

- Five-minute checklist
- Alarm time, impact, dashboard, deploy, logs, AWS Health

## Slide 5

### Slide Title

緩和策

### Slide Message

調査と復旧を分ける

### Narration

ランブックでは、調査と復旧を分けます。原因を完全に特定する前でも、ユーザー影響を小さくする緩和策が必要な場合があります。たとえば、直近デプロイが怪しいなら切り戻しを準備する。依存先が不安定なら一時的な縮退運転に切り替える。実行に承認が必要な操作は、必ず条件と承認者を書きます。

### Visual Notes

- Split path: investigate vs mitigate
- Rollback, feature flag, degraded mode

## Slide 6

### Slide Title

エスカレーション

### Slide Message

15分で次へつなぐ

### Narration

エスカレーション条件も、あらかじめ書いておきます。たとえば、5分で影響確認、15分でサービス責任者へ連絡、30分でインシデントチャンネルを開く。時間で区切ると、抱え込みを防げます。誰へ、どの情報を、どのチャンネルで渡すかまで書くと、引き継ぎが速くなります。

### Visual Notes

- Timeline: 5 minutes, 15 minutes, 30 minutes
- Handoff to service lead and incident channel

## Slide 7

### Slide Title

連絡と記録

### Slide Message

対応を後から追える形にする

### Narration

障害対応では、直すことだけでなく、連絡と記録も重要です。社内の更新先、ステークホルダーへの説明、必要なら利用者向け告知、復旧確認、そしてポストモーテムへのリンク。何を判断し、何を実行したかが残っていれば、後から改善できます。

### Visual Notes

- Communication board and timeline log
- Postmortem link at the end

## Slide 8

### Slide Title

Runbookは育てる

### Slide Message

使ったあとに更新する

### Narration

まとめです。ランブックは、一度書いて終わりではありません。アラートが変わったとき、ダッシュボードが変わったとき、障害対応で迷ったとき、必ず更新します。最初はマークダウンの手順書で十分です。よく使う手順から少しずつ自動化し、チームで使える運用品質へ育てていきましょう。

### Visual Notes

- Continuous improvement loop
- Markdown runbook to automation maturity path
