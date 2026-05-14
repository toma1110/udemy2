# Section 7 Lecture 1 台本

## Title

見るべき指標と見せるべき指標

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

見るべき指標と見せるべき指標

### Slide Message

運用担当とマネジメントでは、必要な粒度が違う

### Narration

このセクションでは、エスエルオーダッシュボードを作ります。最初に大事なのは、見るべき指標と見せるべき指標を分けることです。運用担当は原因調査のために細かい情報が必要です。一方で、マネジメントには判断に必要な要約が必要です。

### Visual Notes

- Section 7 intro
- operator vs management dashboards
- different granularity

## Slide 2

### Slide Title

運用担当が見るもの

### Slide Message

悪化に気づき、原因にたどるための指標

### Narration

運用担当向けには、悪化を見つけて原因にたどる情報が必要です。現在のエスエルアイ、エスエルオー達成率、バーンレート、失敗件数、関連する内部メトリクスを並べます。目的は、次の調査行動に進めることです。

### Visual Notes

- Operator dashboard
- SLI/SLO/burn/internal metrics
- diagnosis path

## Slide 3

### Slide Title

マネジメントが見るもの

### Slide Message

状態、リスク、判断を短く伝える

### Narration

マネジメント向けには、細かいメトリクスよりも、状態、リスク、判断材料が重要です。今月の達成状況、残りエラーバジェット、主な消費理由、リリース判断への影響を短くまとめます。数字は、意思決定のために使います。

### Visual Notes

- Management report
- status/risk/decision
- simple summary

## Slide 4

### Slide Title

分けないと起きる問題

### Slide Message

細かすぎると伝わらず、粗すぎると調査できない

### Narration

一枚のダッシュボードにすべてを詰め込むと、どちらにも使いにくくなります。細かすぎると意思決定者には伝わりません。粗すぎると運用担当は原因を調べられません。用途ごとに画面を分けるほうが、結果的に使われます。

### Visual Notes

- Overloaded dashboard problem
- too detailed vs too summary

## Slide 5

### Slide Title

共通で必要な3つ

### Slide Message

SLO達成率、残り予算、バーンレート

### Narration

どの相手にも共通して必要なのは、エスエルオー達成率、残りエラーバジェット、バーンレートの三つです。達成率は今の状態、残り予算は余裕、バーンレートは悪化の速度を表します。この三つを起点に、粒度を変えて表示します。

### Visual Notes

- Common metrics
- attainment/remaining/burn rate

## Slide 6

### Slide Title

表示の順番

### Slide Message

結論、詳細、原因候補の順に置く

### Narration

画面の並びも重要です。最初に結論として、正常か危険かを見せます。次に、達成率や残り予算を置きます。最後に、原因候補となる内部メトリクスへ進めるようにします。上から下へ、判断から調査へ流れる構成です。

### Visual Notes

- Dashboard hierarchy
- status -> details -> diagnosis

## Slide 7

### Slide Title

更新頻度も分ける

### Slide Message

即時対応とレビューでは、見る時間軸が違う

### Narration

更新頻度も相手によって変わります。オンコールは今の数分を見ます。週次レビューでは、数日から一週間の傾向を見ます。月次報告では、期間全体の達成状況を見ます。時間軸を分けることで、同じ数字の意味が整理されます。

### Visual Notes

- Time horizons
- on-call weekly monthly

## Slide 8

### Slide Title

まとめ

### Slide Message

運用向けと意思決定向けを分けて設計する

### Narration

まとめです。エスエルオーダッシュボードは、一枚ですべてを解決しようとしないことが大切です。運用担当には調査できる粒度を、マネジメントには判断できる要約を用意します。次は、運用担当向けダッシュボードを具体化します。

### Visual Notes

- Summary
- operator vs decision dashboard
- next hands-on

## QA Notes

- `lectures.md` の Lecture 7-1「見るべき指標と見せるべき指標」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
