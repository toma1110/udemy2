# AWS課金事故防止入門: Budgets・Cost Explorer・削除チェックリスト

この講座は、AWS初学者がハンズオン前後の課金事故を避けるために、AWS Budgets、Cost Explorer、Cost Anomaly Detection、削除チェックリストを学ぶ制作領域です。

## Source of Truth

- `course_spec.md`
- `course_curriculum.md`

## Course ID

`aws-cost-safety-course`

## 制作方針

- 「節約額を約束する講座」ではなく、「課金事故を起こしにくい運用習慣を作る講座」として設計する
- AWS Budgetsで月次予算と実績/予測アラートを設定する
- Cost Explorerでサービス別、期間別、タグ別にコストを見る基本を扱う
- Cost Anomaly Detectionは異常コストに早く気づく仕組みとして扱う
- 削除チェックリストと月次確認ルーティンを、他のAWS講座の前提教材として使える形にする
- AWS料金や無料枠は変わるため、公開前に必ず公式情報を再確認する
- 完成動画のスライドと表示文字はGPT-Image2で生成する
- 音声はVOICEVOXを使う

## 講座構成

| Section | Title | Goal |
| --- | --- | --- |
| 1 | 課金事故が起きる理由 | AWSコストの遅延、従量課金、削除漏れの基本リスクを説明できる |
| 2 | Budgetsで最初の安全柵を作る | 月次予算、実績アラート、予測アラートを設定できる |
| 3 | Cost Explorerでコストを見る | サービス別、期間別、タグ別の読み方を説明できる |
| 4 | Cost Anomaly Detectionで異常に気づく | 異常コスト検知の役割と通知設計を説明できる |
| 5 | タグと削除チェックリスト | ハンズオン後に見落としやすい課金源を確認できる |
| 6 | 月次コスト確認ルーティン | 毎月の確認、改善、次の学習導線を作れる |

## ハンズオン

- `handson/README.md`: コンソール操作、確認観点、削除チェックリスト
- `cloudformation/README.md`: optionalな再現用CloudFormation範囲

## ディレクトリ

- `scripts/`: 台本
- `slides/`: GPT-Image2プロンプトとスライド
- `audio/`: VOICEVOX音声
- `video/`: MP4生成レポート
- `qa/`: AWS仕様確認、制作QA、Driveアップロード記録
- `tickets/`: ローカルTask Issue写し
- `cloudformation/`: optionalな教材ハンズオン用テンプレート

## AWS実行ゲート

AWS Budgets、Cost Explorer、Cost Anomaly Detection、CloudFormation stack作成/更新/削除、課金確認APIの実行は、CEO承認後にだけ行います。

標準制作では、まず公式ドキュメント確認、README、画面手順、台本、GPT-Image2スライド、VOICEVOX音声、QAを作成します。
