# Section 6 Lecture 3 台本

## Title

短期窓と長期窓の組み合わせ

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

短期窓と長期窓の組み合わせ

### Slide Message

速い検知と、ノイズ抑制を両立する

### Narration

このレクチャーでは、バーンレートアラートでよく使う、短期窓と長期窓の組み合わせを扱います。短期窓は変化に早く反応します。長期窓は一時的なノイズを抑えます。この二つを組み合わせることで、見逃しと誤報を減らします。

### Visual Notes

- Short window and long window
- two time-series panels
- noise vs detection

## Slide 2

### Slide Title

短期窓

### Slide Message

数分の悪化にすばやく反応する

### Narration

短期窓は、いっぷん、五分、十分のような短い範囲で状態を見ます。急な障害には早く気づけますが、少数のエラーや一時的な揺れにも反応しやすくなります。短期窓だけで通知すると、誤報が増えがちです。

### Visual Notes

- Short window details
- 1m/5m/10m
- fast but noisy

## Slide 3

### Slide Title

長期窓

### Slide Message

数十分から数時間の傾向を見る

### Narration

長期窓は、三十分、一時間、六時間のような長い範囲で状態を見ます。一時的なノイズに強く、継続的な悪化を見つけやすい一方で、検知は遅くなります。長期窓だけでは、急な障害への初動が遅れることがあります。

### Visual Notes

- Long window details
- 30m/1h/6h
- stable but slower

## Slide 4

### Slide Title

両方を満たす条件

### Slide Message

短期も長期も悪いときに通知する

### Narration

実運用では、短期窓と長期窓の両方がしきいちを超えたときに通知する設計がよく使われます。短期だけ悪い場合は一時的なノイズかもしれません。長期も悪いなら、継続的にエラーバジェットを使っている可能性が高くなります。

### Visual Notes

- AND condition
- short window alarm + long window alarm -> page

## Slide 5

### Slide Title

高いバーンレート

### Slide Message

短い窓でも、強い悪化はすぐ拾う

### Narration

高いバーンレートは、短時間でも強い悪化を示します。たとえば、十四倍のように高い速度で予算を消費しているなら、短期窓でも早めに拾う価値があります。これは、ユーザー影響が急速に広がるケースへの備えです。

### Visual Notes

- High burn rate
- urgent lane
- 14x threshold

## Slide 6

### Slide Title

低いバーンレート

### Slide Message

弱い悪化は、長い窓で継続性を見る

### Narration

一方で、低いバーンレートの悪化は、すぐに緊急対応するほどではないかもしれません。その場合は、長い窓で継続しているかを見ます。ゆっくり予算を削っている問題は、週次レビューや計画的改善にもつなげられます。

### Visual Notes

- Low burn rate
- slow drain over hours
- planned improvement

## Slide 7

### Slide Title

設計の考え方

### Slide Message

通知したい緊急度から逆算する

### Narration

しきいちや時間窓は、暗記するものではありません。どれくらい速く予算が減ったら、誰を呼びたいのかから逆算します。深夜に起こす通知なのか、営業時間内に見る通知なのかで、短期窓と長期窓の組み合わせは変わります。

### Visual Notes

- Alert policy design
- who gets notified
- urgency ladder

## Slide 8

### Slide Title

まとめ

### Slide Message

短期窓は速さ、長期窓は信頼度を担当する

### Narration

まとめです。短期窓は早く気づくため、長期窓は一時的なノイズを抑えるために使います。両方を組み合わせることで、必要な通知だけを出しやすくなります。次は、この考え方を使って、バーンレートアラームを設計します。

### Visual Notes

- Summary
- short=fast, long=confidence, next=alarm design

## QA Notes

- `lectures.md` の Lecture 6-3「短期窓と長期窓の組み合わせ」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
