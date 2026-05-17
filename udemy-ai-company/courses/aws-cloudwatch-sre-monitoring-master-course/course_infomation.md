# udemy登録情報

## 想定する学習者

### コースで受講生は何を学びますか？
CloudWatch Metrics、Logs、Alarm、Dashboard、Application Signalsの役割を整理し、監視運用の全体像を説明できる
Logs Insightsで障害調査に使う基本クエリを書き、検索範囲とコストを意識してログを調査できる
Alarm、SNS、Composite Alarm、Runbookを組み合わせ、通知疲れを避けるアラート設計ができる
SLI、SLO、エラーバジェット、バーンレートをCloudWatch監視と週次・月次レビューへ接続できる
CloudFormationで教材用監視基盤を作成、更新、確認、削除し、実運用ではCDK/Terraformへ発展させる判断ができる

### コースを受講するための要件や前提条件は何ですか?
- AWSアカウントを持っている、またはAWSの基本操作を学習できる環境がある
- CloudWatch、CloudWatch Logs、CloudWatch Alarmという名前を聞いたことがある
- AWS CLIをインストールし、認証情報とリージョンを設定できる
- Bashコマンドをコピーして実行できる
- HTTPステータスコード、レイテンシ、エラー率の意味をおおまかに理解している
- CloudFormationは教材ハンズオン再現用に使うため、基本操作を知っていると理解しやすい
- 実運用のIaCは、所属チームの方針に応じてCDKまたはTerraformで設計する前提を持てる

### 誰に向けたコースですか?
- AWS監視をCloudWatchで始めたが、ログ調査、通知設計、SLO運用までつなげられていない人
- SREを目指しているインフラエンジニア、クラウドエンジニア、バックエンドエンジニア
- CloudWatch Logs Insightsで障害調査クエリを書けるようになりたい人
- AlarmやSNS通知を作ったものの、通知疲れや重要度設計に悩んでいる人
- Runbook、初動対応、SLOレビューを現場運用へ組み込みたい人
- AWSハンズオンで課金、IAM、CloudFormation rollbackが不安な人
- 資格対策ではなく、AWSを使った監視運用設計を体系的に学びたい人

## コース紹介ページ

### コースタイトル
AWS CloudWatch/SRE監視実践マスター：Logs Insights・Alarm・SLO・運用改善

### コースのサブタイトル
CloudWatch Logs Insights、Alarm/SNS、Application Signals、SLO、Runbookをつなげて、AWS監視を実務の運用改善へ発展させる長尺実践コース

### コースの説明
※本コースにはAIの使用が含まれています。
本コースのナレーションには、VOICEVOXの「ずんだもん」を使用しています。VOICEVOX利用規約に基づき商用利用しています。

■ このコースはこんな悩みを解決します
・CloudWatchの機能は知っているが、監視運用としてどうつなげればよいかわからない
・Logs Insightsで調査したいが、毎回クエリの書き方で迷ってしまう
・AlarmやSNS通知を作ったものの、通知疲れや重要度設計に悩んでいる
・Runbookを作りたいが、アラート後5分、15分、30分で何を見るべきか整理できていない
・SLI、SLO、エラーバジェットをCloudWatch監視にどう接続するか説明できない
・Application Signalsの使いどころ、課金、SLO機能の前提を整理したい
・AWSハンズオンで課金、IAM、CloudFormation rollbackが不安で手が止まる

---

■ このコースで学べること
このコースは、CloudWatchの個別機能を覚えるだけでなく、ログ調査、通知設計、Runbook、SLOレビュー、改善バックログまでを一続きの監視運用として学ぶ長尺実践コースです。

・CloudWatch Metrics、Logs、Alarm、Dashboard、Application Signalsの全体像
・Logs Insightsの基本クエリと障害調査パターン
・CloudWatch Alarm、SNS、Composite Alarm、Metric Mathの使い分け
・通知疲れを避けるSeverity、Owner、Runbookリンクの設計
・CloudFormationを使った教材用監視基盤の作成、更新、確認、削除
・Application SignalsのService Map、Latency、Availability、Fault、Errorの見方
・SLI、SLO、エラーバジェット、バーンレートの運用判断へのつなげ方
・アラート後5分、15分、30分のRunbook初動対応
・CloudFormation rollback、IAM AccessDenied、課金不安の切り分け
・週次・月次SLOレビューと改善バックログ化

---

■ このコースの特徴
【特徴1】CloudWatchを一続きの運用として学ぶ
メトリクス、ログ、アラーム、ダッシュボードを別々に覚えるのではなく、障害検知、原因調査、初動対応、再発防止、SLOレビューまでつなげて学びます。

