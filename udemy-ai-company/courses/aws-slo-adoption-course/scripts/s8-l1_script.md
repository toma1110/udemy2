# Section 8 Lecture 1 台本

## Title

SLO導入が失敗する3つのパターン

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs

## Slide 1

### Slide Title

SLO導入が失敗する3つのパターン

### Slide Message

失敗の型を知ると、導入の順番を間違えにくい

### Narration

このレクチャーでは、エスエルオー導入でよく起きる失敗を三つに分けて整理します。指標を作ったのに使われない。達成率だけ見て改善につながらない。会議や判断の流れに入らない。この三つを避けると、導入の成功率が上がります。

### Visual Notes

- Three failure patterns
- measurement, diagnosis, decision flow

## Slide 2

### Slide Title

失敗1: 測れるものから始める

### Slide Message

ユーザー体験ではなく、手元のメトリクスだけを選んでしまう

### Narration

一つ目の失敗は、測れるものから始めることです。クラウドウォッチにある数字だけを選ぶと、ユーザー体験とずれることがあります。大切なのは、先に守りたい体験を言葉にし、その体験を表すエスエルアイを選ぶことです。

### Visual Notes

- Metric-first failure
- user journey to SLI

## Slide 3

### Slide Title

失敗2: 達成率だけを見る

### Slide Message

良い、悪い、だけで止まり、原因と次の行動に進まない

### Narration

二つ目の失敗は、達成率だけを見ることです。九十九点九パーセントを超えたかどうかだけでは、次の改善に進めません。どの時間帯に悪化したのか。どの機能で予算を使ったのか。原因候補と行動までつなげて初めて意味があります。

### Visual Notes

- Score-only failure
- drilldown to cause and action

## Slide 4

### Slide Title

失敗3: 会議に入れない

### Slide Message

SLOを作っても、リリース判断や改善計画に使われない

### Narration

三つ目の失敗は、会議や判断の流れに入れないことです。エスエルオーを作っても、リリース判断、優先度づけ、週次レビューに出てこなければ、数字は見られなくなります。最初から、どの場で誰が見るかを決めます。

### Visual Notes

- SLO outside meetings
- release decision and review loop

## Slide 5

### Slide Title

体験から選び直す

### Slide Message

重要なユーザー操作を起点に、SLIを決める

### Narration

一つ目の対策は、ユーザー体験から選び直すことです。ログイン、検索、購入、通知のような重要操作を一つ選びます。その操作が成功したか、遅すぎないかを測ります。これにより、エスエルオーが現場の実感とつながります。

### Visual Notes

- User operation first
- success and latency

## Slide 6

### Slide Title

予算を判断へつなげる

### Slide Message

残りエラーバジェットを、継続、停止、改善の判断に使う

### Narration

二つ目の対策は、エラーバジェットを判断へつなげることです。余白が十分ならリリース継続。急速に減っているなら改善優先。原因が分からないなら監視強化。このように、数字を次の行動に変換します。

### Visual Notes

- Budget to decision
- continue, improve, observe

## Slide 7

### Slide Title

レビューに組み込む

### Slide Message

週次と月次の場で、同じ型で見続ける

### Narration

三つ目の対策は、レビューに組み込むことです。週次では直近の悪化と対応を見ます。月次では、目標が現実的か、改善が進んでいるかを見ます。同じ型で見続けると、エスエルオーが一度きりの資料ではなくなります。

### Visual Notes

- Weekly and monthly review
- repeatable template

## Slide 8

### Slide Title

まとめ

### Slide Message

体験、原因、判断、定例化をそろえる

### Narration

まとめです。エスエルオー導入で避けたい失敗は、測れるものだけを選ぶこと、達成率だけで止まること、会議に入れないことです。ユーザー体験から選び、原因と行動へつなげ、定例の場で見続ける。この形にすると、組織で使える数字になります。

### Visual Notes

- Summary
- experience, cause, decision, routine

## QA Notes

- `lectures.md` の Lecture 8-1「SLO導入が失敗する3つのパターン」に合わせて構成
- ナレーションでは SLO/SLI をエスエルオー/エスエルアイに寄せる
- 8枚構成
