# VOICEVOX Terms Report

## Scope

SLO講座で頻出する英字用語、複合英語、空白読みリスクを確認しました。

対象:

- `udemy-ai-company/docs/VOICEVOX_RULES.md`
- `udemy-ai-company/tools/narration_checker.py`
- `udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md`
- `/home/ubuntu/workspace/udemy/courses/sre-slo-introduction/s1-l1/script.json`

## Added/Confirmed Terms

| Term | Reading |
| --- | --- |
| SLO | エスエルオー |
| SLI | エスエルアイ |
| SLA | エスエルエー |
| Service Level Objective | サービスレベルオブジェクティブ |
| Service Level Indicator | サービスレベルインディケーター |
| Service Level Agreement | サービスレベルアグリーメント |
| Application Signals | アプリケーションシグナル |
| error budget | エラーバジェット |
| burn rate | バーンレート |
| request-based SLO | リクエストベースドエスエルオー |
| period-based SLO | ピリオドベースドエスエルオー |
| SLO Recommendations | エスエルオーレコメンデーション |
| SLO Performance Report | エスエルオーパフォーマンスレポート |

## Space-Reading Risks

以下はVOICEVOXで不自然な間が出やすいため、台本では日本語読みで書くことを推奨します。

- `Application Signals`
- `Service Level Objective`
- `Service Level Indicator`
- `Service Level Agreement`
- `request-based SLO`
- `period-based SLO`
- `SLO Recommendations`
- `SLO Performance Report`

## Checker Behavior

`tools/narration_checker.py` は、正規化後に英字が残らない既知用語について、英字残存エラーを出さないようにしました。

ただし書く時ルールとしては、台本本文では以下のように日本語読みを優先します。

- `Application Signals` ではなく「アプリケーションシグナル」
- `error budget` ではなく「エラーバジェット」
- `burn rate` ではなく「バーンレート」

## Validation

実行済み:

```bash
python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts
python3 udemy-ai-company/tools/narration_checker.py /home/ubuntu/workspace/udemy/courses/sre-slo-introduction/s1-l1/script.json --warnings-ok
```

結果:

- SLO講座サンプル台本: OK
- 既存 `s1-l1/script.json`: OK

## Remaining Risks

- 実際のVOICEVOX聴取では、英字正規化だけでは拾えないイントネーション違和感が残る可能性がある
- Application Signals章ではAWSサービス名が増えるため、台本作成後に再チェックが必要
- 旧WAVは再利用せず、更新後台本から再生成する
