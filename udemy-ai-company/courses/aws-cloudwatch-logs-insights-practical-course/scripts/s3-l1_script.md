# Section 3 Lecture 1 台本

### Title

pattern/anomalyで未知の変化を見る

## Slide 1

### Slide Title

未知の変化

### Slide Message

読めない量を、型にまとめる

### Narration

このセクションでは、2026年版の発展機能を扱います。まずはパターンとアノマリーです。ログが多すぎて読めない時、似たログを型にまとめ、いつもと違う変化を見つける入口になります。

### Visual Notes

- Many logs clustered into patterns
- Unknown change highlighted

## Slide 2

### Slide Title

pattern

### Slide Message

似たログを自動でまとめる

### Narration

パターンは、似た構造のログを自動でまとめます。エラー文の中で変わる数字、リクエストアイディー、時間などはトークンとして扱われます。まず全体にどんな種類のログが多いかを見るのに向いています。

### Visual Notes

- Log lines grouped into pattern cards
- Tokens for varying parts

## Slide 3

### Slide Title

anomaly

### Slide Message

いつもと違うパターンを見つける

### Narration

アノマリーは、パターンをもとに、通常と違うログの変化を見つけます。新しいパターン、頻度の急増、数値の変化などを入口にできます。原因そのものではなく、調査のきっかけとして使います。

### Visual Notes

- Normal pattern vs unusual pattern
- Anomaly signal marker

## Slide 4

### Slide Title

使いどころ

### Slide Message

エラー文言が多すぎる時に使う

### Narration

使いどころは、エラー文言が多すぎて、どれから読むべきか分からない時です。まずパターンで分類し、サンプル数や比率を見ます。気になるパターンを見つけたら、普通のフィルターやパースで深掘りします。

### Visual Notes

- Pattern first, then filter and parse
- Investigation funnel

## Slide 5

### Slide Title

注意点

### Slide Message

発展機能ほど小さく試す

### Narration

発展機能は便利ですが、スキャン範囲が広いほど時間と料金が増えやすくなります。ログクラスによって使えないコマンドもあります。最初は対象ロググループと時間範囲を絞り、小さく試します。

### Visual Notes

- Advanced query caution
- Small scope first

## Slide 6

### Slide Title

次の行動

### Slide Message

パターンから具体ログへ戻る

### Narration

パターンやアノマリーで気になる変化を見つけたら、そこで終わりではありません。該当する時間帯、サービス、ログストリームへ戻り、具体的なログを読みます。発展機能は、入口を見つけるために使います。

### Visual Notes

- Pattern result back to concrete log events
- Next action cards
