# s3-l2 Missing dataとComposite Alarmの使いどころ

Course: `aws-alert-design-practical-course`

Segments: 7

## Slide 1: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

このレクチャーでは、欠損データとコンポジットアラームの使いどころを学びます。アラーム設計では、データがあるときだけでなく、データがないときにどう扱うかも重要です。クラウドウォッチアラームには、欠損データをどう評価するかという考え方があります。ここを雑に決めると、何も起きていないのに通知が増えたり、本当に問題があるのに見逃したりします。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 1.

## Slide 2: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

まず、常に出るはずのメトリクスを考えます。たとえば、ロードバランサーのリクエスト数、サービスのレイテンシ、インスタンスのシーピーユー使用率など、通常時も継続して出るメトリクスがあります。こうしたメトリクスが突然出なくなった場合、監視対象が止まっている、メトリクス送信が壊れている、設定が変わった、という可能性があります。この場合、データがないことを軽く見すぎると、障害を見逃すことがあります。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 2.

## Slide 3: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

一方で、エラーが起きたときだけ出るメトリクスもあります。たとえば、失敗数や特定の例外数のように、正常時にはゼロまたはデータなしに見えるものです。このタイプで、データがないことをすべて異常にすると、正常時に毎回通知される可能性があります。エラー時だけ出るメトリクスでは、データなしが正常に近い意味を持つことがあります。つまり、欠損データの扱いは、メトリクスの性質で決めます。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 3.

## Slide 4: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

次に、コンポジットアラームです。複数のアラームが同時に鳴ると、対応者は何から見るべきか迷います。コンポジットアラームは、複数のアラーム状態を組み合わせ、上位の意味ある通知にまとめる選択肢です。アンド、オア、ノットのような論理で、たとえば、レイテンシが悪化していて、かつエラー率も上がっている場合に通知する、といった設計ができます。個別メトリクスだけでは判断しにくい状態を、サービス影響に近い条件へ変換します。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 4.

## Slide 5: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

ただし、コンポジットアラームは万能ではありません。条件を複雑にしすぎると、なぜ鳴ったのか分からなくなります。最初は、同じ障害で同時に鳴る代表的なアラームをまとめるところから始めます。たとえば、サービスレイテンシ、エラー率、依存先失敗率のように、影響判断に使うものを組み合わせます。通知本文には、どの個別アラームが状態変化したか、最初に見るダッシュボードはどこかを書いておきます。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 5.

## Slide 6: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

欠損データとコンポジットアラームを一緒に考えると、アラート設計はかなり実務的になります。常時出るはずのデータが消えたなら、それ自体が異常かもしれません。エラー時だけ出るデータがないなら、正常かもしれません。複数の軽い異常が同時に起きたなら、サービス影響の可能性が高くなります。逆に一つだけの軽い異常なら、通知ではなくダッシュボード確認に留める選択もあります。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 6.

## Slide 7: Missing dataとComposite Alarmの使いどころ

Message: 欠損データと複合条件で、見逃しとノイズの両方を抑える

### Narration

最後にレビュー質問です。そのメトリクスは、正常時にも常に出ますか。データがないことは、良いことですか、悪いことですか、それとも判断不能ですか。個別アラームが複数同時に鳴ったとき、対応者が見るべき代表アラートはありますか。コンポジットアラームの条件は、説明できる単純さを保っていますか。欠損データと複合条件を正しく扱うことで、見逃しとノイズの両方を減らせます。

### Visual Notes

Missing data choice by metric type and composite alarm decision tree. Segment 7.
