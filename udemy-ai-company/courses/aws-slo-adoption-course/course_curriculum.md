# AWSで学ぶSLO導入実践 カリキュラム入力表

このファイルはUdemyのコースカリキュラム作成時に使うレクチャー一覧です。`course_spec.md` と `lectures.md` をSource of Truthとして、各レクチャーで受講後に身についていること、ハンズオン有無、PublicRepo URLを明記します。

PublicRepo: https://github.com/toma1110/sre-slo-introduction-cfn-templates

| Section | Lecture | レクチャータイトル | レクチャー完了後に身についていること | ハンズオン |
| --- | --- | --- | --- | --- |
| 1 | 1 | このコースで解決するSLO導入あるある | SLO導入でよく起きる現場課題を整理し、この講座で解決する範囲を説明できる | なし |
| 1 | 2 | SREを目指す人がSLOを学ぶ理由 | SREにおけるSLOの役割を理解し、信頼性を数値で扱う必要性を説明できる | なし |
| 1 | 3 | コース全体のロードマップ | コース全体の学習順序と、設計、計測、運用レビューまでの流れを把握できる | なし |
| 2 | 1 | SLI、SLO、SLAを一枚で理解する | SLI、SLO、SLAの違いを整理し、それぞれの役割を説明できる | なし |
| 2 | 2 | エラーバジェットは何を決めるための数字か | エラーバジェットがリリース判断や改善判断に使われる理由を説明できる | なし |
| 2 | 3 | SLO導入前に確認する現場の前提条件 | SLO導入前に必要なサービス範囲、ユーザー体験、運用体制の前提を確認できる | なし |
| 3 | 1 | 良いSLIの3条件 | 良いSLIに必要な、ユーザー体験との近さ、計測可能性、改善行動へのつながりを説明できる | なし |
| 3 | 2 | 可用性、レイテンシ、エラー率を設計する | 可用性、レイテンシ、エラー率をSLO候補として整理し、自サービスに合う指標を選べる | なし |
| 3 | 3 | p95/p99を使う理由 | 平均値だけでは見逃す遅延を理解し、p95/p99を使う場面を説明できる | なし |
| 3 | 4 | AWSサービス別SLI選定ガイド | ALB、API Gateway、ECS、Lambda、RDSなどAWSサービス別にSLI候補を整理できる | なし |
| 3 | 5 | CPU使用率をSLIにしない理由 | CPU使用率など内部指標と、ユーザー体験に近いSLIの違いを説明できる | なし |
| 4 | 1 | CloudWatch MetricsでSLIを表現する | CloudWatch Metricsで可用性、レイテンシ、エラー率を表現する考え方を理解できる | なし |
| 4 | 2 | Application SignalsでLatencyとAvailabilityを見る | CloudWatch Application SignalsでLatencyとAvailabilityを見る流れと前提条件を説明できる | なし |
| 4 | 3 | period-based SLOとrequest-based SLO | period-based SLOとrequest-based SLOの違いを理解し、使い分けを説明できる | なし |
| 4 | 4 | SLO Recommendationsの使いどころ | SLO Recommendationsを使う前提、30日データ、実アプリ計装が必要な理由を説明できる | なし |
| 5 | 1 | ハンズオン構成とコスト注意 | ハンズオンで作成するCloudWatch、SNS、Dashboard、SLO関連リソースと料金注意点を把握できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates |
| 5 | 2 | CloudFormationテンプレートを読む | CloudFormationテンプレート内のParameters、Resources、Outputs、SLO関連リソースの役割を読める | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates/blob/main/template.yaml |
| 5 | 3 | SLO、Alarm、SNS、Dashboardを作成する | READMEに沿ってSLO監視スタックを作成し、作成されるリソースを確認できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates#クイックスタート |
| 5 | 4 | smoke testでSLO基盤を確認する | `smoke_test.sh` でAlarm、Dashboard、SNSなどの作成結果を確認できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates/blob/main/smoke_test.sh |
| 5 | 5 | updateとdeleteまで確認する | スタック更新と削除まで実行し、ハンズオン後に課金を止める流れを確認できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates/blob/main/validate.sh |
| 6 | 1 | エラーバジェットの計算 | SLO目標値から許容できる失敗量を計算し、エラーバジェットの意味を説明できる | なし |
| 6 | 2 | バーンレートとは何か | バーンレートがエラーバジェット消費速度を表すことを理解し、アラート判断に使える | なし |
| 6 | 3 | 短期窓と長期窓の組み合わせ | 短期窓と長期窓を組み合わせることで、急激な悪化と継続的な悪化を分けて捉えられる | なし |
| 6 | 4 | バーンレートAlarmを設計する | CloudWatch Alarmで高速バーンレート、低速バーンレートの通知条件を確認できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates/blob/main/template.yaml |
| 7 | 1 | 見るべき指標と見せるべき指標 | 運用担当者向けの詳細指標と、PMやマネジメント向けの説明指標を分けて考えられる | なし |
| 7 | 2 | 運用担当向けダッシュボード | CloudWatch DashboardでSLO達成率、レイテンシ、エラー率、バーンレートを確認できる | あり: https://github.com/toma1110/sre-slo-introduction-cfn-templates#クイックスタート |
| 7 | 3 | マネジメント向けSLOレポート | 技術指標を、意思決定に使えるSLOレポートとして要約する観点を理解できる | なし |
| 8 | 1 | SLO導入が失敗する3つのパターン | SLOが形骸化する原因を理解し、導入時に避けるべきパターンを説明できる | なし |
| 8 | 2 | 開発チームへの説明と巻き込み方 | 開発チームにSLOの目的、責任範囲、改善アクションを説明する流れを作れる | なし |
| 8 | 3 | PM、経営層への報告テンプレート | PMや経営層へ、信頼性の状態と改善判断を分かりやすく報告する観点を整理できる | なし |
| 8 | 4 | リリース判断とエラーバジェット | エラーバジェットをリリース判断、改善優先度、運用判断に結びつけて説明できる | なし |
| 9 | 1 | 週次SLOレビューの進め方 | 週次レビューで見るべき指標、議題、改善アクションの決め方を説明できる | なし |
| 9 | 2 | 月次SLOレビューの進め方 | 月次レビューで傾向、改善効果、次月のアクションを整理する流れを説明できる | なし |
| 9 | 3 | インシデント対応とSLOの連動 | インシデント対応、ポストモーテム、SLO改善をつなげる考え方を説明できる | なし |
| 9 | 4 | このコースで学んだことの総整理 | SLI設計、SLO定義、エラーバジェット、CloudWatchでの可視化、運用レビューまでの全体像を説明できる | なし |
