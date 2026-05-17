# s2-l1 鳴りすぎるアラートを減らす

Course: `aws-alert-design-practical-course`

Segments: 7

## Slide 1: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

このレクチャーでは、鳴りすぎるアラートを減らす設計を学びます。アラートは多いほど安全、というわけではありません。通知が多すぎると、人は重要な通知を見落とします。監視の目的は、画面やチャンネルを赤くすることではなく、必要な対応を早く始めることです。そのためには、鳴らす条件を少し厳しくしたり、評価時間を長くしたり、同じ原因で一斉に鳴る通知をまとめたりする必要があります。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 1.

## Slide 2: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

最初に見るのは、しきいちだけで判断していないかです。たとえば、シーピーユーが八十パーセントを一回超えたら通知する、という設定は分かりやすいですが、一瞬のスパイクでも鳴ります。短時間だけ負荷が上がってすぐ戻るワークロードでは、毎回通知するとノイズになります。この場合、クラウドウォッチアラームの評価期間とデータポイント数を使います。一分ごとに五回評価し、そのうち三回しきいちを超えたらアラームにする、というように、エヌ回中エム回で判断します。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 2.

## Slide 3: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

この考え方は、エムアウトオブエヌと呼ぶと理解しやすいです。五回中一回の悪化では通知しない。五回中三回悪化したら通知する。こうすると、一瞬だけ跳ねたあたいでは起こされず、継続して悪い状態だけを拾いやすくなります。ただし、評価窓を長くしすぎると検知が遅れます。ユーザー影響が急に大きくなるサービスでは、長い評価窓は危険です。ノイズを減らすことと、検知を遅らせすぎないことのバランスを取ります。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 3.

## Slide 4: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

次に、同じ障害で複数のアラートが鳴っていないかを確認します。ひとつの依存先が遅いだけで、レイテンシ、エラー率、リトライ数、キュー滞留、シーピーユーが同時に鳴ることがあります。通知が五つ届くと、対応者はどれが入口か迷います。このときは、個別アラートを全部消すのではなく、上位の判断用アラートを作る発想が使えます。クラウドウォッチのコンポジットアラームは、複数のアラーム状態を、アンド、オア、ノットで組み合わせて、より意味のある一つの通知にできます。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 4.

## Slide 5: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

たとえば、シーピーユーが高い、だけでは通知しない。しかしシーピーユーが高く、かつレイテンシも悪化しているなら通知する。あるいは、下流サービスの障害が分かっているときは、依存先由来の一部通知を抑制して、代表アラートだけを出す。こうした設計により、通知の数ではなく、対応の入口を整えます。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 5.

## Slide 6: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

もう一つ大切なのは、通知しない状態を決めることです。すべての異常を人に通知すると、運用は長続きしません。自動復旧できる一時的な失敗、ユーザー影響がない低優先度の変化、営業時間外には対応しない検証環境の通知などは、人を起こす必要がない場合があります。もちろん記録は残します。ダッシュボードやログで見える状態にしつつ、人へ通知する条件を絞ります。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 6.

## Slide 7: 鳴りすぎるアラートを減らす

Message: ノイズ、短すぎる評価期間、重複通知を設計で減らす

### Narration

最後に、アラート削減のレビュー手順です。まず、過去一週間または一か月で何回鳴ったかを見ます。次に、そのうち実際に人が対応した回数を見ます。対応しなかった通知は、しきいち、評価期間、通知先、セベリティ、ランブックを見直します。通知数を減らす目的は、監視を弱くすることではありません。本当に対応すべき通知に集中できるようにすることです。

### Visual Notes

Many noisy alarms reduced with M out of N, evaluation window, composite alarm. Segment 7.
