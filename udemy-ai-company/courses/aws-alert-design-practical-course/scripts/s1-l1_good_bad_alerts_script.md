# s1-l1 Script: 深夜3時に動けるアラートとは

Course: `aws-alert-design-practical-course`
Lecture: `s1-l1`
Target length: 8-10 minutes

## Slide 1

### Slide Title

良いアラートと悪いアラート

### Slide Message

深夜3時に動けるか

### Narration

このレクチャーでは、良いアラートと悪いアラートの違いを学びます。判断基準はとてもシンプルです。深夜3時に通知で起こされたとき、次の5分で何をすべきか分かるか。この問いに答えられないアラートは、設定値が正しく見えても、運用では役に立ちにくいアラートです。

### Visual Notes

- Night on-call notification
- Split between confusion and clear action

## Slide 2

### Slide Title

良いアラートの3条件

### Slide Message

Actionable / Timely / Meaningful

### Narration

良いアラートには、三つの条件があります。一つ目はアクション可能であること。受け取った人が次に何を確認するか分かる状態です。二つ目はタイムリーであること。問題が大きくなる前に届くことです。三つ目は意味があること。毎日鳴るノイズではなく、対応する価値がある通知であることです。

### Visual Notes

- Three pillars
- Action, timing, signal quality

## Slide 3

### Slide Title

悪い例

### Slide Message

CPUが高いだけでは動けない

### Narration

悪い例を見てみましょう。アラート名は、シーピーユーハイ。本文は、シーピーユーが80パーセントを超えました。通知先は全員向けチャンネル。これだけでは、どのサービスに影響しているのか、緊急なのか、誰が対応するのか、何を確認するのかが分かりません。多くの人に届いているようで、実際には誰も動かない通知になりがちです。

### Visual Notes

- Noisy generic alert card
- Missing impact, owner, runbook

## Slide 4

### Slide Title

良い例

### Slide Message

影響・Owner・Runbookを入れる

### Narration

良い例では、通知を行動に変えます。たとえば、決済エーピーアイのピーナインティナインレイテンシが5分間で悪化し、3回中3回しきいちを超えた。影響は一部ユーザーの決済遅延。担当は決済チームのオンコール担当。ランブックは決済レイテンシ対応手順。ここまで書いてあれば、受け取った人はまず何を見るべきか判断できます。

### Visual Notes

- Alert card with severity, impact, owner, runbook
- Clear next action path

## Slide 5

### Slide Title

鳴りすぎを防ぐ

### Slide Message

M out of Nでノイズを減らす

### Narration

クラウドウォッチアラームでは、期間、評価回数、アラームにするデータポイント数で、いつアラーム状態にするかを決めます。たとえば1分ごとに5回評価し、そのうち3回しきいちを超えたら通知する、という設計ができます。これは、エヌ回中エム回の考え方です。一瞬だけ跳ねたメトリクスで毎回起こされないように、評価窓を設計します。

### Visual Notes

- Timeline of 5 data points
- 3 breaching points trigger alarm

## Slide 6

### Slide Title

欠損データを考える

### Slide Message

メトリクスの性質で選ぶ

### Narration

欠損データ、つまりデータがない時間の扱いも重要です。常に出るはずのメトリクスが消えたなら、問題の可能性があります。一方で、エラーが起きたときだけ出るメトリクスなら、データがないことは正常かもしれません。欠損データをすべて異常にすると、不要な通知が増えます。逆にすべて正常扱いにすると、検知すべき異常を見逃すことがあります。

### Visual Notes

- Two metric lanes
- Continuous metric vs error-only metric

## Slide 7

### Slide Title

まとめるアラート

### Slide Message

Composite Alarmで判断を絞る

### Narration

複数の個別アラートが同じ障害で一斉に鳴ると、対応者は何から見るべきか迷います。コンポジットアラームは、複数のアラーム状態を、アンド、オア、ノットで組み合わせ、上位の一つのアラートにまとめる選択肢です。たとえば、シーピーユーが高いだけではなく、同時にレイテンシも悪化している場合に通知する、といった設計ができます。

### Visual Notes

- Several low-level alarms feeding one composite alarm
- Reduced notification noise

## Slide 8

### Slide Title

深夜3時チェック

### Slide Message

次の5分で何をするか

### Narration

最後に、アラートを作るたびにこのチェックをしてください。アラート名だけで影響範囲が分かるか。セベリティがあるか。オーナーがいるか。ランブックがあるか。エスカレーション先が決まっているか。そして、次の5分で何をするか言えるか。これに答えられるアラートが、良いアラートです。

### Visual Notes

- Checklist with five checks
- On-call engineer moving from alert to runbook
