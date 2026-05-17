# Application Signalsハンズオン設計

このハンズオンは、CloudWatch Application Signalsを実アプリの通信で体験するための設計メモです。

## 実行前チェック

- AWS料金が発生する可能性を理解している
- `AWS_REGION` を決めている
- CloudFormation、Lambda、IAM、CloudWatch、EventBridge Schedulerを操作できる
- Application Signalsが対象リージョンで利用できる
- ハンズオン後に自動トラフィック停止とstack deleteを実行できる

## 標準アーキテクチャ案

初版はLambda中心の短時間ハンズオンにします。

```text
EventBridge Scheduler
  -> Traffic Generator Lambda
      -> Sample API Lambda Function URL
          -> normal / slow / error response

Application Signals
  -> Services
  -> Application Map
  -> Service detail
  -> SLO
```

## トラフィック方針

- 標準は1分に1回程度
- 1回の実行で1から数リクエストに抑える
- 高負荷テストにしない
- 停止コマンドを必須にする
- 長時間放置しない

## シナリオ

| Scenario | Behavior | Learning Point |
| --- | --- | --- |
| `normal` | 短時間で200応答 | 正常時のLatency、Availability、Call volume |
| `slow` | 意図的に待機して200応答 | Latency悪化の見え方 |
| `error` | 標準では100%例外発生 | Fault/ErrorとSLO悪化の見え方 |
| `recovery` | 正常応答へ戻す | 回復後の画面確認 |

## Servicesを確認する

確認観点:

- サービス名が表示されているか
- Call volumeが増えているか
- Latencyがシナリオに応じて変化しているか
- Fault/Errorがエラーシナリオで増えるか
- SLOを作った場合、SLI healthが確認できるか

## Application Mapを確認する

確認観点:

- サンプルアプリと依存関係がどう表示されるか
- 異常がどのノードやエッジに出るか
- MapからService detailへ進めるか

## Service detailを確認する

確認観点:

- Latency、Availability、Fault、Errorの時系列
- 正常、遅延、エラーの切り替えとグラフ変化
- 関連ログやトレースへの導線
- 運用担当が次に見るべき情報

## SLOを確認する

初版ではApplication Signals SLOを1つ作成します。

候補:

- Latency SLO
- Availability SLO

短時間ハンズオンでは、SLO RecommendationsやPerformance Reportの完成確認は対象外です。これらは実アプリ計装と十分なデータ期間が必要な機能として説明します。

## 停止と削除

必須順序:

1. 自動トラフィックを停止する
2. Application Signals画面で通信が止まることを確認する
3. CloudFormation stackを削除する
4. 残存ロググループ、SLO、サービスリンクロールの扱いを確認する
5. Billing / Cost Explorerで費用確認の導線を確認する

## 未決事項

- Lambda Application Signals用のOpenTelemetry Layer ARNの扱い
- 対応リージョンの初期リスト
- Function URLを使うかAPI Gatewayを使うか
- トラフィック生成LambdaにもApplication Signalsを有効化するか
- SLOをCloudFormationで作るか、画面操作で作るか
