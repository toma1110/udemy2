# CloudFormation Scope

このディレクトリは、長尺旗艦コースの教材用CloudFormationを配置する領域です。

## Planned Resources

- `AWS::Logs::LogGroup`
- `AWS::CloudWatch::Alarm`
- `AWS::CloudWatch::CompositeAlarm`
- `AWS::CloudWatch::Dashboard`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription` はメール通知演習で任意
- `AWS::IAM::Role` は必要最小限に限定

## Required Scripts

- `validate.sh`
- `smoke_test.sh`
- サンプルログまたはサンプルメトリクス投入スクリプト
- delete後の残リソース確認スクリプト

## Quality Gate

- CloudFormation validate success
- stack create success
- smoke test success
- stack update success
- stack delete success
- README reproduction success
- コスト注意と削除手順が明記されている

## Production IaC Positioning

CloudFormationは教材ハンズオンの再現性を重視して使う。実運用では、チームのレビュー、再利用、テスト、CI/CDに合わせてCDKまたはTerraformを推奨する。
