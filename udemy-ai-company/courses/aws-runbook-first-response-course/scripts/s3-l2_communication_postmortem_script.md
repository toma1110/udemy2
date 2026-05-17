# s3-l2 CommunicationとPostmortemへつなげる

Course: `aws-runbook-first-response-course`

Segments: 8

## Slide 1: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

このレクチャーでは、コミュニケーションとポストモーテムへの接続をランブックに入れる方法を学びます。障害対応では、直すことだけが仕事ではありません。誰に何を伝えるか、どの判断をしたか、いつ復旧したか、あとで何を改善するかを残す必要があります。対応が速くても、連絡や記録が不足すると、関係者は状況を判断できず、同じ問題を繰り返します。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 1.

## Slide 2: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

まず、状況共有です。ランブックには、誰へ、どのタイミングで、どのチャンネルに共有するかを書きます。たとえば、セベリティ高ならインシデントチャンネルを作る。十五分以上影響が続くならサービス責任者へ連絡する。利用者影響があるならサポート担当へ共有する。外部告知が必要な場合は、権限を持つ担当へつなぐ。これを事前に決めておくと、対応者は復旧作業と連絡の両方で迷いにくくなります。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 2.

## Slide 3: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

次に、共有する内容です。長い説明ではなく、現在分かっている事実、影響範囲、開始時刻、現在の対応、次の更新予定を短く書きます。原因が分かっていない段階で、推測を断定してはいけません。分かっていること、分かっていないこと、次に確認することを分けます。これにより、関係者は状況を正しく理解できます。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 3.

## Slide 4: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

三つ目は記録です。障害中の判断は、あとで思い出そうとしても抜けます。いつアラートが鳴ったか、誰が参加したか、どのダッシュボードを見たか、何を実行したか、どんな結果だったかを残します。すべてを完璧に書く必要はありませんが、時刻、判断、実行、結果の四つは残します。これがポストモーテムの材料になります。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 4.

## Slide 5: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

四つ目は復旧確認です。ランブックには、復旧したと判断する条件を書きます。エラー率が通常範囲に戻った、レイテンシがしきいち以下で安定した、キューが解消した、ユーザー影響が止まった、サポート問い合わせが増えていない、などです。復旧した気がする、ではなく、どのメトリクスや事実で確認するかを書きます。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 5.

## Slide 6: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

五つ目はポストモーテムへの接続です。ポストモーテムは、誰かを責めるためではなく、再発防止と学びのために行います。ランブックには、ポストモーテムを作る条件、リンク先、最低限残す項目を書きます。たとえば、セベリティ高、ユーザー影響あり、手動復旧あり、同じ問題の再発、対応で迷いがあった場合は、ポストモーテム対象にします。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 6.

## Slide 7: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

最後に、ランブックの改善へ戻します。障害対応で、手順が分かりにくかった、リンクが古かった、確認項目が足りなかった、承認者が曖昧だった、という発見があれば、ランブックを更新します。ランブックは一度作って終わりではありません。使うたびに育てる文書です。コミュニケーション、記録、復旧確認、ポストモーテムを含めることで、障害対応はその場限りではなく、運用品質の改善につながります。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 7.

## Slide 8: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

最後の演習では、障害中の状況共有テンプレートを一つ作ります。開始時刻、影響範囲、現在の対応、次の更新予定、復旧確認条件を短く書いてください。さらに、対応後にポストモーテムへ残すリンクを用意します。対応を記録へつなげることが改善の入口です。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 7. Exercise recap segment.

## Slide 9: CommunicationとPostmortemへつなげる

Message: 状況共有、記録、再発防止までをRunbookに含める

### Narration

実務メモとして、状況共有の更新間隔も事前に決めます。たとえば十五分ごとに、分かっていること、対応中のこと、次の更新予定を出します。情報がなくても、次の更新時刻を出すことで、関係者の不安を減らせます。

### Visual Notes

Communication timeline, recovery confirmation, postmortem improvement loop. Segment 7. Exercise recap segment. Practical memo segment.
