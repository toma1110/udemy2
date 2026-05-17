# Lectures

## Course

- Course ID: `aws-cloudwatch-application-signals-practical-course`
- Source of Truth: `../course_spec.md`
- Production policy: GPT-Image2 generated slide text, VOICEVOX narration, MP4 build
- Visual baseline: `../../docs/VIDEO_QUALITY_BASELINE.md`
- Public repo local working copy: `../../public_repo/cloudwatch-application-signals-practical-cfn/`

## Section 1: Application Signalsの地図

### Section Learning Objective

Application Signalsで見えるサービス状態、依存関係、レイテンシ、可用性、フォルト、エラーを説明し、ハンズオンの安全策を理解する。

### Hands-on Resource Title

`Application Signalsサンプルアプリ CloudFormationハンズオン`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | Application Signalsで何が見えるか | Services、Application Map、Service detail、SLOの位置づけを説明できる | `s1-l1_script.md`, `s1-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s1-l2` | ハンズオン構成とコスト安全策 | 作成するAWSリソース、低頻度通信、停止、削除、料金注意を説明できる | `s1-l2_script.md`, `s1-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 2: CloudFormationでサンプルアプリを作る

### Section Learning Objective

CloudFormationテンプレートの全体像を読み、Lambda 2本構成、低頻度トラフィック、シナリオ切り替えをREADME通りに扱える。

### Hands-on Resource Title

`Application Signals Lambdaサンプルアプリ`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s2-l1` | テンプレート全体を読む | Discovery、Lambda、Scheduler、SLOの関係を読める | `s2-l1_script.md`, `s2-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s2-l2` | サンプルアプリと低頻度トラフィックをデプロイする | CEO承認後のcreate、validate、smokeの流れを説明できる | `s2-l2_script.md`, `s2-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s2-l3` | 正常、遅延、エラーのシナリオを切り替える | normal、slow、error、recoveryの違いと観測ポイントを説明できる | `s2-l3_script.md`, `s2-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 3: Application Signalsで見る

### Section Learning Objective

Services、Application Map、Service detailを順番に確認し、画面を見た後に次の調査へ進む判断を作れる。

### Hands-on Resource Title

`Application Signals画面確認ガイド`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s3-l1` | Servicesで状態を見る | サービス単位の状態、Call volume、Latency、Availabilityを確認できる | `s3-l1_script.md`, `s3-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s3-l2` | Application Mapで依存関係を見る | Traffic GeneratorとSample APIの関係を運用目線で説明できる | `s3-l2_script.md`, `s3-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s3-l3` | Service detailでLatency、Fault、Errorを読む | 遅延、フォルト、エラーをグラフとログ導線から確認できる | `s3-l3_script.md`, `s3-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 4: SLOと運用判断につなげる

### Section Learning Objective

Application Signals SLOの作成タイミング、短時間ハンズオンで確認できる範囲、実運用データが必要な範囲、停止・削除を説明できる。

### Hands-on Resource Title

`Application Signals SLOと後片付け`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s4-l1` | Application Signals SLOを作る | サービスがメトリクスを送信した後にSLOを有効化する理由を説明できる | `s4-l1_script.md`, `s4-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s4-l2` | RecommendationsとPerformance Reportの前提 | 十分な期間の実運用データが必要な機能を短時間ハンズオンと分けて説明できる | `s4-l2_script.md`, `s4-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s4-l3` | 停止、削除、コスト確認 | 自動トラフィック停止、スタック削除、コスト確認の順番を説明できる | `s4-l3_script.md`, `s4-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- `course_spec.md` と `course_curriculum.md` をSource of Truthにする
- AWSリソース作成、更新、削除の実演はCEO承認後の検証結果に合わせる
- Application Signals SLOは、サービスがメトリクスを送信した後で有効化する流れとして説明する
- 自動トラフィックは低頻度、停止可能、削除必須として扱う
- 1スライド1メッセージにする
- 表示文字はGPT-Image2生成にする
- ローカル文字合成は禁止
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- CloudFormationは教材ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
