# Section 7 Lecture 3 台本

## Title

マネジメント向けSLOレポート

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

マネジメント向けSLOレポート

### Slide Message

細かいメトリクスを、判断できる文章と数字に変換する

### Narration

このレクチャーでは、マネジメント向けのエスエルオーレポートを扱います。運用ダッシュボードの細かい数字を、そのまま渡しても判断には使いにくいです。状態、影響、原因、次の判断を短くまとめる形へ変換します。

### Visual Notes

- Management SLO report
- metrics to decision summary

## Slide 2

### Slide Title

1ページで伝える

### Slide Message

今どうなのか、何が必要なのかを先に書く

### Narration

マネジメント向けレポートでは、最初に結論を書きます。今月のエスエルオーは達成中なのか、違反リスクがあるのか。エラーバジェットはどれくらい残っているのか。追加対応が必要なのか。この順番で伝えると、読む側が判断しやすくなります。

### Visual Notes

- One-page report
- status first
- decision summary

## Slide 3

### Slide Title

残り予算を見せる

### Slide Message

何パーセント残っているか、何日分の余裕か

### Narration

残りエラーバジェットは、マネジメントに伝わりやすい指標です。何パーセント残っているか、今のペースなら何日で枯渇しそうかを示します。単なる障害件数ではなく、目標に対する余白として説明します。

### Visual Notes

- Remaining budget
- percent and days remaining
- risk gauge

## Slide 4

### Slide Title

消費理由を書く

### Slide Message

予算を使った主要イベントを3つまでに絞る

### Narration

レポートには、エラーバジェットを消費した理由も書きます。ただし、すべての細かいエラーを並べる必要はありません。主要イベントを三つまでに絞り、いつ、何が起き、どれくらい予算を使ったかを書きます。

### Visual Notes

- Top budget consumers
- three event cards

## Slide 5

### Slide Title

判断につなげる

### Slide Message

リリース継続、改善優先、監視強化を提案する

### Narration

マネジメント向けレポートは、報告で終わらせません。エラーバジェットが十分ならリリース継続、急速に減っているなら改善優先、原因が不明なら監視強化のように、次の判断案を添えます。数字は、判断に使って初めて価値があります。

### Visual Notes

- Decision options
- continue/improve/observe

## Slide 6

### Slide Title

言い方を変える

### Slide Message

技術用語を、事業影響の言葉に置き換える

### Narration

報告では、技術用語をそのまま並べすぎないことも大切です。バーンレート十四倍という数字は、月間予算を約二日で使い切るペースです、のように言い換えます。エスエルオー違反リスクを、事業影響と判断の言葉に変換します。

### Visual Notes

- Translate technical terms
- burn rate -> days to exhaustion

## Slide 7

### Slide Title

テンプレート

### Slide Message

状態、予算、原因、判断、次回確認

### Narration

レポートテンプレートはシンプルで構いません。状態、残り予算、主な消費理由、判断案、次回確認の五つを入れます。毎回同じ型で出すと、過去との比較もしやすくなり、月次レビューに組み込みやすくなります。

### Visual Notes

- Report template
- status/budget/reasons/decision/next review

## Slide 8

### Slide Title

まとめ

### Slide Message

SLOレポートは、信頼性の状況を判断へつなげる

### Narration

まとめです。マネジメント向けエスエルオーレポートでは、細かいメトリクスではなく、状態、残り予算、消費理由、判断案を短く伝えます。これで、エスエルオーが運用チームだけの数字ではなく、組織の意思決定に使える数字になります。

### Visual Notes

- Summary
- status/budget/reason/decision
- bridge to organization rollout

## QA Notes

- `lectures.md` の Lecture 7-3「マネジメント向けSLOレポート」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
