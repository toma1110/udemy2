# PROJECT

## プロジェクト名

AI制作会社 v1

## ミッション

AWS/SRE関連のUdemy講座を、GitHub Issueベースで半自律的に企画、実装、教材化、レビュー、公開できる制作システムを作る。

## 制作対象

- AWS SRE入門
- CloudFormationハンズオン
- CloudWatch、SNS、IAM、ログ、監視、アラート、運用改善
- Terraform講座は例外的にTerraformを利用する

## Source of Truth

各講座の `course_spec.md` を唯一の真実とする。

以下は `course_spec.md` と矛盾してはいけない。

- CloudFormationテンプレート
- ハンズオンREADME
- スライド
- 台本
- 音声
- 動画手順
- QAレポート

## 標準成果物

- 講座仕様書
- CloudFormationテンプレート
- ハンズオンREADME
- 検証スクリプト
- スライドPNG
- 台本
- VOICEVOX音声素材
- VOICEVOXナレーション品質チェック結果
- 動画ファイル
- QAレポート
- Google Driveアップロード記録

## 成功条件

- GitHub Issueだけで作業状態が追跡できる
- WorkerとReviewerが分離されている
- README通りにハンズオンを再現できる
- 変更が承認フローを通っている
- 公開前に品質ゲートを満たしている
