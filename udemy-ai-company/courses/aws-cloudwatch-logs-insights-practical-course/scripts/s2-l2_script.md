# Section 2 Lecture 2 台本

### Title

stats/binで傾向を見る

## Slide 1

### Slide Title

傾向を見る

### Slide Message

件数を時間帯でまとめる

### Narration

このレクチャーでは、スタッツとビンを使って、ログの傾向を見ます。エラーがあるかだけでなく、いつ増えたのか、どの種類が多いのか、どのパスが遅いのかを集計します。

### Visual Notes

- Error count trend chart
- stats and bin blocks

## Slide 2

### Slide Title

count by bin

### Slide Message

5分ごとの件数を見る

### Narration

最初の型は、件数を数えて、5分ごとにまとめるクエリです。スタッツのカウントで件数を数え、ビン5分で時間帯に分けます。これで、エラーが増えた時間帯を見つけやすくなります。

### Visual Notes

- count(*) by bin(5m)
- Time buckets with bars

## Slide 3

### Slide Title

上位エラー

### Slide Message

多い種類から見る

### Narration

次は上位エラーです。エラータイプやサービスごとに件数を集計し、多い順に並べます。すべてのログを読むのではなく、件数が多い種類から見ることで、影響が大きい問題に近づけます。

### Visual Notes

- Top error types table
- service and errorType columns

## Slide 4

### Slide Title

遅延を見る

### Slide Message

平均だけでなくp95とp99を見る

### Narration

遅延調査では、平均だけでは足りません。ピー95やピー99を見ると、遅い側のユーザー体験を拾いやすくなります。エンドポイントごとに、平均、ピー95、ピー99、最大値を並べます。

### Visual Notes

- Latency percentile chart
- p95 and p99 highlighted

## Slide 5

### Slide Title

binの注意

### Slide Message

300sではなく5mを使う

### Narration

時間のまとめ方には注意があります。5分を表す時は、ビン5mのように書きます。秒で300sと書くと、単位ごとの上限に引っかかることがあります。講座では、5m、1hのように読みやすい単位を使います。

### Visual Notes

- Correct bin(5m), avoid bin(300s)
- Small warning callout

## Slide 6

### Slide Title

読み方

### Slide Message

いつ、何が、どれだけ増えたか

### Narration

集計結果で見るのは、いつ、何が、どれだけ増えたかです。時間帯、サービス、エラー種別、遅延の上位を確認します。ここで絞れたら、次はリクエストアイディーで具体的なログへ戻ります。

### Visual Notes

- Aggregate result to request trace transition
- When, what, how much
