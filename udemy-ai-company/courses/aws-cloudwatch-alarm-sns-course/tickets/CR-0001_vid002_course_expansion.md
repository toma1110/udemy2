# Change Request

## Change Summary

VID-002を1動画の単発教材から、CloudWatch Alarm + SNS通知を作成、確認、更新、削除まで扱う短い実践コースへ拡張する。

## Why Change

CloudWatch AlarmとSNS通知は需要が高く、既存動画の品質を維持したまま、Alarm評価条件、メール確認、CloudFormation読解、通知テスト、トラブルシュートまで育てる価値があるため。

## Scope

- `course_spec.md` と `course_curriculum.md` の更新
- 追加レクチャー5本の台本、GPT-Image2プロンプト、スライド、VOICEVOX音声、MP4の作成
- QAレポートとGoogle Driveアップロード記録の作成

## Impact

- 既存の `s1-l1` は保持する
- Course IDは `aws-cloudwatch-alarm-sns-course` のまま
- CloudFormationテンプレートは既存最小構成を維持し、動画内で読み方と検証手順を補強する

## Risks

- AWS stack create/update/deleteは課金影響があるため、CEO承認なしでは実行しない
- メールSubscriptionは受講者側の確認操作が必要
- GPT-Image2生成文字は完全な写植ではないため、ローカル文字合成は禁止しつつQAで確認する

## Approval

- CEO request: 「vhd002の方も同様の対応」
- Implementation allowed for教材・動画制作
- AWS create/update/deleteは別途CEO承認が必要

## Implementation Plan

1. コース仕様とカリキュラムをセクション別に更新する
2. 追加レクチャー5本の台本とプロンプトを作る
3. GPT-Image2スライドを生成し、1920x1080へフィットする
4. VOICEVOX音声とMP4を生成する
5. QA、Driveアップロード、commit、pushを行う
