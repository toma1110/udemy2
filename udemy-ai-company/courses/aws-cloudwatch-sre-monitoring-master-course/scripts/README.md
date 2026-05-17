# Scripts

このディレクトリは、各レクチャーの台本を配置する領域です。

## Rules

- `course_spec.md` と `course_curriculum.md` に矛盾しない
- VOICEVOX読み上げを前提に、略語の読みを統一する
- `CloudWatch` は「クラウドウォッチ」
- `Logs Insights` は「ログズインサイト」
- `Application Signals` は「アプリケーションシグナル」
- `SLI` は「エスエルアイ」
- `SLO` は「エスエルオー」
- `SLA` は「エスエルエー」
- `IAM` は「アイアム」
- 章末演習とCapstoneでは、操作説明だけでなく判断理由を説明する

## Check

台本生成後はナレーションチェッカーを実行する。

```bash
python3 tools/narration_checker.py courses/aws-cloudwatch-sre-monitoring-master-course/scripts
```
