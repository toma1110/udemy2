# AWS CloudWatch入門: Metrics・Logs Insights・Alarm・Dashboardで学ぶ監視の基本

## Course Title

AWS CloudWatch入門: Metrics・Logs Insights・Alarm・Dashboardで学ぶ監視の基本

## Course ID

`aws-cloudwatch-intro-course`

## Source Candidate

- Market research ID: `VID-001`
- Original candidate title: `AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図`
- Course direction: 1本の短尺動画候補を、CloudWatch初学者向けの複数レクチャー講座へ拡張する
- Market basis: `C-03`, `K-01`, `P-05`
- Differentiation source: 日本語、図解、短尺レクチャー、Logs Insights需要、初学者向け

## Course Positioning

本コースは、CloudWatchの用語と画面を「運用監視の地図」として理解するための入門コースです。

1本目の動画品質を基準に、同じトーンで以下まで広げます。

- Metricsの基本
- Logsの基本
- Logs Insightsのクエリ入門
- Logs Insightsを使った障害調査の型
- Alarm、Dashboard、調査フローのつなぎ方

本コースはCloudWatch実践ハンズオン講座の前段です。リソース作成は必須にせず、既存のCloudWatch画面やREADMEのワークシートだけで学習を完了できる構成にします。

## Target Audience

- AWSを学び始めたが、CloudWatchの用語が点で散らばって見える人
- Metrics、Logs、Logs Insights、Alarm、Dashboardの違いを説明できず、監視学習で止まっている人
- エラー調査でCloudWatch Logs Insightsを使いたいが、最初のクエリの型が分からない人
- SREや運用監視に進む前に、CloudWatchの全体像を短時間でつかみたい人
- 実務でダッシュボードやアラームを見ているが、裏側のつながりを整理したい人

## Prerequisites

