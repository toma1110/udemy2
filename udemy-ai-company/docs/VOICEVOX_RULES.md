# VOICEVOX_RULES

## 目的

VOICEVOXでAWS/SRE講座のナレーションを自然に読み上げるための品質ルールです。

`/home/ubuntu/workspace/udemy` の既存ノウハウを反映し、誤読、不自然な間、カッコふりがなの重複読み、英字残存を音声生成前に潰します。

## 基本方針

- できるだけ書く時点で読み上げやすい表記にする
- 読む時の置換テーブルは安全網として扱う
- 音声生成前に `tools/narration_checker.py` を実行する
- VOICEVOX未起動のまま本番音声を生成しない
- gTTSなど別音声へのフォールバックを本番成果物に使わない
- 修正後は可能な限りWAVを聴取確認する

## 書く時ルール

### 英字を残さない

ナレーション本文には英単語を残さず、読み上げ用のカタカナまたは日本語にします。

例:

| 避ける | 推奨 |
| --- | --- |
| AWS CLI | エーダブリューエスシーエルアイ |
| CloudFormation | クラウドフォーメーション |
| CloudWatch Alarm | クラウドウォッチアラーム |
| SNS Topic | エスエヌエストピック |
| Dashboard | ダッシュボード |
| API | エーピーアイ |
| SLO | エスエルオー |
| SLI | エスエルアイ |
| SLA | エスエルエー |
| Application Signals | アプリケーションシグナル |
| error budget | エラーバジェット |
| burn rate | バーンレート |

### サービス名の空白を音声に残さない

VOICEVOXは英語サービス名のスペースで不自然な間を作りやすいです。

| 避ける | 推奨 |
| --- | --- |
| CloudWatch Agent | クラウドウォッチエージェント |
| CloudWatch Logs | クラウドウォッチログス |
| CloudWatch Metrics | クラウドウォッチメトリクス |
| Logs Insights | ログスインサイツ |
| AWS Budgets | エーダブリューエスバジェッツ |
| Cost Anomaly Detection | コストアノマリーディテクション |
| Simple Notification Service | シンプルノティフィケーションサービス |
| Application Signals | アプリケーションシグナル |
| Service Level Objective | サービスレベルオブジェクティブ |
| Service Level Indicator | サービスレベルインディケーター |
| Service Level Agreement | サービスレベルアグリーメント |

### STEP番号の空白を詰める

| 避ける | 推奨 |
| --- | --- |
| STEP 5 | ステップ5 |
| Step 5 | ステップ5 |
| ステップ 5 | ステップ5 |

### 誤読しやすい和語を直す

| 避ける | 推奨 |
| --- | --- |
| 閾値 | しきいち |
| 重大度 | じゅうだいど |
| 根本原因 | こんぽんげんいん |
| 発報 | はっぽう |
| 一気貫通 | いっきかんつう |
| 右上 | みぎうえ |
| 上で | うえで |
| 値を、値が、値に | あたいを、あたいが、あたいに |

`値` は `数値`、`目標値`、`閾値` など他の語に含まれるため、無条件に置換しません。助詞に続く単独の `値` だけを優先して直します。

### カッコふりがなを使わない

VOICEVOXは `Blameless（ブレームレス）` のような表記を両方読みます。

| 避ける | 推奨 |
| --- | --- |
| Blameless（ブレームレス） | ブレームレス |
| CloudFormation（クラウドフォーメーション） | クラウドフォーメーション |

### 伏字記号を使わない

`〇〇`、`××`、`＊＊` は読み上げが不自然になります。

| 避ける | 推奨 |
| --- | --- |
| 〇〇さん | ある運用担当者 |
| ××チーム | とあるチーム |

### 数値と英単位を読み下す

| 避ける | 推奨 |
| --- | --- |
| 500ms | 500ミリ秒 |
| 100GB | 100ギガバイト |
| 5xx | 5系のエラー |
| 4xx | 4系のエラー |
| t3.micro | ティー3ドットマイクロ |

### SLO講座の標準読み

SLO講座では以下を統一します。

| 表記 | 読み |
| --- | --- |
| SLO | エスエルオー |
| SLI | エスエルアイ |
| SLA | エスエルエー |
| error budget | エラーバジェット |
| burn rate | バーンレート |
| request-based SLO | リクエストベースドエスエルオー |
| period-based SLO | ピリオドベースドエスエルオー |
| SLO Recommendations | エスエルオーレコメンデーション |
| SLO Performance Report | エスエルオーパフォーマンスレポート |

### 長文を避ける

1文が長いと息継ぎが不自然になります。

- 1文は80文字以内を目安にする
- 30〜50文字ごとに読点か句点を入れる
- 箇条書き調の読み上げは句点で区切る

## 読む時テーブルの考え方

音声生成処理を実装する場合は、以下の順で正規化します。

1. 日本語の誤読補正
2. 英語・コマンド・サービス名のカタカナ化
3. 正規化後に英字が残っていないか確認

英語からカタカナへの置換テーブルは、長い語を先に置きます。

例:

```text
Cost Anomaly Detection
CloudWatch Alarm
CloudWatch
AWS CLI
AWS
```

短い語を先に置くと、長いサービス名が部分置換で崩れます。

## 音声生成前チェック

ナレーションを保存したら、音声生成前にチェックします。

```bash
python3 tools/narration_checker.py courses/sample-aws-sre-course
```

特定の `script.json` だけ確認する場合:

```bash
python3 tools/narration_checker.py courses/sample-aws-sre-course/scripts/lesson_001_script.json
```

Markdown台本も確認できます。

```bash
python3 tools/narration_checker.py courses/sample-aws-sre-course/scripts
```

警告を残したままQAへ進める場合は、Issueに理由を書きます。

## VOICEVOX起動確認

本番音声の生成前にVOICEVOX Engineを確認します。

```bash
curl -s http://localhost:50021/version
```

起動していない場合:

```bash
/opt/voicevox_engine/linux-cpu-x64/run --host 0.0.0.0 --port 50021
```

標準設定:

- URL: `http://localhost:50021`
- speaker_id: `3`
- 話速: `1.1`
- audio sample rate: `44100`

## QA観点

- 英字が残っていない
- サービス名の空白が不自然な間にならない
- `ステップ 5` のような空白がない
- カッコふりがながない
- `閾値`、`重大度`、`根本原因`、`発報` が修正されている
- `500ms`、`100GB`、`5xx` のような表記が読み下されている
- 長すぎる文がない
- WAVを聴いて違和感がない
