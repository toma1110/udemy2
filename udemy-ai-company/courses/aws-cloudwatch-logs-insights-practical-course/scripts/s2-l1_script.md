# Section 2 Lecture 1 台本

### Title

エラーと例外を探す

## Slide 1

### Slide Title

エラー検索

### Slide Message

まず異常らしいログを集める

### Narration

このセクションでは、障害調査のクエリ集を扱います。最初はエラー検索です。エラー、例外、タイムアウト、5xxのように、異常らしいログを集めて、調査の入口を作ります。

### Visual Notes

- Error search over logs
- ERROR, Exception, timeout, 5xx labels

## Slide 2

### Slide Title

levelを見る

### Slide Message

構造化ログならERRORで絞る

### Narration

JSONの構造化ログなら、レベルというフィールドを使えることがあります。レベルがエラーのログだけに絞ると、メッセージ全文を検索するより読みやすくなります。まず自分のログにどんなフィールドがあるかを見ます。

### Visual Notes

- JSON field level = ERROR
- Structured log table

## Slide 3

### Slide Title

messageを見る

### Slide Message

非構造ログは文字列で探す

### Narration

フィールドが整っていないログでは、アットメッセージを検索します。エラー、エクセプション、タイムアウトなどの文字を含む行を探します。ただし文字列検索は広くなりやすいので、時間範囲を短くします。

### Visual Notes

- @message text search
- regex style filter

## Slide 4

### Slide Title

5xxとtimeout

### Slide Message

HTTP失敗と待ち時間の失敗を見る

### Narration

APIのログでは、ステータスコードが500以上の行を探します。アプリログでは、タイムアウトという言葉や、エラータイプを見ることがあります。ログ形式ごとに、失敗を表すフィールドは変わります。

### Visual Notes

- API 5xx card and timeout card
- statusCode >= 500

## Slide 5

### Slide Title

フィールド名を合わせる

### Slide Message

クエリは現場ログへ調整する

### Narration

講座のクエリは型です。実際のログでは、ステータスコード、エラータイプ、リクエストアイディーなどの名前が違うことがあります。クエリをコピーして終わりではなく、自分のログのフィールド名へ合わせます。

### Visual Notes

- Template query adapted to real log fields
- Field mapping table

## Slide 6

### Slide Title

結果から行動へ

### Slide Message

時間、対象、種類を次の確認へつなげる

### Narration

エラー検索の結果で見るのは、時間、対象、種類です。いつ増えたか。どのサービスか。どのエラーか。この3つが見えたら、次は時間帯の集計や、リクエスト単位の追跡へ進みます。

### Visual Notes

- Result table branching to trend and request trace
- Time, service, error type
