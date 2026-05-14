# Section 5 Lecture 3 台本

## Title

SLO、Alarm、SNS、Dashboardを作成する

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- `cloudformation/validate.sh`
- `cloudformation/template.yaml`
- AWS CloudWatch Alarm official documentation

## Slide 1

### Slide Title

SLO、Alarm、SNS、Dashboardを作成する

### Slide Message

作成、投入、確認の順で進める

### Narration

このレクチャーでは、実際にスタックを作成します。標準構成では、エスエヌエス、クラウドウォッチアラーム、ダッシュボードを作ります。そのあと、サンプルメトリクスを投入して、グラフとアラームが見る対象を用意します。

### Visual Notes

- Create stack flow
- Standard resources: SNS / CloudWatch Alarms / Dashboard
- Sample metrics injection

## Slide 2

### Slide Title

環境変数を決める

### Slide Message

STACK_NAME、AWS_REGION、PROJECT_NAMEを固定する

### Narration

まず、スタック名、リージョン、プロジェクト名を決めます。ハンズオンでは毎回同じ名前を使うと、作成、更新、削除の対象がぶれません。既存スタックとぶつからない名前を選ぶのも大事です。

### Visual Notes

- STACK_NAME example
- AWS_REGION example
- PROJECT_NAME example
- Naming rule: unique and disposable

## Slide 3

### Slide Title

validate

### Slide Message

作る前にテンプレートを検証する

### Narration

最初に、検証コマンドを実行します。ここでは、テンプレートの構文やリソース定義がクラウドフォーメーションとして読めるかを確認します。作成に失敗してから直すより、先に検証する方が安全です。

### Visual Notes

- Command: ./validate.sh validate
- CloudFormation validate-template
- Stop before resource creation if invalid

## Slide 4

### Slide Title

create

### Slide Message

CloudFormation deployでスタックを作る

### Narration

検証が通ったら、作成コマンドを実行します。スタック作成では、テンプレートのパラメーターを渡し、クラウドフォーメーションがリソースを作ります。メール通知を使う場合は、確認メールの承認も忘れないようにします。

### Visual Notes

- Command: ./validate.sh create
- cloudformation deploy
- Optional SNS email confirmation

## Slide 5

### Slide Title

put-metrics

### Slide Message

AvailabilityとLatencyのサンプル値を入れる

### Narration

スタック作成後に、サンプルメトリクスを投入します。アベイラビリティには九十九点九パーセント、レイテンシには百二十ミリ秒を入れます。これにより、ダッシュボードに表示する時系列データができます。

### Visual Notes

- Command: ./validate.sh put-metrics
- Availability: 99.9 percent
- Latency: 120 milliseconds
- Namespace and dimensions

## Slide 6

### Slide Title

Outputsを見る

### Slide Message

作成された名前とARNを確認する

### Narration

作成が終わったら、アウトプッツを確認します。通知トピックの識別子、アラーム名、ダッシュボード名が出力されます。これらは、次のスモークテストで存在確認に使う値です。

### Visual Notes

- AlarmTopicArn
- AvailabilityAlarmName
- LatencyAlarmName
- DashboardName

## Slide 7

### Slide Title

画面でも確認する

### Slide Message

CLI確認とコンソール確認を組み合わせる

### Narration

エーダブリューエスシーエルアイで確認するだけでなく、マネジメントコンソールでも見ておくと理解しやすくなります。アラームの状態、ダッシュボードのグラフ、通知トピックを確認し、テンプレートと実リソースを結びつけます。

### Visual Notes

- CloudWatch Alarms page
- Dashboard page
- SNS topic page
- Match resources with template

## Slide 8

### Slide Title

まとめ: 作成後は確認対象を持つ

### Slide Message

作れた、ではなく、確認できた、まで進める

### Narration

まとめです。クラウドフォーメーションの作成は、リソースができたところで終わりではありません。メトリクスを投入し、出力を確認し、次のスモークテストで存在確認できる状態まで進めます。

### Visual Notes

- Created resources -> metrics -> outputs -> smoke test
- Arrow to Lecture 5-4
- Hands-on checkpoint

## QA Notes

- `lectures.md` の Lecture 5-3 に合わせて構成
- create、put-metrics、Outputs確認を扱う
- 8枚構成
- 読み上げでは英字を残さない
