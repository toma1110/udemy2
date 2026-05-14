# S1-L3 音声QAレポート

## Ticket

- Task ID: TASK-0019
- Owner AI: AI-QA-01
- Reviewer AI: AI-Ops-01
- 実施日: 2026-05-10
- 対象: `audio/s1-l3/slide_001.wav` から `slide_009.wav`

## Result

AI機械QA: Pass

人間の実耳スポット聴取: Pending

この環境では音声を実際に耳で聴いて自然さを判断できないため、実耳聴取完了とは扱わない。動画生成へ進めるための機械QAは通過とし、CEOスポット聴取ポイントを明記する。

## Checks

| Check | Result | Notes |
| --- | --- | --- |
| WAV count | Pass | 9 files / 9 slides |
| WAV decode | Pass | `ffmpeg -v error -i <wav> -f null -` が全件成功 |
| Format | Pass | PCM 16-bit mono 24000 Hz |
| Narration checker | Pass | `OK: 1 files checked` |
| Normalized alphabet leftovers | Pass | 全スライド `leftover_alpha=none` |
| Long silence | Pass | `silencedetect=n=-45dB:d=0.8` で検出なし |
| Volume | Pass | mean -26.4 dB to -25.3 dB、max -6.0 dB to -3.2 dB |
| Known risky expressions | Pass | ナレーション本文に `触れる`、`そうした方`、文脈依存の `上で` はなし |

## Reading Risk Review

対象語:

- `SLO`: 台本上は `エスエルオー`
- `SLI`: 台本上は `エスエルアイ`
- `SLA`: 台本上は `エスエルエー`
- `AWS`: 台本上は `エーダブリューエス`
- `CloudWatch`: 台本上は `クラウドウォッチ`
- `Application Signals`: 台本上は `アプリケーションシグナル`
- `CloudFormation`: 台本上は `クラウドフォーメーション`

文脈依存語:

- `触れる`: ナレーション本文では未使用
- `方`: ナレーション本文では `考えかた`、`見せかた` に置換済み
- `上で`: ナレーション本文では未使用
- `右上`: ナレーション本文では未使用
- `値`: ナレーション本文では未使用

## CEO Spot Listening Points

最低限、次を確認する。

| Slide | 確認ポイント |
| --- | --- |
| 1 | `エスエルオー導入`、`エーダブリューエスで計測` が自然か |
| 2 | `エスエルアイ`、`エスエルオー`、`エスエルエー` の区別が聞き取れるか |
| 3 | `シーピーユー使用率`、`レイテンシ`、`エラー率` が不自然でないか |
| 4 | `アプリケーションシグナル`、`30日データ` が聞き取りやすいか |
| 5 | `クラウドフォーメーション`、`アラーム`、`ダッシュボード` が自然か |
| 6 | `エラーバジェット`、`バーンレート` が自然か |
| 7 | `見せかた` が `みせかた` として自然か |
| 8 | `ピーエム`、`週次や月次` が自然か |
| 9 | `一続き`、`次のセクション` で文末切れがないか |

## Decision

動画生成工程へ進める。ただし、音声の最終承認はCEOのスポット聴取後に行う。
