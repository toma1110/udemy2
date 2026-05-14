# Section 3 Lecture 4 台本

## Title

AWSサービス別SLI選定ガイド

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`

## Slide 1

### Slide Title

AWSサービス別SLI選定ガイド

### Slide Message

サービス名からではなく、ユーザー体験から逆算する

### Narration

このレクチャーでは、エーダブリューエスサービス別に、エスエルアイの候補を整理します。ただし、サービス名から機械的に決めるのではありません。最初に考えるのは、ユーザーが何を達成したいのかです。その体験を測るために、どのメトリクスを使うかを選びます。

### Visual Notes

- User Journeyを起点に、ALB、API Gateway、ECS、Lambda、RDSへ分岐
- サービスロゴ風ではなく抽象アイコンで統一
- 「Service firstではなくExperience first」を表示

## Slide 2

### Slide Title

ALB: 入口の成功と遅さ

### Slide Message

外部リクエストの成功率と応答時間を見る

### Narration

エーエルビーでは、外部から入ってくるリクエストの成功率と応答時間が候補になります。5系のエラーが増えていないか。ターゲットまで含めた応答時間が悪化していないか。入口に近いので、ユーザーから見たサービス全体の状態をつかみやすいのが特徴です。

### Visual Notes

- Internet → ALB → Targetのシンプルな流れ
- HTTPCode_Target_5XX_Count、TargetResponseTimeを表示テキストとして扱う
- 成功率と応答時間の2軸

## Slide 3

### Slide Title

API Gateway: API利用者の体験

### Slide Message

成功、失敗、レイテンシをエンドポイント単位で見る

### Narration

エーピーアイゲートウェイでは、利用者から見たエーピーアイの成功、失敗、レイテンシが候補になります。すべてのエンドポイントをまとめると、重要な操作の悪化が隠れることがあります。ログイン、決済、検索のような主要操作ごとに見ると、ユーザー体験に近づきます。

### Visual Notes

- API Gatewayから複数エンドポイントへ分岐
- 主要操作ごとのSLIカード
- まとめすぎ注意のラベル

## Slide 4

### Slide Title

ECSとLambda: 実行基盤だけで判断しない

### Slide Message

基盤メトリクスは補助、体験メトリクスを主役にする

### Narration

イーシーエスやラムダでは、実行基盤のメトリクスに目が向きがちです。コンテナの利用率、関数の実行時間、失敗回数は重要です。ただし、それだけをエスエルアイの主役にすると、ユーザー体験から離れることがあります。入口の成功率や主要操作のレイテンシと組み合わせて見ます。

### Visual Notes

- ECS/Lambdaを内部実行基盤として配置
- ALB/API Gatewayと組み合わせる構図
- 「基盤メトリクスは補助」を強調

## Slide 5

### Slide Title

RDS: 直接のSLIではなく原因分析に使う

### Slide Message

データベース状態は、体験悪化の調査に使う

### Narration

アールディーエスでは、接続数、待ち時間、シーピーユー、ストレージなどを見ます。これらは重要ですが、多くの場合、ユーザー向けエスエルアイの直接の主役ではありません。画面が遅い、エラーが増えた、という体験悪化が起きたときに、原因を調べるための補助指標として使います。

### Visual Notes

- User request → App → RDSの流れ
- RDSメトリクスを診断パネルとして表示
- 主役SLIと補助メトリクスを分離

## Slide 6

### Slide Title

Application Signals: 体験に近い入口

### Slide Message

サービスレベルの可用性とレイテンシを扱いやすい

### Narration

アプリケーションシグナルは、サービスレベルの可用性やレイテンシを扱いやすくする機能です。エーダブリューエス環境でエスエルオーを作るときの有力な入口になります。ただし、実アプリの計装や一定期間のデータが必要になる場面があります。この講座では、考えかたと制約を分けて扱います。

### Visual Notes

- Application SignalsをSLO設計の入口として表示
- Availability、Latency、SLO Recommendationsのカード
- 「考えかた」と「制約」を分ける注記

## Slide 7

### Slide Title

サービス別ではなく操作別に整理する

### Slide Message

ログイン、検索、決済などの主要操作を軸にする

### Narration

最後に大事なのは、サービス別ではなく操作別に整理することです。エーエルビー、エーピーアイゲートウェイ、イーシーエス、ラムダ、アールディーエスは、ユーザー操作を支える部品です。ログイン、検索、決済のような主要操作を軸にすると、どの部品のメトリクスを使うべきかが見えやすくなります。

### Visual Notes

- User Journeyを横軸、AWSサービスを縦軸にしたマップ
- 操作ごとに関連メトリクスを結ぶ
- 「操作別に見る」を強調

## Slide 8

### Slide Title

まとめ: 体験からメトリクスへ

### Slide Message

ユーザー操作を決めてから、AWSメトリクスを選ぶ

### Narration

まとめです。エスエルアイは、エーダブリューエスサービス名から自動的に決まるものではありません。まずユーザー操作を決めます。次に、その操作の成功、待ち時間、失敗を測るメトリクスを選びます。入口に近い指標を主役にし、内部の指標は原因分析に使う。この順番で考えます。

### Visual Notes

- ユーザー操作 → SLI候補 → CloudWatchメトリクスの3段階
- 入口指標と内部指標の役割分担
- 次講義「CPU使用率をSLIにしない理由」へ矢印

## QA Notes

- `lectures.md` の Lecture 3-4 に合わせて構成
- 対象サービスは course_spec の ALB、API Gateway、ECS、Lambda、RDS を反映
- ナレーションではAWSサービス名を読み上げ用カタカナへ変換
- 8枚構成。サービス別メトリクスの羅列ではなく、ユーザー操作起点を強調
