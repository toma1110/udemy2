# s1-l2 PlaybookとRunbookの違い

Course: `aws-runbook-first-response-course`

Segments: 8

## Slide 1: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

このレクチャーでは、プレイブックとランブックの違いを整理します。どちらも障害対応で使う手順書ですが、役割が少し違います。プレイブックは、何が起きているかを調べるための手順です。影響範囲を確認し、原因候補を絞り、必要ならエスカレーションします。ランブックは、既知の状況に対して、どう緩和または復旧するかを進める手順です。調査の地図がプレイブック、復旧の手順がランブック、と考えると分かりやすいです。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 1.

## Slide 2: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

たとえば、注文エーピーアイのエラー率が上がったとします。最初に必要なのは、どのユーザーに影響しているか、いつから始まったか、直近デプロイがあるか、依存先で障害が起きていないかを調べることです。これはプレイブックの領域です。まだ原因が分かっていないので、いきなり復旧コマンドを実行するのではなく、状況を把握します。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 2.

## Slide 3: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

一方で、原因が直近デプロイにあり、切り戻し手順が既に決まっているなら、ランブックへ移ります。どのバージョンへ戻すか、誰の承認が必要か、実行コマンドは何か、実行後にどのメトリクスを見るか。こうした既知の手順を、誰が実行しても同じように進められる形にするのがランブックです。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 3.

## Slide 4: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

この違いを混同すると、手順書が使いにくくなります。調査用のプレイブックに、長い復旧コマンドを大量に書くと、初動時に読みづらくなります。逆に、ランブックに原因調査の分岐を詰め込みすぎると、復旧手順がぼやけます。最初は、プレイブックでは何を見るか、ランブックでは何を実行するか、と分けて書くと整理しやすくなります。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 4.

## Slide 5: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

プレイブックに書くものは、発生時刻、影響範囲、関連ダッシュボード、ログの見方、直近変更の確認、依存サービスの状態、エスカレーション条件です。目的は、原因候補を絞り、次に使うランブックを選ぶことです。プレイブックのゴールは、完全な原因分析ではありません。初動で迷わず、調査の入口を揃えることです。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 5.

## Slide 6: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

ランブックに書くものは、トリガー、前提条件、実行者、承認者、具体的な手順、戻し方、確認方法、失敗時のエスカレーションです。目的は、既知の問題に対して、緩和または復旧を安定して進めることです。実行にリスクがある操作は、必ず条件と承認を明記します。誰でも押せる危険な手順にしてはいけません。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 6.

## Slide 7: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

最後に、実務での使い分けです。アラートが鳴った直後は、まずプレイブックで状況を見ます。原因候補が見えて、既知の対応があるなら、対応するランブックへ進みます。既知の対応がないなら、エスカレーションし、対応記録を残し、後でポストモーテムから新しいランブックを育てます。プレイブックとランブックを分けることで、調査と復旧の流れが見えやすくなります。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 7.

## Slide 8: PlaybookとRunbookの違い

Message: 調査の手順と、既知の復旧手順を分ける

### Narration

演習として、自分のチームの手順を一つ選び、これは調査のプレイブックなのか、復旧のランブックなのかを分けてください。分けられない場合は、目的、実行条件、成功確認、エスカレーション条件が混ざっている可能性があります。まず入口を分けるだけで、障害時の迷いはかなり減ります。

### Visual Notes

Playbook investigation path and runbook remediation path with handoff. Segment 7. Exercise recap segment.
