# Section 5 Lecture 2 台本

## Title

CloudFormationテンプレートを読む

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- `cloudformation/template.yaml`
- AWS CloudFormation `AWS::ApplicationSignals::ServiceLevelObjective` documentation

## Slide 1

### Slide Title

CloudFormationテンプレートを読む

### Slide Message

Parameters、Resources、Outputsに分けて理解する

### Narration

このレクチャーでは、ハンズオンで使うクラウドフォーメーションテンプレートを読みます。全部を一度に覚える必要はありません。パラメーター、リソース、アウトプッツの三つに分けると、初心者でも追いやすくなります。

### Visual Notes

- Template map: Parameters / Resources / Outputs
- Beginner-friendly reading order
- File: cloudformation/template.yaml

## Slide 2

### Slide Title

Parameters

### Slide Message

スタックごとに変えたい値を外に出す

### Narration

パラメーターは、スタックごとに変えたい設定です。プロジェクト名、通知メール、ダッシュボードタイトル、アプリケーションシグナルズのエスエルオーを作るかどうかを指定できます。固定値を減らすことで、再利用しやすくします。

### Visual Notes

- ProjectName
- NotificationEmail
- DashboardTitle
- EnableApplicationSignalsSlo

## Slide 3

### Slide Title

SNS Topic

### Slide Message

Alarmの通知先を先に作る

### Narration

最初のリソースは、エスエヌエストピックです。アラームが状態変化したときの通知先になります。通知メールを指定した場合だけ、メール購読も作ります。指定しない場合は、トピックだけを作る構成です。

### Visual Notes

- SloAlarmTopic
- Optional email subscription
- AlarmActions target

## Slide 4

### Slide Title

Availability Alarm

### Slide Message

成功率が目標を下回るリスクを見る

### Narration

アベイラビリティ用のアラームは、サンプルの成功率メトリクスを見ます。平均が九十九パーセントを下回ったら、エスエルオーのリスクとして扱います。欠損データは問題なしとして扱い、学習中の不要な通知を減らします。

### Visual Notes

- Metric: Availability
- Namespace: UdemyAICompany/SLO
- Threshold: 99 percent
- TreatMissingData: notBreaching

## Slide 5

### Slide Title

Latency Alarm

### Slide Message

p99が300ミリ秒を超えたら検知する

### Narration

レイテンシ用のアラームは、九十九パーセンタイルを見ます。サンプルでは、三百ミリ秒を超えたら悪化として扱います。平均だけでなく、遅いユーザー体験を見るために、パーセンタイル統計を使います。

### Visual Notes

- Metric: Latency
- ExtendedStatistic: p99
- Threshold: 300 milliseconds
- ComparisonOperator: GreaterThanThreshold

## Slide 6

### Slide Title

Dashboard

### Slide Message

AvailabilityとLatencyを同じ画面で見る

### Narration

ダッシュボードでは、アベイラビリティとレイテンシを並べて表示します。通知のためのアラームだけでなく、状態を見る場所も一緒に作るのがポイントです。あとで運用向けのダッシュボード設計にもつながります。

### Visual Notes

- Text widget with dashboard title
- Availability metric widget
- Latency p99 widget
- Horizontal threshold annotation

## Slide 7

### Slide Title

Optional SLO

### Slide Message

Application Signals SLOは明示的に有効化する

### Narration

オプションのエスエルオーは、アプリケーションシグナルズのリソースです。標準では無効です。有効化すると、サービスリンクロールが作られる場合があります。実務で使う前に、料金と削除後に残る管理リソースを確認します。

### Visual Notes

- Condition: CreateApplicationSignalsSlo
- Resource: AWS::ApplicationSignals::ServiceLevelObjective
- Service-linked role caution

## Slide 8

### Slide Title

まとめ: テンプレートは地図として読む

### Slide Message

入力、作成物、出力を対応づける

### Narration

まとめです。クラウドフォーメーションテンプレートは、入力、作成物、出力の地図として読むと理解しやすくなります。次のレクチャーでは、このテンプレートを使ってスタックを作成し、サンプルメトリクスを投入します。

### Visual Notes

- Parameters -> Resources -> Outputs
- Arrow to stack create
- Section 5 template reading wrap-up

## QA Notes

- `lectures.md` の Lecture 5-2 に合わせて構成
- TemplateのParameters、Resources、Outputsを初心者向けに説明
- Application Signals SLOは標準無効のオプションとして説明
- 8枚構成
