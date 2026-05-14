# Section 8 Lecture 3 台本

## Title

PM、経営層への報告テンプレート

## Source

- `course_spec.md`
- `lectures.md`
- `docs/VOICEVOX_RULES.md`
- Google SRE Workbook: Implementing SLOs

## Slide 1

### Slide Title

PM、経営層への報告テンプレート

### Slide Message

ダッシュボードを、判断できる報告メモに変換する

### Narration

このレクチャーでは、ピーエムや経営層へエスエルオーを報告する型を扱います。細かいダッシュボードをそのまま見せるのではなく、状態、影響、必要な判断を短くまとめます。相手が次の判断に使える形へ変換します。

### Visual Notes

- PM and leadership report
- dashboard to decision memo

## Slide 2

### Slide Title

相手で分ける

### Slide Message

PMはリリース判断、経営層は事業影響を見る

### Narration

報告は相手によって分けます。ピーエムには、リリース判断、スコープ調整、顧客影響を伝えます。経営層には、事業リスク、投資判断、継続的な改善状況を伝えます。同じエスエルオーでも、見る観点が違います。

### Visual Notes

- PM decision lens
- executive business lens

## Slide 3

### Slide Title

1分サマリー

### Slide Message

状態、影響、判断を最初に置く

### Narration

最初に一分サマリーを置きます。今の状態は良いのか、注意なのか、危険なのか。ユーザー影響はあるのか。必要な判断は何か。この三つを先に書くと、読む側は詳細を見る前に状況をつかめます。

### Visual Notes

- One-minute summary
- status, impact, decision

## Slide 4

### Slide Title

PM向けテンプレート

### Slide Message

機能、影響、リリース判断、次の対応

### Narration

ピーエム向けには、機能単位で書くと伝わりやすいです。どの機能の体験が悪化したか。ユーザーにどんな影響があるか。リリースを継続するのか、小さく出すのか、延期するのか。最後に次の対応を書きます。

### Visual Notes

- PM template
- feature, impact, release decision

## Slide 5

### Slide Title

経営層向けテンプレート

### Slide Message

事業影響、残り予算、投資判断を中心にする

### Narration

経営層向けには、事業影響を中心にします。主要なユーザー体験は守れているか。エラーバジェットはどれくらい残っているか。改善に追加投資が必要か。この粒度にすると、技術詳細に入りすぎず判断できます。

### Visual Notes

- Executive template
- business impact and budget

## Slide 6

### Slide Title

予算を翻訳する

### Slide Message

エラーバジェットを、余裕、注意、停止の言葉にする

### Narration

エラーバジェットは、判断の言葉に翻訳します。余白が十分なら、予定どおり進められます。残りが少ないなら、注意して進めます。消費速度が高いなら、新機能より安定化を優先します。数字を行動に結びつけます。

### Visual Notes

- Budget translation
- proceed, caution, stabilize

## Slide 7

### Slide Title

定例に組み込む

### Slide Message

週次PM、月次経営会議で、同じ型で見せる

### Narration

報告テンプレートは、定例に組み込むと効果が出ます。週次のピーエム会議では、リリース判断と改善タスクを確認します。月次の経営会議では、信頼性の傾向と投資判断を確認します。同じ型で続けることが重要です。

### Visual Notes

- Weekly PM meeting
- monthly leadership review

## Slide 8

### Slide Title

まとめ

### Slide Message

相手、結論、予算翻訳、定例化をそろえる

### Narration

まとめです。ピーエムや経営層への報告では、相手の判断に合わせて情報を選びます。最初に結論を置き、エラーバジェットを行動の言葉に翻訳し、定例で同じ型を使い続けます。これで、エスエルオーが組織の判断に入りやすくなります。

### Visual Notes

- Summary
- audience, conclusion, budget, routine

## QA Notes

- `lectures.md` の Lecture 8-3「PM、経営層への報告テンプレート」に合わせて構成
- ナレーションでは PM をピーエム、SLO をエスエルオーに寄せる
- 8枚構成
