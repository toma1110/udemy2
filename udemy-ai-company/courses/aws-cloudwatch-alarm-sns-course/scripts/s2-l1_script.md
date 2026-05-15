# Section 2 Lecture 1 台本

## Title

CloudFormationテンプレートを読む

## Source

- `course_spec.md`
- `cloudformation/template.yaml`
- AWS CloudFormation resource references

## Slide 1

### Slide Title

テンプレートを読む

### Slide Message

入力、条件、部品、出力に分ける

### Narration

このレクチャーでは、VID-002のクラウドフォーメーションテンプレートを読みます。初学者は上から全部読もうとして迷いやすいです。入力、条件、部品、出力の4つに分けると、何を作っているかが見えやすくなります。

### Visual Notes

- テンプレートを4区画の設計図に分割
- Parameters、Conditions、Resources、Outputs

## Slide 2

### Slide Title

Parameters

### Slide Message

受講者が変える値を入口にする

### Narration

パラメータは、受講者が変える値です。VID-002では、通知先メールアドレスと、アラームのしきいちを入力できます。メールアドレスは空でもよく、空ならメールサブスクリプションを作らない設計です。

### Visual Notes

- NotificationEmailとAlarmThresholdの入力欄
- 空の場合はメールなしの分岐

## Slide 3

### Slide Title

Conditions

### Slide Message

メールがある時だけSubscriptionを作る

### Narration

コンディションは、条件によって作るものを変える仕組みです。このテンプレートでは、通知先メールが入力された時だけ、メールサブスクリプションを作ります。空なら、トピックとアラームだけを作れます。

### Visual Notes

- HasNotificationEmailの分岐図
- yesならSubscription、noならskip

## Slide 4

### Slide Title

SNS Topic

### Slide Message

Alarm通知を受ける中継点を作る

### Narration

エスエヌエストピックは、アラーム通知を受ける中継点です。テンプレートでは、トピック名を直接固定せず、クラウドフォーメーションに作成させます。これにより、スタック削除時にまとめて片付けやすくなります。

### Visual Notes

- CloudFormationがSNS Topicを作る図
- TagsとManagedByの小さなラベル

## Slide 5

### Slide Title

Topic Policy

### Slide Message

CloudWatchからのpublishを許可する

### Narration

トピックポリシーでは、クラウドウォッチがトピックへ発行できるようにします。条件として、同じアカウントからのアラームに絞っています。通知の経路を作るだけでなく、発行できる権限もテンプレートで管理します。

### Visual Notes

- CloudWatch service principalからSNS Topicへの許可
- SourceAccountとSourceArnの制限

## Slide 6

### Slide Title

CloudWatch Alarm

### Slide Message

Metric、Threshold、Actionsをまとめる

### Narration

クラウドウォッチアラームでは、メトリクス名、統計、期間、評価回数、しきいち、比較条件をまとめます。そしてアラームアクションとオーケーアクションに、エスエヌエストピックを指定します。状態変化が通知につながる部分です。

### Visual Notes

- Alarmリソースを中心に設定項目を放射状に表示
- AlarmActionsとOKActionsからTopicへ矢印

## Slide 7

### Slide Title

Outputs

### Slide Message

作成後に見る値を外へ出す

### Narration

アウトプットは、作成後に確認したい値です。VID-002では、アラーム名、トピックのエーアールエヌ、メールサブスクリプションを作ったかどうかを出します。後の確認やテストで、この値を使います。

### Visual Notes

- AlarmName、AlarmTopicArn、EmailSubscriptionCreated
- Stack Outputsから確認コマンドへつながる

## Slide 8

### Slide Title

読み方のまとめ

### Slide Message

入力から出力まで、依存関係で追う

### Narration

テンプレートは、入力から条件、リソース、出力へ流れで追います。どの値がどのリソースに渡るか。どのリソースがどの通知経路を作るか。この依存関係がわかると、更新やトラブルシュートも楽になります。

### Visual Notes

- ParametersからResources、Outputsへ流れる依存関係マップ
- 次のレクチャーのStack作成へつながる表示
