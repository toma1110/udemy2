# Existing Asset Migration Plan

## Purpose

`/home/ubuntu/workspace/udemy/courses/sre-slo-introduction` にある既存SLO講座素材を、`aws-slo-adoption-course` へ安全に移植するための分析です。

`course_spec.md` を唯一の真実とし、古い説明や現行AWS機能とずれる内容はそのまま使わず、修正対象として扱います。

## Source Inventory

| Source | Status | Reuse Decision |
| --- | --- | --- |
| `course-overview.json` | 企画情報あり | 方向性は再利用。対象者、差別化、学習目標は `course_spec.md` に反映済み |
| `lectures.json` | 34講義の旧構成あり | 章構成の土台として再利用。新講座では35ユニットへ再整理済み |
| `s1-l1/script.json` | 9スライドの完成台本あり | Section 1 Lecture 1の下書きとして再利用可能 |
| `s1-l1/slides/*.png` | 9枚あり | 旧デザイン確認用。GPT-Image2で再生成する前提 |
| `s1-l1/audio/*.wav` | 9本あり | 読み上げ確認用。VOICEVOX用語ルール更新後に再生成推奨 |
| `s1-l1/*.mp4` | 複数版あり | 参考のみ。新講座の完成動画としては使わない |
| `s1-l2/input.json` | 入力案のみ | Section 1 Lecture 2の設計材料として再利用 |
| `s1-l3/input.json` | 入力案のみ | Section 1 Lecture 3の設計材料として再利用 |

## Reuse Mapping

| New Course Unit | Existing Asset | Action |
| --- | --- | --- |
| 1-1 このコースで解決するSLO導入あるある | `s1-l1/script.json` | 台本構成を移植し、Application Signalsと現行CloudFormation方針を補足 |
| 1-2 SREを目指す人がSLOを学ぶ理由 | `s1-l2/input.json` | 新規台本化 |
| 1-3 コース全体のロードマップ | `s1-l3/input.json` | `lectures.md` に合わせて新規台本化 |
| 2-1〜3-5 SLI/SLO基礎 | `aws-sre-practical/s6-l1/script.json` と `lectures.json` | 概念説明を部分再利用。音声用語は再チェック |
| 4-1〜4-4 Application Signals章 | 既存素材なし | 新規作成。2026年時点のCloudWatch SLO機能を前提にする |
| 5-1〜5-5 CloudFormationハンズオン | 既存素材なし | `aws-slo-adoption-course/cloudformation` を正とする |
| 6-1〜7-3 バーンレート、ダッシュボード | `lectures.json` | 章案のみ再利用。実装は新規 |
| 8-1〜9-4 組織導入、レビュー運用 | `lectures.json` | 章案のみ再利用。ワークシートは新規 |

## Stale Content Risks

- 旧素材はCloudWatch Application Signalsの現行SLO機能を前提にしていない可能性が高い
- `CloudWatch Composite AlarmでSLOを実装する` という旧表現は、現行SLO機能との関係を説明しないと古く見える
- 完成済み `s1-l1` 音声は、`SLO` をそのまま読む箇所と「エスエルオー」に直した箇所が混在する可能性がある
- 旧動画ファイルは複数版があるため、最終版判定なしに再利用しない
- スライドPNGはGPT-Image2の新講座トーンに合わせて再生成する

## Migration Rules

- 既存 `script.json` はそのままコピーせず、`course_spec.md` に合わせて再編集する
- `SLO`、`SLI`、`SLA` は台本上では「エスエルオー」「エスエルアイ」「エスエルエー」に統一する
- `Application Signals` は「アプリケーションシグナル」に統一する
- `burn rate` は「バーンレート」、`error budget` は「エラーバジェット」に統一する
- 移植後は必ず `tools/narration_checker.py` を実行する
- 音声は旧WAVを流用せず、VOICEVOXで再生成する

## First Production Recommendation

最初に作るべき教材は Section 1 Lecture 1 です。

理由:

- 既存 `s1-l1/script.json` があり、再利用効率が高い
- 講座の価値提案を最初に固められる
- VOICEVOX用語ルールの検証に適している

次のIssue案:

- `TASK-0007 Section 1 Lecture 1 台本を移植・更新する`
- `TASK-0008 Section 1 Lecture 1 スライドPNGをGPT-Image2で再生成する`
- `TASK-0009 Section 1 Lecture 1 音声をVOICEVOXで再生成する`

## QA Checklist

- `course_spec.md` と矛盾していない
- Application Signalsの現行SLO機能を無視していない
- 古いComposite Alarm中心の説明に寄りすぎていない
- VOICEVOXチェックが通る
- READMEと動画手順が一致している
