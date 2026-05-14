# Section 5 Lecture 1 台本

## Title

ハンズオン構成とコスト注意

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- `cloudformation/README.md`
- `cloudformation/template.yaml`
- AWS CloudWatch SLO official documentation
- AWS CloudFormation `AWS::ApplicationSignals::ServiceLevelObjective` documentation

## Slide 1

### Slide Title

ハンズオン構成とコスト注意

### Slide Message

低コスト構成で、SLO基盤の流れを作る

### Narration

ここからは、クラウドフォーメーションでエスエルオー基盤を作るハンズオンに入ります。まずは、何を作るのか、どこで料金が発生し得るのか、そして最後にどう削除するのかを確認します。

### Visual Notes

- Section 5 opening slide
- CloudFormation hands-on flow
- Low-cost path highlighted

## Slide 2

### Slide Title

作るもの

### Slide Message

SNS、Alarm、Dashboardを最小構成で用意する

### Narration

このハンズオンで作る中心は、エスエヌエス、クラウドウォッチアラーム、クラウドウォッチダッシュボードです。アプリ本体は作らず、サンプル用のカスタムメトリクスを投入して、エスエルアイを確認できる形にします。

### Visual Notes

- Architecture: Custom Metrics -> CloudWatch Alarm -> SNS Topic
- Dashboard reads availability and latency
- No application workload deployed

## Slide 3

### Slide Title

Custom Metricを使う理由

### Slide Message

実アプリなしで、SLIの形を再現する

### Narration

今回は、実際のロードバランサーやアプリケーションを用意しません。その代わりに、クラウドウォッチのカスタムメトリクスを使います。これにより、低コストで、成功率や待ち時間をエスエルアイとして扱う流れを練習できます。

### Visual Notes

- Simulated service metrics
- Availability percent and latency milliseconds
- Training environment without real traffic

## Slide 4

### Slide Title

Application Signals SLOはオプション

### Slide Message

必要な人だけ、有効化して試す

### Narration

テンプレートには、アプリケーションシグナルズのエスエルオーも入れています。ただし、標準では作成しません。料金、サービスリンクロール、実メトリクスの前提があるため、明示的に有効化した場合だけ作ります。

### Visual Notes

- Optional Application Signals SLO switch
- Default: disabled
- Explicit opt-in and cost caution

## Slide 5

### Slide Title

必要な準備

### Slide Message

AWS CLI、リージョン、スタック名を決める

### Narration

事前に、エーダブリューエスシーエルアイの認証情報を設定しておきます。次に、リージョンとスタック名を決めます。通知メールは任意です。メールを指定した場合は、エスエヌエスの確認メールも確認対象になります。

### Visual Notes

- AWS CLI configured
- Region: us-east-1 example
- StackName and ProjectName
- Optional NotificationEmail

## Slide 6

### Slide Title

料金が発生し得る場所

### Slide Message

Alarm、Dashboard、Custom Metric、SLOに注意する

### Narration

料金が発生し得る場所は、クラウドウォッチアラーム、ダッシュボード、カスタムメトリクス、そしてオプションのエスエルオーです。短時間で確認し、不要になったら必ず削除します。学習用でも、作りっぱなしにはしません。

### Visual Notes

- Cost caution cards
- CloudWatch Alarm
- Dashboard
- Custom Metrics
- Optional Application Signals SLO

## Slide 7

### Slide Title

進め方

### Slide Message

validate、create、metrics、smoke、update、delete

### Narration

流れは六つです。まずテンプレートを検証します。次にスタックを作成します。サンプルメトリクスを投入し、スモークテストで存在確認をします。そのあと更新を試し、最後に削除まで確認します。

### Visual Notes

- Flow: validate -> create -> put-metrics -> smoke -> update -> delete
- Each step as a checkpoint
- Delete is part of the hands-on

## Slide 8

### Slide Title

まとめ: 作る前に削除まで決める

### Slide Message

ハンズオンは、消せる設計まで含めて完成

### Narration

まとめです。セクション5では、低コストのサンプル構成で、エスエルオー基盤の作成から削除までを確認します。次のレクチャーでは、クラウドフォーメーションテンプレートを読み、どのリソースが作られるかを見ていきます。

### Visual Notes

- Checklist: scope, cost, deletion
- Arrow to template reading
- Section 5 roadmap

## QA Notes

- `lectures.md` の Lecture 5-1 に合わせて構成
- 低コスト構成を標準、Application Signals SLOをオプションとして説明
- 8枚構成
- 読み上げでは英字を残さない
