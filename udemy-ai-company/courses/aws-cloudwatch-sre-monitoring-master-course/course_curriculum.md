# AWS CloudWatch/SRE監視実践マスター カリキュラム入力表

このファイルはUdemyのコースカリキュラム作成時に使うレクチャー一覧です。`course_spec.md` をSource of Truthとして、各レクチャーで受講後に身についていること、ハンズオン有無、想定時間を明記します。

PublicRepo: 未作成。公開用テンプレートは `udemy-ai-company/public_repo/aws-cloudwatch-sre-monitoring-master-cfn-templates/` に作成する。

想定本編時間: 約700分（約11時間40分）

## Section 1: 長尺コースのロードマップとAWS学習安全

セクションの学習目標: この長尺コースの到達点、短尺講座との違い、AWSハンズオン前の安全確認を説明できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | このコースで作るCloudWatch/SRE監視運用 | コース全体で扱うログ調査、通知設計、Runbook、SLOレビューの流れを説明できる | なし | なし | 7 |
| 2 | 短尺講座と長尺旗艦コースの違い | 短尺講座の単純連結ではなく、統合演習と設計レビューを追加する理由を理解できる | なし | なし | 8 |
| 3 | ハンズオン前のAWS安全チェック | リージョン、認証情報、料金、削除手順、権限を事前確認できる | あり | ハンズオン前チェックリスト | 7 |
| 4 | CloudFormationとCDK/Terraformの位置づけ | 教材ではCloudFormation、実運用ではCDKまたはTerraformを推奨する理由を説明できる | なし | なし | 8 |

## Section 2: CloudWatchの全体像

セクションの学習目標: CloudWatchの主要機能を監視、可観測性、インシデント対応、SLO運用の中で位置づけられる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | CloudWatchの地図を作る | Metrics、Logs、Alarm、Dashboard、Application Signalsの関係を説明できる | なし | なし | 10 |
| 2 | 監視と可観測性の違い | 何を事前に監視し、何を調査で掘るかを分けて説明できる | なし | なし | 10 |
| 3 | インシデント対応から逆算するCloudWatch | アラート、ログ、メトリクス、ダッシュボードを初動対応の流れに配置できる | なし | なし | 10 |
| 4 | CloudWatch料金で注意するポイント | Logs Insights、Custom Metrics、Alarm、Dashboard、Application Signalsの課金ポイントを説明できる | なし | なし | 10 |
| 5 | 良い監視基盤の完成形 | 受講後に作るべき監視運用の全体像を言語化できる | なし | なし | 10 |

## Section 3: MetricsとDashboardの基礎

セクションの学習目標: CloudWatch Metricsの基本概念を理解し、運用担当者とマネジメントで見せる指標を分けられる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Namespace、Metric、Dimensionを理解する | CloudWatch Metricsの基本単位を説明できる | なし | なし | 10 |
| 2 | Statistic、Period、Datapointの読み方 | Average、Sum、p95などの使い分けを説明できる | なし | なし | 10 |
| 3 | Custom Metricsを教材ハンズオンで使う理由 | 低コストで再現しやすいサンプル指標の作り方を理解できる | あり | Custom Metrics投入手順 | 10 |
| 4 | Dashboardで見るべき指標を選ぶ | 運用担当者向けに異常検知と調査に使う指標を選べる | あり | CloudWatch Dashboard設計演習 | 10 |
| 5 | マネジメント向けに見せる指標を分ける | 技術指標を意思決定に使える説明指標へ変換できる | なし | なし | 10 |

## Section 4: CloudWatch LogsとLogs Insights

セクションの学習目標: Logs Insightsで障害調査に必要な基本クエリを書き、検索範囲とコストを制御できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Log Group、Log Stream、保持期間 | CloudWatch Logsの保存単位と保持期間を説明できる | なし | なし | 10 |
| 2 | Logs Insightsを安全に使う基本 | 検索対象Log Groupと時間範囲を絞り、不要な料金を避けられる | あり | Logs Insights安全実行チェック | 12 |
| 3 | `fields`、`filter`、`sort` の基本 | 必要な列を表示し、条件で絞り、時系列で確認できる | あり | 基本クエリ集 | 12 |
| 4 | `parse` でログから値を取り出す | 非構造ログやJSONログから調査に必要な値を抽出できる | あり | parse演習クエリ | 12 |
| 5 | `stats` でエラー傾向を集計する | エラー数、ステータスコード、パス別集計を作れる | あり | stats演習クエリ | 12 |
| 6 | 障害調査クエリをRunbookへ入れる | 調査クエリを初動対応手順として再利用できる形に整理できる | あり | Runbook用クエリ集 | 10 |

