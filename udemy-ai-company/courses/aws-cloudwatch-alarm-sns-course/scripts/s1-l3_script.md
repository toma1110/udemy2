# Section 1 Lecture 3 台本

## Title

SNS Topicとメール確認

## Source

- `course_spec.md`
- `cloudformation/README.md`
- AWS SNS and CloudWatch alarm notification documentation

## Slide 1

### Slide Title

SNS Topicとメール確認

### Slide Message

Topicが通知の中継点になる

### Narration

このレクチャーでは、エスエヌエストピックとメール確認を整理します。クラウドウォッチアラームは、直接メールを送るのではなく、エスエヌエストピックへ通知を送ります。トピックが中継点になり、登録された宛先へ配信します。

### Visual Notes

- AlarmからSNS Topic、Emailへ流れる図
- Topicを中央の中継点として強調

## Slide 2

### Slide Title

Topicは通知チャネル

### Slide Message

AlarmはTopicへ1回送ればよい

### Narration

トピックは通知チャネルです。アラーム側は、通知先が増えても、基本的にはトピックへ送るだけです。メール、別のエンドポイント、将来の拡張は、トピック側のサブスクリプションとして扱えます。

### Visual Notes

- AlarmからTopicへ一本の矢印
- Topicから複数宛先へ広がる構成

## Slide 3

### Slide Title

Subscriptionは宛先

### Slide Message

誰に、どの方式で届けるかを決める

### Narration

サブスクリプションは、トピックからどこへ届けるかを決める設定です。VID-002ではメールを使います。プロトコルはメール、エンドポイントは通知を受けるメールアドレスです。

### Visual Notes

- Protocol=email、Endpoint=mail addressの設定カード
- Topicにぶら下がる宛先

## Slide 4

### Slide Title

メール確認

### Slide Message

承認するまでPendingのまま

### Narration

メールサブスクリプションでは、受信者の確認が必要です。スタックを作ると確認メールが届きます。そのメールのリンクを開くまで、状態はペンディングコンファメーションのままです。この状態では通知は届きません。

### Visual Notes

- メール受信箱、Confirmリンク、PendingからConfirmedへの流れ
- PendingConfirmationを赤、Confirmedを緑

## Slide 5

### Slide Title

Topic Policy

### Slide Message

CloudWatchがpublishできる許可を置く

### Narration

トピックポリシーは、誰がトピックへ発行できるかを決めます。今回のテンプレートでは、クラウドウォッチのサービスが、同じアカウントのアラームから発行できるようにします。通知が届かない時は、この許可も確認します。

### Visual Notes

- CloudWatchからTopicへ通る許可ゲート
- SourceAccountとSourceArnを短く表示

## Slide 6

### Slide Title

届かない時

### Slide Message

確認、Action、Policyの順に見る

### Narration

通知が届かない時は、順番に見ます。まずメール確認が終わっているか。次にアラームのアクションが有効で、トピックのエーアールエヌが入っているか。最後にトピックポリシーで発行が許可されているかを確認します。

### Visual Notes

- 三段チェックリスト
- Email Confirm、AlarmActions、Topic Policy

## Slide 7

### Slide Title

最小から広げる

### Slide Message

まずメール、次に運用設計へ

### Narration

この講座では、最初の通知体験を小さく作るため、メール通知に絞ります。実運用では、複数宛先、暗号化、チームの受け取り方、通知疲れを防ぐ設計も必要です。まずは最小構成を正しく理解します。

### Visual Notes

- 最小構成から実運用設計へ広がる階段
- Email、Encryption、Team routingのラベル
