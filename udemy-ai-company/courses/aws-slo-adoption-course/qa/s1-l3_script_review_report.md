# S1-L3 Script Review Report

## 対象

- Course: `aws-slo-adoption-course`
- Lecture: Section 1 Lecture 3
- Script: `courses/aws-slo-adoption-course/scripts/s1-l3_script.md`
- Source of Truth: `courses/aws-slo-adoption-course/course_spec.md`

## Ownership

- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## Review Checks

| Check | Result |
|---|---|
| `lectures.md` の Lecture 1-3 と一致 | OK |
| `course_spec.md` の9セクション構成と一致 | OK |
| Application Signals の制約説明 | OK |
| CloudFormationハンズオンの位置づけ | OK |
| バーンレート、ダッシュボード、組織展開への導線 | OK |
| VOICEVOX向けナレーション表記 | OK |
| 文脈依存読みの回避 | OK |
| `tools/narration_checker.py` | OK |
| 1スライド1メッセージ | OK |

## Notes

- S1-L1は現場課題、S1-L2は対象者と学ぶ理由、S1-L3はコース全体の学習地図として役割を分離している。
- 旧 `s1-l3/input.json` のロードマップ意図は利用しつつ、現行 `course_spec.md` の9セクション構成に合わせて再構成した。
- ナレーション本文では英字サービス名を読み上げ表記へ変換済み。
- `触れる`、`そうした方`、`上で` など、S1-L2で問題になった文脈依存読みを避けている。

## Approval

Status: Ready for slide and audio generation

Approved By: AI-QA-01
