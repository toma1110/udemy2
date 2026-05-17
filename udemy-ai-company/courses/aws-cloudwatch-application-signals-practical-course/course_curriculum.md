# AWS CloudWatch Application Signals実践 カリキュラム

Source of Truth: `course_spec.md`

## Course Goal

CloudWatch Application Signalsを、サンプルアプリの通信、APM、Service Map、SLO監視、停止・削除・コスト確認まで含めて体験できる状態にする。

## Course

- Course ID: `aws-cloudwatch-application-signals-practical-course`
- Course Title: `AWS CloudWatch Application Signals実践: サンプルアプリで学ぶAPM・Service Map・SLO監視`
- Hands-on Resource Title: `Application Signalsサンプルアプリ CloudFormationハンズオン`
- PublicRepo local working copy: `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`
- PublicRepo URL: 未公開。公開後にGitHub URLへ更新する

## Section 1: Application Signalsの地図

### Section Learning Objectives

- Application Signalsで見えるサービス状態、依存関係、Latency、Availability、Fault、Errorを説明できる
- 本講座で作るサンプルアプリ、自動トラフィック、コスト安全策を理解できる

| Lecture ID | Lecture Title | Learning Goal | Hands-on | Hands-on Resource |
| --- | --- | --- | --- | --- |
| `s1-l1` | Application Signalsで何が見えるか | Services、Application Map、Service detail、SLOの位置づけを説明できる | なし | なし |
| `s1-l2` | ハンズオン構成とコスト安全策 | 作成するAWSリソース、低頻度通信、停止、削除、料金注意を説明できる | あり | `handson/README.md#実行前チェック` |

## Section 2: CloudFormationでサンプルアプリを作る

### Section Learning Objectives

- CloudFormationテンプレートの全体像を読み、サンプルアプリとトラフィック生成の関係を説明できる
- CEO承認後にREADME通りの作成、確認、シナリオ切り替えを再現できる

| Lecture ID | Lecture Title | Learning Goal | Hands-on | Hands-on Resource |
| --- | --- | --- | --- | --- |
| `s2-l1` | テンプレート全体を読む | Application Signals有効化、Lambda、Scheduler、SLOの関係を読める | あり | `cloudformation/README.md#テンプレートを読む` |
| `s2-l2` | サンプルアプリと低頻度トラフィックをデプロイする | stack create後に低頻度通信が始まる流れを説明できる | あり | `cloudformation/README.md#作成する` |
| `s2-l3` | 正常、遅延、エラーのシナリオを切り替える | 正常、遅延、エラーの通信パターンを切り替え、観測結果の違いを説明できる | あり | `cloudformation/README.md#シナリオを切り替える` |

## Section 3: Application Signalsで見る

### Section Learning Objectives

- Application Signalsの画面を使い、サービス状態、依存関係、詳細メトリクスを順番に確認できる

| Lecture ID | Lecture Title | Learning Goal | Hands-on | Hands-on Resource |
| --- | --- | --- | --- | --- |
| `s3-l1` | Servicesで状態を見る | Services画面でサービス、Latency、Availability、Fault、Errorを見る順番を説明できる | あり | `handson/README.md#servicesを確認する` |
| `s3-l2` | Application Mapで依存関係を見る | Application Mapでサービス間の関係と異常箇所を見る考え方を説明できる | あり | `handson/README.md#application-mapを確認する` |
| `s3-l3` | Service detailでLatency、Fault、Errorを読む | Service detailから原因調査へ進む観点を説明できる | あり | `handson/README.md#service-detailを確認する` |

## Section 4: SLOと運用判断につなげる

### Section Learning Objectives

- Application Signals SLOの位置づけを理解し、短時間ハンズオンで確認できる範囲と実運用データが必要な範囲を分けられる
- 自動トラフィック停止、削除、コスト確認まで実行できる

| Lecture ID | Lecture Title | Learning Goal | Hands-on | Hands-on Resource |
| --- | --- | --- | --- | --- |
| `s4-l1` | Application Signals SLOを作る | Application Signals SLOとSLIの関係を説明できる | あり | `cloudformation/README.md#sloを確認する` |
| `s4-l2` | RecommendationsとPerformance Reportの前提 | 30日データや実運用トラフィックが必要な機能を説明できる | なし | なし |
| `s4-l3` | 停止、削除、コスト確認 | 自動トラフィック停止、stack delete、Cost Explorer確認の流れを説明できる | あり | `cloudformation/README.md#停止と削除` |

## Final Deliverables

- `course_spec.md`
- `course_infomation.md`
- `course_curriculum.md`
- `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/README.md`
- `cloudformation/template.yaml`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `cloudformation/stop_traffic.sh`
- `handson/README.md`
- `scripts/*_script.md`
- `scripts/*_script.json`
- GPT-Image2 source PNG and fitted final PNG
- VOICEVOX WAV
- MP4 video
- QA report
- Google Drive upload report
- Promotion video package
