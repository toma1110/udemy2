# s3-l1 Mitigation、Rollback、Escalationを決める

Course: `aws-runbook-first-response-course`

Segments: 8

## Slide 1: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

このレクチャーでは、ミティゲーション、ロールバック、エスカレーションをランブックにどう書くかを学びます。障害対応では、原因を完全に特定する前でも、ユーザー影響を小さくする判断が必要なことがあります。ミティゲーションは影響を減らすこと、ロールバックは変更を戻すこと、エスカレーションは適切な人やチームへ引き継ぐことです。この三つを分けて書くと、焦っているときでも判断しやすくなります。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 1.

## Slide 2: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

まずミティゲーションです。ミティゲーションは、根本解決ではなく、影響を小さくするための一時対応です。たとえば、問題のある機能を一時停止する、読み取り専用モードにする、トラフィックを減らす、キュー処理を遅らせる、依存先への呼び出しを制限する、などがあります。大切なのは、その操作が何を守るためのものかを書くことです。ユーザー影響を減らすのか、データ破損を防ぐのか、コスト増加を止めるのかで判断が変わります。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 2.

## Slide 3: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

次にロールバックです。直近デプロイや設定変更が原因候補なら、切り戻しを検討します。ただし、切り戻しは安全とは限りません。データベースの変更、移行処理、外部連携、キャッシュ、メッセージキューが関係している場合、単純に戻すと別の問題が起きることがあります。ランブックには、切り戻し可能な条件、必要な承認、実行手順、戻した後の確認項目、失敗した場合の対応を書きます。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 3.

## Slide 4: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

三つ目はエスカレーションです。担当者が一人で抱え込むと、判断が遅れます。エスカレーション条件は、時間、影響、権限、専門性で決めます。五分で影響確認できない、十五分で改善しない、複数サービスへ広がっている、本番変更の承認が必要、データ影響が疑われる、こうした条件では次へつなぎます。誰へ、どのチャンネルで、何を伝えるかまで書くと、引き継ぎが速くなります。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 4.

## Slide 5: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

ランブックでは、ミティゲーション、ロールバック、エスカレーションを同じ場所に混ぜない方が読みやすくなります。最初に影響を減らす選択肢、次に変更を戻す選択肢、最後に引き継ぎ条件、という順にすると、対応者は状況に合わせて選べます。また、それぞれの手順に、実行してよい人、承認が必要な人、実行後に見るメトリクスを書きます。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 5.

## Slide 6: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

危険な操作には必ずガードを付けます。本番データを変更する、リソースを削除する、大量のトラフィックを切り替える、課金影響が大きい操作をする。このような手順は、初動担当者が単独で実行しないようにします。ランブックは自動実行ボタンではありません。安全に判断するための手順です。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 6.

## Slide 7: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

最後に、レビュー観点です。その緩和策は、何の影響を減らすためのものですか。切り戻しは本当に安全ですか。承認者は明確ですか。十五分、三十分で誰へつなぐか決まっていますか。実行後に成功を判断するメトリクスはありますか。ミティゲーション、ロールバック、エスカレーションを分けて書くことで、初動対応は安全で再現しやすくなります。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 7.

## Slide 8: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

演習では、緩和、切り戻し、エスカレーションを三つの欄に分けて書いてください。実行できる人、承認が必要な人、実行後に見るメトリクスも添えます。この分離があると、焦って危険な操作を選ぶリスクを下げられます。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 7. Exercise recap segment.

## Slide 9: Mitigation、Rollback、Escalationを決める

Message: 一次緩和、切り戻し、引き継ぎを分けて書く

### Narration

実務メモとして、緩和策には必ず戻し方を書きます。一時停止した機能をいつ戻すか、切り戻し後にどのメトリクスで安定を確認するかを決めておきます。止血だけで終わらせず、通常運用へ戻る条件まで書くことが大切です。

### Visual Notes

Decision tree for mitigation rollback escalation approval communication. Segment 7. Exercise recap segment. Practical memo segment.
