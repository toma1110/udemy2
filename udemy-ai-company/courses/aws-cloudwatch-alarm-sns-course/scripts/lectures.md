# Lectures

## Course

- Course ID: `aws-cloudwatch-alarm-sns-course`
- Source of Truth: `../course_spec.md`
- Production policy: GPT-Image2 generated slide text, VOICEVOX narration, MP4 build
- Visual baseline: `../../docs/VIDEO_QUALITY_BASELINE.md`

## Section 1: Alarm + SNS通知の地図

### Section Learning Objective

CloudWatch AlarmとSNS通知の役割を分け、状態変化からメール通知までの流れを説明できる。

### Hands-on Resource Title

`Alarm + SNS通知の全体像チェックシート`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | Alarm + SNS通知の最小構成 | CloudFormationでCloudWatch AlarmからSNS通知までの流れを説明できる | `s1-l1_script.md`, `s1-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s1-l2` | CloudWatch Alarmの評価条件 | しきいち、期間、評価回数、データポイントを区別できる | `s1-l2_script.md`, `s1-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s1-l3` | SNS Topicとメール確認 | Topic、Subscription、PendingConfirmation、Topic Policyを説明できる | `s1-l3_script.md`, `s1-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 2: CloudFormationで作る

### Section Learning Objective

VID-002テンプレートを読み、CEO承認後にREADME通りの作成、確認、通知テストを再現できる。

### Hands-on Resource Title

`CloudFormationテンプレート読解とStack作成手順`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s2-l1` | CloudFormationテンプレートを読む | Parameters、Conditions、Resources、Outputsを分けて読める | `s2-l1_script.md`, `s2-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s2-l2` | Stack作成と通知テスト | 作成、メール確認、SNS publish、任意のAlarm state testの順番を説明できる | `s2-l2_script.md`, `s2-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 3: 運用と後片付け

### Section Learning Objective

更新、削除、通知トラブルシュート、実運用IaCの位置づけまで説明できる。

### Hands-on Resource Title

`更新・削除・トラブルシュート確認リスト`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s3-l1` | 更新・削除・トラブルシュート | しきいち更新、削除、PendingConfirmation、AlarmActions、Topic Policyを確認できる | `s3-l1_script.md`, `s3-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- VID-001の視覚品質を下回らない
- 1スライド1メッセージにする
- 表示文字はGPT-Image2生成にする
- ローカル文字合成は禁止
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- CloudFormationは教材ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
