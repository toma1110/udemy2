# Section 2 Lecture 2 台本

## Title

Stack作成と通知テスト

## Source

- `course_spec.md`
- `cloudformation/README.md`
- AWS CloudFormation, SNS, CloudWatch alarm operations

## Slide 1

### Slide Title

作成前の注意

### Slide Message

AWS操作はCEO承認後に実行する

### Narration

このレクチャーでは、スタック作成と通知テストの手順を説明します。実際のスタック作成、更新、削除は、AWS料金に関係するため、CEO承認後にだけ実行します。講座の手順は、README通りに再現できる形で整理します。

### Visual Notes

- 承認ゲート、AWS操作、確認の流れ
- Cost注意とDeleteまでのチェック

## Slide 2

### Slide Title

Stack Create

### Slide Message

template.yamlとメールアドレスを指定する

### Narration

作成では、クラウドフォーメーションにテンプレートを渡し、通知先メールアドレスをパラメータとして指定します。メールなしで構成だけ確認したい場合は、通知先を空にできます。メール通知まで見る場合は、受け取れるアドレスを指定します。

### Visual Notes

- template.yaml、NotificationEmail、AlarmThresholdの入力
- create-stackの流れ

## Slide 3

### Slide Title

作成完了待ち

### Slide Message

CREATE_COMPLETEを確認してから進む

### Narration

スタック作成中は、リソースが順番に作られます。状態がクリエイトコンプリートになるまで待ちます。失敗した場合は、イベント欄でどのリソースが失敗したかを確認します。焦って次の確認に進まないことが大事です。

### Visual Notes

- Stack status timeline
- CREATE_IN_PROGRESSからCREATE_COMPLETE

## Slide 4

### Slide Title

メール確認

### Slide Message

Confirmしないと通知は届かない

### Narration

メールアドレスを指定した場合は、エスエヌエスから確認メールが届きます。リンクを開いて承認するまで、サブスクリプションはペンディングです。スタック作成が成功していても、メール確認前は通知が届きません。

### Visual Notes

- Inboxに届く確認メール
- PendingConfirmationからConfirmed

## Slide 5

### Slide Title

Smoke Test

### Slide Message

Alarm、Topic、Subscriptionを確認する

### Narration

作成後は、スモークテストで最低限の確認をします。スタックのアウトプットからアラーム名とトピックのエーアールエヌを取り出し、アラーム、トピック、サブスクリプションを確認します。存在確認と設定確認を分けるのがポイントです。

### Visual Notes

- Alarm exists、Topic exists、Subscription statusの3チェック
- smoke_test.shの位置づけ

## Slide 6

### Slide Title

SNS Publish Test

### Slide Message

まずTopicへ直接送って通り道を見る

### Narration

通知テストは、まずエスエヌエストピックへ直接送ります。これで、トピックからメールまでの通り道を確認できます。ここで届かなければ、メール確認やサブスクリプションの状態を見るべきです。

### Visual Notes

- SNS direct publishからEmailまでの矢印
- Alarmを経由しないテストであることを明示

## Slide 7

### Slide Title

Alarm State Test

### Slide Message

CLIが使える場合だけ状態を手動で変える

### Narration

エーダブリューエスシーエルアイを使える場合だけ、アラーム状態を手動でアラームに変えるテストもできます。これはアラームアクションの確認に便利です。テスト後はオーケーへ戻し、検証用の操作だと記録します。

### Visual Notes

- set-alarm-state ALARMからOKへ戻す流れ
- optional CLI testのラベル

## Slide 8

### Slide Title

次に見るもの

### Slide Message

更新、削除、届かない時の確認へ進む

### Narration

作成と通知確認ができたら、次は更新と削除です。ハンズオンでは、しきいちを変えて更新し、最後にスタックを削除します。通知が届かない場合の確認ポイントも、次のレクチャーでまとめます。

### Visual Notes

- Create、Confirm、Test、Update、Deleteの流れ
- 次の運用レクチャーへ接続
