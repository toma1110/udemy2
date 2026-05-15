# Section 1 Lecture 1 台本

### Title

Logs Insights実践の地図

## Slide 1

### Slide Title

Logs Insights実践

### Slide Message

障害時に、ログから原因へ近づく

### Narration

このコースでは、クラウドウォッチログインサイトを、障害調査で使うクエリ集として学びます。ゴールは、最近のエラーを見る、時間帯で集計する、遅い処理を探す、リクエスト単位で追う、という型を持ち帰ることです。

### Visual Notes

- CloudWatch Logs Insights as search lens over logs
- Incident investigation workflow

## Slide 2

### Slide Title

調査フロー

### Slide Message

見る、絞る、集計する、追跡する

### Narration

ログ調査は、いきなり複雑なクエリから始めません。まず直近のログを見ます。次にエラーやタイムアウトで絞ります。増えた時間帯を集計し、最後にリクエストアイディーなどのキーで一連の出来事を追います。

### Visual Notes

- Four-step flow: 見る, 絞る, 集計, 追跡
- Clear arrows left to right

## Slide 3

### Slide Title

何が得意か

### Slide Message

ログの中から、必要な出来事を探す

### Narration

ログインサイトが得意なのは、たくさんのログの中から、今必要な出来事を探すことです。メトリクスが数字の変化を見る場所なら、ログインサイトは、その時間に何が起きたかを読む場所です。

### Visual Notes

- Metrics graph vs log search results
- Logs explain events behind metric changes

## Slide 4

### Slide Title

クエリの型

### Slide Message

毎回ゼロから書かない

### Narration

実務では、毎回ゼロからクエリを書く必要はありません。直近ログ、エラー検索、時間ごとの件数、上位エラー、遅延、リクエスト追跡。この型を持っておくと、障害時に迷う時間を減らせます。

### Visual Notes

- Query template library
- Six reusable query cards

## Slide 5

### Slide Title

小さく始める

### Slide Message

ロググループと時間範囲を絞る

### Narration

ログインサイトは、スキャンしたログ量に応じて料金が発生する可能性があります。だから最初は、必要なロググループだけを選び、時間範囲を短くします。小さく見て、必要な時だけ広げるのが基本です。

### Visual Notes

- Narrow log group and time window
- Cost safety indicator

## Slide 6

### Slide Title

このコースの進め方

### Slide Message

読むだけでも、既存ログで試してもよい

### Narration

標準のハンズオンでは、AWSリソースを新しく作りません。サンプルログとクエリを読むだけでも完了できます。既存ロググループがある場合だけ、直近の短い時間範囲で任意実行してください。

### Visual Notes

- Two paths: read sample logs, optional existing log execution
- No resource creation
