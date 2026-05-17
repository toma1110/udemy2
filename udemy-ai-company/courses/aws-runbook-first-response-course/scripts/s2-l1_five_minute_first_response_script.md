# s2-l1 CloudWatch Alarmから5分で確認すること

Course: `aws-runbook-first-response-course`

Segments: 8

## Slide 1: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

このレクチャーでは、クラウドウォッチアラームを受け取ったあと、最初の五分で確認することを整理します。障害対応では、最初の五分がとても重要です。ここで全部を調べようとすると、時間だけが過ぎます。逆に、確認する順番が決まっていれば、影響の有無、悪化しているか、誰へつなぐべきかを早く判断できます。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 1.

## Slide 2: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

最初に見るのは、アラームそのものです。どのアラームが、いつ、どの状態に変わったのかを確認します。アラーム名、対象サービス、セベリティ、しきいち、評価期間、直近の状態変化を見ます。ここで、通知文にオーナーやランブックが書かれていれば、対応の入口が明確になります。もし通知文が曖昧なら、その時点で記録して、後で改善対象にします。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 2.

## Slide 3: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

次に、ダッシュボードを見ます。単一メトリクスだけでは判断できないことが多いからです。エラー率が上がっているなら、レイテンシ、リクエスト数、依存先、キュー、スロットリングも一緒に見ます。レイテンシが悪化しているなら、ユーザー影響があるか、特定のエンドポイントだけか、全体かを見ます。ダッシュボードは、最初の五分で全体像をつかむための地図です。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 3.

## Slide 4: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

三つ目はログです。ただし、最初の五分ではログを深掘りしすぎません。見るべきなのは、エラーが増えた時刻、代表的なエラー文、対象リクエスト、影響範囲を示す情報です。ログ検索で原因を完全に特定しようとすると、時間が溶けます。まずは、ユーザー影響の有無と、次に見るべき方向を決めます。詳細調査は、その後に進めます。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 4.

## Slide 5: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

四つ目は直近デプロイです。多くの障害は、変更の直後に起きます。直近でアプリケーション、インフラ、設定、依存先、シークレット、権限が変わっていないかを確認します。もし時刻が一致しているなら、切り戻し準備や変更担当者への連絡が必要かもしれません。ただし、直近変更があるからといって必ず原因とは限りません。事実として時刻と内容を確認します。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 5.

## Slide 6: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

五つ目はエーダブリューエスヘルスや依存サービスです。自分たちのアプリケーションだけでなく、利用しているマネージドサービスや外部依存先に影響がないかを見ます。依存先の問題なら、自分たちで復旧できる範囲と、利用者への説明、代替経路、縮退運転の判断が必要になります。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 6.

## Slide 7: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

最後に、五分後の判断を決めます。影響なしなら監視を継続し、記録だけ残します。影響ありで原因候補が見えるなら、対応ランブックへ進みます。影響ありで原因候補が見えないなら、エスカレーションします。大切なのは、五分で完全な原因を出すことではありません。五分で次の行き先を決めることです。ランブックには、この順番を短く書いておきます。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 7.

## Slide 8: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

演習では、実際に受け取ったことがあるアラートを一つ思い出し、五分以内に見るものを五つだけ並べてください。全部を見るのではなく、影響、傾向、変更、ログ、依存先の順に絞ります。五分後に次の行動を決められるかが合格条件です。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 7. Exercise recap segment.

## Slide 9: CloudWatch Alarmから5分で確認すること

Message: Alarm、Dashboard、Logs、Deploy、AWS Healthを順番に見る

### Narration

実務メモとして、五分確認の結果は必ず一行で残します。影響あり、悪化中、直近デプロイあり、依存先異常なし、次は切り戻し確認、というように短く書きます。この一行があるだけで、あとから入ったメンバーも状況を追いやすくなります。

### Visual Notes

Five minute first response checklist from alarm to dashboard logs deploy health. Segment 7. Exercise recap segment. Practical memo segment.
