# Section 5 Lecture 4 台本

## Title

smoke testでSLO基盤を確認する

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- `cloudformation/smoke_test.sh`
- `cloudformation/README.md`

## Slide 1

### Slide Title

smoke testでSLO基盤を確認する

### Slide Message

README通りに再現できるかを機械的に見る

### Narration

このレクチャーでは、スモークテストでエスエルオー基盤を確認します。目的は、画面で見て作れた気がする、で終わらせないことです。リードミー通りに作った結果を、コマンドで再現確認します。

### Visual Notes

- Smoke test as reproducibility gate
- README -> command -> resource existence
- Not just visual confirmation

## Slide 2

### Slide Title

smoke testの役割

### Slide Message

最低限の存在確認を自動化する

### Narration

スモークテストは、詳細な負荷試験ではありません。最低限の存在確認です。スタックの出力を取得し、エスエヌエス、アラーム、ダッシュボードが本当に存在するかを確認します。

### Visual Notes

- Scope: existence checks
- Not load testing
- Outputs as source for checks

## Slide 3

### Slide Title

Outputsを取得する

### Slide Message

テスト対象の名前をCloudFormationから読む

### Narration

テストでは、まずクラウドフォーメーションのアウトプッツを読みます。手で名前を入力すると間違いやすいため、スタックから取得します。これにより、テンプレートで作った対象をそのまま検証できます。

### Visual Notes

- describe-stacks
- OutputKey lookup
- Topic ARN, alarm names, dashboard name

## Slide 4

### Slide Title

SNS Topicを確認する

### Slide Message

通知先が存在するかを見る

### Narration

最初の確認対象は、エスエヌエストピックです。アウトプッツから取得したトピック識別子を使い、属性を取得できるかを確認します。ここが失敗する場合は、通知の出口が作れていません。

### Visual Notes

- get-topic-attributes
- Expected TopicArn equals actual TopicArn
- Notification path checkpoint

## Slide 5

### Slide Title

Alarmを確認する

### Slide Message

AvailabilityとLatencyの2本を確認する

### Narration

次に、アラームを確認します。アベイラビリティ用とレイテンシ用の二本です。アラーム名で検索し、期待した名前が返ってくるかを見ます。ここで、通知条件の入口が存在することを確認できます。

### Visual Notes

- describe-alarms
- Availability alarm
- Latency alarm
- AlarmName equality check

## Slide 6

### Slide Title

Dashboardを確認する

### Slide Message

可視化の入口も確認対象に入れる

### Narration

最後に、ダッシュボードを確認します。ダッシュボード名で取得できれば、可視化の入口が作れています。アラームだけでなく、見る場所も確認対象に含めることで、運用の流れに近づきます。

### Visual Notes

- get-dashboard
- DashboardName check
- Visualization gate

## Slide 7

### Slide Title

失敗したら切り分ける

### Slide Message

Output、権限、リージョン、スタック状態を見る

### Narration

失敗した場合は、順番に切り分けます。アウトプッツが空ではないか。権限が足りているか。リージョンが合っているか。スタックが作成完了になっているか。いきなりテンプレート全体を疑わず、確認点を分けます。

### Visual Notes

- Troubleshooting checklist
- Outputs empty
- IAM permission
- Region mismatch
- Stack status

## Slide 8

### Slide Title

まとめ: README再現性を確認する

### Slide Message

ハンズオン品質は、smoke testで底上げする

### Narration

まとめです。スモークテストは、ハンズオンの再現性を守るための最低限の品質ゲートです。次のレクチャーでは、スタック更新と削除まで確認し、作ったものを安全に片づけます。

### Visual Notes

- Smoke test pass as quality gate
- Arrow to update and delete
- README reproducibility

## QA Notes

- `lectures.md` の Lecture 5-4 に合わせて構成
- smoke testの確認対象を説明
- 8枚構成
- 読み上げでは英字を残さない
