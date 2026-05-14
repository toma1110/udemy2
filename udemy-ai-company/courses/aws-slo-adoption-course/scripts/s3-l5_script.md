# Section 3 Lecture 5 台本

## Title

CPU使用率をSLIにしない理由

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`

## Slide 1

### Slide Title

CPU使用率をSLIにしない理由

### Slide Message

内部状態とユーザー体験を混同しない

### Narration

このレクチャーでは、シーピーユー使用率をエスエルアイにしない理由を説明します。シーピーユー使用率は重要な監視項目です。しかし、ユーザー体験そのものではありません。エスエルアイとして主役にするのではなく、体験悪化を調べるための補助指標として扱います。

### Visual Notes

- CPUメーターとユーザー満足度を分離
- 「Internal Metric」と「User Experience」を対比
- 補助指標としての位置づけを表示

## Slide 2

### Slide Title

CPUは内部状態

### Slide Message

ユーザーが見ているのは、成功と待ち時間

### Narration

シーピーユー使用率は、サーバーやコンテナの内部状態です。ユーザーが直接見ているのは、処理が成功したか、どれくらい待たされたかです。内部状態が悪くても、ユーザー体験が保たれているなら、急いでリリースを止める判断にはなりません。反対に、内部状態がよく見えても、体験が悪いことはあります。

### Visual Notes

- 内部メトリクスと外部体験の2レイヤー
- Success、Latency、Error Rateを外側に配置
- CPUは内側の診断要素として表示

## Slide 3

### Slide Title

高いCPUが悪いとは限らない

### Slide Message

負荷に応じて効率よく使えている場合もある

### Narration

シーピーユー使用率が高いこと自体は、必ずしも悪い状態ではありません。アクセスが多い時間帯に、リソースを効率よく使えているだけかもしれません。オートスケーリングが効いていて、成功率や待ち時間が守られているなら、ユーザー体験としては問題が小さい可能性があります。

### Visual Notes

- 高CPUでも成功率とレイテンシが正常な例
- 負荷増加とスケールアウトの図
- 「高い = 失敗ではない」を表示

## Slide 4

### Slide Title

低いCPUでも体験は悪化する

### Slide Message

待ち時間の原因はCPU以外にもある

### Narration

反対に、シーピーユー使用率が低くても、ユーザー体験が悪くなることがあります。データベース待ち、外部サービス待ち、ロック競合、ネットワーク遅延などが原因です。この場合、シーピーユーだけを見ていると、問題がないように見えてしまいます。だから、体験指標を先に見る必要があります。

### Visual Notes

- 低CPUだが応答遅延が大きい例
- DB wait、external dependency、network latencyを補助ラベル
- 「CPUだけでは見えない」を強調

## Slide 5

### Slide Title

SLIは外側、原因分析は内側

### Slide Message

まず体験を見て、次に内部メトリクスで調べる

### Narration

設計の順番は、まず外側の体験を見ることです。成功率、待ち時間、エラー率をエスエルアイとして見ます。そこで悪化が分かったら、内側のメトリクスで原因を調べます。シーピーユー、メモリ、データベース、キューの長さは、この原因分析で力を発揮します。

### Visual Notes

- 外側にSLI、内側に診断メトリクスの同心円
- 悪化検知から原因分析へ矢印
- CPU、Memory、DB、Queueを内側に配置

## Slide 6

### Slide Title

アラートの主語を変える

### Slide Message

「CPUが高い」より「ユーザー体験が悪い」を優先する

### Narration

アラート設計でも、主語を変えます。シーピーユーが高いから起こすのではなく、ユーザー体験が悪いから起こす、という考えかたです。もちろん、シーピーユーのアラートをゼロにする必要はありません。ただし、信頼性の重要アラートは、成功率や待ち時間の悪化を中心にします。

### Visual Notes

- Bad: CPU high alert
- Good: User impact alert
- 補助アラートと重要アラートの階層

## Slide 7

### Slide Title

CPUは捨てない

### Slide Message

SLIではなく、診断と容量計画に使う

### Narration

シーピーユー使用率をエスエルアイにしないと言っても、捨てるわけではありません。シーピーユーは、原因分析、容量計画、コスト最適化に役立ちます。違いは、目的です。ユーザー体験を説明する主役ではなく、体験悪化の理由を探すための材料として使います。

### Visual Notes

- CPUの用途: Diagnosis、Capacity、Cost
- SLIではないが重要、というバランス
- 捨てるのではなく役割を分ける図

## Slide 8

### Slide Title

まとめ: ユーザー体験を先に置く

### Slide Message

CPU使用率は補助指標として活かす

### Narration

まとめです。シーピーユー使用率は内部状態であり、ユーザー体験そのものではありません。エスエルアイは、成功率、待ち時間、エラー率のように、ユーザーの困りごとに近い指標から選びます。シーピーユーは、悪化の原因を調べる補助指標として活かします。

### Visual Notes

- User Experience first、Internal metrics secondの構図
- Section 3全体の3指標を再掲
- Section 4「AWSでSLOを計測する」へ矢印

## QA Notes

- `lectures.md` の Lecture 3-5 に合わせて構成
- CPUの読みはナレーション内で「シーピーユー」に統一
- CPU監視を否定せず、SLIと診断メトリクスの役割分担を説明
- 8枚構成。Section 4のAWS計測へ接続
