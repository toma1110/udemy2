# GPT-Image2 Prompts: s2-l2

Use the same premium AWS/SRE educational visual style as VID-001 and VID-002 s1-l1. 16:9 slide, clean hands-on operations aesthetic, white and pale blue background, navy, teal, green, and amber accents, readable Japanese text generated inside the image, no logos, no watermark, no local text overlay.

## slide_001.png

Create a Japanese course slide. Large title: `作成前の注意`. Subtitle: `AWS操作はCEO承認後に実行する`. Visual: approval gate before AWS operation, cost warning icon, final delete checklist.

## slide_002.png

Create a Japanese course slide. Large title: `Stack Create`. Subtitle: `template.yamlとメールアドレスを指定する`. Visual: `template.yaml`, `NotificationEmail`, `AlarmThreshold` flowing into CloudFormation stack creation.

## slide_003.png

Create a Japanese course slide. Large title: `作成完了待ち`. Subtitle: `CREATE_COMPLETEを確認してから進む`. Visual: stack status timeline from `CREATE_IN_PROGRESS` to green `CREATE_COMPLETE`.

## slide_004.png

Create a Japanese course slide. Large title: `メール確認`. Subtitle: `Confirmしないと通知は届かない`. Visual: email inbox confirmation flow, status `PendingConfirmation` becomes `Confirmed`.

## slide_005.png

Create a Japanese course slide. Large title: `Smoke Test`. Subtitle: `Alarm、Topic、Subscriptionを確認する`. Visual: checklist with `Alarm exists`, `Topic exists`, `Subscription status`, plus small `smoke_test.sh`.

## slide_006.png

Create a Japanese course slide. Large title: `SNS Publish Test`. Subtitle: `まずTopicへ直接送って通り道を見る`. Visual: direct publish arrow to SNS Topic and Email, clearly bypassing Alarm.

## slide_007.png

Create a Japanese course slide. Large title: `Alarm State Test`. Subtitle: `CLIが使える場合だけ状態を手動で変える`. Visual: optional CLI flow `set-alarm-state ALARM` then `set-alarm-state OK`, connected to AlarmActions.

## slide_008.png

Create a Japanese course slide. Large title: `次に見るもの`. Subtitle: `更新、削除、届かない時の確認へ進む`. Visual: workflow `Create`, `Confirm`, `Test`, `Update`, `Delete`.
