# Section 4 Lecture 1 台本

### Title

Application Signals SLOを作る

## Slide 1

### Slide Title

SLOを作る前に

### Slide Message

メトリクス到達を確認する

### Narration

エスエルオーを作る前に、対象サービスがアプリケーションシグナルズのメトリクスを送っていることを確認します。サービスが見えていない段階で作ろうとすると、失敗する可能性があります。 エスエルオーを作る前に、対象サービスと操作のメトリクスが届いていることを確認します。データがない状態で目標を作ろうとしても、期待通りに進まないことがあります。まずサービス一覧と詳細画面で観測できているかを見ます。

### Visual Notes

- Metrics first
- SLO creation second

## Slide 2

### Slide Title

今回のSLO

### Slide Message

Availabilityを見る

### Narration

今回のテンプレートでは、サンプルアプリの可用性を見るエスエルオーを用意しています。リクエストが期待通り成功しているかを、運用目標として見ます。 今回の学習では、可用性を入口にします。成功したリクエストの割合を見れば、利用者が目的の操作を完了できているかを考えやすくなります。ただし、本番ではレイテンシ目標も同じくらい重要になる場合があります。

### Visual Notes

- Availability SLO target
- Sample API service

## Slide 3

### Slide Title

Request-based

### Slide Message

成功したリクエストの割合

### Narration

リクエストベースのエスエルオーでは、成功したリクエストの割合を見ます。短時間の学習では数字が安定しないことがありますが、仕組みを理解するには十分です。 リクエストベースのエスエルオーは、リクエストごとの成功や失敗をもとに考えます。何を良いイベントとするか、何を悪いイベントとするかを決める必要があります。設定画面では、目標だけでなく、測る対象を慎重に選びます。

### Visual Notes

- Good requests divided by total requests
- Request-based SLO concept

## Slide 4

### Slide Title

有効化の流れ

### Slide Message

updateでSLOを追加する

### Narration

まずスタックを作り、通信を発生させ、サービスが見えることを確認します。その後で、エスエルオー作成フラグを有効にして、スタックを更新します。 この教材では、最初からエスエルオーを作るのではなく、通信が見えたあとに更新で追加する流れにしています。これは、アプリケーションシグナルズのサービス操作が見えてから目標を結びつけるためです。

### Visual Notes

- Create stack
- Wait for service metrics
- Update with SLO flag

## Slide 5

### Slide Title

見方

### Slide Message

目標と現在値を見る

### Narration

作成後は、エスエルオーの目標、現在の状態、エラーバジェットの考え方を確認します。短時間のハンズオンでは、長期的な達成率を断定しないようにします。 見方では、現在の達成状況と目標を比べます。短時間のハンズオンでは、実運用の信頼性を判断するにはデータが少なすぎます。そのため、ここでは画面の意味、目標との関係、アラートに広げる考え方を学びます。

### Visual Notes

- SLO status
- Target and current state
- Error budget concept

## Slide 6

### Slide Title

運用への接続

### Slide Message

何を重要とするかを決める

### Narration

エスエルオーは、ただ作るだけでは意味がありません。どのサービス、どの体験、どのしきいちを重要とするかを決め、運用判断につなげることが大切です。 運用へつなげるには、どの体験を守りたいかを決めます。すべての操作を同じ重みで見るのではなく、ログイン、購入、検索、登録など、利用者にとって重要な操作から目標を考えると現実的です。

### Visual Notes

- Service, user journey, threshold, action
- SLO to operations
