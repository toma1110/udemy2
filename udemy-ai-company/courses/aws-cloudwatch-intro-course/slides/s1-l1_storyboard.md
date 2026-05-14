# S1-L1 Slide Storyboard

## Target

- Course: `aws-cloudwatch-intro-course`
- Lecture: `s1-l1`
- Script: `../scripts/s1-l1_script.md`
- Output: `slides/s1-l1/slide_001.png` to `slide_010.png`

## Global Visual Direction

- Format: 1920 x 1080 PNG
- Style: AWS/SRE教材向けの読みやすい図解スライド
- Background: white and pale blue-gray
- Main colors: navy, blue, green, teal, orange, red
- Avoid: decorative gradients, small unreadable text, crowded UI mockups
- Rule: 1 slide, 1 message

## Slide Plan

| Slide | Title | Visual |
| ---: | --- | --- |
| 1 | CloudWatchの地図 | 4つの主要部品を地図として配置 |
| 2 | Metrics: 数値の時系列 | 折れ線グラフとnamespace/metric/dimensionのラベル |
| 3 | Logs: 出来事の記録 | タイムスタンプ付きログ行とロググループ構造 |
| 4 | Alarm: 条件と状態 | メトリクスがしきいちを越えて状態が変わる図 |
| 5 | Dashboard: まとめて見る画面 | 3つのウィジェットを持つダッシュボード |
| 6 | 4つのつながり | 表示、判断、数字、出来事の調査フロー |
| 7 | Metricsを探す3つの言葉 | 棚、数値名、ラベルの比喩 |
| 8 | 障害時の見始め方 | Dashboard -> Alarm -> Metrics -> Logs の4ステップ |
| 9 | ハンズオンと実運用IaC | 講座ハンズオンと実運用を左右比較 |
| 10 | まとめ | 4部品の再掲と次に進む学習候補 |

## Text Placement Rules

- タイトルは上部中央
- サブタイトルはタイトル下
- 本文はカード、フロー、ラベルに分ける
- 1カード内の主要テキストは3行以内
- 英字はスライド内の用語表示に限定し、ナレーションでは読み上げ表記を使う

## Review Criteria

- スクリプトの10スライドと数が一致している
- すべてのPNGが1920 x 1080である
- contact sheetで文字切れがない
- CloudFormationを実運用標準と誤解させる表現がない
- Dashboardがデータ保存場所ではなく表示面として表現されている

