# Hands-on Validation Report

## Target Course

AWS SRE入門：CloudFormationで作る監視基盤ハンズオン

## Stack Name

`sample-aws-sre-dev-monitoring-20260510-0146`

## Region

`us-east-1`

## Validator

AI-Engineer-01

## Validation Date

2026-05-10

## Source of Truth

対象 `course_spec.md`:

`udemy-ai-company/courses/sample-aws-sre-course/course_spec.md`

## Commands

```bash
cd udemy-ai-company/courses/sample-aws-sre-course/cloudformation

STACK_NAME=sample-aws-sre-dev-monitoring-20260510-0146 \
PROJECT_NAME=udemy-sre-sample-20260510 \
AWS_REGION=us-east-1 \
./validate.sh full
```

再確認:

```bash
./validate.sh validate
bash -n validate.sh
bash -n smoke_test.sh
```

## Results

- validate: success
- create: success
- smoke test after create: success
- update: success
- smoke test after update: success
- delete: success
- stack deletion confirmation: success, stack no longer exists

## Smoke Test Coverage

`smoke_test.sh` で以下を確認した。

- CloudFormation Outputs取得
- CloudWatch Alarm存在確認
- SNS Topic存在確認
- CloudWatch Dashboard存在確認

確認対象:

- `udemy-sre-sample-20260510-sample-alarm`
- `arn:aws:sns:us-east-1:668602146132:udemy-sre-sample-20260510-alarm-topic`
- `udemy-sre-sample-20260510-dashboard`

## README Reproduction

README通りに再現できたか:

Yes.

以下のREADME手順に対応する操作を実行し、成功を確認した。

- template validation
- stack create
- smoke test
- stack update
- stack delete
- deletion confirmation

## Course Spec Consistency

`course_spec.md` のCloudFormation Scopeと実装の対応:

| course_spec.md | template.yaml | Status |
| --- | --- | --- |
| `AWS::CloudWatch::Alarm` | `SampleAlarm` | OK |
| `AWS::SNS::Topic` | `AlarmTopic` | OK |
| `AWS::SNS::Subscription` はメールアドレス指定時のみ | `AlarmEmailSubscription` with condition | OK |
| `AWS::CloudWatch::Dashboard` | `MonitoringDashboard` | OK |

## Cost and Cleanup

- CloudWatch Alarm、Dashboard、SNSは料金が発生する場合がある
- READMEに想定コスト注意がある
- `validate.sh full` は最後にdeleteまで実行する
- 検証スタックは削除済み

削除確認:

`aws cloudformation describe-stacks` で対象スタックが存在しないことを確認済み。

## Worker and Reviewer

- Owner AI: AI-Engineer-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: satisfied

## Notes

- 2026-05-10 04:59 UTC に `./validate.sh validate` を再実行し成功
- `bash -n validate.sh` と `bash -n smoke_test.sh` も成功
- 実AWSでの `full` 検証は2026-05-10に完了済み
- SNSメール購読は `NOTIFICATION_EMAIL` 未指定のため作成していない

## Approval

Reviewer AI:

AI-QA-01

Status:

Pending review
