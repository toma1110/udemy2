# aws-slo-adoption-course Lectures

このファイルは `course_spec.md` に基づく講義一覧です。制作時は1講義1成果物を原則とします。

## Section 1: SLO導入で解決する現場課題

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 1-1 | このコースで解決するSLO導入あるある | Concept | AI-Production-01 | AI-QA-01 |
| 1-2 | SREを目指す人がSLOを学ぶ理由 | Concept | AI-Production-01 | AI-QA-01 |
| 1-3 | コース全体のロードマップ | Concept | AI-Production-01 | AI-QA-01 |

## Section 2: SLI、SLO、SLA、エラーバジェットの関係

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 2-1 | SLI、SLO、SLAを一枚で理解する | Concept | AI-Production-01 | AI-QA-01 |
| 2-2 | エラーバジェットは何を決めるための数字か | Concept | AI-Production-01 | AI-QA-01 |
| 2-3 | SLO導入前に確認する現場の前提条件 | Work | AI-Production-01 | AI-QA-01 |

## Section 3: ユーザー体験からSLIを選ぶ

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 3-1 | 良いSLIの3条件 | Concept | AI-Production-01 | AI-QA-01 |
| 3-2 | 可用性、レイテンシ、エラー率を設計する | Concept | AI-Production-01 | AI-QA-01 |
| 3-3 | p95/p99を使う理由 | Concept | AI-Production-01 | AI-QA-01 |
| 3-4 | AWSサービス別SLI選定ガイド | Concept | AI-Production-01 | AI-QA-01 |
| 3-5 | CPU使用率をSLIにしない理由 | Concept | AI-Production-01 | AI-QA-01 |

## Section 4: AWSでSLOを計測する

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 4-1 | CloudWatch MetricsでSLIを表現する | Concept | AI-Production-01 | AI-QA-01 |
| 4-2 | Application SignalsでLatencyとAvailabilityを見る | Demo | AI-Production-01 | AI-QA-01 |
| 4-3 | period-based SLOとrequest-based SLO | Concept | AI-Production-01 | AI-QA-01 |
| 4-4 | SLO Recommendationsの使いどころ | Demo | AI-Production-01 | AI-QA-01 |

## Section 5: CloudFormationでSLO基盤を作る

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 5-1 | ハンズオン構成とコスト注意 | Hands-on | AI-Engineer-01 | AI-QA-01 |
| 5-2 | CloudFormationテンプレートを読む | Hands-on | AI-Engineer-01 | AI-QA-01 |
| 5-3 | SLO、Alarm、SNS、Dashboardを作成する | Hands-on | AI-Engineer-01 | AI-QA-01 |
| 5-4 | smoke testでSLO基盤を確認する | Hands-on | AI-Engineer-01 | AI-QA-01 |
| 5-5 | updateとdeleteまで確認する | Hands-on | AI-Engineer-01 | AI-QA-01 |

## Section 6: エラーバジェットとバーンレート

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 6-1 | エラーバジェットの計算 | Concept | AI-Production-01 | AI-QA-01 |
| 6-2 | バーンレートとは何か | Concept | AI-Production-01 | AI-QA-01 |
| 6-3 | 短期窓と長期窓の組み合わせ | Concept | AI-Production-01 | AI-QA-01 |
| 6-4 | バーンレートAlarmを設計する | Hands-on | AI-Engineer-01 | AI-QA-01 |

## Section 7: SLOダッシュボードを作る

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 7-1 | 見るべき指標と見せるべき指標 | Concept | AI-Production-01 | AI-QA-01 |
| 7-2 | 運用担当向けダッシュボード | Hands-on | AI-Engineer-01 | AI-QA-01 |
| 7-3 | マネジメント向けSLOレポート | Work | AI-Production-01 | AI-QA-01 |

## Section 8: SLOを組織に導入する

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 8-1 | SLO導入が失敗する3つのパターン | Concept | AI-Production-01 | AI-QA-01 |
| 8-2 | 開発チームへの説明と巻き込み方 | Work | AI-Production-01 | AI-QA-01 |
| 8-3 | PM、経営層への報告テンプレート | Work | AI-Production-01 | AI-QA-01 |
| 8-4 | リリース判断とエラーバジェット | Concept | AI-Production-01 | AI-QA-01 |

## Section 9: SLOレビューを運用に組み込む

| Lecture | Title | Type | Owner AI | Reviewer AI |
| --- | --- | --- | --- | --- |
| 9-1 | 週次SLOレビューの進め方 | Work | AI-Production-01 | AI-QA-01 |
| 9-2 | 月次SLOレビューの進め方 | Work | AI-Production-01 | AI-QA-01 |
| 9-3 | インシデント対応とSLOの連動 | Concept | AI-Production-01 | AI-QA-01 |
| 9-4 | このコースで学んだことの総整理 | Concept | AI-Production-01 | AI-QA-01 |

## Reusable Existing Assets

既存素材候補:

- `/home/ubuntu/workspace/udemy/courses/sre-slo-introduction/course-overview.json`
- `/home/ubuntu/workspace/udemy/courses/sre-slo-introduction/lectures.json`
- `/home/ubuntu/workspace/udemy/courses/sre-slo-introduction/s1-l1/script.json`
- `/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l1/script.json`

注意:

- 既存素材はApplication Signalsの2026年SLO機能を前提としていない可能性がある
- VOICEVOX用語は `docs/VOICEVOX_RULES.md` と `course_spec.md` の用語ルールに合わせて再チェックする
- 古いComposite Alarm中心の説明は、現行Application Signals SLO機能との関係を明確にする

## Task Decomposition

次に作るべきIssue:

- Section 1 script and slides
- Section 2 script and slides
- Section 3 script and slides
- Section 4 Application Signals demo script
- Section 5 CloudFormation hands-on implementation
- Section 6 burn rate explanation and hands-on
- Section 7 dashboard implementation
- Section 8 organization rollout worksheets
- Section 9 review workflow worksheets
