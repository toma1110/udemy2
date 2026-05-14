# Section 7 Lecture 2 台本

## Title

運用担当向けダッシュボード

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs
- Amazon CloudWatch SLO / Alarm / Dashboard documentation

## Slide 1

### Slide Title

運用担当向けダッシュボード

### Slide Message

異常検知から原因調査までを一画面で進める

### Narration

このレクチャーでは、運用担当向けのエスエルオーダッシュボードを設計します。目的は、異常に気づき、状況を把握し、原因候補へ進むことです。きれいなレポートではなく、対応中に使える画面を作ります。

### Visual Notes

- Operator dashboard hands-on
- detect -> understand -> diagnose

## Slide 2

### Slide Title

上段: 状態を置く

### Slide Message

正常、注意、危険がすぐ分かるようにする

### Narration

上段には、今の状態を置きます。エスエルオー達成率、残りエラーバジェット、現在のバーンレートを並べると、まず危険度が分かります。対応中の人が最初に見る場所なので、結論を大きく表示します。

### Visual Notes

- Top row status
- SLO attainment, remaining budget, burn rate

## Slide 3

### Slide Title

中段: 時系列を見る

### Slide Message

悪化がいつ始まり、続いているかを確認する

### Narration

中段には時系列グラフを置きます。成功率、レイテンシ、エラー率、バーンレートを時間で見ると、いつ悪化したか、続いているか、回復しているかが分かります。ここで、対応の緊急度と影響範囲を確認します。

### Visual Notes

- Middle row time series
- success/latency/error/burn

## Slide 4

### Slide Title

下段: 原因候補へ進む

### Slide Message

内部メトリクスは、体験悪化の後に見る

### Narration

下段には原因候補を置きます。シーピーユー、メモリ、データベース待ち、キューの長さ、外部依存の失敗などです。ここで大事なのは、内部メトリクスを主役にしないことです。まず体験悪化を見てから、原因候補として使います。

### Visual Notes

- Bottom row diagnostic metrics
- CPU/DB/Queue/external dependency

## Slide 5

### Slide Title

Alarm状態も置く

### Slide Message

通知が出ている理由を、その場で確認できるようにする

### Narration

運用中は、なぜ通知が出ているのかをすぐ確認できることが重要です。クラウドウォッチアラームの状態や、短期窓、長期窓のどちらが発火しているかを表示します。通知とダッシュボードをつなげると、初動が速くなります。

### Visual Notes

- Alarm status panel
- short/long burn alarm states

## Slide 6

### Slide Title

Runbookへの導線

### Slide Message

次に何をするかまで置いておく

### Narration

ダッシュボードは見るだけでは不十分です。異常を見つけたら、次に何をするかへ進める必要があります。ランブックやリードミーへのリンク、確認コマンド、担当チーム、関連サービスを置くと、対応の迷いを減らせます。

### Visual Notes

- Runbook links
- next action panel
- owner/team/service

## Slide 7

### Slide Title

コストと整理

### Slide Message

増やしすぎず、使われる画面に絞る

### Narration

クラウドウォッチダッシュボードは便利ですが、増やしすぎると管理されなくなります。講座では低コストを前提に、必要なウィジェットに絞ります。サービス単位、重要操作単位など、使う人が迷わない単位で整理します。

### Visual Notes

- Cost and dashboard hygiene
- focused widgets
- low cost

## Slide 8

### Slide Title

まとめ

### Slide Message

状態、時系列、原因候補、行動を一画面に置く

### Narration

まとめです。運用担当向けダッシュボードでは、上段に状態、中段に時系列、下段に原因候補を置きます。さらにアラーム状態とランブックへの導線を入れると、対応に使える画面になります。次は、マネジメント向けのレポートに変換します。

### Visual Notes

- Summary
- status/timeline/diagnosis/action

## QA Notes

- `lectures.md` の Lecture 7-2「運用担当向けダッシュボード」に合わせて構成
- ナレーションでは SLO/SLI/SLA を原則としてエスエルオー/エスエルアイ/エスエルエーに寄せる
- CloudWatch はナレーション内ではクラウドウォッチに寄せる
- バーンレート、エラーバジェットは日本語表記で統一
- 8枚構成
