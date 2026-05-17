# AWS CloudWatch Logs Insights実践: 障害調査クエリ集

## Course Title

AWS CloudWatch Logs Insights実践: 障害調査クエリ集

## Course ID

`aws-cloudwatch-logs-insights-practical-course`

## Source Candidate

- Market research ID: `VID-004`
- Original candidate title: `Logs Insightsでエラーを探す10個のクエリ`
- Market basis: `K-04`, `P-05`, `P-06`, `P-14`
- Strategic source: VID-001 Section 2で扱ったLogs Insightsを、独立した実践コースへ拡張する
- Priority: high

## Course Positioning

本コースは、CloudWatch Logs Insightsを使って障害調査の入口を作る実践コースです。

VID-001ではCloudWatch全体像の一部としてLogs Insightsを紹介しました。本コースでは、ロググループ選択、時間範囲、基本構文、エラー調査、集計、parse、requestId追跡、pattern/anomaly、JOIN/subquery、SOURCEまでを、実務で使うクエリの型として整理します。

AWSリソース作成を必須にせず、サンプルログとクエリ読解だけでも学習できる構成にします。既存ロググループを持つ受講者は、短い時間範囲で任意実行できます。

## Target Audience

- CloudWatch Logs Insightsを開いたことはあるが、何を書けばよいか分からない人
- 障害時にログを探す順番を持っていない開発者、運用担当者
- Lambda、API Gateway、アプリケーションログのエラー調査を始めたい人
- `fields`、`filter`、`stats`、`parse` などの基本構文を、実務クエリで覚えたい人
- 2026年時点のJOIN、subquery、タグ指定クエリなど、新しいLogs Insights機能の入口を知りたい人

## Prerequisites

- AWSマネジメントコンソールの基本的な画面遷移を見たことがある
- ログ、エラー、リクエストID、ステータスコードという言葉を聞いたことがある
- AWSアカウントはあると望ましいが、必須ではない
- 既存ロググループがある場合は、任意で短時間のクエリ実行ができる
- AWS CLI、CloudFormation、CDK、Terraformの事前準備は不要

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- Logs Insightsでロググループと時間範囲を絞る理由を説明できる
- `@timestamp`、`@message`、`@logStream`、`@log` などの自動生成フィールドを説明できる
- `fields`、`filter`、`sort`、`limit` の基本形を読める
- `stats` と `bin()` で時間ごとの件数や傾向を集計できる
- JSONログのフィールドと `parse` を使い分けられる
- エラー、例外、タイムアウト、遅延、リクエストID追跡のクエリを選べる
- `dedup` で同じリクエストの重複を抑える考え方を説明できる
- `pattern` と `anomaly` の使いどころを説明できる
- `JOIN`、subquery、`SOURCE`、タグ指定クエリの位置づけを説明できる
- Logs Insights実行時のコスト注意を説明できる

## Course Promise

受講後、障害調査時に「最近のエラーを見る」「時間帯で集計する」「遅い処理を探す」「リクエストIDで追う」「発展クエリへ広げる」というLogs Insightsの実践パターンを、自分の現場ログへ持ち帰れる状態になります。

## Differentiation

- 操作説明ではなく、障害調査で使うクエリの型に絞る
- AWSリソース作成なしでも、サンプルログとクエリ読解で完了できる
- 既存ロググループがある場合だけ任意実行できるため、初学者の課金不安を抑えられる
- 2026年版としてJOIN、subquery、SOURCEタグ指定、pattern/anomalyにも触れる
- VID-001、VID-002のCloudWatch/Alarm教材から自然につながる
- 実運用IaCはCDKまたはTerraform推奨、CloudFormationは教材ハンズオン用途という方針を維持する

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. クエリの安全運転と基本形
   - `s1-l1` Logs Insights実践の地図
   - `s1-l2` ロググループと時間範囲
   - `s1-l3` 基本構文: fields/filter/sort/limit

2. 障害調査クエリ集
   - `s2-l1` エラーと例外を探す
   - `s2-l2` stats/binで傾向を見る
   - `s2-l3` parseとrequestId追跡

3. 2026年版の発展機能
   - `s3-l1` pattern/anomalyで未知の変化を見る
   - `s3-l2` JOIN/subquery/SOURCEの入口

## Hands-on Scope

- サンプルログを読み、クエリの意図を説明する
- `handson/queries/` のクエリを読む
- 既存ロググループがある場合だけ、短い時間範囲で任意実行する
- AWSリソース作成は標準手順に含めない
- ダッシュボードへのLogs Insightsウィジェット追加は扱わない
- 長時間範囲、複数ロググループ、大量スキャンは避ける
- JOIN/subquery/SOURCEは上級入口として読み方を扱い、実行は任意にする

## Hands-on Resources

| Resource Title | Path | Purpose |
| --- | --- | --- |
| Logs Insights安全運転チェック | `handson/README.md#logs-insights安全運転チェック` | スキャン量と料金を抑える実行前確認 |
| 基本クエリ読解 | `handson/queries/01_recent_events.sql` | 直近ログを見る基本形 |
| 障害調査クエリ集 | `handson/queries/` | エラー、傾向、遅延、requestId追跡の型 |
| サンプルログ読解 | `handson/sample_logs/` | AWSアカウントなしでもクエリの意図を読める教材 |
| 発展機能メモ | `handson/README.md#2026年版の発展機能` | JOIN、subquery、SOURCE、pattern/anomalyの位置づけ |

