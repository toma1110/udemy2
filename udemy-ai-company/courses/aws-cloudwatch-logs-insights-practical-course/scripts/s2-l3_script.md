# Section 2 Lecture 3 台本

### Title

parseとrequestId追跡

## Slide 1

### Slide Title

追跡する

### Slide Message

1つのリクエストを時系列で見る

### Narration

このレクチャーでは、パースとリクエストアイディー追跡を扱います。集計で問題の時間帯や種類が見えたら、次は1つのリクエストを時系列で追い、どこで失敗したかを確認します。

### Visual Notes

- Timeline for one request across services
- requestId as thread

## Slide 2

### Slide Title

JSONログ

### Slide Message

フィールドがあればそのまま使う

### Narration

JSONログでは、サービス名、ステータスコード、処理時間、リクエストアイディーなどがフィールドとして見えることがあります。この場合は、パースせずに、そのフィールドをそのまま使うのが簡単です。

### Visual Notes

- JSON log fields auto-discovered
- requestId, service, durationMs

## Slide 3

### Slide Title

parse

### Slide Message

文字列から値を取り出す

### Narration

非構造ログでは、メッセージの中から必要な値を取り出すことがあります。そこで使うのがパースです。ワイルドカードや正規表現で、ユーザー、処理名、エラー理由などをフィールドとして取り出します。

### Visual Notes

- Raw message transformed into fields
- parse command as extractor

## Slide 4

### Slide Title

requestId

### Slide Message

同じキーで出来事をつなぐ

### Narration

リクエストアイディーは、一連の処理をつなぐキーです。同じリクエストアイディーで絞ると、開始、途中の処理、エラー、終了ログを時系列で見られます。障害調査では非常に重要な手がかりです。

### Visual Notes

- Same requestId connecting multiple log events
- Start, service, error, end

## Slide 5

### Slide Title

dedup

### Slide Message

同じ対象の重複を抑える

### Narration

ディーダップは、同じフィールド値の重複を抑えるコマンドです。たとえば、同じリクエストアイディーのエラーが何行も出ている時、代表の1行だけを見たい場合に使えます。全体を見やすくするための道具です。

### Visual Notes

- Duplicate request rows collapsed
- dedup requestId

## Slide 6

### Slide Title

時系列で読む

### Slide Message

ascで古い順に並べる

### Narration

リクエスト追跡では、新しい順ではなく、古い順に並べることがよくあります。アットタイムスタンプを昇順にして、最初に何が起き、次にどこで遅くなり、どこで失敗したかを読みます。

### Visual Notes

- Ascending timeline
- Root cause path
