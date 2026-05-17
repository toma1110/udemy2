# AWSアラート設計入門: 良いアラートと悪いアラート

この講座は、AWS/SRE初学者がCloudWatch Alarmや通知設定を作る前に、アラート設計の良し悪しを判断できるようにする短尺講座です。

## Source of Truth

- `course_spec.md`
- `course_curriculum.md`

## Course ID

`aws-alert-design-practical-course`

## 制作方針

- 操作説明ではなく、Alert Fatigueを防ぐ判断基準を売りにする
- 悪いアラート例を、対応可能な良いアラート例へ直す流れで説明する
- CloudWatch AlarmのPeriod、Evaluation Periods、Datapoints to Alarm、missing data、Composite Alarmを実務判断に結びつける
- Runbook、Owner、Severity、Escalationをアラート本文とセットで扱う
- 標準制作ではAWSリソースを作成しない
- 完成動画のスライドと表示文字はGPT-Image2で生成する
- 音声はVOICEVOXを使う
- 動画、コース画像はQA後にGoogle Driveへアップロードし、IssueとQAに記録する

## 講座構成

| Section | Title | Goal |
| --- | --- | --- |
| 1 | 良いアラートと悪いアラート | 深夜3時に動けるアラートの条件を説明できる |
| 2 | Alert Fatigueを防ぐ設計 | 鳴りすぎ、曖昧、Owner不在を改善できる |
| 3 | AWSメトリクスに落とす | CloudWatch Alarmの評価設定を設計判断として説明できる |

## ディレクトリ

- `scripts/`: 台本
- `slides/`: GPT-Image2プロンプトとスライド計画
- `audio/`: VOICEVOX音声
- `video/`: MP4生成レポート
- `qa/`: AWS仕様確認、制作QA、Driveアップロード記録
- `tickets/`: ローカルTask Issue写し
- `handson/`: 設計演習チェックリスト
- `cloudformation/`: v1では未使用。実AWS作成が必要になった場合のみCEO承認後に追加

## AWS実行ゲート

標準コンテンツは設計講義と演習で完結し、AWSリソース作成は不要です。

CloudWatch Alarm、SNS、Composite Alarm、CloudFormation stack作成/更新/削除など、実AWSでの検証を追加する場合はCEO承認後にだけ実行します。
