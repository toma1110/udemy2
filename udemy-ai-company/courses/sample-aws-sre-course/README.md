# sample-aws-sre-course

このサンプル講座は、AWS SRE入門向けにCloudFormationで低コストな監視基盤を作るハンズオンです。

## Source of Truth

この講座では [course_spec.md](course_spec.md) を唯一の真実として扱います。

## 構成

- `cloudformation/`: CloudFormationテンプレートと検証スクリプト
- `slides/`: GPT-Image2で生成するスライドPNG
- `scripts/`: 台本
- `audio/`: VOICEVOX音声素材
- `video/`: 動画素材と完成動画
- `qa/`: QAレポート

## 標準作業順

1. `course_spec.md` を確認する
2. `cloudformation/README.md` に沿ってハンズオンを検証する
3. AI-QA-01が技術レビューする
4. AI-Production-01が教材素材を作る
5. AI-QA-01が教材レビューする
6. CEOが公開判断する
