# Section 6 Lecture 4 台本

## Title

バーンレートAlarmを設計する

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

バーンレートAlarmを設計する

### Slide Message

CloudWatchで、予算消費速度に基づく通知へ落とし込む

### Narration

このレクチャーでは、バーンレートアラームの設計を扱います。実装の細部よりも、何をメトリクスにし、どの時間窓で評価し、どの緊急度で通知するかを整理します。クラウドウォッチアラームに落とし込む前の設計図を作るイメージです。

### Visual Notes

- Hands-on design intro
- CloudWatch Alarm from burn rate
- design sheet

## Slide 2

### Slide Title

入力を決める

### Slide Message

分母、分子、許容失敗率を固定する

### Narration

最初に、入力を決めます。分母は対象リクエスト、分子は失敗リクエストです。さらに、エスエルオー目標から許容失敗率を決めます。ここが曖昧なままだと、アラームの意味も曖昧になります。

### Visual Notes

- Input definition
- good/bad/total
- allowed failure rate

## Slide 3

### Slide Title

Metric Mathで速度にする

### Slide Message

実失敗率を、許容失敗率で割る

### Narration

次に、メトリクスマスでバーンレートを計算します。実際の失敗率を許容失敗率で割ることで、何倍の速度で予算を使っているかが出ます。CloudWatchでは、メトリクスを直接見るだけでなく、計算式をアラーム対象にできます。

### Visual Notes

- Metric Math expression
- failure_rate / allowed_failure_rate
- single time series

## Slide 4

### Slide Title

短期アラーム

### Slide Message

急な悪化を拾うための条件

### Narration

短期アラームは、急な悪化を拾うために使います。たとえば五分間のバーンレートが高い状態を見ます。ここでは、単発の一分だけではなく、数データポイント続いたかを見ることで、ノイズを少し減らします。

### Visual Notes

- Short-window alarm
- 5 minutes
- datapoints to alarm

## Slide 5

### Slide Title

長期アラーム

### Slide Message

継続的な悪化を確認する条件

### Narration

長期アラームは、悪化が続いているかを確認するために使います。三十分や一時間の範囲でバーンレートを見ると、一時的な揺れを抑えられます。短期と長期を組み合わせることで、通知の信頼度を上げます。

### Visual Notes

- Long-window alarm
- 30 minutes or 1 hour
- stability

## Slide 6

### Slide Title

Composite Alarmでまとめる

### Slide Message

短期と長期をAND条件で扱う

### Narration

短期と長期の二つのアラームを作ったら、コンポジットアラームでまとめる考え方があります。短期も長期も悪いときだけ通知すれば、単発ノイズを避けやすくなります。ハンズオンでは、構成と考え方をリードミーに沿って確認します。

### Visual Notes

- Composite Alarm
- short AND long
- single notification

## Slide 7

### Slide Title

通知先を分ける

### Slide Message

高緊急度と低緊急度を同じ扱いにしない

### Narration

通知設計では、すべてを同じ宛先に送らないことも重要です。高いバーンレートは即時対応、低いバーンレートはレビューや営業時間内対応に分けられます。通知先は、エスエヌエスやチャット連携に接続する前に、緊急度で整理します。

### Visual Notes

- Severity routing
- high/low urgency
- SNS topic routing

## Slide 8

### Slide Title

まとめ

### Slide Message

入力、計算、時間窓、通知先を順番に決める

### Narration

まとめです。バーンレートアラームは、分母と分子を決め、失敗率を計算し、許容失敗率で割り、短期窓と長期窓で評価します。最後に、緊急度に合わせて通知先を決めます。次のセクションでは、これらを見せるダッシュボードへ進みます。

### Visual Notes

- Summary checklist
- input/math/windows/routing
- next dashboard

## QA Notes

- `lectures.md` の Lecture 6-4「バーンレートAlarmを設計する」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