- AWSマネジメントコンソールの基本的な画面遷移を見たことがある
- サーバー、ログ、メトリクス、通知という言葉を聞いたことがある
- AWSアカウントはあると望ましいが、本コースの中心部分はリソース作成なしで学習できる
- AWS CLI、CloudFormation、CDK、Terraformの事前準備は不要

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- CloudWatchがAWSリソースとアプリケーションを監視するためのサービスであると説明できる
- Metrics、Logs、Logs Insights、Alarm、Dashboardの役割を分けて説明できる
- namespace、metric、dimension、statistic、periodの基本関係を説明できる
- log group、log stream、ログイベントの関係を説明できる
- Logs Insightsで`fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める
- Logs Insightsのクエリでは、ロググループと時間範囲を絞る理由を説明できる
- Alarmが「メトリクス」「条件」「状態」「アクション」で構成されることを説明できる
- Dashboardはデータ保存場所ではなく、メトリクスやアラームを見るための表示面だと説明できる
- 障害調査時に、Dashboard、Alarm、Metrics、Logs Insightsのどこから見始めるかを判断できる
- ハンズオン用CloudFormationと実運用IaCの位置づけを混同せず説明できる

## Course Promise

受講後、CloudWatchの主要部品を地図として理解し、Logs Insightsでログを読み始め、AlarmやDashboardを使った監視の基本設計へ進むための土台を作れる状態になります。

## Differentiation

- 初学者が混乱しやすい「メトリクス」「ログ」「ログインサイト」「アラーム」「ダッシュボード」を地図で整理する
- Logs Insightsを単なる機能紹介ではなく、障害調査で使うクエリの型として扱う
- AWS公式ドキュメントの用語に寄せつつ、実務での見方に翻訳する
- リソース作成を必須にせず、特別な準備なしで学べる短尺レクチャー群にする
- 後続のSRE、SLO、CloudWatch実践、Terraform監視講座へ自然につながる導入講座にする
- VOICEVOXで読み上げやすい日本語にし、英字略語はナレーション内で読み表記へ寄せる

## Chapter Structure

本コースは6レクチャー構成とする。

| Section | Section Title | Section Learning Goal | Lecture | Lecture Title | Lecture Learning Goal |
| --- | --- | --- | --- | --- | --- |
| 1 | CloudWatchの地図 | CloudWatchの部品を役割ごとに分けて説明できる | `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる |
| 1 | CloudWatchの地図 | CloudWatchの部品を役割ごとに分けて説明できる | `s1-l2` | Metricsの基本 | namespace、metric、dimension、statistic、periodを使ってメトリクスを探す考え方を説明できる |
| 1 | CloudWatchの地図 | CloudWatchの部品を役割ごとに分けて説明できる | `s1-l3` | Logsの基本 | log group、log stream、ログイベントを区別し、メトリクスとの違いを説明できる |
| 2 | Logs Insightsでログを読む | Logs Insightsの基本クエリを読み、調査の入口を作れる | `s2-l1` | Logs Insights入門 | `fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める |
| 2 | Logs Insightsでログを読む | Logs Insightsの基本クエリを読み、調査の入口を作れる | `s2-l2` | Logs Insightsで障害調査 | 最近のエラー、エラー件数、遅延、リクエスト単位の追跡という調査の型を説明できる |
| 3 | Alarm/Dashboardと調査フロー | 監視情報を見て、次に深掘りする場所を判断できる | `s3-l1` | Alarm/Dashboardと次の一歩 | Alarm、Dashboard、Metrics、Logs Insightsを使った障害時の見始め方を説明できる |

## Hands-on Scope

本コースのハンズオン範囲は「リソース作成なしでCloudWatchの見方を確認する」ことです。

- AWSリソース作成は必須にしない
- AWSアカウントがある場合はCloudWatchコンソールで画面を確認する
- 既存ロググループがある場合だけ、Logs Insightsで短い時間範囲のサンプルクエリを試す
- 既存リソースがない場合でも、READMEの表とサンプルクエリの読解だけで完了できる
- ダッシュボード、アラーム、ロググループ、メトリクスを新規作成しない
- サンプルクエリは既存ログに対して読む・試す用途に限定し、ログ投入やアプリ作成はしない

## Hands-on Resources

| Resource Title | Path | Purpose |
| --- | --- | --- |
| CloudWatch地図ワークシート | `handson/README.md` | Metrics、Logs、Alarm、Dashboardの役割を整理する |
| Metrics確認メモ | `handson/README.md#metrics確認メモ` | namespace、metric、dimensionを既存画面で確認する |
| Logs Insightsクエリ読解 | `handson/README.md#logs-insightsクエリ読解` | 基本クエリをリソース作成なしで読めるようにする |
| 障害調査の見始め方チェック | `handson/README.md#障害調査の見始め方チェック` | Dashboard、Alarm、Metrics、Logs Insightsの順番を整理する |

## CloudFormation Scope

本コースではCloudFormationテンプレートを作成しない。

理由:

- 初学者向けの地図とLogs Insights導入コースであり、実リソース作成より概念整理と読解を優先するため
- 「実行に特別な用意がいらない」ハンズオンにするため
- リソース作成を伴うCloudWatch実践動画は後続コースへ分離するため

位置づけ:

- CloudFormationは、講座内ハンズオンで受講者が追加ツールなしにREADME通り再現するための選択肢
- 実運用のIaCでは、チーム開発、抽象化、保守性を考慮してCDKまたはTerraformを使う前提
- Terraform講座ではTerraformを教材対象として扱う

## Cost Warning

本コースの中心ハンズオンではAWSリソースを作成しない。

ただし、受講者が任意でCloudWatch画面やLogs Insightsを操作した場合は、以下に料金が発生する可能性がある。

- ログ取り込み、ログ保存、ログ検索
- Logs Insightsクエリでスキャンしたログデータ
- カスタムメトリクス
- アラーム
- ダッシュボード
- 通知連携

Logs Insightsを試す場合は、公式ドキュメントの推奨に合わせて、対象ロググループを必要最小限にし、時間範囲を短くし、不要なクエリをキャンセルする。ダッシュボードにLogs Insights結果を追加すると、更新のたびにクエリが実行される可能性があるため、本コースでは行わない。

## Udemy成立尺是正方針

