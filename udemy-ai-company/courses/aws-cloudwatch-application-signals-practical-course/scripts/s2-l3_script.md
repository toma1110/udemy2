# Section 2 Lecture 3 台本

### Title

正常、遅延、エラーのシナリオを切り替える

## Slide 1

### Slide Title

シナリオで学ぶ

### Slide Message

画面の変化を作る

### Narration

このハンズオンでは、ただ通信を流すだけではありません。シナリオを切り替えて、正常、遅延、エラー、回復が画面にどう出るかを確認します。 シナリオ切り替えの目的は、異常を再現することではなく、画面の変化を安全に観察することです。正常時の基準、遅延時の変化、失敗時の変化、回復時の戻り方を順番に見ます。順番を決めることで、何が変わったかを説明しやすくなります。

### Visual Notes

- Scenario switcher
- Metrics changing by scenario

## Slide 2

### Slide Title

normal

### Slide Message

正常時の基準を作る

### Narration

まずは正常シナリオです。エラーがない状態で、通信量とレイテンシがどのように見えるかを確認します。これが比較の基準になります。 正常シナリオでは、まず基準を作ります。通信量があり、レイテンシが安定し、失敗がほとんどない状態を確認します。この基準がないと、遅延や失敗に切り替えた時に、どれくらい悪化したのかを判断しにくくなります。

### Visual Notes

- Healthy baseline
- Stable latency and availability

## Slide 3

### Slide Title

slow

### Slide Message

レイテンシ悪化を見る

### Narration

遅延シナリオでは、サンプルアプリが意図的に待機します。通信は成功していても、レイテンシが悪くなる状態を作り、グラフの変化を見ます。 遅延シナリオでは、処理が遅くなった時にレイテンシがどう見えるかを確認します。平均だけではなく、遅いリクエストが混ざった時にグラフがどう変わるかを意識します。利用者影響がある遅さかどうかは、サービスの性質で変わります。

### Visual Notes

- Latency spike
- Successful but slow requests

## Slide 4

### Slide Title

error

### Slide Message

失敗の増え方を見る

### Narration

エラーシナリオでは、標準で失敗を確実に発生させます。割合はパラメータで変えられますが、教材ではフォルトやエラーが見える状態を優先します。 エラーシナリオでは、失敗が増えた時にフォルトやエラーがどう見えるかを確認します。五百番台の失敗、アプリケーション側の例外、呼び出し失敗など、原因は一つとは限りません。ここではまず、失敗の入口を画面で見つけます。

### Visual Notes

- Error count increase
- Availability drop
- Fault marker

## Slide 5

### Slide Title

recovery

### Slide Message

戻った後も確認する

### Narration

回復シナリオでは、正常応答へ戻します。異常を作って終わりではなく、戻った後に、サービス一覧や詳細画面でどう見えるかを確認します。 回復シナリオでは、設定を戻したあともすぐにすべての表示が消えるとは限らないことを確認します。監視画面は時間範囲を持っているため、過去の失敗がしばらく見える場合があります。現在の状態と過去の履歴を分けて読みます。

### Visual Notes

- Recovery trend
- Metrics returning to healthy state

## Slide 6

### Slide Title

更新後の注意

### Slide Message

反映には時間がかかる

### Narration

シナリオを更新しても、画面にすぐ反映されないことがあります。数分待ち、時間範囲を確認し、必要ならスモークテストで通信が出ているかを見ます。 更新後は、クラウドフォーメーションの完了、スケジュールの反映、メトリクスの到着、画面の更新がそれぞれ別のタイミングになります。うまく見えない時は、時間範囲、通信有無、シナリオ設定を順番に確認します。

### Visual Notes

- Wait after update
- Time range check
- Smoke test confirmation
