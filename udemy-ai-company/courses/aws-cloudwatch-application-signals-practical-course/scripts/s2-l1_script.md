# Section 2 Lecture 1 台本

### Title

テンプレート全体を読む

## Slide 1

### Slide Title

テンプレートの地図

### Slide Message

作るものを先に読む

### Narration

ここから、クラウドフォーメーションテンプレートを読みます。最初に大事なのは、細かいプロパティへ入る前に、何を作るテンプレートなのかを地図としてつかむことです。 テンプレートを読む目的は、何が作られるかを理解してから実行することです。リソース名、ロール、ログ、スケジュール、アプリケーションシグナルズ関連の設定を先に見ます。作成後に慌てて止めるのではなく、止め方まで読んでから始めます。

### Visual Notes

- Template overview map
- Resources grouped by role

## Slide 2

### Slide Title

Discovery

### Slide Message

Application Signalsの準備

### Narration

テンプレートには、アプリケーションシグナルズのディスカバリーを入れています。これは、サービス検出のための準備です。アプリを見えるようにする入口として扱います。 ディスカバリーは、アプリケーションシグナルズでサービスを見つけるための準備です。これだけで十分な画面が出るわけではなく、実際の通信と計装されたサービスのメトリクスが必要です。準備、通信、画面反映の順番を分けて理解します。

### Visual Notes

- Discovery setup block
- Service-linked role concept

## Slide 3

### Slide Title

2つのLambda

### Slide Message

呼ぶ側と呼ばれる側

### Narration

ラムダは2つあります。ひとつはサンプルアプリです。もうひとつは、サンプルアプリを低頻度で呼び出すトラフィック生成用です。役割を分けることで、依存関係を見やすくします。 二つのラムダに分ける理由は、呼ぶ側と呼ばれる側の関係を作るためです。単体の関数だけでは、依存関係の地図を学びにくくなります。呼び出し元、呼び出し先、どちらで遅延や失敗が起きるかを見ることで、画面の意味が分かりやすくなります。

### Visual Notes

- Traffic generator Lambda
- Sample API Lambda
- Directional arrow

## Slide 4

### Slide Title

Instrumentation

### Slide Message

Layerと環境変数

### Narration

ラムダでアプリケーションシグナルズを使うために、オープンテレメトリーのレイヤーと、実行ラッパー用の環境変数を設定します。さらに、実行ロールには必要な管理ポリシーを付けます。 計装では、オープンテレメトリーのレイヤーや環境変数、実行ロールの権限が重要になります。講座では細かい実装を暗記するより、計装がないとサービスや操作が見えない、という関係を押さえます。レイヤーのエーアールエヌはリージョンで確認が必要です。

### Visual Notes

- Lambda layer
- Environment variables
- Execution role policy

## Slide 5

### Slide Title

Schedule

### Slide Message

低頻度で通信を作る

### Narration

イベントブリッジスケジューラーは、標準で低頻度に設定します。学習目的は負荷をかけることではありません。画面に変化が出るだけの小さな通信を作ることです。 スケジュールは、観測に必要な通信を少しだけ作るために使います。常時高負荷を作るものではありません。頻度が高すぎると料金とノイズが増えるため、学習では低頻度で十分です。確認が終わったら、まず通信を止めます。

### Visual Notes

- Low-frequency scheduler
- Traffic pulse every minute
- Cost safety marker

## Slide 6

### Slide Title

SLOは条件付き

### Slide Message

最初から作らない

### Narration

エスエルオーは条件付きです。対象サービスがメトリクスを送る前には、作成に失敗する可能性があります。まず通信を作り、サービスが見えてから有効化する流れにしています。 エスエルオーをテンプレートで扱う場合でも、サービス操作のメトリクスが届いていない段階では作れないことがあります。そのため、最初はサンプルアプリと通信を作り、あとから更新でエスエルオーを追加する流れにします。

### Visual Notes

- Conditional SLO resource
- First traffic, then SLO
