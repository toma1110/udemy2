# s2-l5 image assets

- `slide_005_cloudformation.png`: STEP 1 CloudFormationでの一括構築
- `slide_006_flask_deploy.png`: STEP 2 FlaskアプリのEC2デプロイ
- `slide_007_cwagent_metrics.png`: STEP 3 CloudWatch Agentとメトリクス収集
- `slide_008_cloudwatch_logs.png`: STEP 4 CloudWatch Logsへのログ転送
- `slide_009_xray_trace.png`: STEP 5 X-Rayトレース可視化
- `slide_010_alb_s3_logs.png`: STEP 6 ALBアクセスログのS3保存
- `slide_011_verification.png`: 動作確認チェックリスト
- `slide_012_shutdown.png`: 作業後の停止とコスト注意
- `slide_013_aws_architecture_raw.png`: AWS MCPサーバーで作成したdraw.io構成図のスクリーンショット
- `slide_013_aws_architecture.png`: まとめページ用に構成図と「今回作ったもの」を合成した画像

`generate_assets.py` を再実行すると、STEP 1〜6 と確認・停止の画像を再生成できます。
まとめページ用画像は `docs/s2-l5-aws-architecture.drawio` から取得した構成図を利用しています。
