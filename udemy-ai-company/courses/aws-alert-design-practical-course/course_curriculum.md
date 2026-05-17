# AWSアラート設計入門 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-alert-design-practical-course`
- Course Title: `AWSアラート設計入門: 良いアラートと悪いアラート`
- Course Information: `course_infomation.md`
- Target Lecture Count: 6
- Target Main Lecture Runtime: 30〜36分
- Current Audit Result: 2026-05-17時点で通常レクチャーMP4は1本、合計約3.1分。`s1-l2`、`s2-l1`、`s2-l2`、`s3-l1`、`s3-l2` が未作成。

## Curriculum Review Gate

- 動画生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で生成してよい。
- 標準範囲ではAWSリソースを作成しない。追加検証でAWS実行する場合はCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: 良いアラートと悪いアラート

Section Learning Goal: 深夜3時に動けるアラートの条件と、悪いアラートを良いアラートへ直す観点を説明できる。

Hands-on Resource Title: `アラートレビュー演習`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | 深夜3時に動けるアラートとは | Actionable、Timely、Meaningfulの3条件で良いアラートを説明できる | 良いアラート条件チェック | 5〜6分 | Produced - regenerate for runtime |
| `s1-l2` | 悪いアラートを良いアラートへ直す | 鳴りすぎ、原因だけ、Owner不在、Runbook不在のアラートを改善できる | 悪いアラート改善演習 | 5〜6分 | Not produced |

## Section 2: Alert Fatigueを防ぐ設計

Section Learning Goal: アラート数を減らし、Owner、Runbook、Escalationを決めて、通知後に動ける状態へ整えられる。

Hands-on Resource Title: `Alert Fatigue削減チェック`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | 鳴りすぎるアラートを減らす | ノイズ、重複通知、短すぎる評価期間、Composite Alarmの使いどころを説明できる | 鳴りすぎアラート削減演習 | 5〜6分 | Not produced |
| `s2-l2` | Owner、Runbook、Escalationを決める | Severity、Owner、Runbook、Escalationをアラート設計に入れる理由を説明できる | Owner/Runbook/Escalation設計 | 5〜6分 | Not produced |

## Section 3: AWSメトリクスに落とす

Section Learning Goal: CloudWatch Alarmの評価設定、missing data、Composite Alarmを、ノイズ削減と実務判断に結びつけて説明できる。

Hands-on Resource Title: `CloudWatch Alarm設計読解`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | CloudWatch Alarmの評価設定を読む | Period、Evaluation Periods、Datapoints to AlarmをM out of Nとして説明できる | Alarm評価設定読解 | 5〜6分 | Not produced |
| `s3-l2` | Missing dataとComposite Alarmの使いどころ | 常時出るメトリクスとエラー時だけ出るメトリクスでmissing dataの扱いを分けられる | missing data/Composite Alarm設計 | 5〜6分 | Not produced |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| アラートレビュー演習 | `handson/README.md` | なし | 標準は設計演習のみ |
| Alert Fatigue削減チェック | `handson/README.md` | なし | 通知数削減の判断を扱う |
| CloudWatch Alarm設計読解 | `handson/README.md` | なし | 実AWS作成は標準範囲外 |

## Definition of Done

- 通常レクチャー6本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを生成し、既存の短尺 `s1-l1` だけを完成扱いにしない。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