## CloudFormation Scope

本コースではCloudFormationテンプレートを標準ハンズオンに含めません。

理由:

- Logs Insightsは既存ログを読む機能であり、初学者に不要なリソース作成を求めないため
- クエリ実行料金の主な注意点は、ロググループ選択と時間範囲にあるため
- サンプルログ読解だけでも講座価値を出せるため

位置づけ:

- 教材ハンズオンで再現用リソースを作る場合はCloudFormationを使う
- 実運用のIaCでは、ロググループ、メトリクス、アラーム、ダッシュボードをCDKまたはTerraformで管理する前提
- 社内検証でロググループ作成やログ投入を行う場合はCEO承認後にだけ実行する

## Cost Warning

本コースの標準ハンズオンではAWSリソースを作成しません。

ただし、既存ロググループでLogs Insightsクエリを実行する場合は、スキャンしたログデータ量に応じて料金が発生する可能性があります。以下を必ず守ります。

- 必要なロググループだけを選ぶ
- 時間範囲を直近5分から15分など短くする
- 不要な実行中クエリはキャンセルする
- まず `limit` を付けて小さく見る
- ダッシュボードにLogs Insights結果を追加しない
- JOIN/subquery/SOURCEなどスキャン範囲が広がりやすいクエリは、読解中心または最小範囲で扱う

## Udemy成立尺是正方針

2026-05-17の既存コース動画監査では、通常レクチャーMP4は8本存在するが、合計尺は約11.7分でUdemy標準コースの30分要件に届いていない。

是正後の制作方針:

- レクチャー数は現行の8本を維持する
- 各レクチャーをおおむね4〜5分に再設計し、講義本編の計画尺を32〜40分にする
- 既存の短すぎる台本を、クエリの読み方、実務判断、料金注意、失敗例、復習を含む構成へ拡張する
- プロモーション動画は30分要件に含めない
- 動画再生成前に、CEOが更新後の `course_spec.md` と `course_infomation.md` を確認・承認する
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で再生成してよい

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- 1スライド1メッセージにする
- WorkerとReviewerを分離する

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: Logs Insightsで障害調査クエリの型を持ちたい受講者へ、実践コースの価値を短く伝える
- 主な訴求: AWSリソース作成なしでもサンプルログとクエリ読解で学べる、エラー調査、集計、parse、requestId追跡、2026年版の発展機能まで入口を扱う
- 必須素材: `scripts/promo_video_script.md`、GPT-Image2 source PNG、GPT-Image2由来最終PNG、VOICEVOX音声、MP4、Drive upload report
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャー `s1-l1` をプロモーション動画の代用にしない

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である
- 動画再生成前にCEOが `course_spec.md` と `course_infomation.md` を確認・承認している
- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- `course_curriculum.md` にセクションタイトル、セクション学習目標、ハンズオンリソースタイトルがある
- `README.md` と `handson/README.md` が存在し、標準手順ではAWSリソース作成なしで再現できる
- `handson/queries/` に実践クエリが存在する
- 全レクチャーの `scripts/*_script.md` と `scripts/*_script.json` が存在する
- 全レクチャーのGPT-Image2プロンプトが存在する
- GPT-Image2 source PNG、最終PNG、contact sheetが各レクチャーに存在する
- VOICEVOX音声、MP4、QAレポート、Drive URLが各レクチャーに存在する
- プロモーション動画の台本、GPT-Image2素材、VOICEVOX音声、MP4、Drive URL、QAレポートが存在する
- WorkerとReviewerが別AIである

## Out of Scope

- CloudWatch Logsへのサンプルログ投入を必須化する
- 新規Lambda、API Gateway、ECSなどのアプリケーション作成
- CloudWatch Agent、ADOT、X-Ray、Application Signalsの導入
- ダッシュボード作成ハンズオン
- Alarm/SNS通知作成ハンズオン
- 本番ログ設計、ログ保持ポリシー、マルチアカウント集約の設計代行
- Athena、OpenSearch、DatadogなどCloudWatch Logs Insights以外のログ分析基盤

## Voice and Terminology Rules

ナレーションでは以下の読みを優先する。

| 表記 | ナレーション |
| --- | --- |
| AWS | エーダブリューエス |
| CloudWatch | クラウドウォッチ |
| Logs Insights | ログインサイト |
| fields | フィールズ |
| filter | フィルター |
| sort | ソート |
| limit | リミット |
| stats | スタッツ |
| bin | ビン |
| parse | パース |
| dedup | ディーダップ |
| pattern | パターン |
| anomaly | アノマリー |
| JOIN | ジョイン |
| subquery | サブクエリ |
| SOURCE | ソース |
| Lambda | ラムダ |
| API Gateway | エーピーアイゲートウェイ |
| CloudFormation | クラウドフォーメーション |
| CDK | シーディーケー |
| Terraform | テラフォーム |
| CLI | シーエルアイ |

## References

- Amazon CloudWatch Logs User Guide: CloudWatch Logs Insights query syntax
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
- Amazon CloudWatch Logs User Guide: Sample queries
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html
- Amazon CloudWatch Logs User Guide: Supported logs and discovered fields
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html
- Amazon CloudWatch Logs User Guide: SOURCE
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html
- Amazon CloudWatch Logs User Guide: join
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Join.html
- Amazon CloudWatch Logs User Guide: subqueries
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Subqueries.html
