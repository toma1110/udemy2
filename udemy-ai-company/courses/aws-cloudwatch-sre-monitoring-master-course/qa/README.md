# QA

このディレクトリは、長尺旗艦コースの企画、教材、動画、ハンズオンQAレポートを配置する領域です。

## Review Roles

- Worker: AI-Production-01 または AI-Engineer-01
- Reviewer: AI-QA-01
- WorkerとReviewerは同一AIにしない

## Required QA

- `course_spec.md` と制作物の整合性
- `course_curriculum.md` とUdemy入力内容の整合性
- GPT-Image2スライドであること
- VOICEVOX読み上げ品質
- CloudFormation validate、create、update、smoke test、delete
- README通り再現できること
- AWSリソース削除とコスト確認
- 短尺講座との過剰重複がないこと
