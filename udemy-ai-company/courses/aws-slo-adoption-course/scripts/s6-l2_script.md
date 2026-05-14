# Section 6 Lecture 2 台本

## Title

バーンレートとは何か

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

バーンレートとは何か

### Slide Message

エラーバジェットを、予定より何倍の速さで使っているか

### Narration

このレクチャーでは、バーンレートを扱います。バーンレートは、エラーバジェットを予定より何倍の速さで使っているかを表す数字です。残り予算だけではなく、今の消費速度を見ることで、対応の緊急度を判断しやすくなります。

### Visual Notes

- Burn rate definition
- budget tank with speed meter
- 倍速表現

## Slide 2

### Slide Title

1倍の意味

### Slide Message

期間ちょうどで予算を使い切るペース

### Narration

バーンレート一倍は、対象期間が終わるタイミングで、ちょうどエラーバジェットを使い切るペースです。月間予算を一か月で使い切る速度なので、理論上は目標ぴったりです。ただし、常に一倍に張り付いているなら余裕はありません。

### Visual Notes

- 1x burn rate
- month-long budget timeline
- normal pace

## Slide 3

### Slide Title

14倍の意味

### Slide Message

月間予算を、約2日で使い切るペース

### Narration

バーンレート十四倍なら、月間のエラーバジェットを約二日で使い切るペースです。これは、月末まで待つ判断ではありません。短時間で続けば、すぐに目標違反へ近づくため、対応優先度を上げるサインになります。

### Visual Notes

- 14x burn rate
- 30 days / 14 = about 2 days
- urgent indicator

## Slide 4

### Slide Title

失敗率から計算する

### Slide Message

実際の失敗率 ÷ 許容失敗率

### Narration

計算は、実際の失敗率を、エスエルオーで許容した失敗率で割ります。許容失敗率が〇点一パーセントで、今の失敗率が一パーセントなら、バーンレートは十倍です。許容ペースの十倍で予算を使っている、という意味になります。

### Visual Notes

- actual failure rate / allowed failure rate
- 0.1% -> 1.0% = 10x

## Slide 5

### Slide Title

残量だけでは遅い

### Slide Message

まだ残っていても、急速に減っているなら危険

### Narration

残量だけを見ると、判断が遅れることがあります。まだ七十パーセント残っていても、今の速度が高ければ、数時間後には大きく減っているかもしれません。バーンレートは、この急な悪化を早く見つけるための指標です。

### Visual Notes

- Remaining budget vs burn speed
- compare slow drain and fast drain

## Slide 6

### Slide Title

バーンレートとアラート

### Slide Message

単発の失敗ではなく、予算消費の速さで通知する

### Narration

バーンレートを使うと、単発エラーではなく、エラーバジェットの消費速度でアラートを設計できます。少しのエラーでも長く続けば問題になりますし、短時間でも強い悪化なら急ぎます。重要なのは、ユーザー体験への影響と緊急度を合わせることです。

### Visual Notes

- Burn-rate alert flow
- short burst vs sustained issue
- budget-aware alerting

## Slide 7

### Slide Title

使いどころ

### Slide Message

オンコール、リリース判断、週次レビューで使う

### Narration

バーンレートは、オンコールだけの数字ではありません。オンコールでは緊急度判断に使い、リリース判断では一時停止や継続の根拠に使います。週次レビューでは、どの時間帯に予算を使ったかを振り返る材料になります。

### Visual Notes

- Use cases
- on-call/release/review cards

## Slide 8

### Slide Title

まとめ

### Slide Message

バーンレートは、エラーバジェット消費の速度

### Narration

まとめです。バーンレートは、実際の失敗率を許容失敗率で割った数字です。一倍なら予定通り、十倍なら許容ペースの十倍で予算を使っています。次は、短期窓と長期窓を組み合わせて、ノイズと見逃しを減らす方法を見ます。

### Visual Notes

- Summary
- definition/formula/next windows

## QA Notes

- `lectures.md` の Lecture 6-2「バーンレートとは何か」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
