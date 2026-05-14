# Lectures

## Course

- Course ID: `aws-cloudwatch-alarm-sns-course`
- Source of Truth: `../course_spec.md`
- Production policy: GPT-Image2 generated slide text, VOICEVOX narration, MP4 build
- Visual baseline: `../../docs/VIDEO_QUALITY_BASELINE.md`

## Section 1

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | Alarm + SNS通知の最小構成 | CloudFormationでCloudWatch AlarmからSNS通知までの流れを説明できる | `s1-l1_script.md`, `s1-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- VID-001の視覚品質を下回らない
- 1スライド1メッセージにする
- 表示文字はGPT-Image2生成にする
- ローカル文字合成は禁止
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- CloudFormationは教材ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
