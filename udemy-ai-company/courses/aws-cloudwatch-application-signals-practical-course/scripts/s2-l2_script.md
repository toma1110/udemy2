# Section 2 Lecture 2 台本

### Title

サンプルアプリと低頻度トラフィックをデプロイする

## Slide 1

### Slide Title

作成前チェック

### Slide Message

料金と削除手順を確認する

### Narration

作成に入る前に、料金が発生する可能性と、削除手順を確認します。ラムダ、ログ、スケジューラー、アプリケーションシグナルズは、学習用でも放置しない前提で進めます。 作成前チェックでは、料金、リージョン、削除手順、停止手順を確認します。特に学習環境は、作れたことよりも、終わったあとに戻せることが重要です。手元のアカウントで権限が足りるかも、この段階で確認します。

### Visual Notes

- Pre-create checklist
- Cost and cleanup warning

## Slide 2

### Slide Title

validate

### Slide Message

まずテンプレートだけ検証

### Narration

最初に実行するのは、テンプレート検証です。この段階では、スタックを作りません。テンプレートの形式やリソース定義に問題がないかを、先に確認します。 バリデートは、クラウドフォーメーションの構文確認です。ここではスタックを作らないため、料金影響はありません。まずテンプレートとして読めるかを確認し、作成系の操作へ進む前に、パラメーターと出力を見直します。

### Visual Notes

- Validate template step
- No resources created

## Slide 3

### Slide Title

create

### Slide Message

承認後にスタック作成

### Narration

スタック作成は、エーダブリューエス上にリソースを作る操作です。この教材制作では、承認後にだけ実行します。受講者向けにも、作るものと削除手順を確認してから進める流れにします。 作成は、承認後にだけ行います。スタック名、リージョン、シナリオ設定、トラフィック有効化の設定を確認します。作成中に失敗した場合は、エラーイベントを見て原因を調べますが、無理に何度も実行せず、まず状態を整理します。

### Visual Notes

- Approval gate
- Stack creation
- AWS resource boundary

## Slide 4

### Slide Title

traffic

### Slide Message

低頻度通信を待つ

### Narration

作成後、スケジューラーがトラフィック生成用ラムダを呼びます。すぐに画面へ反映されるとは限りません。数分待ってから、サービス一覧やスモークテストで確認します。 通信は、作成直後にすぐ画面へ出るとは限りません。アプリケーションシグナルズでは、サービス発見やメトリクス反映に時間差があります。数分待ち、時間範囲も確認しながら、通信量が増えているかを見ます。

### Visual Notes

- Low-frequency traffic pulse
- Wait for telemetry
- Service discovery delay

## Slide 5

### Slide Title

smoke test

### Slide Message

作成結果を確認する

### Narration

スモークテストでは、スタック、ラムダ、ロググループ、スケジュール、環境変数を確認します。アプリケーションシグナルズのサービス表示は、反映まで時間がかかることもあります。 スモークテストでは、必要なリソースができているか、通信を止められるか、出力から確認できるかを見ます。これは本番品質の負荷試験ではなく、教材として次の画面確認に進めるかを見る軽い確認です。

### Visual Notes

- Smoke test checklist
- Lambda, logs, schedule, Application Signals

## Slide 6

### Slide Title

次に見るもの

### Slide Message

Services画面へ進む

### Narration

作成が終わったら、次はサービス一覧へ進みます。ここで、サンプルアプリがサービスとして見えるか、通信量が増えているかを確認します。 次に見るのはサービス一覧です。スタック作成の成功だけでは、アプリケーションシグナルズの学習は完了しません。通信が届き、サービスが見え、指標が変わるところまで確認して初めて、画面の読み方へ進めます。

### Visual Notes

- Move from deployment to Services view
- Course flow arrow
