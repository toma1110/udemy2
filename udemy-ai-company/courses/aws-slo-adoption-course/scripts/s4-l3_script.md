# Section 4 Lecture 3 台本

## Title

period-based SLOとrequest-based SLO

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- AWS CloudWatch Service Level Objectives documentation

## Slide 1

### Slide Title

period-based SLOとrequest-based SLO

### Slide Message

時間で見るか、リクエスト数で見るか

### Narration

このレクチャーでは、期間ベースのエスエルオーと、リクエストベースのエスエルオーを比較します。どちらも目標達成率を見る考え方ですが、評価の単位が違います。時間の区切りで見るのか、リクエスト数で見るのかを分けて理解します。

### Visual Notes

- Two-column comparison: period-based vs request-based
- Time windows vs request dots
- Section 4 marker

## Slide 2

### Slide Title

period-basedは時間で評価する

### Slide Message

良い期間 ÷ 全期間

### Narration

期間ベースのエスエルオーでは、決められた期間ごとに、目標を満たしたかを判定します。たとえば、いっぷんごとにレイテンシが目標以内かを見ます。そして、良い期間の数を、全期間の数で割って達成率を出します。時間を均等に扱うのが特徴です。

### Visual Notes

- Timeline split into equal periods
- Good and bad periods colored
- Formula: good periods / total periods

## Slide 3

### Slide Title

request-basedは件数で評価する

### Slide Message

良いリクエスト数 ÷ 全リクエスト数

### Narration

リクエストベースのエスエルオーでは、リクエスト一件一件を評価します。良いリクエスト数を、全リクエスト数で割って達成率を出します。トラフィックが大きく変動するサービスでは、実際に影響を受けたリクエスト数で見られるため、体験に近い判断がしやすくなります。

### Visual Notes

- Request dots split into good/bad
- Formula: good requests / total requests
- Traffic-weighted evaluation

## Slide 4

### Slide Title

少ないトラフィックに注意

### Slide Message

少数の失敗が、見え方を大きく変える

### Narration

どちらの方式でも、少ないトラフィックには注意が必要です。リクエストが少ないサービスでは、一件の失敗が達成率を大きく動かします。期間ベースでもリクエストベースでも、数字だけを見て決めず、対象サービスの利用量と重要度を合わせて確認します。

### Visual Notes

- Low traffic example with one bad request
- Big percentage swing warning
- Data volume checklist

## Slide 5

### Slide Title

Latency SLOでの使い分け

### Slide Message

しきいち以内のリクエストを良い体験とする

### Narration

レイテンシのエスエルオーでは、待ち時間がしきいち以内なら良い体験、と定義します。期間ベースなら、各期間で目標を満たしたかを見ます。リクエストベースなら、しきいち以内だったリクエストの割合を見ます。どちらも、先に良い体験の条件を決めることが大切です。

### Visual Notes

- Latency threshold line
- Period evaluation vs request evaluation
- Good experience definition first

## Slide 6

### Slide Title

Availability SLOは成功条件を決める

### Slide Message

どのレスポンスを成功として扱うか

### Narration

アベイラビリティのエスエルオーでは、どのレスポンスを成功として扱うかが重要です。アプリケーションシグナルズの標準メトリクスでは、五百系のフォルトがないレスポンスを成功として扱います。業務エラーを別の条件で扱いたい場合は、クラウドウォッチメトリクスやメトリクスマスで、独自のエスエルアイを設計します。

### Visual Notes

- Standard Availability definition cards
- 5xx fault vs successful response
- Custom SLI path for business errors

## Slide 7

### Slide Title

エラーバジェットの見え方

### Slide Message

評価方式で、消費の見え方が変わる

### Narration

期間ベースとリクエストベースでは、エラーバジェットの減り方の見え方も変わります。期間ベースは、悪いじかんたいを重く見ます。リクエストベースは、影響を受けたリクエスト数を重く見ます。どちらが良いかではなく、判断したいリスクに合う方式を選びます。

### Visual Notes

- Error budget burn comparison
- Bad time window vs bad request count
- Risk-based selection card

## Slide 8

### Slide Title

まとめ: 評価単位を選ぶ

### Slide Message

時間で見るか、リクエストで見るかを明確にする

### Narration

まとめです。期間ベースは、良い期間を全期間で割って達成率を見ます。リクエストベースは、良いリクエスト数を全リクエスト数で割って達成率を見ます。次のレクチャーでは、アプリケーションシグナルズのエスエルオー推奨値を、どう使えばよいかを整理します。

### Visual Notes

- Final comparison table
- Formula recap
- Arrow to SLO推奨値

## QA Notes

- `lectures.md` の Lecture 4-3 に合わせて構成
- 読み上げではperiod-based/request-basedを「期間ベース」「リクエストベース」に統一
- 8枚構成。S4-L4のSLO推奨値へ接続
- CEOコメント反映: Availability SLOの表題を成功条件の説明に寄せる
- CEOコメント反映: 「時間帯」はナレーションで「じかんたい」と読ませる
