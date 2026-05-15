# GPT-Image2 Prompts: s2-l1

Use the same premium AWS/SRE educational visual style as VID-001 and VID-002 s1-l1. 16:9 slide, clean infrastructure-as-code education aesthetic, white and pale blue background, navy, teal, and green accents, readable Japanese text generated inside the image, no logos, no watermark, no local text overlay.

## slide_001.png

Create a Japanese course slide. Large title: `テンプレートを読む`. Subtitle: `入力、条件、部品、出力に分ける`. Visual: CloudFormation template split into four panels: `Parameters`, `Conditions`, `Resources`, `Outputs`.

## slide_002.png

Create a Japanese course slide. Large title: `Parameters`. Subtitle: `受講者が変える値を入口にする`. Visual: input form cards for `NotificationEmail` and `AlarmThreshold`, with optional empty email branch.

## slide_003.png

Create a Japanese course slide. Large title: `Conditions`. Subtitle: `メールがある時だけSubscriptionを作る`. Visual: decision diamond `HasNotificationEmail`, yes path creates `Subscription`, no path skips it.

## slide_004.png

Create a Japanese course slide. Large title: `SNS Topic`. Subtitle: `Alarm通知を受ける中継点を作る`. Visual: CloudFormation creates SNS Topic, with small tags `Course` and `ManagedBy`.

## slide_005.png

Create a Japanese course slide. Large title: `Topic Policy`. Subtitle: `CloudWatchからのpublishを許可する`. Visual: permission gate from CloudWatch service to SNS Topic, constraints `SourceAccount` and `SourceArn`.

## slide_006.png

Create a Japanese course slide. Large title: `CloudWatch Alarm`. Subtitle: `Metric、Threshold、Actionsをまとめる`. Visual: alarm resource in center with spokes `Metric`, `Period`, `Threshold`, `AlarmActions`, arrows to SNS Topic.

## slide_007.png

Create a Japanese course slide. Large title: `Outputs`. Subtitle: `作成後に見る値を外へ出す`. Visual: stack outputs panel listing `AlarmName`, `AlarmTopicArn`, `EmailSubscriptionCreated`, connected to verification commands.

## slide_008.png

Create a Japanese course slide. Large title: `読み方のまとめ`. Subtitle: `入力から出力まで、依存関係で追う`. Visual: dependency map flowing from `Parameters` to `Resources` to `Outputs`, with arrows and checkmarks.
