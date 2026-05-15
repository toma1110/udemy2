# Section 3 Lecture 1 台本

## Title

Alarm/Dashboardと次の一歩

## Source

- `course_spec.md`
- `handson/README.md`
- Amazon CloudWatch concepts

## Slide 1

### Slide Title

Alarm/Dashboardと次の一歩

### Slide Message

監視は、気づく、見る、掘る、動くの流れ

### Narration

このレクチャーでは、アラーム、ダッシュボード、メトリクス、ログインサイトを調査の流れとしてつなげます。監視は、異常に気づき、全体を見て、原因を掘り、次の行動へつなげる活動です。

### Visual Notes

- 監視フロー全体
- 気づく、見る、掘る、動く

## Slide 2

### Slide Title

Alarmは状態を持つ

### Slide Message

正常、警告、データ不足を切り替えて判断する

### Narration

アラームは、条件をもとに状態を持ちます。正常、警告、データ不足のように、メトリクスのあたいと評価条件によって状態が変わります。通知は、この状態変化に反応して動くものとして考えると整理しやすくなります。

### Visual Notes

- OK、ALARM、INSUFFICIENT_DATAの状態
- 状態変化と通知

## Slide 3

### Slide Title

条件は行動に合わせる

### Slide Message

鳴ったあと、誰が何をするかまで考える

### Narration

アラームの条件は、ただ厳しくすればよいわけではありません。鳴ったあと、誰が何を見るのか、何分以内に対応するのか、通知先はどこかまで考えます。行動につながらないアラームは、運用を疲れさせます。

### Visual Notes

- 条件から担当者と行動へ
- 通知疲れを避ける表現

## Slide 4

### Slide Title

Dashboardは表示面

### Slide Message

必要な情報を、1画面で見始める

### Narration

ダッシュボードは、監視情報の表示面です。大事なのは、全部を詰め込むことではありません。最初に見るべきメトリクス、アラーム状態、ログへの入口を、1画面で判断しやすく並べることです。

### Visual Notes

- 1画面のダッシュボード
- グラフ、状態、ログ入口

## Slide 5

### Slide Title

障害時の見始め方

### Slide Message

Dashboard、Alarm、Metrics、Logs Insights

### Narration

障害時に迷ったら、見る順番を決めます。まずダッシュボードで全体を見ます。次にアラームで、どの条件が問題かを確認します。メトリクスで数字の変化を見て、ログインサイトで同じ時間帯の出来事を探します。

### Visual Notes

- 4ステップの調査ルート
- 同じ時間帯で深掘りする表現

## Slide 6

### Slide Title

講座ハンズオンと実運用

### Slide Message

学習はCloudFormation、実運用はCDKまたはTerraform

### Narration

このコースでは、リソース作成なしで見方を学びました。後続の教材ハンズオンで作る場合は、受講者が追加ツールなしで再現しやすいように、クラウドフォーメーションを使うことがあります。一方で、実運用のアイエーシーでは、シーディーケーかテラフォームを前提にします。

### Visual Notes

- 学習用と実運用の比較
- CloudFormation、CDK、Terraformの位置づけ

## Slide 7

### Slide Title

次に学ぶこと

### Slide Message

Alarm設計、Logs Insights実践、SLOへ進む

### Narration

次に学ぶなら、アラーム設計とログインサイト実践へ進みます。地図を持ち、見る場所を判断できる状態を作ります。

### Visual Notes

- 学習ロードマップ
- Alarm、Logs Insights、SLO

## Slide 8

### Slide Title

まとめ

### Slide Message

CloudWatchは、監視の流れで理解する

### Narration

まとめです。監視は流れで理解します。ダッシュボードで見始め、アラームで入口をつかみます。メトリクスで数字を見て、ログで出来事を掘ります。

### Visual Notes

- コース全体の再掲
- 監視フローの完成図

## QA Notes

- CloudFormationは教材ハンズオン用途として説明
- 実運用IaCはCDK/Terraform
- 後続コースへの接続
