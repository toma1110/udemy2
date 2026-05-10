# qa

QAレポート、ハンズオン検証レポート、差戻し記録を配置します。

## 使うテンプレート

- `templates/qa_report_template.md`
- `templates/handson_validation_report_template.md`
- `templates/impact_analysis_template.md`

## ルール

- WorkerとReviewerが別AIであることを確認する
- `course_spec.md` との整合性を確認する
- README再現結果を記録する
- 未実施項目がある場合は理由とリスクを書く
- `docs/VOICEVOX_RULES.md` に沿って台本と音声を確認する
- `tools/narration_checker.py` の結果を記録する

## 承認条件

`docs/QUALITY_GATE.md` の該当項目を満たした場合のみ承認する。
