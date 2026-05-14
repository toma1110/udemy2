# Section 8 Lecture 4 台本

## Title

リリース判断とエラーバジェット

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs

## Slide 1

### Slide Title

リリース判断とエラーバジェット

### Slide Message

信頼性の余白を見て、出す、絞る、止めるを決める

### Narration

このレクチャーでは、エラーバジェットをリリース判断に使う考え方を扱います。信頼性の余白が十分なら進める。余白が少なければ小さく出す。急速に悪化しているなら安定化を優先する。このように判断を分けます。

### Visual Notes

- Release decision and error budget
- ship, limit, pause

## Slide 2

### Slide Title

リリース前に見る数字

### Slide Message

残り予算、消費速度、直近の障害を見る

### Narration

リリース前には、三つの数字を見ます。残りエラーバジェットは十分か。バーンレート、つまり消費速度は高すぎないか。直近で大きな障害が続いていないか。この三つを見ると、このリリースを進めてよいかを判断しやすくなります。

### Visual Notes

- Remaining budget
- burn rate
- recent incidents

## Slide 3

### Slide Title

余白が十分な場合

### Slide Message

通常リリースを継続し、監視を強める

### Narration

余白が十分な場合は、通常どおりリリースを進めやすい状態です。ただし、出したあとに見ないわけではありません。リリース直後のエラー率、レイテンシ、ユーザー影響を見て、想定外の悪化があればすぐ戻れるようにします。

### Visual Notes

- Continue release
- watch after release

## Slide 4

### Slide Title

余白が少ない場合

### Slide Message

スコープを絞り、段階的に出す

### Narration

余白が少ない場合は、リリースを小さくします。対象ユーザーを絞る、機能を分ける、変更量を減らす、ロールバック手順を確認する。全部止める前に、リスクを下げて出す選択肢を検討します。

### Visual Notes

- Reduce scope
- phased rollout

## Slide 5

### Slide Title

消費が速い場合

### Slide Message

新機能より、安定化と原因調査を優先する

### Narration

エラーバジェットの消費が速い場合は、新機能より安定化を優先します。今の悪化が続くと、短期間で目標違反に近づくためです。原因が分かるまで大きな変更を避け、監視、切り分け、修正に集中します。

### Visual Notes

- High burn rate
- stabilize before shipping

## Slide 6

### Slide Title

判断基準を事前に決める

### Slide Message

リリース前に、継続、縮小、停止の条件を合意する

### Narration

判断基準は、リリース当日に初めて決めると揉めやすくなります。残り予算が十分なら継続。少ないなら縮小。消費速度が高いなら停止して安定化。このような条件を、開発、運用、ピーエムで事前に合意しておきます。

### Visual Notes

- Decision table
- continue, reduce, pause

## Slide 7

### Slide Title

リリース後に確認する

### Slide Message

出したあと、予算とユーザー影響がどう変わったかを見る

### Narration

リリース後は、出して終わりではありません。予算の減り方が変わったか。特定の機能で悪化していないか。アラームや問い合わせが増えていないかを見ます。結果を次の判断基準に反映します。

### Visual Notes

- Post-release review
- budget and user impact

## Slide 8

### Slide Title

まとめ

### Slide Message

余白を見て、小さく出し、レビューへ戻す

### Narration

まとめです。エラーバジェットは、リリースを止めるためだけの数字ではありません。余白があれば進める。少なければ小さく出す。消費が速ければ安定化を優先する。そしてリリース後に結果を見る。この流れで、信頼性と開発速度を両立しやすくなります。

### Visual Notes

- Summary
- budget, scope, stabilize, review

## QA Notes

- `lectures.md` の Lecture 8-4「リリース判断とエラーバジェット」に合わせて構成
- ナレーションでは PM をピーエム、SLO をエスエルオーに寄せる
- 8枚構成
