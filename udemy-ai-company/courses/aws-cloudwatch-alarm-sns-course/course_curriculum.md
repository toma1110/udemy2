# Course Curriculum

## Course

- Course ID: `aws-cloudwatch-alarm-sns-course`
- Course Title: `CloudFormationで作るCloudWatch Alarm + SNS通知`
- Source Candidate: `VID-002`
- Source of Truth: `course_spec.md`
- Hands-on Resource Title: `CloudFormationで作るCloudWatch Alarm + SNSメール通知ハンズオン`

## Section 1: Alarm + SNS通知の地図

### Section Learning Objectives

- CloudWatch Alarmがメトリクス、しきいち、評価期間、状態、アクションで動くことを説明できる
- SNS TopicとEmail Subscriptionの役割を説明できる
- メール確認が終わるまで通知が届かない理由を説明できる

### Hands-on Resource Title

`Alarm + SNS通知の全体像チェックシート`

| Lecture ID | Lecture Title | Learning Goal | Production Status |
| --- | --- | --- | --- |
| `s1-l1` | Alarm + SNS通知の最小構成 | AlarmからSNS Topic、Emailまでの通知経路を説明できる | Produced |
| `s1-l2` | CloudWatch Alarmの評価条件 | しきいち、期間、評価回数、データポイントを区別できる | Produced |
| `s1-l3` | SNS Topicとメール確認 | Topic、Subscription、PendingConfirmation、Topic Policyを説明できる | Produced |

## Section 2: CloudFormationで作る

### Section Learning Objectives

- テンプレートをParameters、Conditions、Resources、Outputsに分けて読める
- SNS Topic、Subscription、Topic Policy、CloudWatch Alarmのリソース関係を説明できる
- CEO承認後にREADME通りの作成、確認、通知テストを再現できる

### Hands-on Resource Title

`CloudFormationテンプレート読解とStack作成手順`

| Lecture ID | Lecture Title | Learning Goal | Production Status |
| --- | --- | --- | --- |
| `s2-l1` | CloudFormationテンプレートを読む | VID-002テンプレートの入力、条件、リソース、出力を読める | Produced |
| `s2-l2` | Stack作成と通知テスト | Stack作成、メール確認、SNS publish、任意のAlarm state testの順番を説明できる | Produced |

## Section 3: 運用と後片付け

### Section Learning Objectives

- stack update/deleteを含めてハンズオンを完了できる
- 通知が届かない時に確認すべき基本ポイントを説明できる
- 教材用CloudFormationと実運用IaCのCDK/Terraformを混同せず説明できる

### Hands-on Resource Title

`更新・削除・トラブルシュート確認リスト`

| Lecture ID | Lecture Title | Learning Goal | Production Status |
| --- | --- | --- | --- |
| `s3-l1` | 更新・削除・トラブルシュート | しきいち更新、削除、PendingConfirmation、AlarmActions、Topic Policyの確認ポイントを説明できる | Produced |

## Final Deliverables

- `scripts/*_script.md`
- `scripts/*_script.json`
- `slides/*_gpt_image_prompts.md`
- GPT-Image2 source PNG and fitted final PNG
- VOICEVOX WAV
- MP4 video
- QA report
- Google Drive upload report