2026-05-17の既存コース動画監査では、通常レクチャーMP4は6本存在するが、合計尺は約12.3分でUdemy標準コースの30分要件に届いていない。

是正後の制作方針:

- レクチャー数は現行の6本を維持する
- 各レクチャーをおおむね5〜6分に再設計し、講義本編の計画尺を30〜36分にする
- CloudWatchの地図、Metrics、Logs、Logs Insights、Alarm、Dashboardの説明に、具体的な見る順番と初学者のつまずき例を追加する
- プロモーション動画は30分要件に含めない
- 動画再生成前に、CEOが更新後の `course_spec.md` と `course_infomation.md` を確認・承認する
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で再生成してよい

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- 1レクチャー1メッセージ群で、1スライド1メッセージを守る
- WorkerとReviewerを分離する

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: CloudWatchの全体像を短時間で整理したい初学者に、Metrics、Logs、Logs Insights、Alarm、Dashboardを地図として学べる講座だと伝える
- 主な訴求: AWSリソース作成なしでも学べる、Logs Insightsの入口まで扱う、後続のCloudWatch実践/SRE講座へ進む土台になる
- 必須素材: `scripts/promo_video_script.md`、GPT-Image2 source PNG、GPT-Image2由来最終PNG、VOICEVOX音声、MP4、Drive upload report
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャー `s1-l1` をプロモーション動画の代用にしない

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である
- 動画再生成前にCEOが `course_spec.md` と `course_infomation.md` を確認・承認している
- AWS公式ドキュメントに基づく用語確認レポートが存在する
- `README.md` と `handson/README.md` が存在し、リソース作成なしで再現できる
- 全レクチャーの `scripts/*_script.md` と `scripts/*_script.json` が存在する
- ナレーション本文がVOICEVOX向けにチェック済みである
- 全レクチャーのGPT-Image2プロンプトが存在する
- GPT-Image2 source PNG、最終PNG、contact sheetが各レクチャーに存在する
- VOICEVOX音声、MP4、QAレポートが各レクチャーに存在する
- プロモーション動画の台本、GPT-Image2素材、VOICEVOX音声、MP4、Drive URL、QAレポートが存在する
- `*_slide_generation_report.md` で `Final PNGs are GPT-Image2-derived: PASS` になっている
- WorkerとReviewerが別AIである

## Out of Scope

- CloudWatch Alarm、SNS、Dashboardの新規作成ハンズオン
- 新規ロググループやサンプルアプリの作成
- CloudWatch Agent、OpenTelemetry、Application Signalsの導入
- SLO、エラーバジェット、バーンレート設計
- 本番監視基盤の設計代行
- マルチアカウント、マルチリージョンの運用設計
- CDKまたはTerraformによる本番IaC実装
- Logs Insightsの高度な`pattern`、`diff`、`anomaly`、`join`、`subqueries`の実践

## Voice and Terminology Rules

ナレーションでは以下の読みを優先する。

| 表記 | ナレーション |
| --- | --- |
| AWS | エーダブリューエス |
| CloudWatch | クラウドウォッチ |
| Metrics | メトリクス |
| Logs | ログ |
| Logs Insights | ログインサイト |
| Alarm | アラーム |
| Dashboard | ダッシュボード |
| Namespace | ネームスペース |
| Dimension | ディメンション |
| Statistic | スタティスティック |
| Period | ピリオド |
| Lambda | ラムダ |
| API Gateway | エーピーアイゲートウェイ |
| CloudFormation | クラウドフォーメーション |
| CDK | シーディーケー |
| Terraform | テラフォーム |
| IaC | アイエーシー |
| CLI | シーエルアイ |

台本生成後は必ず以下を実行する。

```bash
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts
```

## References

- Amazon CloudWatch User Guide: What is Amazon CloudWatch?
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- Amazon CloudWatch User Guide: Amazon CloudWatch concepts
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
- Amazon CloudWatch Logs User Guide: CloudWatch Logs Insights query syntax
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
- Amazon CloudWatch Logs User Guide: Sample queries
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html
