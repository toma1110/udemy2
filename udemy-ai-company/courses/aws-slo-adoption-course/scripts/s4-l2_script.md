# Section 4 Lecture 2 台本

## Title

Application SignalsでLatencyとAvailabilityを見る

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- AWS CloudWatch Service Level Objectives documentation

## Slide 1

### Slide Title

Application SignalsでLatencyとAvailabilityを見る

### Slide Message

サービスと操作を軸に、体験指標を見る

### Narration

このレクチャーでは、アプリケーションシグナルズでレイテンシとアベイラビリティを見る考え方を整理します。アプリケーションシグナルズは、サービスや操作を軸に、リクエストの成功、失敗、待ち時間を見やすくする機能です。エスエルオー設計の入口として使えます。

### Visual Notes

- Application Signals service map
- Latency and Availability KPI cards
- Service and operation labels

## Slide 2

### Slide Title

サービスと操作で見る

### Slide Message

どのサービスの、どの操作かを先に決める

### Narration

アプリケーションシグナルズでは、サービス全体だけでなく、操作単位で体験を見ます。たとえば、ログイン、検索、決済のように、ユーザーが意識する操作を分けます。サービス名だけでまとめるより、どの操作が悪いのかを判断しやすくなります。

### Visual Notes

- Service node with operations: login/search/payment
- Operation-level metric cards
- User journey to service operation mapping

## Slide 3

### Slide Title

Latencyを見る

### Slide Message

ユーザーが待たされた時間を、操作単位で確認する

### Narration

レイテンシは、ユーザーがどれだけ待たされたかを見る指標です。アプリケーションシグナルズでは、サービスや操作に紐づけてレイテンシを確認できます。単にサーバーが忙しいかではなく、どの操作が遅いのかを見られることが重要です。

### Visual Notes

- Latency chart for operation
- p95 line and threshold line
- Slow operation highlighted

## Slide 4

### Slide Title

Availabilityを見る

### Slide Message

リクエストが成功した割合を確認する

### Narration

アベイラビリティは、リクエストが成功した割合を見ます。エラーが増えれば、ユーザー体験は悪化します。アプリケーションシグナルズでは、標準的なアプリケーション指標として、レイテンシとアベイラビリティをエスエルオー候補にしやすい形で扱えます。

### Visual Notes

- Availability percentage gauge
- Good/bad request split
- Error rate trend below

## Slide 5

### Slide Title

依存先も見る

### Slide Message

外向きリクエストの遅さや失敗を切り分ける

### Narration

ユーザー体験の悪化は、自分のサービスだけで起きるとは限りません。データベース、外部エーピーアイ、別サービスへの依存先が遅い場合もあります。依存先を含めて見られると、エスエルアイ悪化後の原因分析に進みやすくなります。

### Visual Notes

- Service dependency map
- Database/external API dependency cards
- Latency/faults on outgoing requests

## Slide 6

### Slide Title

計装とデータ期間を確認する

### Slide Message

見えている数字には、前提条件がある

### Narration

アプリケーションシグナルズの数字を使う前に、計装とデータ期間を確認します。対象のサービスが正しく検出されているか。十分なリクエストが集まっているか。短い期間の少ないデータだけで判断すると、実態より強い結論を出してしまうことがあります。

### Visual Notes

- Instrumentation checklist
- Data volume and time window
- Caution banner for sparse traffic

## Slide 7

### Slide Title

SLO作成時の注意

### Slide Message

初回作成ではサービスリンクロールが関係する

### Narration

アプリケーションシグナルズでエスエルオーを作るときは、必要な権限とサービスリンクロールにも注意します。初回作成時には、クラウドウォッチがアプリケーションシグナルズ用のサービスリンクロールを作成する場合があります。ハンズオンでは、この前提をリードミーに明記します。

### Visual Notes

- IAM/service-linked role caution card
- First SLO creation flow
- README prerequisite marker

## Slide 8

### Slide Title

まとめ: 操作に近い指標を使う

### Slide Message

LatencyとAvailabilityを、SLO候補として見る

### Narration

まとめです。アプリケーションシグナルズでは、サービスと操作を軸に、レイテンシとアベイラビリティを見ます。これは、エスエルアイをユーザー体験に近づける助けになります。次のレクチャーでは、期間ベースとリクエストベースのエスエルオーの違いを整理します。

### Visual Notes

- Service operation -> latency/availability -> SLO candidate
- Arrow to period-based and request-based lecture
- Key takeaway card

## QA Notes

- `lectures.md` の Lecture 4-2 に合わせて構成
- Application Signalsはナレーション内で「アプリケーションシグナルズ」に統一
- 8枚構成。Demo扱いだが、実アプリ計装はSection 5以降のハンズオン制約に合わせて概念デモに留める
