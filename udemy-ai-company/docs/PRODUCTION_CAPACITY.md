# PRODUCTION_CAPACITY

動画制作を「どれだけ速く、どれだけ並列に、どれだけ安定して」進めるかを決める運用基準です。

対象は AWS/SRE Udemy 講座の制作パイプラインです。GPT-Image2でスライドPNGを作り、VOICEVOXで音声を作り、ffmpegでMP4を組み立て、Google Driveへアップロードする前提です。

## 結論

現在の小型ホストでは、CPUを使う工程は原則1本だけ実行します。

- 安全な同時実行: `VOICEVOX 1本` または `ffmpeg 1本`
- 避ける同時実行: `VOICEVOX + ffmpeg`、`ffmpeg複数講義`、`decode check複数本`
- 並列化しやすい作業: 台本作成、レビュー、Issue整備、スライドプロンプト作成、Google Driveアップロード待ちの記録
- まず測るべき指標: 1講義ごとの stage elapsed time、失敗率、retry回数、最大CPU、最大RSS、swap発生有無

2026-05-10 の read-only スナップショットでは、ホストは `2 vCPU / 約1.9GiB RAM`、swap使用あり、VOICEVOX Engine常駐、ディスク使用率約78%でした。CPUネックは十分あり得ますが、安定性の主リスクは「CPU飽和 + メモリ不足 + swap」の組み合わせです。

## 工程別の性質

| 工程 | 主な制約 | 現行ホストでの並列度 | 備考 |
| --- | --- | ---: | --- |
| 企画、台本、レビュー | 人間判断、LLM | 複数可 | ローカルCPU負荷は軽い |
| GPT-Image2スライド生成 | API、品質確認 | 2から3講義相当まで | API制限と品質レビュー待ちを優先 |
| 画像整形、contact sheet | CPU、I/O | 1から2本 | ffmpeg実行中は控える |
| VOICEVOX音声生成 | CPU、メモリ | 1本 | 2 vCPUでは単独実行を標準にする |
| ffmpegセグメント生成 | CPU、I/O | 1講義 | `-nostdin` 必須。セグメント単位で検証する |
| ffprobe、decode check | CPU、I/O | 1本 | 本番encodeと同時に走らせない |
| Google Driveアップロード | ネットワーク、API | 1本 | ローカルCPU負荷は軽いが記録の混線を避ける |

## 現行ホストの実行基準

以下を満たすときだけ、新しいCPU系ジョブを開始します。

- `ffmpeg` が走っていない
- VOICEVOX音声生成ジョブが走っていない
- 1分load averageがCPU数未満
- available memoryが700MiB以上
- swap-in / swap-outが継続していない
- ディスク使用率が85%未満

以下のいずれかに該当する場合は、新しいCPU系ジョブを開始しません。

- load averageがCPU数以上
- available memoryが500MiB未満
- swap使用量が増加し続けている
- ディスク使用率が85%以上
- decode check中
- Google Driveアップロードの成否確認中で、同じ講義の成果物を更新しようとしている

## 推奨並列キュー

小型ホストでは、工程ごとにロックを分けます。

| ロック | 対象工程 | 同時実行数 |
| --- | --- | ---: |
| `voicevox.lock` | VOICEVOX音声生成 | 1 |
| `ffmpeg.lock` | segment生成、concat、faststart、decode check | 1 |
| `drive_upload.lock` | Google Driveアップロード | 1 |
| `course_asset.lock` | 同じ講義ディレクトリへの書き込み | 1 |

ロックは「同じ講義の成果物が混ざらない」ためのものです。待機中のIssueは `blocked` ではなく `ready` とし、AI-Ops-01が順番を管理します。

## 速度計測

各チケットのQAレポートには、必ず以下を記録します。

- stage name
- start time
- end time
- elapsed seconds
- input slide count
- input audio count
- output duration seconds
- output file size
- command summary
- max RSS
- user CPU time
- system CPU time
- exit code
- retry count

CPU系コマンドは、可能なら `/usr/bin/time -v` で包んで記録します。

```bash
/usr/bin/time -v ffmpeg -nostdin ...
```

既存の動画レポートには完成動画のdurationとdecode結果はありますが、ビルドにかかった実時間は不足しています。今後は「動画尺」ではなく「生成にかかった実時間」を必ず残します。

## 安定化ルール

ffmpegは以下を標準にします。

- すべてのffmpegコマンドに `-nostdin` を付ける
- セグメント単位で生成し、各セグメントを検証する
- 一時ファイルに出力し、検証後に完成名へ移動する
- concat後にfaststartを付与する
- 最終MP4はffprobeとdecode checkで検証する
- 破損ファイルは上書き再生成前に原因をQAレポートへ記録する

VOICEVOXは以下を標準にします。

- Engine起動確認後に生成する
- 同時に複数講義の音声を生成しない
- 用語チェックを音声生成前に通す
- 生成済みWAVの数、duration、ファイルサイズを記録する

## スケール方針

| 環境 | 推奨運用 |
| --- | --- |
| 2 vCPU / 2GiB RAM | CPU系ジョブは1本。最安定だが並列度は低い |
| 4 vCPU / 8GiB RAM | VOICEVOX 1本 + 軽いレビュー作業、またはffmpeg 1本。実測後にsegment 2並列を検討 |
| 8 vCPU / 16GiB RAM | 2講義相当のCPU系ジョブを検討可能。ただし同一講義の成果物書き込みは直列 |
| 専用制作ホスト | CPU系ジョブをキュー化し、AI-Ops-01が開始条件を自動判定する |

まずはホストを大きくするより、計測を揃えます。elapsed timeと失敗率が取れない状態で並列度だけ上げると、速くなる代わりに再実行とQA手戻りが増えます。

## AWS Batch on Fargate

重い動画生成処理の逃がし先として、`infrastructure/batch-fargate/` を標準基盤にします。

- AWS Batch job未実行時はFargateのvCPU/RAM compute料金を発生させない
- NAT Gatewayを作らない
- ECS Serviceを常駐させない
- S3に素材とmanifestを置く
- Batch jobがS3からPNG/WAVを取得し、ffmpegでMP4とQAレポートを生成する
- 生成物はS3へ戻し、AI-QA-01がレビューする

MVPではVOICEVOX生成済みWAVを入力にします。VOICEVOX自体をFargate workerへ同梱するかは、image size、cold start、音声生成時間を実測してから判断します。

## AI社員の責任分界

- AI-Ops-01: キュー、ロック、Blocked検知、容量診断、Driveアップロード順序
- AI-Production-01: スライド、音声、動画生成
- AI-QA-01: レポート確認、decode check確認、成果物整合性レビュー
- AI-Strategy-01: 講座優先度、制作順序、スケール投資判断

AI-Production-01は自分の動画生成結果を承認してはいけません。容量診断も、最終判断はAI-QA-01またはAI-Ops-01が確認します。

## CEO判断が必要な基準

次のどれかが発生したら、AI-Ops-01はCEO判断Issueを作ります。

- 1講義の動画生成が3回以上失敗する
- ディスク使用率が90%を超える
- swap使用量が1.5GiBを超える
- 1講義あたりの実生成時間が動画尺の3倍を超える
- Google Driveアップロード後の取り違え、重複、URL不一致が発生する
- 並列度を上げるためにインスタンス増強または制作ホスト分離が必要になる

## 診断コマンド

read-only診断は以下で実行します。

```bash
./tools/production_capacity_check.sh
```

このスクリプトはプロセスを停止せず、CPU、メモリ、swap、ディスク、ffmpeg、VOICEVOXの状態だけを表示します。
