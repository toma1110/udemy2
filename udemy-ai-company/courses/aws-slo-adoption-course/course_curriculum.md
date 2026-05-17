# AWSで学ぶSLO導入実践 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-slo-adoption-course`
- Course Title: `AWSで学ぶSLO導入実践: SLI設計・エラーバジェット・SRE運用レビュー`
- Public Repo: `https://github.com/toma1110/sre-slo-introduction-cfn-templates`
- Target Lecture Count: 35
- Current Audit Result: 2026-05-17時点で通常レクチャー35本、合計約86.5分。動画数と尺はUdemy標準コース要件を満たしている。

## Curriculum Review Gate

- `course_spec.md` をSource of Truthとする。`lectures.md` はSource of Truthにしない。
- CloudFormation create、update、delete、smoke test、Application Signals関連検証はCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- 音声はVOICEVOXを使う。
- WorkerとReviewerは分離する。

## Section 1: SLO導入で解決する現場課題

Section Learning Goal: SLO導入でよく起きる現場課題を整理し、このコースで学ぶ全体像とSREを目指す人にとっての学習価値を説明できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | このコースで解決するSLO導入あるある | SLO導入でよく起きる現場課題を整理し、この講座で解決する範囲を説明できる | なし | なし | Produced |
| 2 | SREを目指す人がSLOを学ぶ理由 | SREにおけるSLOの役割を理解し、信頼性を数値で扱う必要性を説明できる | なし | なし | Produced |
| 3 | コース全体のロードマップ | コース全体の学習順序と、設計、計測、運用レビューまでの流れを把握できる | なし | なし | Produced |

## Section 2: SLI、SLO、SLA、エラーバジェットの関係

Section Learning Goal: SLI、SLO、SLA、エラーバジェットの違いと関係を整理し、信頼性を数値で扱うための基本用語を説明できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | SLI、SLO、SLAを一枚で理解する | SLI、SLO、SLAの違いを整理し、それぞれの役割を説明できる | なし | なし | Produced |
| 2 | エラーバジェットは何を決めるための数字か | エラーバジェットがリリース判断や改善判断に使われる理由を説明できる | なし | なし | Produced |
| 3 | SLO導入前に確認する現場の前提条件 | SLO導入前に必要なサービス範囲、ユーザー体験、運用体制の前提を確認できる | なし | なし | Produced |

## Section 3: ユーザー体験からSLIを選ぶ

Section Learning Goal: ユーザー体験に近いSLIを選ぶ観点を理解し、可用性、レイテンシ、エラー率、AWSサービス別の候補指標を整理できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | 良いSLIの3条件 | 良いSLIに必要な、ユーザー体験との近さ、計測可能性、改善行動へのつながりを説明できる | なし | なし | Produced |
| 2 | 可用性、レイテンシ、エラー率を設計する | 可用性、レイテンシ、エラー率をSLO候補として整理し、自サービスに合う指標を選べる | なし | なし | Produced |
| 3 | p95/p99を使う理由 | 平均値だけでは見逃す遅延を理解し、p95/p99を使う場面を説明できる | なし | なし | Produced |
| 4 | AWSサービス別SLI選定ガイド | ALB、API Gateway、ECS、Lambda、RDSなどAWSサービス別にSLI候補を整理できる | なし | なし | Produced |
| 5 | CPU使用率をSLIにしない理由 | CPU使用率など内部指標と、ユーザー体験に近いSLIの違いを説明できる | なし | なし | Produced |

## Section 4: AWSでSLOを計測する

Section Learning Goal: CloudWatch MetricsとApplication SignalsでSLOを計測する考え方を理解し、period-based SLO、request-based SLO、SLO Recommendationsの使いどころを説明できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | CloudWatch MetricsでSLIを表現する | CloudWatch Metricsで可用性、レイテンシ、エラー率を表現する考え方を理解できる | なし | なし | Produced |
| 2 | Application SignalsでLatencyとAvailabilityを見る | CloudWatch Application SignalsでLatencyとAvailabilityを見る流れと前提条件を説明できる | なし | なし | Produced |
| 3 | period-based SLOとrequest-based SLO | period-based SLOとrequest-based SLOの違いを理解し、使い分けを説明できる | なし | なし | Produced |
| 4 | SLO Recommendationsの使いどころ | SLO Recommendationsを使う前提、30日データ、実アプリ計装が必要な理由を説明できる | なし | なし | Produced |

## Section 5: CloudFormationでSLO基盤を作る

Section Learning Goal: CloudFormationで低コストなSLO監視基盤を作成し、validate、create、smoke test、update、deleteまでREADME通りに再現できる。

