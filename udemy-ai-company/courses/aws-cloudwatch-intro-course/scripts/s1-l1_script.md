# Section 1 Lecture 1 台本

## Title

CloudWatchの地図

## Source

- `course_spec.md`
- `handson/README.md`
- `qa/cloudwatch_source_verification_report.md`

## Slide 1

### Slide Title

CloudWatchの地図

### Slide Message

監視の部品を、まず4つに分ける

### Narration

こんにちは。このレクチャーでは、クラウドウォッチの全体像を地図として整理します。最初に覚える部品は、メトリクス、ログ、アラーム、ダッシュボードの4つです。細かい機能へ進む前に、それぞれが何を見る場所なのかを分けておきます。

### Visual Notes

- 画面中央にCloudWatchの地図
- Metrics、Logs、Alarm、Dashboardの4ブロック
- 初学者が迷わずたどれる地図の表現

## Slide 2

### Slide Title

Metrics: 数値の時系列

### Slide Message

どれくらいかを、時間ごとの数字で見る

### Narration

メトリクスは、時間ごとに並ぶ数値です。たとえば、利用率、エラー数、待ち時間のように、どれくらいかを数字で見ます。クラウドウォッチでは、サービスごとのまとまりや、対象を示すラベルと一緒に、メトリクスを探します。

### Visual Notes

- 折れ線グラフ
- 横軸は時間、縦軸は数値
- namespace、metric、dimensionを小さなラベルとして配置

## Slide 3

### Slide Title

Logs: 出来事の記録

### Slide Message

何が起きたかを、文章やイベントで追う

### Narration

ログは、何が起きたかを残す記録です。メトリクスが数値を見るものなら、ログは出来事の中身を見るものです。エラーの文章、実行時刻、処理の流れなど、数字だけでは分からない背景を確認するときに使います。

### Visual Notes

- タイムスタンプ付きログ行
- 数値グラフとは別の「出来事リスト」
- log groupとlog streamを棚とファイルのように表現

## Slide 4

### Slide Title

Alarm: 条件と状態

### Slide Message

危ないかどうかを、条件で判断する

### Narration

アラームは、メトリクスを見て、条件を超えたかどうかを判断します。状態は、正常、警告、データ不足のように変わります。さらに、必要に応じて通知や自動処理につなげられます。つまりアラームは、数字を見て行動につなげる入口です。

### Visual Notes

- メトリクスからしきいち線を越えてアラームへ進む流れ
- 状態は正常、警告、データ不足
- 通知アイコンを配置

## Slide 5

### Slide Title

Dashboard: まとめて見る画面

### Slide Message

保存場所ではなく、監視情報の表示面

### Narration

ダッシュボードは、監視情報をまとめて見る画面です。ここで大事なのは、ダッシュボード自体がデータの保存場所ではないことです。メトリクス、アラーム、ログなどの情報を、調査しやすい形で並べる表示面として考えます。

### Visual Notes

- 3つのウィジェットが並ぶ画面
- メトリクスグラフ、アラーム状態、ログの入口
- 「データ源」から「表示面」へ矢印

## Slide 6

### Slide Title

4つのつながり

### Slide Message

数字、出来事、判断、表示を分ける

### Narration

4つの部品は、ばらばらではありません。メトリクスは数字、ログは出来事、アラームは判断、ダッシュボードは表示です。障害調査では、ダッシュボードで全体を見て、アラームで異常の入口を見つけ、メトリクスとログで背景を掘っていきます。

### Visual Notes

- Dashboard -> Alarm -> Metrics -> Logs の調査フロー
- それぞれに「表示」「判断」「数字」「出来事」とラベル
- 迷ったときの見方を矢印で示す

## Slide 7

### Slide Title

Metricsを探す3つの言葉

### Slide Message

namespace、metric、dimensionで対象を絞る

### Narration

メトリクスを探すときは、3つの言葉を押さえると楽になります。ネームスペースは、サービスや用途ごとの棚です。メトリクスは、その棚に入っている数値の名前です。ディメンションは、どの対象の数字なのかを決めるラベルです。

### Visual Notes

- 棚、ファイル、ラベルの比喩
- AWS/EC2のようなnamespace例は画面テキストだけにする
- 初学者向けに専門語を1つずつ対応させる

## Slide 8

### Slide Title

障害時の見始め方

### Slide Message

全体、入口、数字、出来事の順に見る

### Narration

障害時に迷ったら、見る順番を決めます。まずダッシュボードで全体を見ます。次にアラームで、どの条件が問題になっているかを確認します。そのあとメトリクスで数字の変化を見て、最後にログで具体的な出来事を追います。

### Visual Notes

- 4ステップの調査ルート
- Dashboard、Alarm、Metrics、Logsを順番に並べる
- 「まず全体」「次に入口」「数字」「出来事」の短いラベル

## Slide 9

### Slide Title

ハンズオンと実運用IaC

### Slide Message

CloudFormationは教材内、実運用はCDKまたはTerraform

### Narration

この動画では、リソースを作らずに地図を理解します。後続のハンズオンでクラウドウォッチの部品を作る場合は、受講者が追加ツールを用意しなくてよいように、クラウドフォーメーションを使うことがあります。一方で、実運用のアイエーシーでは、シーディーケーかテラフォームを使う前提で考えます。

### Visual Notes

- 左に「講座ハンズオン」、右に「実運用」
- 講座側はCloudFormation、実運用側はCDK/Terraform
- 目的の違いを強調

## Slide 10

### Slide Title

まとめ

### Slide Message

CloudWatchは4つの部品で地図化できる

### Narration

まとめです。クラウドウォッチで最初に迷ったら、4つに分けて考えます。メトリクスは数字、ログは出来事、アラームは判断、ダッシュボードは表示です。この地図を持っておくと、次にアラーム作成、ログ調査、監視ダッシュボード作成へ進みやすくなります。

### Visual Notes

- 4つの部品を再掲
- 次に学ぶ候補としてアラーム、ログ調査、監視ダッシュボードを配置
- 最後に「地図を持って次へ進む」

## QA Notes

- `course_spec.md` のVID-001範囲に限定
- 本動画ではAWSリソースを作成しない
- CloudFormationは講座ハンズオン内の再現性用途として説明
- 実運用IaCはCDKまたはTerraform前提として説明
- ナレーション本文はVOICEVOX向けに英字略語を読み上げ表記へ変換済み

