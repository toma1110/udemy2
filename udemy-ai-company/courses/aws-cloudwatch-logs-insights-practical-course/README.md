# AWS CloudWatch Logs Insights実践: 障害調査クエリ集

この講座は、CloudWatch Logs Insightsで障害調査に使うクエリの型を学ぶための制作領域です。

## Source of Truth

- `course_spec.md`
- `course_curriculum.md`

## Course ID

`aws-cloudwatch-logs-insights-practical-course`

## 制作方針

- Logs Insightsを「障害時に原因へ近づくためのクエリ集」として扱う
- AWSリソース作成は必須にしない
- 既存ロググループがある受講者だけ、短い時間範囲で任意実行する
- サンプルログとクエリ読解だけでも完了できる
- クエリ料金を抑えるため、ロググループ、時間範囲、不要クエリキャンセルを必ず説明する
- `JOIN`、subquery、`SOURCE`、タグ指定クエリなど2026年時点の新しい要素は、上級入口として扱う
- 完成動画のスライドと表示文字はGPT-Image2で生成する
- 音声はVOICEVOXを使う

## 講座構成

| Section | Title | Goal |
| --- | --- | --- |
| 1 | クエリの安全運転と基本形 | スキャン量を抑えながら、基本クエリを読める |
| 2 | 障害調査クエリ集 | エラー、傾向、遅延、リクエストID追跡の型を使える |
| 3 | 2026年版の発展機能 | pattern、anomaly、JOIN、subquery、SOURCEの使いどころを説明できる |

## ハンズオン

- `handson/README.md`: 実行手順とクエリ読解
- `handson/queries/`: クエリ集
- `handson/sample_logs/`: 読解用サンプルログ

## ディレクトリ

- `scripts/`: 台本
- `slides/`: GPT-Image2プロンプトとスライド
- `audio/`: VOICEVOX音声
- `video/`: MP4生成レポート
- `qa/`: AWS仕様確認、制作QA、Driveアップロード記録
- `tickets/`: ローカルTask Issue写し

## AWS実行ゲート

この講座の標準ハンズオンではAWSリソースを作成しません。

既存ロググループに対してLogs Insightsを実行する場合は、ログ検索のスキャン量に応じて料金が発生する可能性があります。社内検証で新規ロググループ作成やログ投入を行う場合は、CEO承認後にだけ実行します。
