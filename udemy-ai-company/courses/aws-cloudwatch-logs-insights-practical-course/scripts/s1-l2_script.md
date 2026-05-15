# Section 1 Lecture 2 台本

### Title

ロググループと時間範囲

## Slide 1

### Slide Title

安全運転

### Slide Message

まずスキャン量を小さくする

### Narration

このレクチャーでは、ログインサイトを安全に使う前提を整理します。最初に意識するのは、スキャン量です。必要なロググループだけを選び、時間範囲を短くし、クエリを小さく始めます。

### Visual Notes

- Safety dashboard for query scan volume
- Narrow query funnel

## Slide 2

### Slide Title

ロググループ

### Slide Message

調査対象のログだけを選ぶ

### Narration

ロググループは、ログのまとまりです。複数のロググループを選ぶほど、見る範囲は広がります。障害時でも、関係しそうなアプリ、API、ラムダなど、まず対象を絞って始めます。

### Visual Notes

- Many log groups, only a few selected
- Application, API, Lambda labels

## Slide 3

### Slide Title

時間範囲

### Slide Message

直近5分から15分で始める

### Narration

時間範囲は、クエリのコストと速度に直結します。最初から1日や1週間を見ず、障害が起きた時間の周辺、たとえば直近5分から15分で始めます。必要なら、後から広げます。

### Visual Notes

- Timeline with small selected window
- 5m, 15m, then expand if needed

## Slide 4

### Slide Title

limitを付ける

### Slide Message

最初は結果件数を抑える

### Narration

直近ログを見る時は、リミットを付けます。結果件数を抑えることで、画面で読みやすくなります。まず50件、100件のように小さく見て、条件が正しいかを確認します。

### Visual Notes

- Query block with limit 50
- Small result table

## Slide 5

### Slide Title

キャンセル

### Slide Message

不要な実行中クエリを止める

### Narration

コンソールでクエリを実行したあと、不要になったクエリはキャンセルします。画面を閉じれば必ず止まる、と考えないほうが安全です。実行中のクエリを確認し、不要なら止める癖を付けます。

### Visual Notes

- Running query with cancel button
- Stop unused query

## Slide 6

### Slide Title

チェックリスト

### Slide Message

対象、時間、件数、停止を確認する

### Narration

まとめです。実行前に、ロググループは必要最小限か。時間範囲は短いか。リミットは付いているか。不要な実行中クエリを止めたか。この4点を確認してから、調査に入ります。

### Visual Notes

- Four-item checklist
- Log group, time range, limit, cancel
