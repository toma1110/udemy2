# GPT-Image2 Prompts: s1-l3

Use the same premium AWS/SRE educational visual style as VID-001 and VID-002 s1-l1. 16:9 slide, clean cloud notification architecture aesthetic, white and pale blue background, navy, teal, and amber accents, readable Japanese text generated inside the image, no logos, no watermark, no local text overlay.

## slide_001.png

Create a Japanese course slide. Large title: `SNS Topicとメール確認`. Subtitle: `Topicが通知の中継点になる`. Visual: CloudWatch Alarm sends to central SNS Topic, then to Email inbox.

## slide_002.png

Create a Japanese course slide. Large title: `Topicは通知チャネル`. Subtitle: `AlarmはTopicへ1回送ればよい`. Visual: one arrow from Alarm to Topic, then multiple clean arrows to possible destinations, with Topic highlighted as channel.

## slide_003.png

Create a Japanese course slide. Large title: `Subscriptionは宛先`. Subtitle: `誰に、どの方式で届けるかを決める`. Visual: configuration cards `Protocol: email` and `Endpoint: mail address` connected under SNS Topic.

## slide_004.png

Create a Japanese course slide. Large title: `メール確認`. Subtitle: `承認するまでPendingのまま`. Visual: inbox with confirmation email, status changes from red `PendingConfirmation` to green `Confirmed`.

## slide_005.png

Create a Japanese course slide. Large title: `Topic Policy`. Subtitle: `CloudWatchがpublishできる許可を置く`. Visual: CloudWatch passes through an authorization gate into SNS Topic, small labels `SourceAccount` and `SourceArn`.

## slide_006.png

Create a Japanese course slide. Large title: `届かない時`. Subtitle: `確認、Action、Policyの順に見る`. Visual: three-step checklist: `Email Confirm`, `AlarmActions`, `Topic Policy`.

## slide_007.png

Create a Japanese course slide. Large title: `最小から広げる`. Subtitle: `まずメール、次に運用設計へ`. Visual: staircase from `Email` to `Encryption` to `Team routing`, small label `最小構成`.
