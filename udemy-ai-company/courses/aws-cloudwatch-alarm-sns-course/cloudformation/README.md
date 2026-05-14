# CloudFormation Hands-on

このハンズオンは、CloudWatch AlarmからSNS Topicへ通知する最小構成をCloudFormationで作ります。

## 作るもの

- SNS Topic
- SNS Email Subscription
- SNS Topic Policy
- CloudWatch Alarm

## 重要な注意

- stack create/update/deleteはCEO承認後にのみ実行します。
- Email Subscriptionは、受信者が確認メールを承認するまで `PendingConfirmation` になります。
- この教材テンプレートでは、初学者の再現性を優先してSNS TopicのKMS暗号化は扱いません。
- 実運用で暗号化SNS TopicをCloudWatch Alarmから使う場合は、customer managed keyとCloudWatch向けKMS権限を設計してください。

## 事前準備

- CloudFormation、CloudWatch、SNSを利用できるAWSアカウント
- 通知確認用メールアドレス
- 任意: AWS CLI

## 静的検証

```bash
./validate.sh
```

## 作成

CEO承認後に実行します。

```bash
aws cloudformation create-stack \
  --stack-name udemy-vid002-cloudwatch-alarm-sns \
  --template-body file://template.yaml \
  --parameters ParameterKey=NotificationEmail,ParameterValue=you@example.com
```

## 作成完了待ち

```bash
aws cloudformation wait stack-create-complete \
  --stack-name udemy-vid002-cloudwatch-alarm-sns
```

## 確認

```bash
./smoke_test.sh udemy-vid002-cloudwatch-alarm-sns
```

## SNS疎通テスト

CloudFormation Outputsの `AlarmTopicArn` を使って、SNS Topicへ直接テスト通知します。

```bash
aws sns publish \
  --topic-arn <AlarmTopicArn> \
  --subject "VID-002 SNS test" \
  --message "CloudWatch Alarm + SNS hands-on test message"
```

## 任意: AlarmActionsのテスト

AWS CLIを使える場合だけ実行します。

```bash
aws cloudwatch set-alarm-state \
  --alarm-name <AlarmName> \
  --state-value ALARM \
  --state-reason "VID-002 manual alarm action test"
```

数秒後に戻します。

```bash
aws cloudwatch set-alarm-state \
  --alarm-name <AlarmName> \
  --state-value OK \
  --state-reason "VID-002 manual alarm action test complete"
```

## 更新

```bash
aws cloudformation update-stack \
  --stack-name udemy-vid002-cloudwatch-alarm-sns \
  --template-body file://template.yaml \
  --parameters ParameterKey=NotificationEmail,ParameterValue=you@example.com ParameterKey=AlarmThreshold,ParameterValue=2
```

## 削除

```bash
aws cloudformation delete-stack \
  --stack-name udemy-vid002-cloudwatch-alarm-sns
```

```bash
aws cloudformation wait stack-delete-complete \
  --stack-name udemy-vid002-cloudwatch-alarm-sns
```

## トラブルシュート

- メールが届かない: SNS Subscriptionが `PendingConfirmation` のままではないか確認する
- Alarm通知が届かない: AlarmActionsにSNS Topic ARNが入っているか確認する
- SNS publishが拒否される: Topic PolicyでCloudWatchまたは実行者のpublish権限を確認する
- 暗号化SNS Topicを使った: `alias/aws/sns` ではCloudWatch Alarm actionが失敗する場合があるため、customer managed keyの権限を確認する
