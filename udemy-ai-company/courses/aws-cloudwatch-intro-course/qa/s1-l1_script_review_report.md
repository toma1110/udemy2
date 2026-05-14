# S1-L1 Script Review Report

## Target

- Course: `aws-cloudwatch-intro-course`
- Lecture: `s1-l1`
- Script: `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.md`
- JSON: `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- Source of Truth: `courses/aws-cloudwatch-intro-course/course_spec.md`

## Ownership

- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## Review Checks

| Check | Result |
| --- | --- |
| VID-001の講座範囲と一致 | OK |
| `course_spec.md` のLearning Objectivesと一致 | OK |
| Metrics、Logs、Alarm、Dashboardを分離して説明 | OK |
| Dashboardを保存場所と誤解させない説明 | OK |
| Alarmを条件、状態、アクションで説明 | OK |
| ハンズオンはリソース作成なし | OK |
| CloudFormationは教材ハンズオン内の再現性用途として説明 | OK |
| 実運用IaCはCDKまたはTerraform前提として説明 | OK |
| 1スライド1メッセージ | OK |
| VOICEVOX向けナレーション表記 | OK |

## Automated Checks

```bash
python3 udemy-ai-company/tools/markdown_script_to_json.py \
  udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.md \
  udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json

python3 udemy-ai-company/tools/narration_checker.py \
  udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts \
  --warnings-ok
```

Result:

- Markdown to JSON: OK, 10 slides
- Narration checker: OK, 1 file checked

## Notes

- ナレーション本文では英字サービス名を読み上げ表記へ変換済み。
- `しきいち`、`アイエーシー`、`シーディーケー`、`テラフォーム` など、VOICEVOXで読み崩れやすい語を事前に調整した。
- スライドタイトルとメッセージには受講者が検索しやすい英字表記を残しているが、音声対象のナレーション本文には残していない。

## Approval

Status: Ready for slide storyboard and asset generation

Approved By: AI-QA-01
