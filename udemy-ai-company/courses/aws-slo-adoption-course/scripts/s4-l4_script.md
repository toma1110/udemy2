# Section 4 Lecture 4 台本

## Title

SLO推奨値の使いどころ

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- AWS CloudWatch Service Level Objectives documentation
- AWS What's New: CloudWatch Application Signals SLO capabilities

## Slide 1

### Slide Title

SLO推奨値の使いどころ

### Slide Message

過去データから、しきいちと目標の候補を得る

### Narration

このレクチャーでは、アプリケーションシグナルズのエスエルオー推奨値の使いどころを整理します。これは単独のサービス名ではなく、エスエルオー作成時に、過去のメトリクスデータをもとに、しきいち、目標、バーンレート窓の候補を出してくれる機能です。ただし、最終判断を自動化するものではありません。

### Visual Notes

- Application Signals SLO recommendation concept
- Historical data -> threshold/goal/burn windows
- Human review checkpoint

## Slide 2

### Slide Title

30日データを見る

### Slide Message

直近の実測値をもとに候補を出す

### Narration

エスエルオー推奨値は、過去三十日程度の履歴データをもとに候補を作ります。実際のサービスがどれくらい速く、どれくらい成功しているかを見て、現実的な初期値を考える助けになります。データが足りないサービスでは、候補の信頼度も下がります。

### Visual Notes

- 30-day metric timeline
- Historical latency and availability data
- Data sufficiency caution

## Slide 3

### Slide Title

入力する情報

### Slide Message

サービス、操作、評価方式、標準メトリクスを選ぶ

### Narration

推奨値を使うときは、対象を指定します。サービス操作を見るのか、サービス依存先を見るのか。評価方式は期間ベースか、リクエストベースか。標準メトリクスはレイテンシか、アベイラビリティか。これらを選んだうえで候補を受け取ります。

### Visual Notes

- Input form style diagram
- Service operation / service dependency
- Evaluation type and metric type cards

## Slide 4

### Slide Title

出てくる候補

### Slide Message

しきいち、SLO目標、バーンレート窓

### Narration

出てくる候補は、主に三つです。メトリクスのしきいち、エスエルオーの目標、そしてバーンレートの評価窓です。たとえば、レイテンシなら何ミリ秒以内を良い体験とするか。アベイラビリティなら何パーセントを目標にするか、という候補が出ます。

### Visual Notes

- Output cards: threshold, objective, burn rate windows
- Latency threshold example
- Availability goal example

## Slide 5

### Slide Title

そのまま採用しない

### Slide Message

事業重要度とユーザー期待で見直す

### Narration

推奨値は便利ですが、そのまま採用するものではありません。過去データは、あくまで過去の実績です。重要な決済機能と、社内向けの低頻度機能では、同じ数字でも意味が違います。事業重要度、ユーザー期待、改善余地を合わせて見直します。

### Visual Notes

- Recommendation vs business review
- Critical payment vs internal tool comparison
- Human decision gate

## Slide 6

### Slide Title

最初の会話に使う

### Slide Message

白紙から決めるより、合意形成しやすい

### Narration

使いどころとして一番大きいのは、最初の会話です。白紙で九十九点九パーセントを決めるより、過去データから出た候補を見ながら話す方が、合意形成しやすくなります。エンジニア、プロダクト、運用担当が同じ数字を見て議論できます。

### Visual Notes

- Team discussion around recommendation panel
- Engineering/Product/Ops stakeholders
- Data-informed consensus

## Slide 7

### Slide Title

運用しながら調整する

### Slide Message

初期値は、レビューで育てる

### Narration

エスエルオーは、一度決めたら終わりではありません。最初の候補を採用したあと、アラートの多さ、エラーバジェットの減り方、ユーザー影響を見ながら調整します。推奨値は、完成形ではなく、運用を始めるための初期案として扱います。

### Visual Notes

- SLO lifecycle: recommend -> adopt -> review -> adjust
- Alert noise and error budget feedback
- Continuous improvement loop

## Slide 8

### Slide Title

まとめ: 推奨値として使う

### Slide Message

データの提案に、チームの判断を重ねる

### Narration

まとめです。アプリケーションシグナルズのエスエルオー推奨値は、過去データから、しきいち、目標、バーンレート窓の候補を出す機能です。重要なのは、候補をそのまま採用するのではなく、チームの判断を重ねることです。次のセクションでは、クラウドフォーメーションでエスエルオーを作るハンズオンに進みます。

### Visual Notes

- Candidate -> team judgment -> SLO baseline
- Arrow to Section 5 SLO hands-on
- Section 4 wrap-up

## QA Notes

- `lectures.md` の Lecture 4-4 に合わせて構成
- SLO Recommendationsは単独サービス名ではなく、Application SignalsのSLO推奨値機能として説明
- 読み上げでは「エスエルオー推奨値」に統一
- 8枚構成。Section 5のSLOハンズオンへ接続
- CEOコメント反映: 「次: CloudFormation」表記は「次: SLOハンズオン」へ寄せる
