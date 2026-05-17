# Section 4 Lecture 3 台本

### Title

停止、削除、コスト確認

## Slide 1

### Slide Title

最後は片付け

### Slide Message

学習環境を放置しない

### Narration

ハンズオンの最後は、片付けです。学んだ後に、通信やスタックを放置しないことまで含めて、ひとつの手順として扱います。 最後の片付けは、教材ハンズオンの一部です。作成、確認、停止、削除、料金確認までを一つの流れとして扱います。観測できたから終わりではなく、不要な通信とリソースを残さないことが合格条件です。

### Visual Notes

- Cleanup checklist
- Learning environment boundary

## Slide 2

### Slide Title

stop traffic

### Slide Message

まず通信を止める

### Narration

最初に、自動トラフィックを止めます。スケジューラーを無効化し、追加の呼び出しが続かない状態にします。 まず通信を止めます。スケジュールやパラメーターで自動呼び出しを止めることで、不要なメトリクス、ログ、アプリケーションシグナルズの発生を抑えます。削除前に止める習慣を作ると、検証中の無駄な動きを減らせます。

### Visual Notes

- Stop traffic switch
- Scheduler disabled

## Slide 3

### Slide Title

delete stack

### Slide Message

リソースを削除する

### Narration

次に、クラウドフォーメーションスタックを削除します。ラムダ、スケジュール、ロググループ、エスエルオーなど、テンプレートで管理しているリソースを片付けます。 次にスタックを削除します。削除は作成と同じくらい重要です。削除に失敗した場合は、残ったリソースや権限、依存関係を確認します。削除が完了するまで、学習環境を終えたとは扱いません。

### Visual Notes

- CloudFormation stack deletion
- Resources removed

## Slide 4

### Slide Title

残る可能性

### Slide Message

履歴やロールを確認する

### Narration

削除後も、過去のテレメトリ表示や、サービスリンクロールのように残る可能性があるものがあります。削除後に何が残り得るかを知っておくと、あわてず確認できます。 削除後も、過去のメトリクス、ログ、ロール、サービスリンクロール、履歴表示が残る可能性があります。これはリソースが動き続けていることとは限りません。残るものと課金につながるものを分けて確認します。

### Visual Notes

- Historical telemetry
- Service-linked role note

## Slide 5

### Slide Title

コスト確認

### Slide Message

請求画面まで見る

### Narration

最後に、請求とコストの画面を確認します。すぐに反映されない費用もありますが、学習後に確認する習慣を作ることが大切です。 コスト確認では、請求ダッシュボードやコストエクスプローラーで、想定外の増加がないかを見ます。料金はリージョン、通信量、保存期間、エスエルオー設定で変わるため、講座内の説明だけで断定せず、公式情報を確認します。

### Visual Notes

- Billing and Cost Explorer check
- Delayed cost visibility

## Slide 6

### Slide Title

次の一歩

### Slide Message

自分のサービスに置き換える

### Narration

このコースで学んだ後は、自分のサービスで、どのサービスを見たいか、どの体験をエスエルオーにしたいかを整理してください。画面を見るだけでなく、運用判断へつなげます。 次の一歩は、自分のサービスに置き換えることです。どの操作が重要か、どの依存関係を見たいか、どの目標を守りたいかを決めます。サンプルで学んだ流れを、そのまま本番設計へ持ち込まず、チームの運用に合わせて育てます。

### Visual Notes

- From sample app to own service
- SLO design worksheet
