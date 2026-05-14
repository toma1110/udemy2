# Section 6 Lecture 1 台本

## Title

エラーバジェットの計算

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

エラーバジェットの計算

### Slide Message

信頼性の余白を、時間と失敗数で説明できるようにする

### Narration

このレクチャーでは、エラーバジェットの計算を扱います。エラーバジェットは、エスエルオーを守るために、どれくらい失敗を許容できるかを表す余白です。計算式そのものは難しくありません。大事なのは、数字を開発と運用の判断に使える形にすることです。

### Visual Notes

- Section 6の導入
- SLO targetからError Budgetへ変換する流れ
- 時間とリクエスト数の2軸

## Slide 2

### Slide Title

基本式

### Slide Message

エラーバジェット = 100% - SLO目標

### Narration

まず基本式です。エスエルオー目標が九十九点九パーセントなら、許容できる失敗割合は〇点一パーセントです。つまり、全体のうち〇点一パーセントまでなら、目標の範囲内として扱える、という意味になります。

### Visual Notes

- Formula card
- 99.9% SLO -> 0.1% budget
- 差分を強調

## Slide 3

### Slide Title

時間で見る

### Slide Message

月間99.9%なら、約43分の余白

### Narration

時間で見ると、直感的に理解しやすくなります。月間のエスエルオーが九十九点九パーセントなら、月の〇点一パーセントがエラーバジェットです。三十日で考えると、およそ四十三分です。この四十三分を、障害や劣化でどれだけ使ったかを追います。

### Visual Notes

- 30 days -> 43.2 minutes
- calendar visual
- budget as time tank

## Slide 4

### Slide Title

リクエスト数で見る

### Slide Message

100万リクエストなら、失敗許容は1000件

### Narration

リクエストベースで考える場合は、全リクエスト数に許容失敗割合をかけます。たとえば月間百番リクエストで、エスエルオーが九十九点九パーセントなら、許容失敗は千件です。時間ではなく、成功と失敗の件数で管理する見方です。

### Visual Notes

- 1,000,000 requests
- 0.1% failure budget
- 1,000 failed requests

## Slide 5

### Slide Title

残量を計算する

### Slide Message

使った分を引くと、今残っている余白が見える

### Narration

エラーバジェットは、作って終わりではありません。許容できる失敗から、実際に起きた失敗を引くことで、残量が分かります。残りが多いのか、急速に減っているのかを見ることで、リリース判断や改善優先度の会話ができます。

### Visual Notes

- Initial budget -> consumed -> remaining
- progress bar
- remaining budget

## Slide 6

### Slide Title

悪い使い方

### Slide Message

予算を使い切るまで放置する数字ではない

### Narration

注意点もあります。エラーバジェットは、使い切るまで何もしなくてよい数字ではありません。短時間で急に消費しているなら、月末にまだ残っていても危険です。そこで次のレクチャーから、消費速度、つまりバーンレートを扱います。

### Visual Notes

- Do not wait until zero
- burn speed warning
- budget tank draining too fast

## Slide 7

### Slide Title

チームに伝える形

### Slide Message

割合、時間、件数を相手に合わせて使い分ける

### Narration

チームに伝えるときは、割合だけでなく、時間や件数にも変換します。エンジニアには失敗件数、マネジメントには残り割合、オンコールには残り時間が伝わりやすいことがあります。同じ数字でも、相手に合わせて表現を変えます。

### Visual Notes

- Audience-specific presentation
- engineer/ops/management cards

## Slide 8

### Slide Title

まとめ

### Slide Message

エラーバジェットは、SLO目標から計算する信頼性の余白

### Narration

まとめです。エラーバジェットは、百パーセントとエスエルオー目標の差分です。時間で見れば許容できる劣化時間、リクエスト数で見れば許容できる失敗件数になります。次は、この予算がどれくらいの速さで減っているか、バーンレートを見ていきます。

### Visual Notes

- Summary cards
- formula/time/requests
- next burn rate

## QA Notes

- `lectures.md` の Lecture 6-1「エラーバジェットの計算」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
