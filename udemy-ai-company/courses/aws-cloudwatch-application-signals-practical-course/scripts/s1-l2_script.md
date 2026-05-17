# Section 1 Lecture 2 台本

### Title

ハンズオン構成とコスト安全策

## Slide 1

### Slide Title

小さく作って見る

### Slide Message

低頻度通信の学習環境

### Narration

このハンズオンでは、大きなシステムを作りません。ラムダのサンプルアプリと、低頻度で呼び出すラムダを作り、アプリケーションシグナルズで見える変化を確認します。 この講座のハンズオンは、長時間負荷をかけるための環境ではありません。短時間だけ通信を発生させ、画面にどう見えるかを確認するための学習環境です。作ったら観測し、見終わったら止めて削除する流れを必ずセットで扱います。

### Visual Notes

- Small learning lab
- Two Lambda functions
- Low-frequency pulse

## Slide 2

### Slide Title

標準構成

### Slide Message

SchedulerからLambdaへ

### Narration

流れはシンプルです。イベントブリッジスケジューラーがトラフィック生成用ラムダを呼び、そこからサンプルアプリ用ラムダを呼びます。公開用のエンドポイントは作りません。 標準構成では、トラフィックを発生させるラムダが、サンプルエーピーアイ用のラムダを低頻度で呼び出します。イベントブリッジスケジューラーは、通信を定期的に作る役割です。これにより、サービス一覧や地図で観測できる材料を作ります。

### Visual Notes

- EventBridge Scheduler to traffic Lambda to sample Lambda
- No public endpoint marker

## Slide 3

### Slide Title

4つのシナリオ

### Slide Message

正常、遅延、エラー、回復

### Narration

シナリオは、正常、遅延、エラー、回復の4つです。動きを切り替えることで、レイテンシやエラーが画面でどう見えるかを確認します。 正常だけでは、異常時に画面がどう変わるかを学べません。遅延シナリオではレイテンシの変化を見ます。エラーシナリオでは失敗率の変化を見ます。回復シナリオでは、戻ったあとも画面反映に時間差があることを確認します。

### Visual Notes

- Scenario cards: normal, slow, error, recovery
- Metrics change over time

## Slide 4

### Slide Title

料金の安全策

### Slide Message

低頻度、停止、削除

### Narration

アプリケーションシグナルズ、ログ、ラムダ、スケジューラー、エスエルオーでは、料金が発生する場合があります。だから通信は低頻度にし、止める手順と削除手順を必ず扱います。 料金面では、通信頻度を低くし、実行時間を短くし、不要になったら止めることが基本です。アプリケーションシグナルズ、ログ、エスエルオー、スケジューラーは料金に関係する可能性があります。金額は断定せず、公式料金ページと請求画面で確認します。

### Visual Notes

- Cost caution panel
- Stop traffic control
- Delete stack checklist

## Slide 5

### Slide Title

SLOは後から

### Slide Message

メトリクス確認後に作る

### Narration

エスエルオーは、最初の作成時には有効化しません。対象サービスがメトリクスを送った後で作る必要があるためです。まず通信を発生させ、見えることを確認してから有効化します。 エスエルオーは、サービスと操作のメトリクスが届いてから作る方が自然です。最初から目標だけ作るのではなく、まず通信を発生させ、サービス一覧と詳細画面で観測できることを確認し、そのあと目標へつなげます。

### Visual Notes

- Step 1 traffic and service discovery
- Step 2 enable SLO
- Avoid premature SLO creation

## Slide 6

### Slide Title

実行ルール

### Slide Message

作成系は承認後に実行

### Narration

クラウドフォーメーションの検証だけならリソースは作りません。一方で、作成、更新、削除はエーダブリューエス上の操作です。この教材制作では、承認後にだけ実行します。 クラウドフォーメーションでスタックを作る、更新する、削除する作業は、料金や環境変更に関係します。この制作では実行しません。受講者が実行する場合も、作成前に手順、停止方法、削除方法、対象リージョンを確認してから進めます。

### Visual Notes

- Validate only vs create update delete
- Approval gate
- AWS cost boundary
