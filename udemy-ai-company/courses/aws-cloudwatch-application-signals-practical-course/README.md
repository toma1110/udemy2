# AWS CloudWatch Application Signals実践

このディレクトリは、Application Signalsを主役にした新規Udemy講座の制作管理用です。

## Source of Truth

- [course_spec.md](course_spec.md)

## 講座の位置づけ

CloudWatch入門、SLO導入講座の次に進む「実アプリ観測編」です。

サンプルアプリをCloudFormationでデプロイし、低頻度の通信を発生させながら、Application SignalsのServices、Application Map、Service detail、SLOを確認します。

## 重要な方針

- Application Signalsを主役にする
- 自動トラフィックは低頻度、停止可能、削除必須にする
- 料金注意を講座冒頭、README、ハンズオン内で繰り返し明記する
- SLO Recommendationsなど30日データが必要な機能は短時間ハンズオンの完了条件にしない
- 教材ハンズオンはCloudFormation、実運用IaCはCDKまたはTerraform推奨と分ける
- 完成動画スライドはGPT-Image2由来PNGのみ使用する
- 音声はVOICEVOXを使用する

## 作成予定ファイル

- `cloudformation/template.yaml`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `cloudformation/stop_traffic.sh`
- `handson/README.md`
- `scripts/*_script.md`
- `slides/*_gpt_image2_prompts.md`
- `qa/*_report.md`

## 現在のステータス

- Course spec: 作成済み
- Course information: 作成済み
- Curriculum: 作成済み
- Handson design: 初版作成済み
- Public repo working copy: `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/` に作成済み
- CloudFormation implementation: `template.yaml`、`validate.sh`、`smoke_test.sh`、`stop_traffic.sh` 作成済み。`validate-template` 成功。create/update/deleteはCEO承認待ち
- Source verification: 初版作成済み
- Promo video script: 台本、JSON、GPT-Image2プロンプト作成済み
- Lecture scripts: `s1-l1` から `s4-l3` まで全11本の台本、JSON、GPT-Image2プロンプト作成済み
- Video production: GPT-Image2画像生成、VOICEVOX音声生成、MP4作成は未着手
