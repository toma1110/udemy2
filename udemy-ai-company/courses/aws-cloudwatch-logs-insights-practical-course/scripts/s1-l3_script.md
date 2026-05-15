# Section 1 Lecture 3 台本

### Title

基本構文: fields/filter/sort/limit

## Slide 1

### Slide Title

基本構文

### Slide Message

表示、絞り込み、並べ替え、件数制限

### Narration

このレクチャーでは、ログインサイトの基本構文を扱います。最初に覚えるのは、フィールズ、フィルター、ソート、リミットです。表示する列を選び、条件で絞り、新しい順に並べ、件数を抑えます。

### Visual Notes

- Query pipeline with four commands
- fields filter sort limit

## Slide 2

### Slide Title

fields

### Slide Message

見たい列を選ぶ

### Narration

フィールズは、結果に表示する列を選ぶコマンドです。よく使うのは、アットタイムスタンプ、アットメッセージ、アットログストリームです。JSONログなら、サービス名やステータスコードなどのフィールドも表示できます。

### Visual Notes

- Select columns from log event
- @timestamp, @message, @logStream

## Slide 3

### Slide Title

filter

### Slide Message

必要な行だけに絞る

### Narration

フィルターは、必要なログだけに絞るコマンドです。レベルがエラー、ステータスコードが500以上、メッセージにタイムアウトを含む、というように条件を置きます。最初は単純な条件から始めます。

### Visual Notes

- Many rows filtered into error rows
- ERROR, statusCode >= 500, timeout

## Slide 4

### Slide Title

sortとlimit

### Slide Message

新しい順に、小さく見る

### Narration

ソートは並べ替えです。障害調査では、アットタイムスタンプの降順で新しいログから見ます。リミットは件数制限です。最初は50件や100件に抑えて、条件が合っているか確認します。

### Visual Notes

- Latest logs first
- limit 50 as guardrail

## Slide 5

### Slide Title

pipeでつなぐ

### Slide Message

クエリは左から順に処理される

### Narration

ログインサイトでは、コマンドをパイプでつなぎます。表示列を選び、絞り込み、並べ替え、件数制限へ進みます。この流れを読めると、知らないクエリも分解して理解できます。

### Visual Notes

- Pipe character between command blocks
- Left to right processing

## Slide 6

### Slide Title

最初のクエリ

### Slide Message

直近ログを見る型を持つ

### Narration

最初の型は、直近ログを見るクエリです。タイムスタンプ、メッセージ、ログストリームを表示し、新しい順に並べ、50件に絞ります。まずこれで、ログがどんな形かを見ます。

### Visual Notes

- Query card for recent events
- Result table preview
