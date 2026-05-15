# Section 1 Lecture 2 台本

## Title

CloudWatch Alarmの評価条件

## Source

- `course_spec.md`
- `course_curriculum.md`
- AWS::CloudWatch::Alarm official documentation

## Slide 1

### Slide Title

Alarmの評価条件

### Slide Message

しきいちだけでなく、期間と回数で判断する

### Narration

このレクチャーでは、クラウドウォッチアラームの評価条件を整理します。アラームは、ただしきいちを超えたかだけで決まるわけではありません。どのメトリクスを見るか。何分ごとに見るか。何回のうち何回を異常と見るか。この組み合わせで状態が決まります。

### Visual Notes

- メトリクス線、しきいち、時間窓、判定回数の図
- Alarmの判定を4つの部品に分解

## Slide 2

### Slide Title

メトリクスを選ぶ

### Slide Message

まず、どの数字を監視するかを決める

### Narration

最初に決めるのはメトリクスです。メトリクスは監視する数字です。たとえばエラー数、レイテンシー、キューの件数などです。VID-002では、学習用の名前空間とメトリクス名を使い、通知の仕組みに集中します。

### Visual Notes

- 複数メトリクスから1つを選ぶ画面
- Namespace、MetricName、Statisticのラベル

## Slide 3

### Slide Title

しきいち

### Slide Message

どの値から異常と見るかを決める

### Narration

しきいちは、どの値から異常と見るかを決める線です。しきいち以上、しきいちより大きい、しきいち以下など、比較の向きもセットで考えます。今回のテンプレートでは、エラー数がしきいち以上になったら異常と見る形です。

### Visual Notes

- 折れ線グラフと水平なしきいち線
- 比較演算子を短いラベルで表示

## Slide 4

### Slide Title

期間と評価回数

### Slide Message

何分ごとに、何回分を見るか

### Narration

次に、期間と評価回数です。期間は、メトリクスを何秒単位でまとめるかです。評価回数は、その期間を何個分見て判断するかです。1分を1回だけ見る設定なら、反応は速い一方で、短いゆらぎにも反応しやすくなります。

### Visual Notes

- 時間軸を1分ごとに区切る図
- PeriodとEvaluationPeriodsを日本語併記

## Slide 5

### Slide Title

データポイント

### Slide Message

何個中、何個が異常ならAlarmにするか

### Narration

データポイントトゥアラームを使うと、何個中、何個が異常ならアラームにするかを決められます。たとえば3個中2個が異常ならアラーム、という形です。連続して異常でなくても、一定数を超えたら反応できます。

### Visual Notes

- 3つの時間枠のうち2つが赤い図
- N個中M個の判定を強調

## Slide 6

### Slide Title

状態とアクション

### Slide Message

状態が変わる時に通知が動く

### Narration

評価結果は、オーケー、アラーム、データ不足という状態に反映されます。通知アクションは、状態が変わる時に実行されます。アクションズイネーブルドが有効で、アラームアクションにエスエヌエストピックが入っていることが重要です。

### Visual Notes

- OK、ALARM、INSUFFICIENT_DATAの状態遷移
- ActionsEnabledとAlarmActionsの確認ポイント

## Slide 7

### Slide Title

設定の考え方

### Slide Message

速さと安定性のバランスを取る

### Narration

最後に考え方です。アラームを速く反応させるほど、短いゆらぎも拾いやすくなります。評価回数を増やすほど安定しますが、通知は遅くなります。学習では小さく速く、実運用では業務影響に合わせて調整します。

### Visual Notes

- 速さと安定性のバランスバー
- 学習用設定と実運用設定を左右比較