## Section 5: Alarm、SNS、通知設計

セクションの学習目標: CloudWatch AlarmとSNS通知を作るだけでなく、通知疲れを避けるSeverity、Owner、Runbookリンクを設計できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Metric Alarmの基本構造 | Threshold、Evaluation Period、Datapoints to Alarmを説明できる | なし | なし | 10 |
| 2 | Missing Dataと誤通知の考え方 | データ欠落時の扱いが通知品質に与える影響を説明できる | なし | なし | 12 |
| 3 | SNS通知と確認メール | SNS TopicとSubscriptionの役割、メール確認の流れを理解できる | あり | SNS通知ハンズオン | 12 |
| 4 | Composite Alarmでノイズを減らす | 複数条件を組み合わせて通知を絞る考え方を説明できる | あり | Composite Alarm設計演習 | 12 |
| 5 | Severity、Owner、Runbookリンク | アラートに対応者、重要度、初動手順を結びつけられる | あり | アラート設計シート | 10 |
| 6 | 良いアラートと悪いアラートのレビュー | 通知すべきアラートとダッシュボードで見るだけの指標を分けられる | なし | なし | 12 |

## Section 6: CloudFormationで監視基盤を作る

セクションの学習目標: 教材用CloudFormationテンプレートを読み、validate、create、update、smoke test、deleteまでREADME通りに再現できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | 統合ハンズオンの構成を読む | 作成するLog Group、Alarm、SNS、Dashboard、サンプルメトリクスを説明できる | あり | 統合ハンズオンREADME | 12 |
| 2 | CloudFormationテンプレートを読む | Parameters、Resources、Outputsの役割を理解できる | あり | template.yaml解説 | 12 |
| 3 | validateとcreate | `aws cloudformation validate-template` とstack createの流れを実行できる | あり | validate.sh | 12 |
| 4 | smoke testで作成結果を確認する | Alarm、SNS、Dashboard、Log Groupの存在を確認できる | あり | smoke_test.sh | 12 |
| 5 | updateで変更を反映する | Alarm閾値やDashboardを安全に変更する流れを確認できる | あり | update演習 | 12 |
| 6 | deleteとコスト確認 | スタック削除と残リソース確認でハンズオンを終了できる | あり | deleteチェックリスト | 12 |

## Section 7: Application SignalsとAPMの入口

セクションの学習目標: Application Signalsを、従来のCloudWatch監視、ログ調査、SLO運用と接続して使いどころから判断できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Application Signalsで何が見えるか | Service Map、Latency、Availability、Fault、Errorの意味を説明できる | なし | なし | 10 |
| 2 | 実アプリ計装とADOTの前提 | Application Signalsを使うために必要な計装と運用前提を理解できる | なし | なし | 12 |
| 3 | Service Mapから原因仮説を作る | 依存関係、遅延、エラー箇所から調査方針を組み立てられる | なし | なし | 12 |
| 4 | Application SignalsのSLO機能 | Latency、Availability、period-based、request-based SLOの概要を説明できる | なし | なし | 12 |
| 5 | SLO Recommendationsと30日データ | 推奨値が過去データに依存する理由と使いどころを説明できる | なし | なし | 12 |
| 6 | Alarm、Logs Insightsとの使い分け | APMで見つけ、Alarmで気づき、Logs Insightsで掘る流れを説明できる | なし | なし | 12 |

## Section 8: SLI/SLO、エラーバジェット、バーンレート

セクションの学習目標: SLI、SLO、SLA、エラーバジェットの違いを理解し、AWSメトリクスと運用判断へ接続できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | SLI、SLO、SLAを一枚で理解する | 3つの違いと関係を説明できる | なし | なし | 10 |
| 2 | ユーザー体験からSLIを選ぶ | 可用性、レイテンシ、エラー率をユーザー体験から選べる | なし | なし | 12 |
| 3 | SLO目標値を決める | 99%、99.9%、99.95%の違いと現実的な目標値を考えられる | なし | なし | 12 |
| 4 | エラーバジェットを計算する | SLO目標値から許容失敗量を説明できる | あり | エラーバジェット計算シート | 10 |
| 5 | バーンレートを通知設計に入れる | 急激な悪化と継続的な悪化を分けて捉えられる | あり | バーンレートAlarm設計 | 12 |

## Section 9: Runbookと初動対応

