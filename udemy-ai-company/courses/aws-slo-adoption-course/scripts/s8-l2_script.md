# Section 8 Lecture 2 台本

## Title

開発チームへの説明と巻き込み方

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs

## Slide 1

### Slide Title

開発チームへの説明と巻き込み方

### Slide Message

評価ではなく、共同改善の約束として伝える

### Narration

このレクチャーでは、開発チームへエスエルオーをどう説明し、どう巻き込むかを扱います。エスエルオーは、開発チームを責めるための数字ではありません。ユーザー体験を守るために、運用と開発が同じものを見るための約束です。

### Visual Notes

- Explain SLO to developers
- shared improvement agreement

## Slide 2

### Slide Title

身構える理由

### Slide Message

新しい評価指標に見えると、協力されにくい

### Narration

開発チームが身構えるのは自然です。新しい評価指標に見えたり、リリースを止める口実に見えたりするからです。最初に伝えるべきことは、個人評価ではなく、ユーザー影響を早く見つけるための仕組みだという点です。

### Visual Notes

- Developer concerns
- not personal evaluation

## Slide 3

### Slide Title

ユーザー影響で話す

### Slide Message

技術指標を、利用者が困る状況に変換する

### Narration

説明では、技術指標をユーザー影響に変換します。レイテンシが上がった、ではなく、検索結果が返るまで待たされている。エラー率が上がった、ではなく、購入を完了できない人が増えている。この言い方にすると、改善の意味が共有しやすくなります。

### Visual Notes

- Technical metric to user impact
- latency and errors

## Slide 4

### Slide Title

共同で候補を作る

### Slide Message

運用だけで決めず、開発とPMを初期設計に入れる

### Narration

エスエルオー候補は、運用だけで決めないほうがよいです。開発チームは、機能の重要度や制約を知っています。ピーエムは、ユーザー期待や事業優先度を知っています。三者で候補を作ると、あとから使いやすい数字になります。

### Visual Notes

- SRE, developers, PM
- joint SLO draft

## Slide 5

### Slide Title

共有テンプレート

### Slide Message

守りたい体験、測る指標、目標、判断を1枚にする

### Narration

開発チーム向けの共有では、一枚のテンプレートが便利です。守りたいユーザー体験。測るエスエルアイ。目標。エラーバジェットを使った判断。この四つをまとめると、何のための数字なのかがぶれにくくなります。

### Visual Notes

- Developer SLO template
- experience, SLI, target, decision

## Slide 6

### Slide Title

改善タスクへ落とす

### Slide Message

レビュー結果を、担当と期限のある行動に変える

### Narration

レビューで悪化が見つかったら、改善タスクへ落とします。アラートを増やす、タイムアウトを見直す、重い処理を分ける、計測を追加する。担当と期限を決めることで、エスエルオーが報告だけで終わらなくなります。

### Visual Notes

- Review to action items
- owner and due date

## Slide 7

### Slide Title

反発への返し方

### Slide Message

責める数字ではなく、優先度を決める材料だと戻す

### Narration

反発が出たときは、目的に戻します。これは責める数字ではなく、改善の優先度を決める材料です。守れない目標なら、目標を見直します。計測が粗いなら、計測を直します。数字を押しつけず、一緒に育てる姿勢が大切です。

### Visual Notes

- Handle objections
- improve together

## Slide 8

### Slide Title

まとめ

### Slide Message

責めない、翻訳する、共同設計し、タスク化する

### Narration

まとめです。開発チームにエスエルオーを説明するときは、評価ではなく共同改善の約束として伝えます。技術指標をユーザー影響に翻訳し、候補を一緒に作り、レビュー結果を改善タスクへつなげる。この流れで、協力を得やすくなります。

### Visual Notes

- Summary
- no blame, translate, co-design, action

## QA Notes

- `lectures.md` の Lecture 8-2「開発チームへの説明と巻き込み方」に合わせて構成
- ナレーションでは PM をピーエム、SLO/SLI をエスエルオー/エスエルアイに寄せる
- 8枚構成
