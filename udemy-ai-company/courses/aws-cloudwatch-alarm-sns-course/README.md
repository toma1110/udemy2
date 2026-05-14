# AWS CloudWatch Alarm + SNS通知ハンズオン

この講座は、VID-002「CloudFormationで作るCloudWatch Alarm + SNS通知」を制作するための作業領域です。

## Source of Truth

- `course_spec.md`

## 制作方針

- 教材ハンズオンではCloudFormationを使う
- 実運用IaCはCDKまたはTerraform推奨として説明する
- CloudWatch Alarm、SNS Topic、SNS Subscriptionを低コストで作る
- stack create/update/deleteはCEO承認後にのみ実行する
- 完成動画のスライドと表示文字はGPT-Image2で生成する
- VID-001の動画品質を基準にする

## ディレクトリ

- `cloudformation/`: 教材ハンズオン用テンプレートと検証スクリプト
- `scripts/`: 台本
- `slides/`: GPT-Image2プロンプト、source PNG、最終PNG
- `audio/`: VOICEVOX音声
- `video/`: MP4生成レポート
- `qa/`: AWS仕様確認、制作QA、Driveアップロード記録
- `tickets/`: ローカルTask Issue写し
