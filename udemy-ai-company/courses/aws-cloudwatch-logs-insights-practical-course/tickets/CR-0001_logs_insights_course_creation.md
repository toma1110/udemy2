# Change Request

## Change Summary

CloudWatch Logs Insightsを独立した実践コースとして新規作成する。

## Why Change

VID-001とVID-002でCloudWatch基礎とAlarm/SNS通知を制作済み。次に障害調査で需要が高いLogs Insightsへ進むことで、既存コース群から自然に購入導線を作れるため。

## Scope

- 新規コースディレクトリ作成
- `course_spec.md`、`course_curriculum.md`、`README.md`、`course_infomation.md` 作成
- ハンズオンREADME、サンプルログ、クエリ集作成
- AWS公式ドキュメント確認レポート作成
- 動画制作チケット作成

## Impact

- 既存VID-001のLogs Insights入門を前提にできる
- 新コースは「障害調査クエリ集」としてより実践寄りにする
- AWSリソース作成なしでも学習できる構成にする

## Risks

- Logs Insightsクエリはログ形式によってフィールド名が変わる
- 既存ログでクエリ実行するとスキャン料金が発生する可能性がある
- JOIN/subquery/SOURCEなどの発展機能はスキャン範囲が広がりやすい

## Approval

- CEO request: 「logsinsights良いですね！コース作成お願いします！」
- Course creation approved
- AWSリソース作成やログ投入は別途CEO承認が必要

## Implementation Plan

1. AWS公式ドキュメントでLogs Insights構文と最新機能を確認する
2. 新規コース仕様とカリキュラムを作る
3. リソース作成なしのハンズオンとクエリ集を作る
4. 制作チケットを作る
5. QA、commit、pushを行う