セクションの学習目標: アラート発生後の5分、15分、30分で見るべき情報、残す証跡、エスカレーションをRunbook化できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Runbookは何を書くべきか | 前提、影響確認、調査手順、暫定対応、復旧確認を整理できる | なし | なし | 10 |
| 2 | アラート後5分の初動 | 影響範囲、現在状態、エスカレーション要否を確認できる | あり | 5分初動Runbook | 12 |
| 3 | アラート後15分の調査 | Logs Insights、Dashboard、Application Signalsの順に調査できる | あり | 15分調査Runbook | 12 |
| 4 | アラート後30分の判断 | 暫定対応、告知、ロールバック、継続監視を判断できる | あり | 30分判断Runbook | 12 |
| 5 | Runbookレビューと改善 | 実行後に不足手順と自動化候補を改善バックログへ入れられる | あり | Runbookレビューシート | 12 |

## Section 10: AWS学習安全とトラブルシュート

セクションの学習目標: AWSハンズオンで詰まりやすい課金不安、CloudFormation rollback、IAM AccessDeniedを安全に切り分けられる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | 課金不安を下げる確認手順 | 作成リソース、削除手順、Cost Explorer、Budgetsの確認観点を説明できる | あり | コスト安全チェック | 12 |
| 2 | CloudFormation rollbackを読む | Stack status、Events、Status Reasonから失敗原因を追える | あり | rollback読解演習 | 12 |
| 3 | IAM AccessDeniedを切り分ける | エラー文、対象Action、Resource、ポリシー種類を確認できる | あり | AccessDenied切り分けシート | 12 |
| 4 | 失敗時の証跡を残す | CLI出力、Stack Events、ログ、スクリーンショットの保存観点を説明できる | あり | 証跡保存テンプレート | 12 |
| 5 | 学習環境を閉じる最終確認 | スタック削除、SNS購読、Dashboard、Log Group、料金を確認できる | あり | クリーンアップチェックリスト | 12 |

## Section 11: 統合Capstone: CloudWatch/SRE監視運用を作る

セクションの学習目標: サンプルサービスの監視要求を読み、Logs Insights、Alarm、Dashboard、Runbook、SLOレビューを統合して設計できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | Capstoneシナリオを読む | サンプルサービスの構成、ユーザー体験、監視要求を把握できる | あり | Capstone要求定義 | 10 |
| 2 | 監視対象とSLI候補を決める | 可用性、レイテンシ、エラー率から最初に測る指標を選べる | あり | SLI設計ワークシート | 12 |
| 3 | Logs Insightsクエリを作る | 障害調査で使うエラー抽出、集計、時系列クエリを作れる | あり | Capstone Logs Insights演習 | 14 |
| 4 | Alarm、Dashboard、Runbookを統合する | 通知、可視化、初動対応を1つの運用設計にまとめられる | あり | Capstone監視基盤演習 | 14 |
| 5 | 障害調査シミュレーション | アラート発生から原因仮説、影響説明、暫定対応までを実施できる | あり | インシデント演習 | 12 |
| 6 | SLOレビュー会議を行う | エラーバジェット、改善アクション、次月の運用改善を説明できる | あり | SLOレビュー議事録テンプレート | 12 |

## Section 12: 運用改善と次の学習パス

セクションの学習目標: コースで作った監視運用を継続改善し、実運用IaCや本番計装へ発展させる道筋を説明できる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン | ハンズオンリソースタイトル | 想定分 |
| --- | --- | --- | --- | --- | --- |
| 1 | 週次レビューの進め方 | アラート、ログ、SLO、Runbook改善を週次で確認できる | なし | なし | 10 |
| 2 | 月次レビューと改善バックログ | 信頼性の傾向を整理し、改善優先度を決められる | なし | なし | 12 |
| 3 | CDK/Terraformへ発展させる | 教材CloudFormationから実運用IaCへ移す観点を説明できる | なし | なし | 12 |
| 4 | このコースの総整理 | CloudWatch/SRE監視運用の全体像と次の実践ステップを説明できる | なし | なし | 10 |

## Curriculum Definition of Done

- 60前後のレクチャーで10〜12時間の学習量になっている
- 短尺講座と重複する前提説明だけでなく、章末演習と統合演習がある
- CloudFormationハンズオンは作成、更新、smoke test、削除まで含む
- Logs Insights、Alarm/SNS、Application Signals、SLO、Runbook、学習安全が一続きで学べる
- AWSリソース作成を伴う検証はCEO承認後にのみ行う
- 完成動画のスライドはGPT-Image2由来PNGのみを使う
- ナレーションはVOICEVOXを前提にする
