# CloudFormationで作るCloudWatch Alarm + SNS通知 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-cloudwatch-alarm-sns-course`
- Course Title: `CloudFormationで作るCloudWatch Alarm + SNS通知`
- Course Information: `course_infomation.md`
- Target Lecture Count: 6
- Target Main Lecture Runtime: 30〜42分
- Current Audit Result: 2026-05-17に通常レクチャー6本を再生成済み。合計2115.726秒、35.26分でUdemy標準コースの30分要件を満たしている。Google Driveアップロードは未実施。

## Curriculum Review Gate

- 動画再生成は2026-05-17のCEO依頼により実施済み。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- 全レクチャーの台本、VOICEVOX音声、MP4を一括で再生成済み。
- CloudFormation stack作成、更新、削除、通知テストはCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: Alarm + SNS通知の地図

Section Learning Goal: CloudWatch Alarm、SNS Topic、Email Subscription、通知確認の関係を説明できる。

Hands-on Resource Title: `Alarm + SNS通知の全体像チェックシート`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | Alarm + SNS通知の最小構成 | AlarmからSNS Topic、Emailまでの通知経路と最小構成を説明できる | Alarm + SNS通知の全体像チェックシート | 6.39分 | Produced - runtime remediated 2026-05-17 |
| `s1-l2` | CloudWatch Alarmの評価条件 | しきいち、期間、評価回数、データポイント、M out of Nを説明できる | Alarm評価条件チェック | 6.25分 | Produced - runtime remediated 2026-05-17 |
| `s1-l3` | SNS Topicとメール確認 | Topic、Subscription、PendingConfirmation、Topic Policyを説明できる | SNSメール確認チェック | 5.15分 | Produced - runtime remediated 2026-05-17 |

## Section 2: CloudFormationで作る

Section Learning Goal: CloudFormationテンプレートを読み、作成、通知確認、更新対象をREADME通りに追える。

Hands-on Resource Title: `CloudFormationテンプレート読解とStack作成手順`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | CloudFormationテンプレートを読む | Parameters、Conditions、Resources、Outputsと作成されるAlarm/SNSの関係を説明できる | CloudFormationテンプレート読解 | 5.73分 | Produced - runtime remediated 2026-05-17 |
| `s2-l2` | Stack作成と通知テスト | Stack作成、メール確認、SNS publish、任意のAlarm state testの順番を説明できる | Stack作成と通知テスト手順 | 5.83分 | Produced - runtime remediated 2026-05-17 |

## Section 3: 運用と後片付け

Section Learning Goal: stack update/delete、通知が届かない時の切り分け、教材CloudFormationと実運用IaCの違いを説明できる。

Hands-on Resource Title: `更新・削除・トラブルシュート確認リスト`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | 更新・削除・トラブルシュート | しきいち更新、削除、PendingConfirmation、AlarmActions、Topic Policyの確認ポイントを説明できる | 更新・削除・トラブルシュート確認リスト | 5.91分 | Produced - runtime remediated 2026-05-17 |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Alarm + SNS通知の全体像チェックシート | `handson/README.md` | なし | 作成前の概念整理 |
| CloudFormationテンプレート読解 | `cloudformation/template.yaml` | なし | 実行前に読む |
| Stack作成と通知テスト手順 | `cloudformation/README.md` | SNS Topic、Subscription、CloudWatch Alarm | CEO承認後のみ実行 |
| 更新・削除・トラブルシュート確認リスト | `cloudformation/README.md` | 作成済みStack | 削除確認まで必須 |

## Definition of Done

- 通常レクチャー6本が存在する。
- 講義本編の合計動画尺が30分以上である。2026-05-17時点で35.26分。
- CEO依頼後に全レクチャーを再生成し、短尺版をそのまま完成扱いにしていない。
- CloudFormation validate、create、update、smoke test、deleteの結果をQAに残す。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポートが各レクチャーに存在する。
- Drive upload reportはGoogle Driveアップロード承認後に追加する。