【特徴2】短尺講座の単純な連結ではない長尺設計
既存の短尺講座で扱うテーマを土台にしつつ、章末演習、統合CloudFormationハンズオン、障害調査シミュレーション、SLOレビュー会議を追加します。

【特徴3】AWS学習の不安も本編で扱う
課金、削除手順、CloudFormation rollback、IAM AccessDeniedを後回しにせず、ハンズオン前後の安全確認として扱います。

【特徴4】教材用CloudFormationと実運用IaCを分ける
本コースのハンズオンでは、初学者がREADME通りに再現しやすいCloudFormationを使います。実運用では、チームの開発体制に応じてCDKまたはTerraformを推奨する前提で説明します。

【特徴5】Application SignalsとSLOを現実的に扱う
Application SignalsのService MapやSLO機能は、実アプリ計装、継続データ、リクエスト数やSLO数に応じた料金が関係します。本コースでは、使いどころと制約を分けて理解します。

---

■ 受講後にできること
・CloudWatchを使った監視運用の全体像を説明できる
・Logs Insightsでエラー調査、時系列集計、パス別集計の基本クエリを書ける
・AlarmとSNS通知を、Owner、Severity、Runbookリンク付きで設計できる
・アラート発生後の初動対応をRunbookとして整理できる
・SLI/SLOとエラーバジェットを、週次・月次レビューの判断材料にできる
・CloudFormationハンズオンをREADME通りに実行し、作成後に安全に削除できる
・Application Signalsを導入すべき場面と、標準CloudWatch監視で十分な場面を判断できる
・実運用IaCとしてCDK/Terraformへ発展させる観点を説明できる

---

■ ハンズオンとコストについて
本コースの標準ハンズオンでは、CloudWatch Logs、Logs Insights、Custom Metrics、Alarm、Dashboard、SNS、CloudFormationを使います。これらのサービスには料金が発生する場合があります。

ハンズオンは、短時間で作成、確認、削除できる教材用構成に限定します。READMEには、作成するリソース、想定リージョン、料金注意、削除手順、確認コマンドを明記します。

Application SignalsやSLO関連機能は、実アプリ計装、継続データ、リクエスト数、SLO数に応じた料金が関係するため、標準ハンズオンと補講・デモの範囲を分けて扱います。

---

■ 想定受講時間
約10〜12時間（講義、章末演習、統合ハンズオン、Capstone演習を含む）

## コース画像
ここにコース画像をアップロードしてください。使用する画像は、Udemyのコース画像品質基準に適合している必要があります。重要なガイドライン: 750x422ピクセル、.jpg、.jpeg、.gif、または.png形式、テキストを含む画像は不可。

本コースの画像方針:

- 登録候補: `course_image.png`
- GPT-Image2生成元: `course_image_gpt_image2_source.png`
- テキストを含めない
- CloudWatch、監視ダッシュボード、ログ調査、SRE運用レビューを連想できるビジュアルにする
- AWS公式ロゴや実在UIの模写は避け、抽象化された監視・運用のビジュアルにする
- 生成AI画像を使う場合は、Udemy登録前に不自然な文字、ロゴ、UI崩れ、権利上の懸念がないか確認する

## コースメッセージ

### 歓迎のメッセージ
ご受講ありがとうございます。

このコースでは、CloudWatchの個別機能を覚えるだけでなく、ログ調査、通知設計、Runbook、SLOレビューまでを一続きの監視運用として学びます。

ハンズオンを実行する場合は、READMEのコスト注意、リージョン、作成リソース、削除手順を先に確認してください。CloudFormationは教材用の再現手段として使い、実運用ではCDKまたはTerraformへ発展させる前提で進めます。

受講中は、自分のサービスならどのアラートを鳴らすか、どのログを調査するか、どのSLOをレビューするかを考えながら進めると、学習内容を現場へ持ち帰りやすくなります。

### お祝いのメッセージ
コース修了お疲れさまでした。

ここまでで、CloudWatchの全体像、Logs Insightsの調査、Alarm/SNSの通知設計、Runbook初動対応、Application Signals、SLI/SLO、エラーバジェット、学習安全までを一通り確認しました。

次の一歩として、自分のサービスで「最初に監視するユーザー体験」「必要なLogs Insightsクエリ」「通知すべきアラート」「Runbookの初動手順」「週次レビューで見るSLO」を1枚にまとめてみてください。

ハンズオンでAWSリソースを作成した場合は、最後にCloudFormationスタック削除、SNS購読、Dashboard、Log Group、料金の確認も忘れずに行ってください。
