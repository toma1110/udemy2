# Course Information

## Course Title

AWS CloudWatch Logs Insights実践: 障害調査クエリ集

## Subtitle

エラー検索、集計、parse、requestId追跡、JOIN/subqueryまで、CloudWatch Logs Insightsの実務クエリを学びます。

## Description

CloudWatch Logs Insightsは、AWS運用で障害調査を始めるための強力なログ検索ツールです。

この講座では、CloudWatch Logs Insightsを機能紹介ではなく、障害調査クエリ集として学びます。直近ログを見る、エラーを探す、時間帯ごとに集計する、遅い処理を探す、requestIdで一連の出来事を追う、という実務の型を順番に整理します。

標準ハンズオンではAWSリソース作成を必須にしません。サンプルログとクエリ読解だけでも進められます。既存ロググループを持つ受講者は、短い時間範囲で任意実行できます。

2026年版の発展機能として、pattern、anomaly、JOIN、subquery、SOURCE、タグ指定クエリの入口も扱います。

## Learning Goals

- Logs Insightsの基本構文を読める
- クエリ実行時のスキャン量と料金注意を説明できる
- エラー、例外、タイムアウト、5xxを探すクエリを使い分けられる
- `stats` と `bin()` でログの傾向を集計できる
- `parse` とrequestIdで調査対象を追跡できる
- 2026年時点のJOIN、subquery、SOURCEの位置づけを説明できる

## Target Students

- CloudWatch Logs Insightsを使い始めたいAWS初学者
- 障害時にログ検索の型を持ちたい開発者、運用担当者
- Lambda/API Gateway/アプリケーションログの調査を始めたい人
- CloudWatch入門の次に、実践的なログ調査へ進みたい人

## Requirements

- AWSの基本用語
- ログ、エラー、リクエストIDの基礎
- AWSアカウントは任意
- 既存ロググループがある場合だけ、短時間の任意実行が可能

## AI/Voice Disclosure

本講座のスライドはGPT-Image2で生成し、ナレーション素材はVOICEVOXを使用します。
