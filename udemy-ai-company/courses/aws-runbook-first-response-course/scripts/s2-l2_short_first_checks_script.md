# s2-l2 First Checksを短く書く

Course: `aws-runbook-first-response-course`

Segments: 8

## Slide 1: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

このレクチャーでは、ランブックのファーストチェックを短く書く方法を学びます。ファーストチェックは、アラートを受け取った直後に見る項目です。ここが長すぎると、対応者は焦っているときに読み切れません。よいファーストチェックは、五分以内に終わり、順番があり、結果によって次の判断へ進める形になっています。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 1.

## Slide 2: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

まず、ファーストチェックには目的を書きます。目的は、原因を完全に特定することではなく、影響の有無と次の行き先を決めることです。たとえば、ユーザー影響があるか、悪化が続いているか、直近変更と関係がありそうか、既知のランブックへ進めるか。この四つを確認できれば、初動としては十分なことが多いです。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 2.

## Slide 3: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

次に、確認項目を五つ以内に絞ります。一つ目はアラームの発火時刻と対象。二つ目はダッシュボードの主要メトリクス。三つ目は代表的なエラーログ。四つ目は直近デプロイや設定変更。五つ目は依存先やエーダブリューエスヘルスです。これ以上増える場合は、ファーストチェックではなく詳細調査に分けます。初動の手順と詳細調査の手順を混ぜないことが重要です。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 3.

## Slide 4: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

三つ目に、見方を具体的に書きます。ダッシュボードを見る、とだけ書くと、人によって見る場所が変わります。どのダッシュボードのどのパネルを見るか、通常値はどれくらいか、どの状態なら異常と判断するかを書きます。ログを見る場合も、ロググループ、時間範囲、検索語、代表エラーの例を書きます。コマンドを使う場合は、実行に必要な権限と、読み取り専用かどうかを明記します。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 4.

## Slide 5: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

四つ目に、判断基準を書きます。確認して終わりではなく、結果によって次に進む必要があります。ユーザー影響あり、かつ悪化中ならエスカレーション。直近デプロイと時刻が一致するなら切り戻しランブックへ進む。依存先障害ならサービス責任者へ連絡し、状況共有テンプレートを使う。影響なしなら監視継続し、チケットに記録する。こうした分岐を短く書くと、対応者は迷いにくくなります。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 5.

## Slide 6: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

五つ目に、やらないことを書きます。初動では、原因の完全特定、長時間のログ探索、本番変更、危険な再起動、承認のない切り戻しをしない、などです。やらないことを明確にすると、焦って危険な操作をするリスクを下げられます。特に本番に影響する操作は、ランブックの別セクションに置き、承認条件を書きます。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 6.

## Slide 7: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

最後に、ファーストチェックをレビューする問いです。初めて当番に入った人が読んでも、五分で終わるでしょうか。どの画面を見るか具体的でしょうか。正常と異常の境目が分かるでしょうか。次の行き先が書かれているでしょうか。ファーストチェックは、短く、具体的で、判断につながることが大切です。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 7.

## Slide 8: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

演習として、既存の手順書から最初の五分に不要な項目を消してみてください。詳細調査、本番変更、長い原因分析は後ろに移します。残すのは、誰でも同じ画面を開き、同じ基準で判断できる確認だけです。短くした手順ほど、障害時に使われます。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 7. Exercise recap segment.

## Slide 9: First Checksを短く書く

Message: 焦っていても追える確認順にする

### Narration

実務メモとして、ファーストチェックは定期的に読み合わせます。実際に五分で終わるか、リンクが古くないか、権限が足りるかを確認します。読んで分かるだけではなく、当番者が本当に使えることを確認するのが重要です。

### Visual Notes

Short first checks checklist with time box and decision point. Segment 7. Exercise recap segment. Practical memo segment.
