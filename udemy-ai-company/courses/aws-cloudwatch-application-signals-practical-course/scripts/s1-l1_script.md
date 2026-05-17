# Section 1 Lecture 1 台本

### Title

Application Signalsで何が見えるか

## Slide 1

### Slide Title

Application Signalsの入口

### Slide Message

アプリの状態をサービス単位で見る

### Narration

このコースでは、クラウドウォッチアプリケーションシグナルズを、実アプリの通信で学びます。まずは、何を見るための機能なのかを整理します。入口は、サービス単位で状態を見ることです。 メトリクスだけを見る監視では、どのサービスのどの操作が利用者体験に効いているかを切り分けにくいことがあります。アプリケーションシグナルズでは、アプリをサービスとして見て、通信、遅さ、失敗、目標を同じ流れで確認します。まず全体を見てから、必要なサービスへ入る順番を作ります。

### Visual Notes

- Application Signals entry point
- Service health overview
- One service highlighted

## Slide 2

### Slide Title

4つの基本指標

### Slide Message

量、速さ、成功、失敗

### Narration

アプリケーションシグナルズでは、通信量、レイテンシ、可用性、フォルト、エラーを確認します。数字を個別に見るだけでなく、サービスの健康状態としてまとめて見るのがポイントです。 ここでの通信量は、そもそも観測対象に呼び出しが来ているかを見る入口です。レイテンシは遅さ、可用性は成功割合、フォルトとエラーは失敗の種類を見るための指標です。単独の数字ではなく、同じ時間帯に何が一緒に変わったかを読むことが重要です。

### Visual Notes

- Call volume, latency, availability, fault, error tiles
- Healthy and unhealthy state contrast

## Slide 3

### Slide Title

Services

### Slide Message

まず一覧で状態をつかむ

### Narration

最初に見るのはサービス一覧です。どのサービスに通信が来ているか。レイテンシが悪化していないか。フォルトやエラーが増えていないか。調査の出発点をここで決めます。 サービス一覧では、いきなり詳細に入らず、どこから見るべきかを決めます。通信がないサービスは、計装や時間範囲を疑います。通信があるのに遅い、または失敗が増えているサービスは、詳細画面や地図へ進む候補になります。

### Visual Notes

- Service list abstraction
- Status, latency, availability columns

## Slide 4

### Slide Title

Application Map

### Slide Message

依存関係を地図で見る

### Narration

次に、アプリケーションマップで依存関係を見ます。サービス同士がどのようにつながり、どこで遅延や失敗が出ているかを、地図として確認します。 地図で見る利点は、自分が担当するサービスだけでなく、呼び出し先や呼び出し元も同時に意識できることです。障害は一つのサービスに見えても、実際には依存先の遅延や失敗が影響している場合があります。

### Visual Notes

- Abstract service map
- Two Lambda nodes connected
- Error marker on one node

## Slide 5

### Slide Title

Service detail

### Slide Message

原因へ近づく詳細画面

### Narration

サービスディテールでは、レイテンシ、可用性、フォルト、エラーを時間の流れで見ます。ここからログやトレースへ進み、何が起きたのかを調べる流れを作ります。 詳細画面では、一覧で見つけた違和感を時間の流れで確認します。遅くなった時間、失敗が増えた時間、ログやトレースで深掘りすべき場所を決めます。ここで原因を断定するのではなく、次に見る証拠を選びます。

### Visual Notes

- Detailed metrics timeline
- Link from metric to logs and traces

## Slide 6

### Slide Title

SLOへつなげる

### Slide Message

重要な体験を目標にする

### Narration

最後に、重要なサービス状態をエスエルオーへつなげます。ただし、短時間のハンズオンで十分な実運用データが集まるわけではありません。このコースでは、作り方と見方を分けて学びます。 エスエルオーは、監視を利用者体験の目標へ変えるための仕組みです。ただし、目標は思いつきで決めるものではありません。どの操作が重要か、どの遅さや失敗を許容できないかを考え、実データを見ながら調整します。

### Visual Notes

- SLO target connected to service health
- Learning scope vs production data boundary
