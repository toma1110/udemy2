# Udemy Market Research

このディレクトリは、Udemyで売れる可能性が高いAWS/SRE関連動画テーマを調査し、次に制作する講座候補へ落とし込むための作業領域です。

## 目的

- Udemy上の需要、競合、受講者の悩みを調査する
- 50本以上の動画テーマ候補を作る
- 各候補を根拠付きでスコアリングする
- CEOが次に制作する講座を判断できる資料を作る

## 前提

- 「売れる」は保証ではなく、市場シグナルに基づく仮説として扱う
- AWS/SRE領域を中心にする
- 既存講座の `course_spec.md` は変更しない
- 新講座化する場合は、CEO承認後に別途 `course_spec.md` を作成する
- 外部有料ツールや課金APIは使わない
- AWSリソース作成やCloudFormation実行は行わない
- GitHub IssueはPM運用上、CEOの実行開始承認待ちとして `approval-required` / `blocked` で管理する

## 市場シグナル

- Udemy上の検索結果、ベストセラー表示、レビュー数、評価、更新日
- 競合講座の章立て、プロモーション訴求、対象者
- 低評価レビュー、Q&A、学習者が詰まりやすい論点
- AWS/SRE実務で需要があるテーマ
- 初学者がREADME通りに再現できるハンズオン化のしやすさ

## チケット

| Task ID | GitHub Issue | 内容 |
| --- | --- | --- |
| TASK-0121 | https://github.com/toma1110/udemy2/issues/128 | 調査設計と評価軸 |
| TASK-0122 | https://github.com/toma1110/udemy2/issues/129 | Udemy競合講座調査 |
| TASK-0123 | https://github.com/toma1110/udemy2/issues/130 | キーワード需要調査 |
| TASK-0124 | https://github.com/toma1110/udemy2/issues/131 | レビュー/Q&A痛点調査 |
| TASK-0125 | https://github.com/toma1110/udemy2/issues/132 | 50本以上の動画候補リスト |
| TASK-0126 | https://github.com/toma1110/udemy2/issues/133 | スコアリングと上位10本選定 |
| TASK-0127 | https://github.com/toma1110/udemy2/issues/134 | CEO判断パック |
| TASK-0128 | https://github.com/toma1110/udemy2/issues/135 | 市場調査QA |
