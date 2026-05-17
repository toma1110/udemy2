# udemy登録情報

## 想定する学習者

### コースで受講生は何を学びますか？
※コースを修了後に学習者が達成できると期待できる学習目的や成果を4つ以上入力する必要があります。（160文字以内）

CloudWatch Application SignalsでLatency、Availability、Fault、Error、Call volumeを確認できる
Services、Application Map、Service detailを使い、サービス状態と依存関係を説明できる
サンプルアプリに正常、遅延、エラーの通信を発生させ、APMの見方を体験できる
Application Signals SLOとCloudWatch Alarm/Dashboardの役割の違いを説明できる
SLO RecommendationsやSLO Performance Reportの前提、制約、使いどころを判断できる

### コースを受講するための要件や前提条件は何ですか?
コースを受講する学習者に求められるスキル、経験、ツール、機器をリストアップします。
そのような要件がない場合は、その点を初心者にとってのハードルを下げるチャンスとして利用しましょう。

- AWSアカウントを持っている
- AWS CLIを実行できる環境がある
- CloudFormation、Lambda、IAM、CloudWatch、EventBridge Schedulerを操作できる権限がある
- Lambda、HTTP、レイテンシ、エラー率の基本を理解している
- AWS利用料金が発生する可能性を理解し、検証後に削除できる

### 誰に向けたコースですか?
コースの内容が必ず役に立つ、想定する学習者を明確に示します。
そうすることで、最適な学習者にコースをアピールすることができます。

- CloudWatchの次にApplication SignalsやAPMを学びたい人
- SRE、DevOps、クラウド運用に進みたい人
- LambdaやAWSアプリケーションの状態をサービス単位で見たい人
- SLO監視を実アプリのLatencyやAvailabilityへつなげたい人
- OpenTelemetryやX-Rayの前に、AWSマネージドな入口を体験したい人

## コース紹介ページ

### コースタイトル
AWS CloudWatch Application Signals実践: サンプルアプリで学ぶAPM・Service Map・SLO監視

※タイトルは、目立ち、わかりやすく、検索エンジン用に最適化されている必要があります

### コースのサブタイトル
CloudFormationでサンプルアプリと低頻度通信を作り、Application SignalsでAPM、Service Map、SLO監視を体験する実践講座。

※関連するキーワードを1つまたは2つ使用し、コースで取り上げた最も重要な分野を3～4つ挙げてください。

### コースの説明
※本コースにはAIの使用が含まれています。
本コースのナレーションには、VOICEVOXの「ずんだもん」を使用しています。VOICEVOX利用規約に基づき商用利用しています。

■ このコースはこんな悩みを解決します
・AWSアプリケーションの遅延やエラーをサービス単位で見たい
・Application Signalsの画面で何を確認すればよいか分からない
・Service MapやService detailの読み方を体験したい
・SLO監視をLatencyやAvailabilityへどうつなげるか知りたい
・課金、計装、サービスリンクロール、データ期間などの注意点を先に理解したい

---

■ このコースで学べること
AWSでアプリケーションを動かしていても、遅延、エラー、依存関係、SLOをどこから見ればよいか分からない。そんな人のために、CloudWatch Application Signalsを実アプリで体験する講座です。

・Application Signalsで見える主要指標
・Services、Application Map、Service detailの読み方
・サンプルアプリに正常、遅延、エラーの通信を発生させる流れ
・Application Signals SLOの基本
・Application SignalsとCloudWatch Alarm/Dashboardの役割の違い
・SLO Recommendations、Service-Level SLO、SLO Performance Reportの前提
・自動トラフィック停止、スタック削除、コスト確認

---

■ このコースの特徴
【特徴1】実アプリでAPMを体験する
CloudFormationで短時間検証用のサンプルアプリと低頻度通信を作り、Application Signalsの見方を実際に確認します。

【特徴2】課金と制約を先に整理する
Application Signalsは便利ですが、課金、計装、対応リージョン、十分なメトリクス期間などの注意点があります。無理な常時高負荷検証は避け、停止できる構成にします。

【特徴3】SLO関連機能を現実的に扱う
SLO RecommendationsやSLO Performance Reportなど、実運用データや期間が必要な機能は、短時間ハンズオンで無理に完了させず、使いどころと前提条件を整理します。

---

■ ハンズオンとコストについて
本講座はAWSリソースを作成する実践講座です。Application Signals、Lambda、CloudWatch Logs、EventBridge Schedulerなどで料金が発生する場合があります。
READMEのコスト注意、自動トラフィック停止、CloudFormation stack削除、コスト確認を必ず実施してください。

---

■ 想定受講時間
約2〜3時間（講義本編30分以上＋Application Signalsハンズオン）

■ 講座尺・動画生成前確認
本コースは11レクチャー構成で、講義本編の動画尺を合計30分以上に再設計します。動画再生成前に、CEOが `course_spec.md` と本 `course_infomation.md` を確認・承認する前提です。承認後は、全レクチャー動画を一括で再生成します。

## コース画像
ここにコース画像をアップロードしてください。使用する画像は、Udemyのコース画像品質基準に適合している必要があります。重要なガイドライン: 750x422ピクセル、.jpg、.jpeg、.gif、または.png形式、テキストを含む画像は不可。

本コースの画像方針:

- 登録候補: `course_image.png`
- GPT-Image2生成元: `course_image_gpt_image2_source.png`
- テキストを含めない
- サービスマップ、アプリケーション監視、SLOを連想できるビジュアルにする
- 公式UIの模写、ロゴ乱用、読めない文字列を避ける

## コースメッセージ
受講生がコースに参加したときやコースを修了したときに自動的に送信するメッセージを設定して、コースで学ぶ受講生を励ましましょう（設定は任意です）。コースに参加したときの歓迎のメッセージやコースを修了したときのお祝いのメッセージを送信しない場合は、テキストボックスを空白のままにしておきます。

### 歓迎のメッセージ
ご受講ありがとうございます。

このコースでは、CloudWatch Application Signalsを実際のサンプルアプリと通信で体験します。Services、Application Map、Service detail、SLOを見ながら、アプリケーションの状態をどのように運用判断へつなげるかを確認します。

ハンズオンではAWSリソースを作成し、自動トラフィックも発生させます。READMEのコスト注意、停止手順、削除手順を確認しながら進めてください。

### お祝いのメッセージ
コース修了お疲れさまでした。

Application Signalsを使って、サービス状態、依存関係、レイテンシ、エラー、SLOを確認する流れを体験できました。

次の一歩として、自分のサービスで「まず見たいサービス」「重要な操作」「SLOにしたいLatencyまたはAvailability」「異常時の確認順序」を整理してみてください。APMは画面を見るだけでなく、運用判断に使える形へ落とし込むことで価値が出ます。

ハンズオンでAWSリソースを作成した場合は、最後に自動トラフィック停止、スタック削除、コスト確認を忘れずに行ってください。
