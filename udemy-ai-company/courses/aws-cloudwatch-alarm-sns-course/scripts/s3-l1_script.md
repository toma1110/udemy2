# Section 3 Lecture 1 台本

## Title

更新・削除・トラブルシュート

## Source

- `course_spec.md`
- `cloudformation/README.md`
- AWS CloudWatch and SNS troubleshooting guidance

## Slide 1

### Slide Title

運用の終わりまで見る

### Slide Message

作成、更新、削除までがハンズオン

### Narration

このレクチャーでは、更新、削除、トラブルシュートをまとめます。ハンズオンは、作れたら終わりではありません。変更できること、消せること、通知が届かない時に切り分けられることまで確認して完了です。

### Visual Notes

- Create、Update、Delete、Troubleshootの流れ
- 最後まで完了するチェックリスト

## Slide 2

### Slide Title

Stack Update

### Slide Message

しきいちを変えて変更管理を体験する

### Narration

更新では、アラームのしきいちを変えます。テンプレートとパラメータを使って変更を反映することで、手作業ではなく、スタックとして管理する感覚をつかみます。更新後は、アラームの設定値を確認します。

### Visual Notes

- AlarmThresholdが1から2へ変わる図
- update-stackと設定確認

## Slide 3

### Slide Title

Stack Delete

### Slide Message

削除まで実行して残りを防ぐ

### Narration

削除では、スタックを消して、アラームとトピックを残さないようにします。ハンズオン後の削除は、コストと不要な通知を防ぐために重要です。削除完了まで待ち、必要ならコンソールで残りがないか確認します。

### Visual Notes

- delete-stackからDELETE_COMPLETE
- AlarmとTopicが消える図

## Slide 4

### Slide Title

メールが届かない

### Slide Message

まずPendingConfirmationを見る

### Narration

メールが届かない時は、まずサブスクリプションの状態を見ます。ペンディングコンファメーションのままなら、確認メールの承認が終わっていません。迷惑メールや入力したアドレスの間違いも確認します。

### Visual Notes

- Subscription statusチェック
- PendingConfirmationからConfirmedへの変更

## Slide 5

### Slide Title

Alarmが通知しない

### Slide Message

ActionsEnabledとAlarmActionsを見る

### Narration

アラーム経由で通知されない時は、アクション設定を確認します。アクションズイネーブルドが有効か。アラームアクションにエスエヌエストピックのエーアールエヌが入っているか。状態変化が起きているかを順に見ます。

### Visual Notes

- Alarm設定画面の抽象図
- ActionsEnabled、AlarmActions、State change

## Slide 6

### Slide Title

Policyと暗号化

### Slide Message

publish権限とKMS設計を分けて見る

### Narration

トピックポリシーは、クラウドウォッチからの発行許可を持ちます。暗号化したトピックを実運用で使う場合は、カスタマーマネージドキーと、クラウドウォッチ向けのキーポリシーも設計対象です。VID-002では、初学者向けに暗号化なしの最小構成にしています。

### Visual Notes

- Topic PolicyとKMS Keyを別レイヤーで表示
- 教材範囲と実運用範囲を分ける

## Slide 7

### Slide Title

実運用IaC

### Slide Message

CloudFormation教材からCDK/Terraform運用へ

### Narration

この講座では、追加ツールを減らし、受講者が再現しやすいようにクラウドフォーメーションを使います。実運用では、チーム開発、テスト、再利用性を考え、シーディーケーかテラフォームで保守する前提にします。

### Visual Notes

- 教材CloudFormationからCDK/Terraformへ橋渡し
- LearningとProductionを左右比較

## Slide 8

### Slide Title

完了条件

### Slide Message

README通りに再現し、最後に消せる

### Narration

VID-002の完了条件は明確です。README通りに作成し、メール確認と通知テストを行い、しきいち更新を確認し、最後に削除できることです。動画を見るだけでなく、手順として再現できることをゴールにします。

### Visual Notes

- 完了チェックリスト
- Create、Confirm、Test、Update、Deleteの5項目
