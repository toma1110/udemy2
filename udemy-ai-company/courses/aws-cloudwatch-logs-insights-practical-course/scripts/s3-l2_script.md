# Section 3 Lecture 2 台本

### Title

JOIN/subquery/SOURCEの入口

## Slide 1

### Slide Title

複数ログを見る

### Slide Message

必要な時だけ範囲を広げる

### Narration

最後のレクチャーでは、ジョイン、サブクエリ、ソースを扱います。どれも複数ログや広い範囲を扱いやすくする機能です。ただしスキャン範囲が広がりやすいので、必要な時だけ使います。

### Visual Notes

- Advanced feature map: JOIN, subquery, SOURCE
- Expand only when needed

## Slide 2

### Slide Title

JOIN

### Slide Message

共通キーでログをつなぐ

### Narration

ジョインは、複数のログを共通キーでつなぐ機能です。たとえばAPIログとラムダログを、リクエストアイディーで結びます。APIの5xxと、裏側のラムダのエラーを同じ行で見たい時に使います。

### Visual Notes

- API log joined with Lambda log by requestId
- One combined result row

## Slide 3

### Slide Title

subquery

### Slide Message

内側の結果を外側の条件に使う

### Narration

サブクエリは、内側のクエリで見つけた値を、外側のクエリの条件に使います。たとえば、下流サービスでタイムアウトしたリクエストアイディーだけを、上流サービスのログで追う、という使い方です。

### Visual Notes

- Inner query result feeds outer query
- Downstream failure to upstream context

## Slide 4

### Slide Title

SOURCE

### Slide Message

CLI/APIでロググループを指定する

### Narration

ソースは、シーエルアイやAPIでクエリを開始する時に、ロググループを指定するコマンドです。名前のプレフィックス、アカウント、ログクラス、タグで対象を選べます。コンソールではなく、プログラム実行向けです。

### Visual Notes

- SOURCE selects log groups by prefix and tags
- CLI/API label

## Slide 5

### Slide Title

制約を読む

### Slide Message

上級機能は条件と上限を確認する

### Narration

ジョインやサブクエリには制約があります。結合キー、使える条件、サブクエリの実行時間、スキャン量などを確認します。便利だから使うのではなく、基本クエリで足りない時に使います。

### Visual Notes

- Limitations checklist
- Key, time, cost, scope

## Slide 6

### Slide Title

まとめ

### Slide Message

小さく見て、必要な時だけ広げる

### Narration

まとめです。ログインサイト実践では、まず直近ログを小さく見ます。エラーで絞り、時間帯で集計し、リクエスト単位で追います。発展機能は、必要な時だけ範囲を広げる道具として使います。

### Visual Notes

- Full course summary workflow
- Recent, filter, aggregate, trace, advanced
