# Section 4 Lecture 2 台本

### Title

RecommendationsとPerformance Reportの前提

## Slide 1

### Slide Title

発展機能の前提

### Slide Message

短時間では完了しない

### Narration

アプリケーションシグナルズには、エスエルオーのおすすめや、パフォーマンスレポートのような発展機能があります。ただし、短時間のハンズオンだけで完成確認するものではありません。 発展機能は便利ですが、短時間ハンズオンで結果を断定するものではありません。推奨値やレポートは、十分な期間の実データがあって意味を持ちます。この講座では、使いどころと前提を理解することをゴールにします。

### Visual Notes

- Advanced features area
- Time and data requirement

## Slide 2

### Slide Title

Recommendations

### Slide Message

実データから候補を出す

### Narration

レコメンデーションは、実際のサービスメトリクスをもとに、エスエルオー候補を考える機能です。十分な期間のデータがあるほど、現実的な候補を検討しやすくなります。 レコメンデーションは、過去のサービスメトリクスをもとに目標候補を考える機能です。発表情報では、三十日分のメトリクスを分析する位置づけです。短時間のサンプル通信だけで、妥当な本番目標が出るとは考えません。

### Visual Notes

- Historical metrics
- SLO recommendation candidate

## Slide 3

### Slide Title

Service-Level SLO

### Slide Message

サービス全体を見る

### Narration

サービスレベルのエスエルオーは、ひとつの操作だけではなく、サービス全体をどう見るかという考え方につながります。どの単位を重要とするかが設計ポイントです。 サービスレベルのエスエルオーは、個別操作だけでなくサービス全体の信頼性を見たい時に役立ちます。チームや事業側に説明する時は、細かい操作単位と全体像の両方を使い分ける必要があります。

### Visual Notes

- Service-level objective
- Service boundary

## Slide 4

### Slide Title

Performance Report

### Slide Message

継続データで振り返る

### Narration

パフォーマンスレポートは、継続的なデータをもとに振り返るための機能です。短いデモではなく、実運用で期間をおいて見るものとして扱います。 パフォーマンスレポートは、日次、週次、月次のような期間で信頼性を振り返る考え方につながります。障害が起きた瞬間だけでなく、継続的に目標を満たしているか、改善傾向があるかを見るための材料です。

### Visual Notes

- Periodic report
- Trend over days

## Slide 5

### Slide Title

このコースの範囲

### Slide Message

入口と使いどころを学ぶ

### Narration

このコースでは、発展機能を無理に完了条件にしません。入口、必要な前提、運用で使う場面を整理し、実サービスで試すための準備にします。 このコースでは、サンプルアプリで画面の入口を体験し、発展機能は実運用データで使うものとして整理します。学習環境で無理に結果を作るより、どの条件がそろえば使えるかを説明できることを優先します。

### Visual Notes

- Course scope boundary
- Hands-on versus production operation

## Slide 6

### Slide Title

無理に断定しない

### Slide Message

データ期間を尊重する

### Narration

信頼性の数字は、短い時間だけで断定しないことが大切です。十分なデータ期間を取り、チームでしきいちや目標を見直す前提で使います。 監視機能は、見えた数字をそのまま正解にするものではありません。データ期間、通信量、対象サービス、利用者影響を見て、判断に使えるかを確認します。無理に断定しない姿勢が、誤った運用判断を防ぎます。

### Visual Notes

- Data duration
- Team review
- Threshold adjustment