Hands-on Resource Title: `SLO CloudFormationハンズオン README`

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | ハンズオン構成とコスト注意 | ハンズオンで作成するCloudWatch、SNS、Dashboard、SLO関連リソースと料金注意点を把握できる | あり | SLO CloudFormationハンズオン README | Produced |
| 2 | CloudFormationテンプレートを読む | CloudFormationテンプレート内のParameters、Resources、Outputs、SLO関連リソースの役割を読める | あり | CloudFormationテンプレート | Produced |
| 3 | SLO、Alarm、SNS、Dashboardを作成する | READMEに沿ってSLO監視スタックを作成し、作成されるリソースを確認できる | あり | クイックスタート手順 | Produced |
| 4 | smoke testでSLO基盤を確認する | `smoke_test.sh` でAlarm、Dashboard、SNSなどの作成結果を確認できる | あり | smoke_test.sh | Produced |
| 5 | updateとdeleteまで確認する | スタック更新と削除まで実行し、ハンズオン後に課金を止める流れを確認できる | あり | validate.sh | Produced |

## Section 6: エラーバジェットとバーンレート

Section Learning Goal: SLO目標値からエラーバジェットを計算し、バーンレートと短期窓・長期窓を使ってアラート設計に落とし込める。

Hands-on Resource Title: `バーンレートAlarm CloudFormationテンプレート`

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | エラーバジェットの計算 | SLO目標値から許容できる失敗量を計算し、エラーバジェットの意味を説明できる | なし | なし | Produced |
| 2 | バーンレートとは何か | バーンレートがエラーバジェット消費速度を表すことを理解し、アラート判断に使える | なし | なし | Produced |
| 3 | 短期窓と長期窓の組み合わせ | 短期窓と長期窓を組み合わせ、急激な悪化と継続的な悪化を分けて捉えられる | なし | なし | Produced |
| 4 | バーンレートAlarmを設計する | CloudWatch Alarmで高速バーンレート、低速バーンレートの通知条件を確認できる | あり | バーンレートAlarm CloudFormationテンプレート | Produced |

## Section 7: SLOダッシュボードを作る

Section Learning Goal: 運用担当者向けとマネジメント向けで見るべき指標を分け、SLO達成率、エラーバジェット、バーンレートを説明できる。

Hands-on Resource Title: `SLO Dashboard確認手順`

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | 見るべき指標と見せるべき指標 | 運用担当者向けの詳細指標と、PMやマネジメント向けの説明指標を分けられる | なし | なし | Produced |
| 2 | 運用担当向けダッシュボード | CloudWatch DashboardでSLO達成率、レイテンシ、エラー率、バーンレートを確認できる | あり | SLO Dashboard確認手順 | Produced |
| 3 | マネジメント向けSLOレポート | 技術指標を意思決定に使えるSLOレポートとして要約する観点を理解できる | なし | なし | Produced |

## Section 8: SLOを組織に導入する

Section Learning Goal: SLOを開発チーム、PM、経営層へ説明し、エラーバジェットをリリース判断や改善優先度に結びつける進め方を整理できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | SLO導入が失敗する3つのパターン | SLOが形骸化する原因を理解し、導入時に避けるべきパターンを説明できる | なし | なし | Produced |
| 2 | 開発チームへの説明と巻き込み方 | 開発チームにSLOの目的、責任範囲、改善アクションを説明する流れを作れる | なし | なし | Produced |
| 3 | PM、経営層への報告テンプレート | PMや経営層へ信頼性の状態と改善判断を報告する観点を整理できる | なし | なし | Produced |
| 4 | リリース判断とエラーバジェット | エラーバジェットをリリース判断、改善優先度、運用判断に結びつけて説明できる | なし | なし | Produced |

## Section 9: SLOレビューを運用に組み込む

Section Learning Goal: 週次・月次SLOレビュー、インシデント対応、ポストモーテムをつなげ、SLOを継続的に改善する運用サイクルを説明できる。

Hands-on Resource Title: なし

| Lecture | Lecture Title | Learning Goal | Hands-on | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- | --- |
| 1 | 週次SLOレビューの進め方 | 週次レビューで見るべき指標、議題、改善アクションの決め方を説明できる | なし | なし | Produced |
| 2 | 月次SLOレビューの進め方 | 月次レビューで傾向、改善効果、次月のアクションを整理する流れを説明できる | なし | なし | Produced |
| 3 | インシデント対応とSLOの連動 | インシデント対応、ポストモーテム、SLO改善をつなげる考え方を説明できる | なし | なし | Produced |
| 4 | このコースで学んだことの総整理 | SLI設計、SLO定義、エラーバジェット、CloudWatchでの可視化、運用レビューまでの全体像を説明できる | なし | なし | Produced |

## Definition of Done

- 通常レクチャー35本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CloudFormation検証はCEO承認後に実行され、validate、create、update、smoke test、delete結果がQAへ残っている。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
