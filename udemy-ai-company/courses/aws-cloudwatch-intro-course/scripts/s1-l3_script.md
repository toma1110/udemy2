# Section 1 Lecture 3 台本

## Title

Logsの基本

## Source

- `course_spec.md`
- `handson/README.md`
- Amazon CloudWatch Logs documentation

## Slide 1

### Slide Title

Logsの基本

### Slide Message

ログは、数字だけでは見えない出来事を残す

### Narration

このレクチャーでは、クラウドウォッチのログを整理します。メトリクスが数字の変化を見るものなら、ログは出来事の中身を見るものです。エラーの文、処理の流れ、リクエストの情報など、原因を探る手がかりになります。

### Visual Notes

- ログ行と時刻
- 数字から出来事へ視点が移る表現

## Slide 2

### Slide Title

log groupはまとまり

### Slide Message

アプリや機能ごとに、ログをまとめる

### Narration

ロググループは、ログのまとまりです。アプリケーション、関数、環境など、まとめて扱いたい単位でログを置きます。ログを見るときは、まずどのロググループを見るのかを選びます。

### Visual Notes

- 大きなフォルダとしてのロググループ
- アプリ別のまとまり

## Slide 3

### Slide Title

log streamは流れ

### Slide Message

同じまとまりの中で、発生元ごとに分かれる

### Narration

ログストリームは、ロググループの中にある細かい流れです。同じロググループでも、実行環境やインスタンスや処理単位によって、別の流れになります。どこから出たログかを見るときに役立ちます。

### Visual Notes

- 複数の流れが同じロググループに入る
- 発生元の違い

## Slide 4

### Slide Title

log eventは1つの出来事

### Slide Message

時刻とメッセージを持つ最小単位

### Narration

ログイベントは、時刻とメッセージを持つ1つの出来事です。エラー、開始、終了、処理時間など、アプリケーションが残した情報がここに入ります。調査では、問題が起きた時間帯のログイベントを探します。

### Visual Notes

- タイムスタンプ付きイベントカード
- 問題時間帯の強調

## Slide 5

### Slide Title

MetricsとLogsの違い

### Slide Message

数字で気づき、ログで中身を見る

### Narration

メトリクスとログは、役割が違います。メトリクスは、何かが増えた、遅くなった、落ちた、という変化に気づくために使います。ログは、その時間帯に何が起きたのかを読むために使います。

### Visual Notes

- 左にグラフ、右にログ行
- 気づく、読む、の2段階

## Slide 6

### Slide Title

読みやすいログ

### Slide Message

時刻、レベル、識別子、理由があると追いやすい

### Narration

読みやすいログには、時刻、重要度、リクエストの識別子、失敗理由が含まれます。あとからログインサイトで探すことを考えると、ただ文章を出すよりも、調査に使う情報をそろえておくことが大切です。

### Visual Notes

- よいログの要素
- 識別子で追跡する表現

## Slide 7

### Slide Title

まとめ

### Slide Message

ログは、原因を読むための記録

### Narration

まとめです。ロググループはまとまり、ログストリームは流れ、ログイベントは1つの出来事です。メトリクスで異常に気づいたら、ログで中身を読みます。次は、ログインサイトを使って、ログを探して集計する入口へ進みます。

### Visual Notes

- ログの3階層
- Logs Insightsへの接続

## QA Notes

- リソース作成なし
- Logs Insights前段として構成する
