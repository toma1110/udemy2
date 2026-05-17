# AWS障害対応Runbook入門: アラートから初動対応へ

この講座は、AWS/SRE初学者がCloudWatch Alarmを受け取ったあとに、何を確認し、誰へ連絡し、どう緩和へ進むかをRunbookとして整理する短尺講座です。

## Source of Truth

- `course_spec.md`
- `course_curriculum.md`

## Course ID

`aws-runbook-first-response-course`

## 制作方針

- 「アラートが鳴ったあと、次に何をするか」を主題にする
- Runbookを、Owner、Severity、Trigger、First Checks、Mitigation、Escalation、Communication、Postmortem Linkで構成する
- PlaybookとRunbookの違いを簡潔に説明する
- CloudWatch Alarm、Dashboard、Logs、Recent deploy、AWS Healthを初動確認の入口として扱う
- 標準制作ではAWSリソースを作成しない
- 完成動画のスライドと表示文字はGPT-Image2で生成する
- 音声はVOICEVOXを使う
- 動画、コース画像はQA後にGoogle Driveへアップロードし、IssueとQAに記録する

## 講座構成

| Section | Title | Goal |
| --- | --- | --- |
| 1 | Runbookの地図 | Runbookに何を書くべきか説明できる |
| 2 | アラートから初動確認へ | CloudWatch Alarmから確認順序へ進める |
| 3 | 緩和とエスカレーション | 復旧判断、切り戻し、連絡、振り返りへつなげる |

## ディレクトリ

- `scripts/`: 台本
- `slides/`: GPT-Image2プロンプトとスライド
- `audio/`: VOICEVOX音声
- `video/`: MP4生成レポート
- `qa/`: AWS仕様確認、制作QA、Driveアップロード記録
- `tickets/`: ローカルTask Issue写し
- `handson/`: Runbookテンプレートと演習
- `cloudformation/`: v1では未使用。実AWS作成が必要になった場合のみCEO承認後に追加

## AWS実行ゲート

標準コンテンツは設計講義とテンプレート演習で完結し、AWSリソース作成は不要です。

CloudWatch Alarm、Systems Manager Automation、Incident Manager、CloudFormation stack作成/更新/削除など、実AWSでの検証を追加する場合はCEO承認後にだけ実行します。
