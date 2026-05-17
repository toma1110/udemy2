# Section 3 Lecture 2 台本

### Title

Application Mapで依存関係を見る

## Slide 1

### Slide Title

Application Map

### Slide Message

つながりを地図で見る

### Narration

アプリケーションマップでは、サービス同士のつながりを見ます。今回のサンプルでは、トラフィック生成用ラムダから、サンプルアプリ用ラムダへ呼び出す関係を確認します。 アプリケーションマップは、サービスのつながりを俯瞰するための画面です。障害時は一つのグラフだけを見ていると、依存先や呼び出し元を見落とすことがあります。地図で見ることで、どこからどこへ通信しているかを確認できます。

### Visual Notes

- Two service nodes
- Dependency arrow

## Slide 2

### Slide Title

呼ぶ側

### Slide Message

Traffic Generatorを見る

### Narration

呼ぶ側は、トラフィック生成用ラムダです。ここに問題があると、サンプルアプリへ通信が届かない可能性があります。まず、呼び出し元としての役割を確認します。 呼ぶ側のトラフィック生成サービスは、学習環境で通信を作る役割です。ここに通信がない場合、スケジュールが止まっている、権限や設定が違う、作成直後で反映待ち、といった確認が必要になります。

### Visual Notes

- Caller service highlighted
- Scheduler to generator context

## Slide 3

### Slide Title

呼ばれる側

### Slide Message

Sample APIを見る

### Narration

呼ばれる側は、サンプルアプリ用ラムダです。レイテンシやエラーの確認では、このサービスが主な対象になります。どちらのサービスに異常があるのかを分けて見ます。 呼ばれる側のサンプルエーピーアイは、利用者向け処理に相当する場所として見ます。遅延や失敗を起こした時に、ここがどのように見えるかを確認します。呼び出し元だけでなく、受ける側の状態を見ることが大切です。

### Visual Notes

- Callee service highlighted
- Sample API metrics

## Slide 4

### Slide Title

線を見る

### Slide Message

関係の上に異常が出る

### Narration

地図では、ノードだけでなく、つながりも見ます。呼び出しの関係の上に遅延や失敗の兆候が出ると、どのやり取りを深掘りするかを決めやすくなります。 線は、サービス同士の関係を示します。どちらのノードが悪いのか、どの関係で遅さや失敗が増えているのかを読む入口になります。地図だけで断定せず、気になる場所を詳細画面へつなげます。

### Visual Notes

- Edge with latency or error marker
- Dependency health

## Slide 5

### Slide Title

全体から詳細へ

### Slide Message

地図は迷子防止

### Narration

アプリケーションマップの役割は、迷子にならないことです。全体像を見てから、問題がありそうなサービスや関係を選び、サービスディテールへ進みます。 地図は迷子防止の道具です。サービス数が増えるほど、一覧だけでは関係が分かりにくくなります。全体から対象を選び、対象から詳細へ入ることで、調査の順番を保てます。

### Visual Notes

- Map to service detail transition
- Operator path

## Slide 6

### Slide Title

実運用での見方

### Slide Message

依存先も候補に入れる

### Narration

実運用では、ラムダだけでなく、データベース、キュー、外部サービスなどの依存先も候補になります。地図を見る目的は、原因候補を広く、しかし順番に絞ることです。 実運用では、自分のサービスだけでなく、外部依存、下流サービス、呼び出し元チームも候補に入ります。地図を見ながら、誰に確認すべきか、どの依存先を切り分けるべきかを考えます。

### Visual Notes

- Broader dependency map
- Database, queue, external service abstractions
