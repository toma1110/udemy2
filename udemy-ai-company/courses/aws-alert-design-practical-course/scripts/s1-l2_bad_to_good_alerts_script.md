# s1-l2 悪いアラートを良いアラートへ直す

Course: `aws-alert-design-practical-course`

Segments: 7

## Slide 1: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

このレクチャーでは、悪いアラートを良いアラートへ直す練習をします。アラート設計で大切なのは、しきいちの数字を当てることだけではありません。通知を受け取った人が、影響を判断し、次の確認へ進めることです。まず悪い例を見ます。アラート名は、シーピーユー八十パーセント超過。本文は、インスタンスのシーピーユーが高いです。通知先は全員チャンネルです。この通知は一見すると監視しているように見えますが、実際には多くの情報が足りません。どのサービスなのか、ユーザー影響があるのか、今すぐ起きるべきなのか、誰が見るのか、何を確認するのかが分かりません。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 1.

## Slide 2: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

このような通知は、鳴った瞬間は目立ちます。しかし毎日何度も鳴ると、受け手はだんだん反応しなくなります。これがアラート疲れです。アラート疲れが起きると、本当に重要な通知まで流れてしまいます。悪いアラートを直す第一歩は、原因だけでなく影響を書くことです。シーピーユーが高い、という原因候補だけではなく、注文処理の遅延が増えている、ログイン失敗が増えている、バッチ処理が期限内に終わらない、といった利用者や業務への影響に寄せます。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 2.

## Slide 3: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

次に、誰が対応するかを書きます。全員へ通知すると、全員が見ているようで、誰も自分の仕事だと思わないことがあります。良いアラートには、オーナーが必要です。たとえば、決済サービスは決済チーム、認証サービスは認証チーム、共通基盤はプラットフォームチーム、というように担当を明確にします。担当が決まっていれば、通知先も絞れます。通知先を絞ることは、情報を隠すことではありません。一次対応する人へ早く届け、必要なときに広げるための設計です。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 3.

## Slide 4: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

三つ目は、ランブックです。ランブックがないアラートは、対応者の経験に依存します。経験のある人なら何とかできても、初めて当番に入った人は迷います。良い通知には、最初に見るダッシュボード、確認するログ、直近デプロイの見方、緩和策、エスカレーション先をつなげます。通知本文にすべてを書く必要はありません。リンクでも構いません。大切なのは、通知を見た瞬間に手順へ移れることです。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 4.

## Slide 5: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

では、悪い例を直します。悪い通知は、シーピーユー八十パーセント超過、だけでした。良い通知に直すなら、たとえば、決済エーピーアイのピーナインティナインレイテンシが五分間悪化し、注文完了までの時間が通常より遅くなっています。セベリティは中。オーナーは決済チーム。最初の五分では、ダッシュボードのレイテンシ、エラー率、直近デプロイ、依存先の状態を確認してください。十五分で改善しない場合はサービス責任者へ連絡してください、という形にします。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 5.

## Slide 6: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

ここで注意したいのは、通知文を長くすれば良いわけではないことです。良いアラートは、短くても判断に必要な情報が入っています。影響、オーナー、手順、エスカレーション。この四つをまず確認します。逆に、詳しいメトリクス名や内部実装の説明が長くても、次に何をするかが書かれていなければ、良いアラートとは言えません。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 6.

## Slide 7: 悪いアラートを良いアラートへ直す

Message: 曖昧な通知を、影響・Owner・Runbookつき通知へ変える

### Narration

最後にレビュー観点です。そのアラートを深夜三時に受け取ったと想像してください。自分が担当者でなくても、どのチームに渡すべきか分かるでしょうか。担当者なら、最初の五分で何を見るか分かるでしょうか。ユーザー影響があるか、まだ様子見でよいか、判断できるでしょうか。この問いに答えられるように、悪いアラートを良いアラートへ直していきます。

### Visual Notes

Bad CPU alert transformed into actionable alert with impact, owner, runbook, next action. Segment 7.
