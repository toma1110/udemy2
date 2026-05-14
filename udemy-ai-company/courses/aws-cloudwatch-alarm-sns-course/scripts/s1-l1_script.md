# Section 1 Lecture 1 台本

## Title

Alarm + SNS通知の最小構成

## Source

- `course_spec.md`
- `cloudformation/README.md`
- `qa/aws_source_verification_report.md`
- `docs/VIDEO_QUALITY_BASELINE.md`

## Slide 1

### Slide Title

Alarm + SNS通知

### Slide Message

状態が変わったら、通知へつなげる

### Narration

こんにちは。このレクチャーでは、クラウドウォッチアラームからエスエヌエス通知へつなげる最小構成を作ります。ゴールは、アラーム、通知先、メール確認、削除までの流れを、クラウドフォーメーションで再現できるようになることです。

### Visual Notes

- AlarmからSNS Topic、Emailへ流れる大きな図
- 状態変化から通知へ進む一本道
- 高品質なVID-001基準のクラウド監視ビジュアル

## Slide 2

### Slide Title

作るもの

### Slide Message

Topic、Subscription、Policy、Alarmの4つ

### Narration

今回作るものは4つです。通知を受けるエスエヌエストピック。メールを登録するサブスクリプション。クラウドウォッチから発行できるようにするトピックポリシー。そして、条件を見て通知アクションを実行するクラウドウォッチアラームです。

### Visual Notes

- 4つの部品をカードで表示
- Topic、Subscription、Policy、Alarmの関係
- 作成対象と役割が一目でわかる構成

## Slide 3

### Slide Title

テンプレートの地図

### Slide Message

Parameters、Conditions、Resources、Outputsで読む

### Narration

クラウドフォーメーションテンプレートは、4つに分けて読むと楽です。パラメータで入力を決めます。コンディションで、メールアドレスがある時だけ作る条件を決めます。リソースで実際の部品を作り、アウトプットで確認に必要なあたいを出します。

### Visual Notes

- テンプレートを4区画の設計図として表示
- Parameters、Conditions、Resources、Outputsの短いラベル
- 初学者がテンプレートを読む道筋

## Slide 4

### Slide Title

SNS Topic

### Slide Message

通知を集める入口を作る

### Narration

エスエヌエストピックは、通知を集める入口です。アラームはこのトピックにメッセージを送ります。その後、トピックにぶら下がる宛先へ通知が配信されます。まずは、通知の通り道の中心を作る、と考えます。

### Visual Notes

- 中央にSNS Topic
- AlarmからTopicへ矢印
- Topicから複数宛先へ広がる表現

## Slide 5

### Slide Title

Email Subscription

### Slide Message

メール確認が終わるまで通知は届かない

### Narration

メール通知では、サブスクリプションの確認が必要です。スタックを作ると確認メールが届きます。受信者が承認するまでは、状態がペンディングのままで、通知は届きません。ここは初学者がつまずきやすいポイントです。

### Visual Notes

- Email inboxとConfirmボタンの抽象図
- PendingからConfirmedへ変わる流れ
- メール確認を強調

## Slide 6

### Slide Title

Topic Policy

### Slide Message

CloudWatchがTopicへ送れるようにする

### Narration

トピックポリシーは、誰がトピックへ発行できるかを決めます。アラーム通知では、クラウドウォッチがエスエヌエストピックへメッセージを送れる必要があります。通知が届かない時は、アクション設定だけでなく、ポリシーも確認します。

### Visual Notes

- CloudWatchからSNS Topicへの許可ゲート
- publish permissionの視覚化
- 許可される流れと拒否される流れ

## Slide 7

### Slide Title

CloudWatch Alarm

### Slide Message

条件、状態、アクションを1つにまとめる

### Narration

クラウドウォッチアラームは、メトリクス、条件、状態、アクションをまとめたものです。今回のテンプレートでは、学習用のメトリクス名を使います。長時間動くサーバーは作らず、通知の仕組みに集中します。

### Visual Notes

- メトリクス線、しきい値、状態、通知アクション
- AlarmActionsからSNS Topicへつながる
- 低コスト学習用であることを視覚的に示す

## Slide 8

### Slide Title

作成と確認

### Slide Message

Stack、Email、Outputsを順に確認する

### Narration

作成後は、順番に確認します。まずスタックが作成完了になっているかを見ます。次にメールの確認を完了します。最後にアウトプットから、アラーム名とトピックのエーアールエヌを確認します。この順番にすると、原因を切り分けやすくなります。

### Visual Notes

- Stack complete、Email confirmed、Outputsの3ステップ
- 確認チェックリスト
- 受講者が手順を追いやすい画面

## Slide 9

### Slide Title

通知テスト

### Slide Message

まずSNS、次にAlarmActionsを見る

### Narration

通知テストは、2段階で考えます。まずエスエヌエストピックへ直接テストメッセージを送って、メールの通り道を確認します。次に、エーダブリューエスシーエルアイを使える場合だけ、アラーム状態を手動で変えて、アラームアクションを確認します。

### Visual Notes

- SNS direct testとAlarmActions testの2段階
- 直接通知とアラーム経由の違い
- CLIは任意であることを示す

## Slide 10

### Slide Title

更新と削除

### Slide Message

作ったら、変えて、最後に消す

### Narration

ハンズオンは、作って終わりではありません。しきいちを変える更新を行い、テンプレート変更がスタックへ反映されることを確認します。最後はスタックを削除し、アラームとトピックが残っていないことを確認します。削除までが合格条件です。

### Visual Notes

- Create、Update、Deleteの3ステップ
- しきい値変更と削除確認
- 課金事故を防ぐチェックマーク

## Slide 11

### Slide Title

実運用では

### Slide Message

CDKかTerraformで保守し、通知設計を広げる

### Narration

最後に位置づけです。この講座では、受講者が追加ツールなしで再現しやすいように、クラウドフォーメーションを使います。一方で、実運用ではシーディーケーかテラフォームで保守する前提で考えます。暗号化、複数通知先、チーム運用は、次の設計テーマです。

### Visual Notes

- 左に講座ハンズオン、右に実運用
- CloudFormationからCDK/Terraformへ橋渡し
- 暗号化、複数通知先、チーム運用の広がり

## QA Notes

- `course_spec.md` のVID-002範囲に限定
- CloudFormationは教材ハンズオン内の再現性用途として説明
- stack create/update/deleteはCEO承認後にのみ実行
- 実運用IaCはCDKまたはTerraform前提として説明
- 表示文字はGPT-Image2生成にする
- VID-001の品質基準と比較する
