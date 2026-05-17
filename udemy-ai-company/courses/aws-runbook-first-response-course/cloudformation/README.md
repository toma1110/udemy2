# CloudFormation

本コースv1ではCloudFormationテンプレートを作成しません。

理由:

- 講座の主目的は、AWSリソース作成ではなく、障害対応Runbookの型を学ぶこと
- 標準コンテンツはAWSリソース作成なしで成立すること
- Alarm + SNSの実装ハンズオンは `aws-cloudwatch-alarm-sns-course` に分離すること

## 将来追加する場合

CloudFormationテンプレートを追加する場合は、以下を守ります。

- 教材ハンズオン用途に限定する
- 実運用IaCはCDKまたはTerraformを推奨する
- `validate.sh`、`smoke_test.sh`、削除手順を必須にする
- stack create/update/deleteはCEO承認後にのみ実行する
- 料金と削除漏れリスクを明記する
