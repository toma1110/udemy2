# GPT-Image2 Prompts: s1-l2

Use the same premium AWS/SRE educational visual style as VID-001 and VID-002 s1-l1. 16:9 slide, clean cloud monitoring dashboard aesthetic, white and pale blue background, navy and teal accents, readable Japanese text generated inside the image, no logos, no watermark, no local text overlay.

## slide_001.png

Create a Japanese course slide. Large title: `Alarmの評価条件`. Subtitle: `しきいちだけでなく、期間と回数で判断する`. Visual: CloudWatch alarm line chart with threshold line, time windows, evaluation count markers, and a clean flow from Metric to State.

## slide_002.png

Create a Japanese course slide. Large title: `メトリクスを選ぶ`. Subtitle: `まず、どの数字を監視するかを決める`. Visual: selector panel choosing one metric from Error count, Latency, Queue depth, with labels `Namespace`, `MetricName`, `Statistic`.

## slide_003.png

Create a Japanese course slide. Large title: `しきいち`. Subtitle: `どの値から異常と見るかを決める`. Visual: line graph crossing a horizontal threshold, small comparison labels `>=`, `>`, `<=`, calm red alert accent.

## slide_004.png

Create a Japanese course slide. Large title: `期間と評価回数`. Subtitle: `何分ごとに、何回分を見るか`. Visual: time axis divided into one minute windows, labels `Period` and `EvaluationPeriods`, with three evaluation blocks.

## slide_005.png

Create a Japanese course slide. Large title: `データポイント`. Subtitle: `何個中、何個が異常ならAlarmにするか`. Visual: three time boxes, two red and one normal, big label `3個中2個`, state becomes `ALARM`.

## slide_006.png

Create a Japanese course slide. Large title: `状態とアクション`. Subtitle: `状態が変わる時に通知が動く`. Visual: state transition diagram `OK`, `ALARM`, `INSUFFICIENT_DATA`, with `ActionsEnabled` and `AlarmActions` leading to SNS Topic.

## slide_007.png

Create a Japanese course slide. Large title: `設定の考え方`. Subtitle: `速さと安定性のバランスを取る`. Visual: balanced scale or slider with `速い通知` on one side and `安定した判定` on the other, small cards `学習用` and `実運用`.
