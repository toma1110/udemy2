# Lectures

## Course

- Course ID: `aws-cloudwatch-intro-course`
- Source of Truth: `../course_spec.md`
- Production policy: VOICEVOX narration, slide PNG, MP4 build

## Section 1

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる | `s1-l1_script.md`, `s1-l1_script.json`, slide PNG, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- 1スライド1メッセージにする
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- ナレーション本文には英字略語を残さない
- CloudFormationは講座内ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
- 本動画ではAWSリソースを作成しない

