# AWS CloudWatch/SRE監視実践マスター

このディレクトリは、短尺講座とバンドルを将来の長尺旗艦コースへ発展させるためのコース設計です。

## Course ID

`aws-cloudwatch-sre-monitoring-master-course`

## Course Title

AWS CloudWatch/SRE監視実践マスター：Logs Insights・Alarm・SLO・運用改善

## Positioning

この講座は、既存の短尺講座をそのまま連結したものではありません。

短尺講座では1テーマ1成果物を扱い、長尺版では以下を追加して統合コースとして成立させます。

- 章末演習
- 統合CloudFormationハンズオン
- 障害調査シナリオ
- アラート設計レビュー
- Runbook初動対応シミュレーション
- SLOレビュー会議シナリオ
- 課金、安全、権限、rollbackの横断チェック

## Source Files

- `course_spec.md`: コース設計のSource of Truth
- `course_curriculum.md`: Udemyカリキュラム入力表
- `course_infomation.md`: Udemy登録画面へ入力する販売ページ情報
- `handson/README.md`: 統合ハンズオン設計
- `cloudformation/README.md`: 教材用CloudFormation方針
- `slides/README.md`: GPT-Image2スライド制作方針
- `scripts/README.md`: 台本制作方針
- `audio/README.md`: VOICEVOX音声制作方針
- `video/README.md`: 動画制作方針
- `qa/README.md`: QA方針

## Production Rule

- 完成動画に使うスライドはGPT-Image2由来PNGのみ
- ナレーションはVOICEVOXを前提にする
- CloudFormationは教材ハンズオンの再現性のために使う
- 実運用IaCはCDKまたはTerraform推奨として説明する
- AWSリソース作成、更新、削除を伴う検証はCEO承認後にのみ実行する
- WorkerとReviewerは必ず分離する
