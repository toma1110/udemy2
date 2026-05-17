# Section 3 Lecture 1 台本

### Title

Servicesで状態を見る

## Slide 1

### Slide Title

Servicesを見る

### Slide Message

調査の入口を決める

### Narration

ここから、アプリケーションシグナルズの画面で見る順番を整理します。最初はサービス一覧です。どのサービスを見るべきか、調査の入口を決める画面として使います。 サービス一覧は、調査の入口を決める画面です。すべての詳細をここで読むのではなく、どのサービスが怪しいか、どこに利用者影響がありそうかを選びます。一覧から詳細、地図、ログへ進むための分岐点として使います。

### Visual Notes

- Services overview
- Investigation starting point

## Slide 2

### Slide Title

サービス名

### Slide Message

対象を間違えない

### Narration

まずサービス名を確認します。今回のサンプルでは、サンプルアプリ用ラムダと、トラフィック生成用ラムダが出る想定です。どちらを見ているのかを間違えないようにします。 サービス名を見る時は、想定したラムダやアプリが表示されているかを確認します。名前が見えない場合は、通信がない、計装が足りない、時間範囲が合っていない、反映待ちなどが候補です。まず対象を間違えないことが大切です。

### Visual Notes

- Two service rows
- Sample app highlighted

## Slide 3

### Slide Title

Call volume

### Slide Message

通信が来ているかを見る

### Narration

次に通信量を見ます。通信量が増えていなければ、アプリの問題を見る前に、スケジュールや呼び出しが動いているかを確認します。 コールボリュームは、通信が届いているかを見る基本指標です。通信がないのにレイテンシや失敗を議論しても、判断材料が足りません。まず呼び出しがあるか、いつ増えたか、シナリオ切り替えと時間が合うかを見ます。

### Visual Notes

- Call volume line
- No traffic versus traffic

## Slide 4

### Slide Title

Latency

### Slide Message

遅くなっていないか

### Narration

レイテンシは、ユーザー体験に近い重要な指標です。遅延シナリオに切り替えた時、ここがどう変わるかを見ることで、遅さの入口を確認できます。 レイテンシでは、どの時間帯から遅くなったかを見ます。正常シナリオから遅延シナリオへ切り替えたあと、グラフに変化が出るかを確認します。すぐに反映されない場合もあるため、時間範囲と待ち時間を見直します。

### Visual Notes

- Latency chart
- Slow scenario marker

## Slide 5

### Slide Title

Availability

### Slide Message

成功率を見る

### Narration

可用性は、リクエストが期待通り成功しているかを見る入口です。エラーシナリオでは、フォルトやエラーとあわせて、可用性の低下を確認します。 可用性は、成功している割合を見る入口です。失敗が少し混ざっただけなのか、継続的に悪化しているのかを分けて考えます。運用では、単発の失敗と利用者影響のある失敗を同じ扱いにしないことが重要です。

### Visual Notes

- Availability percentage
- Error scenario drop

## Slide 6

### Slide Title

次へ進む判断

### Slide Message

一覧から詳細へ

### Narration

サービス一覧で異常の入口を見つけたら、次はアプリケーションマップやサービスディテールへ進みます。一覧は、終着点ではなく、調査の出発点です。 一覧で違和感を見つけたら、次に何を見るかを決めます。遅いなら詳細画面で時間の流れを見ます。依存関係が気になるなら地図を見ます。失敗の中身を知りたいならログやトレースへ進みます。

### Visual Notes

- Services to map to detail flow
- Operator decision path
