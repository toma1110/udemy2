# AWS障害対応Runbook入門: アラートから初動対応へ

## Course Title

AWS障害対応Runbook入門: アラートから初動対応へ

## Course ID

`aws-runbook-first-response-course`

## Source Candidate

- Market research ID: `VID-008`
- Candidate title: `AWS障害対応Runbookを作る`
- Priority: high
- GitHub Issue: `#173` / `TASK-0201`

## Course Positioning

本コースは、アラート設計の次に必要になる「初動対応の型」を学ぶ短尺講座です。

`aws-alert-design-practical-course` では、良いアラートの条件としてOwner、Severity、Runbookを扱いました。本コースでは、そのRunbookの中身を具体化します。CloudWatch Alarmを受け取ったあと、影響確認、初期切り分け、緩和、エスカレーション、連絡、ポストモーテムへの接続までを、受講者がテンプレートとして書ける状態にします。

## Target Audience

- CloudWatch Alarmを受け取ったあとに何をすべきか迷う人
- SRE、DevOps、クラウド運用に進みたい初学者
- 属人化した障害対応を、チームで使える手順にしたい人
- アラート設計、Runbook、ポストモーテムの流れをつなげたい人
- 既存CloudWatch、Alarm + SNS、SLO講座の理解を実務運用へ寄せたい人

## Prerequisites

- AWS CloudWatch Alarm、Dashboard、Logsの基本用語を知っている
- エラー率、レイテンシ、可用性、デプロイ、ロールバックの意味を聞いたことがある
- SRE、Runbook、Postmortemの詳細経験は不要
- AWS CLIやCloudFormationの実行環境は不要

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- Runbookが、特定の結果を得るための手順であることを説明できる
- Playbookが調査手順、Runbookが既知の緩和・復旧手順であることを区別できる
- RunbookにTrigger、Owner、Severity、Scope、First Checks、Mitigation、Escalation、Communication、Postmortem Linkを書く理由を説明できる
- CloudWatch Alarmから、Dashboard、Logs、Recent deploy、AWS Healthへ進む初動確認を整理できる
- 5分、15分、30分の時間軸で初動対応を分けられる
- Runbookの変更管理、定期レビュー、演習が必要であることを説明できる

## Course Promise

受講後、CloudWatch Alarmが鳴ったあとに「何を見るか」「誰が動くか」「いつエスカレーションするか」をRunbookとして書ける状態になります。

## Differentiation

- AWS操作ではなく、障害対応の初動判断を主役にする
- アラート設計動画の次に自然につながる
- Runbookテンプレートを中心に、受講者がすぐ使える型へ落とす
- Playbook、Runbook、Postmortemの違いを混同しない
- 標準範囲ではAWSリソースを作成せず、低リスクで学べる
- 将来Systems Manager Automationへ発展できるが、初学者向けv1では手順書から始める

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. Runbookの地図
   - `s1-l1` Runbookに何を書くか
   - `s1-l2` PlaybookとRunbookの違い

2. アラートから初動確認へ
   - `s2-l1` CloudWatch Alarmから5分で確認すること
   - `s2-l2` Dashboard、Logs、Recent deploy、AWS Healthを見る

3. 緩和とエスカレーション
   - `s3-l1` Mitigation、Rollback、Escalationを決める
   - `s3-l2` CommunicationとPostmortemへつなげる

## Hands-on Scope

標準ハンズオンはAWSリソースを作らないRunbook作成演習にする。

- アラート例を1つ選ぶ
- Trigger、Owner、Severityを決める
- First Checksを5分以内の確認に絞る
- MitigationとEscalationを分ける
- CommunicationとPostmortem Linkを追加する
- レビュー観点でRunbookをチェックする

## CloudFormation Scope

v1ではCloudFormationテンプレートを作成しない。

教材で実AWS例が必要になった場合のみ、既存 `aws-cloudwatch-alarm-sns-course` のCloudWatch Alarm構成を参照する。CloudFormationは教材再現用であり、実運用IaCはCDKまたはTerraformを推奨する。

## Systems Manager Automation Scope

AWS Systems Manager Automationは、将来的にテキストRunbookを自動化する発展先として紹介する。

初版ではAutomation documentの実装、Incident Manager連携、IAMロール作成、実AWS実行は扱わない。なお、Incident Managerは新規顧客向け提供状況に注意が必要なため、標準導線にはしない。

## Cost Warning

標準範囲ではAWSリソースを作成しないため、AWS利用料金は発生しません。

追加検証としてCloudWatch Alarm、Systems Manager Automation、Incident Manager、CloudFormation stackを作成する場合は料金や権限影響が発生する可能性があるため、CEO承認後に実施し、削除手順をQAへ残します。

## Udemy成立尺是正方針

2026-05-17の既存コース動画監査では、course spec上は6レクチャー構成だが、通常レクチャーMP4は1本、合計尺は約2.8分のみである。

是正後の制作方針:

- レクチャー数は現行の6本を維持する
- 各レクチャーをおおむね5〜6分に設計し、講義本編の計画尺を30〜36分にする
- 未作成の `s1-l2`、`s2-l1`、`s2-l2`、`s3-l1`、`s3-l2` を含め、全レクチャーを完成対象にする
- プロモーション動画は30分要件に含めない
- 動画生成前に、CEOが更新後の `course_spec.md` と `course_infomation.md` を確認・承認する
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で生成してよい

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- コース画像もGPT-Image2由来PNGにし、QA後にGoogle Driveへアップロードする
- WorkerとReviewerを分離する

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である
- 動画生成前にCEOが `course_spec.md` と `course_infomation.md` を確認・承認している
- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- `course_infomation.md` にUdemy登録情報、歓迎メッセージ、お祝いメッセージがある
- `course_curriculum.md` にセクションタイトル、学習目標、制作対象レクチャーがある
- `handson/runbook_template.md` が存在する
- `scripts/s1-l1_runbook_map_script.md` に初回動画台本がある
- `slides/s1-l1_gpt_image2_prompts.md` にGPT-Image2プロンプトがある
- 台本、スライド計画、QA計画が一致している
- スライドと表示文字はGPT-Image2生成である
- VOICEVOX音声、MP4、Drive URL、QAレポートが作成済みである
- WorkerとReviewerが別AIである

## Out of Scope

- 本番インシデント対応体制の設計代行
- PagerDuty、Opsgenie、Slack連携の実装
- AWS Incident Managerの実装
- Systems Manager Automation documentの実装
- CloudFormationテンプレートの新規作成
- CDKまたはTerraformによる本番IaC実装
- 実AWSでのロールバック、リスタート、フェイルオーバー実行

## References

- AWS Well-Architected: OPS07-BP03 Use runbooks to perform procedures
  - https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html
- AWS Well-Architected: OPS07-BP04 Use playbooks to investigate issues
  - https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html
- AWS Cloud Operations Blog: Achieving Operational Excellence using automated playbook and runbook
  - https://aws.amazon.com/blogs/mt/achieving-operational-excellence-using-automated-playbook-and-runbook/
- Systems Manager Incident Manager runbooks
  - https://docs.aws.amazon.com/incident-manager/latest/userguide/runbooks.html
