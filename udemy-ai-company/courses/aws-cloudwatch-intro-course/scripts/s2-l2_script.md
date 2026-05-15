# Section 2 Lecture 2 台本

## Title

Logs Insightsで障害調査

## Source

- `course_spec.md`
- `handson/README.md`
- Amazon CloudWatch Logs Insights sample queries

## Slide 1

### Slide Title

Logs Insightsで障害調査

### Slide Message

調査は、時間帯、エラー、傾向、対象の順に進める

### Narration

このレクチャーでは、ログインサイトを障害調査でどう使うかを見ます。最初から完璧なクエリを書く必要はありません。時間帯を絞り、最近のエラーを見て、件数の傾向を見て、対象を追う。この順番を持つことが大切です。

### Visual Notes

- 障害調査の4段階
- ログインサイトが調査レンズになる表現

## Slide 2

### Slide Title

最近のエラーを見る

### Slide Message

まずは新しい順で、失敗の手がかりを拾う

### Narration

最初は、最近のエラーを見る形が使いやすいです。時刻、メッセージ、ログストリームを表示し、エラーや例外らしい文字列で絞ります。新しい順に並べることで、いま起きている問題へ近づけます。

### Visual Notes

- エラー行の抽出
- 新しい順タイムライン

## Slide 3

### Slide Title

件数の傾向を見る

### Slide Message

いつ増えたかを、時間ごとに数える

### Narration

次に、エラーがいつ増えたのかを見ます。スタッツで件数を数え、ビンで5分ごとにまとめると、増えた時間帯が見えます。ログを1行ずつ読む前に、山がある時間を見つけるのがコツです。

### Visual Notes

- 5分ごとのエラー件数
- 山がある時間帯

## Slide 4

### Slide Title

遅い処理を見る

### Slide Message

処理時間の長いログを上から見る

### Narration

遅延調査では、処理時間が長いログを上から見ます。ラムダ関数のレポートログなら、実行時間を使って並べ替えられます。対象によって項目名は変わりますが、長いものを上に出す考え方は同じです。

### Visual Notes

- 遅い処理ランキング
- durationの棒

## Slide 5

### Slide Title

識別子で追う

### Slide Message

requestIdなどで、同じ処理の流れをつなぐ

### Narration

原因を深掘りするときは、リクエストの識別子が役立ちます。同じ識別子を持つログを追うと、どの処理がどこで失敗したのかをつなげて見られます。重複が多いときは、ディーダップで同じ識別子をまとめることもできます。

### Visual Notes

- requestIdでログ行がつながる
- 重複をまとめる表現

## Slide 6

### Slide Title

結果から行動へ

### Slide Message

ログは結論ではなく、次の判断材料

### Narration

ログインサイトで見つけた結果は、結論そのものではなく、次の判断材料です。エラーが増えた時間、遅い処理、特定の対象が分かったら、メトリクス、アラーム、アプリケーション変更履歴と合わせて確認します。

### Visual Notes

- ログ結果から次の確認先へ
- メトリクス、アラーム、変更履歴

## Slide 7

### Slide Title

まとめ

### Slide Message

Logs Insightsは、原因へ近づくための絞り込み道具

### Narration

まとめです。ログインサイトは、原因へ近づくための絞り込み道具です。最近のエラーを見る、件数の傾向を見る、遅い処理を見る、識別子で追う。この4つの型を持っておくと、障害調査の最初の一歩を踏み出しやすくなります。

### Visual Notes

- 4つの型を再掲
- 次のAlarm/Dashboardへ接続

## QA Notes

- サンプルクエリは対象ログ形式に依存するため、読解中心で説明
- 課金注意を前提にする
