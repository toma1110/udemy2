# Section 4 Lecture 1 台本

## Title

CloudWatch MetricsでSLIを表現する

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- AWS CloudWatch Service Level Objectives documentation
- AWS Application Load Balancer CloudWatch metrics documentation

## Slide 1

### Slide Title

CloudWatch MetricsでSLIを表現する

### Slide Message

ユーザー体験を、時系列メトリクスに落とす

### Narration

このセクションでは、エスエルオーをエーダブリューエスでどう計測するかを見ていきます。最初はクラウドウォッチメトリクスです。ユーザー操作の成功率、待ち時間、エラー率を、クラウドウォッチ上のじけいれつデータとして表す考え方を整理します。

### Visual Notes

- Section 4の導入スライド
- ユーザー操作からCloudWatch Metricsへ変換する流れ
- 成功率、レイテンシ、エラー率の3カード

## Slide 2

### Slide Title

メトリクスの基本単位

### Slide Message

名前空間、メトリクス名、ディメンション、期間で読む

### Narration

クラウドウォッチメトリクスを見るときは、名前空間、メトリクス名、ディメンション、統計、期間をセットで考えます。同じメトリクス名でも、ロードバランサーごと、ターゲットグループごと、エーピーアイごとに意味が変わります。まず、どの単位の体験を測るかを明確にします。

### Visual Notes

- Metric anatomy diagram
- Namespace、MetricName、Dimensions、Statistic、Periodの分解図
- ALB例では `LoadBalancer`、`TargetGroup`、`AvailabilityZone` を使い、`Operation` ディメンションは使わない

## Slide 3

### Slide Title

成功率を作る

### Slide Message

良いリクエスト数 ÷ 全リクエスト数

### Narration

成功率のエスエルアイは、良いリクエスト数を全リクエスト数で割って作ります。たとえば、二百系や三百系を良いリクエスト、五百系を悪いリクエストとして扱います。ここで大事なのは、サービスやチームで成功の定義を決めてから、メトリクスを選ぶことです。

### Visual Notes

- Good requests / total requests formula
- 2xx/3xx as good, 5xx as bad
- ALB/API Gateway style request count cards

## Slide 4

### Slide Title

待ち時間を作る

### Slide Message

p95やp99で、遅い体験を見落とさない

### Narration

待ち時間のエスエルアイでは、平均だけでなく、九十五パーセンタイルや九十九パーセンタイルを使います。平均が良くても、一部のユーザーが大きく待たされていることがあります。クラウドウォッチでは、対象メトリクスが対応していれば、パーセンタイル統計で遅い体験を見ます。

### Visual Notes

- Latency distribution chart
- Average vs p95/p99 comparison
- Slow users highlighted at tail

## Slide 5

### Slide Title

Metric MathでSLIにする

### Slide Message

複数メトリクスを、1本の時系列にまとめる

### Narration

エスエルアイは、単一メトリクスそのものとは限りません。成功数、失敗数、総数を組み合わせて、計算式で一つのじけいれつにすることがあります。クラウドウォッチのメトリクスマスを使うと、複数のメトリクスを組み合わせ、エスエルアイとして扱いやすい形にできます。

### Visual Notes

- Metric math expression card
- good / total * 100
- Single time series output to SLI gauge

## Slide 6

### Slide Title

Periodをそろえる

### Slide Message

評価間隔が変わると、見える悪化も変わる

### Narration

期間の設定も重要です。いっぷんごとに見るのか、五分ごとに見るのかで、エラーの見え方は変わります。短すぎるとノイズが増え、長すぎると悪化に気づくのが遅れます。エスエルオーに使う前に、どの期間で評価するかを決めておきます。

### Visual Notes

- 1 minute / 5 minutes / 1 hour comparison
- Noise vs delay tradeoff
- Period selection checklist

## Slide 7

### Slide Title

DashboardとAlarmは出口

### Slide Message

先にSLI定義、次に表示と通知

### Narration

ダッシュボードやアラームは、エスエルアイを使う出口です。先に、何を良い体験とするかを決めます。そのあとで、グラフに表示し、アラーム条件を決めます。先にアラームを作ってから、あとで意味を考える順番にすると、運用で使いにくい通知になりがちです。

### Visual Notes

- Flow: SLI definition -> dashboard -> alarm -> action
- Warning for alarm-first design
- Clean operational workflow

## Slide 8

### Slide Title

まとめ: SLIは計算できる形にする

### Slide Message

定義、メトリクス、期間をそろえてからSLOへ進む

### Narration

まとめです。クラウドウォッチメトリクスでエスエルアイを表すには、まず体験の定義を決め、使うメトリクスを選び、期間と統計をそろえます。次のレクチャーでは、アプリケーションシグナルズを使って、レイテンシとアベイラビリティを見る方法へ進みます。

### Visual Notes

- Checklist: Definition, Metric, Period, Statistic
- Arrow to Application Signals
- Section 4 flow marker

## QA Notes

- `lectures.md` の Lecture 4-1 に合わせて構成
- CloudWatchの読みはナレーション内で「クラウドウォッチ」に統一
- Metric Mathは読み上げでは「メトリクスマス」に寄せる
- 8枚構成。次講義のApplication Signalsへ接続
- CEOコメント反映: ALBメトリクス例ではOperationディメンションを使わない
- CEOコメント反映: ナレーションでは「時系列」を「じけいれつ」、「1分」を「いっぷん」、「Application Signals」を「アプリケーションシグナルズ」に寄せる
