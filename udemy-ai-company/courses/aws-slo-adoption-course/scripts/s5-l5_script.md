# Section 5 Lecture 5 台本

## Title

updateとdeleteまで確認する

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- `cloudformation/validate.sh`
- `cloudformation/README.md`

## Slide 1

### Slide Title

updateとdeleteまで確認する

### Slide Message

作成後の変更と片づけまでをハンズオンに含める

### Narration

このレクチャーでは、スタックの更新と削除を確認します。ハンズオンでは、作成できたことだけでなく、変更できること、そして確実に片づけられることまで確認します。

### Visual Notes

- Update and delete lifecycle
- Create is not the finish line
- Safe cleanup focus

## Slide 2

### Slide Title

なぜupdateを見るのか

### Slide Message

運用では、SLO基盤も変更される

### Narration

エスエルオー基盤は、一度作ったら固定ではありません。ダッシュボードタイトルを変える、しきいちを見直す、通知先を追加する。こうした変更が起きます。だから、更新手順もハンズオンに含めます。

### Visual Notes

- Dashboard title update
- Threshold review
- Notification change
- Operational lifecycle

## Slide 3

### Slide Title

updateを実行する

### Slide Message

変更差分をCloudFormationで反映する

### Narration

更新コマンドでは、既存スタックに変更を反映します。サンプルでは、ダッシュボードタイトルの変更を想定します。変更がない場合でも失敗扱いにしない設定にしているため、繰り返し実行しやすくなっています。

### Visual Notes

- Command: ./validate.sh update
- DashboardTitle parameter change
- no-fail-on-empty-changeset

## Slide 4

### Slide Title

fullで通し確認する

### Slide Message

validate、create、metrics、smoke、update、deleteをまとめる

### Narration

検証スクリプトには、通し確認のモードもあります。テンプレート検証、作成、メトリクス投入、スモークテスト、更新、削除をまとめて実行します。既存スタックがある場合は、誤って壊さないように停止します。

### Visual Notes

- Command: ./validate.sh full
- End-to-end validation
- Existing stack guard

## Slide 5

### Slide Title

deleteを実行する

### Slide Message

学習後は、必ずスタックを削除する

### Narration

最後に、削除コマンドを実行します。クラウドフォーメーションの削除完了を待つことで、アラーム、ダッシュボード、エスエヌエスなどが片づいたことを確認します。学習用スタックは残さない運用にします。

### Visual Notes

- Command: ./validate.sh delete
- wait stack-delete-complete
- Cleanup as part of hands-on

## Slide 6

### Slide Title

残る可能性があるもの

### Slide Message

Custom Metricの履歴やService-linked roleに注意

### Narration

削除後も、メトリクスの履歴や管理用ロールが残る場合があります。標準構成ではアプリケーションシグナルズのエスエルオーは作りません。オプションを有効化した場合は、サービスリンクロールが残る可能性も確認します。

### Visual Notes

- Metric history retention
- Optional Application Signals service-linked role
- No active stack resources after delete

## Slide 7

### Slide Title

失敗時の片づけ

### Slide Message

スタック状態を見て、削除可能か判断する

### Narration

もし作成や更新に失敗したら、まずスタック状態を確認します。削除できる状態なら削除します。削除に失敗する場合は、イベントを見て、どのリソースが原因かを確認します。手動削除は最後の手段です。

### Visual Notes

- Stack events
- DELETE_FAILED handling
- Identify blocking resource
- Manual cleanup as last resort

## Slide 8

### Slide Title

まとめ: 作成から削除までが合格条件

### Slide Message

README通りに再現できる状態を目指す

### Narration

まとめです。セクション5の合格条件は、作成できることだけではありません。検証、作成、投入、確認、更新、削除をリードミー通りに再現できることです。次のセクションでは、エラーバジェットとバーンレートに進みます。

### Visual Notes

- Done: validate/create/put metrics/smoke/update/delete
- README reproducibility
- Arrow to Section 6 error budget and burn rate

## QA Notes

- `lectures.md` の Lecture 5-5 に合わせて構成
- update、delete、full validationを説明
- 残存リソース注意を明記
- 8枚構成
