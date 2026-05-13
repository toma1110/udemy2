# aws-slo-adoption-course

この講座は、SREを目指すエンジニアがAWS上でSLO導入を実践できるようになるための講座です。

## Source of Truth

[course_spec.md](course_spec.md) を唯一の真実として扱います。

## 制作方針

- CloudFormationを原則とする
- SLOは概念だけでなく、計測、可視化、通知、組織導入まで扱う
- CloudWatch Application Signalsの現行SLO機能を扱う
- ただし30日データや実アプリ計装が必要な機能は補講/デモとして扱う
- VOICEVOX読み上げでは `SLO` を「エスエルオー」、`SLI` を「エスエルアイ」に統一する

## ハンズオン

CloudFormationハンズオンは [cloudformation/README.md](cloudformation/README.md) を参照してください。

扱う内容:

- CloudWatch Custom Metricsによる可用性、レイテンシ、エラー率のSLI
- Metric Mathによるバーンレート
- CloudWatch Alarm、Dashboard、SNS
- Optional: Application Signals SLO

## 次の作業

1. AI-QA-01が `qa/handson_cloudformation_validation_report.md` をレビューする
2. CEOがAWSリソース作成コストを許容した場合、`cloudformation/README.md` に沿って `./validate.sh full` を実行する
3. 実行結果をハンズオン検証レポートへ追記する
