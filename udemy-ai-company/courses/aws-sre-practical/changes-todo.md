# 動画変更点まとめ（aws-sre-practical）

最終更新: 2026-05-08（高優先修正の公開反映と追加監査）

`courses/aws-sre-practical/memo.md`（動画レビューメモ）と、ハンズオン公開リポジトリ
`/home/ubuntu/workspace/publicRepo/aws-sre-cfn-templates`（最近の修正コミット群）を突き合わせて
反映が必要な変更点を整理したもの。

> 本ドキュメントは下記2ファイルを統合したもの。元ファイルは履歴として `/home/ubuntu/workspace/old/` に退避推奨。
> - `/home/ubuntu/workspace/modification_impact_analysis.md`（2026-05-04 時点の CFN 修正8項目）
> - `/home/ubuntu/workspace/sre-course-validation-results.md`（2026-05-04 時点のテンプレ06本デプロイ検証）

---

## A. ハンズオン公開リポジトリの変更点を動画へ反映

公開リポジトリ側はハンズオン検証で多数修正済。動画／script.json が古いままなので、再生成または
ナレーション修正が必要なものをレクチャー単位でまとめる。

### A-0. アプリケーション本体の差し替え（2026-05-06 追加・最重要）

**変更内容**: ハンズオンで使うサンプルアプリを **TODO アプリ → 確率で 5xx を返す単純なスタブアプリ** に差し替え。
**実装場所**: `aws-sre-cfn-templates/cloudformation/01-base-infrastructure.yaml` の **UserData に Flask アプリを直接埋め込み**（`sre-todo-app` GitHub リポは実質未使用に格下げ）。

**新アプリの仕様**（UserData 内に確定済み）:
| エンドポイント | 仕様 |
|---|---|
| `GET /` | 常に 200。10–50ms の擬似処理 |
| `GET /api/data` | **20% の確率で 500**。50–200ms の擬似処理 |
| `GET /api/process` | **15% の確率で 500**。10% の確率で 500–1000ms の遅延、それ以外は 100–500ms |
- ログは **JSON 形式**（`requestId`、`status`、`duration` 等）。出力先 `/var/log/todo-app.log`
- **X-Ray middleware** で全リクエストをトレース（CW Agent の `traces` セクション経由で送信）
- ポート **8080** / Flask 3.0 / `aws-xray-sdk` 2.12
- DB 接続なし（RDS は CFN 上に残っているが**新アプリからは未使用**）

**狙い**: CloudWatch ダッシュボードで **エラー率の変化が一目で分かる** ようにする（TODO アプリだと意図的にエラーを起こさないと 5xx が出ず、ダッシュボード/アラーム/SLI の体感が湧きにくかった）。

| レクチャー | 影響 | 必要対応 | 優先度 |
|---|---|---|---|
| **s2-l5** | アプリ名・性質・デプロイ手順が全面的に変わる。**git clone / pip / 環境変数設定が一切不要**になる | ナレ・スライドを「TODO アプリをデプロイ」→「**確率で 5xx を返すデモアプリ（CFN UserData で自動生成）**」に書き換え。STEP 2 の git clone 手順を**丸ごと削除**。3エンドポイント仕様（`/`、`/api/data`、`/api/process`）と確率値も明記 | 🔴 致命 |
| **s2-l5（CFN）** | RDS は **CFN に残す方針**（決定済 2026-05-06）。新アプリは未使用だが教材構成として保持 | CFN 側の変更は不要。動画では「RDS は後続セクション/拡張用に作成しているが、今回のスタブアプリ自体は DB を使わない」と一言補足 | 🟢 低 |
| **s2-l5** | アーキテクチャ図に RDS あり／ナレ「RDS MySQL にデータを保存」が新アプリの挙動と不一致 | 構成図に RDS は残しつつ、ナレを「RDS は後続セクション用に用意。今回のデモアプリは DB 未使用で確率的にエラーを返す」へ修正 | 🟡 中 |
| **s2-l5** | 動作確認が「TODO の追加・削除」から「**エラー率の体感**」に変わる | チェックリストを更新: `curl /api/data` を連打して 5xx が ~20% 出ること、X-Ray サービスマップ、CW Logs に JSON ログ | 🟡 中 |
| **s3-l4** ダッシュボード | 5xx エラー率ウィジェットが**主役**に格上げできる | 「エラー率ウィジェットの動き」を主軸にナレ書き換え。「`/api/data` を叩くと 20% で 500 が出る」体験で説明 | 🔴 高 |
| **s4-l4** Logs Insights | エラーログ（JSON 形式・`requestId`/`status`/`duration` 付き）の検索が分かりやすくなる | クエリ例を新ログスキーマに更新（`status >= 500` の集計、`duration` のパーセンタイル、`requestId` でのトレース突合せ） | 🟡 中 |
| **s4-l5** メトリクスフィルター | フィルター発火の挙動確認がやりやすい | `{ $.status >= 500 }` 等の JSON フィルターパターン例を新ログスキーマで記述 | 🟡 中 |
| **s5-l5** アラーム | 5xx 率アラームの体感確認が容易 | 「`ab` や `curl` ループで `/api/data` を叩く → アラーム発火 → Slack 通知」のデモ手順を追記。`set-alarm-state` 強制発火と並べて2通り示せる | 🟡 中 |
| **s6-l4** SLI/SLO | 可用性 SLI（成功率）と p99 レイテンシの計測が分かりやすい | 確率設定（20% エラー）= SLO 違反のシナリオに直結。SLO ドキュメントテンプレに「20% エラーが 28日 続いたらバジェット枯渇」例を入れられる | 🟡 中 |
| **s7-l4** インシデント対応 | `stress-ng` での CPU 負荷に加え、**`/api/data` を叩いて 5xx を増やす**模擬障害が可能 | 「エラー率上昇シナリオ」を追加して CPU 負荷とセットで説明 | 🟡 中 |
| **公開リポ** `sre-todo-app` | **そのまま残す方針**（決定済 2026-05-06）。実質未使用だがリポ整理・改名は行わない | 動画・CLI_COMMANDS.md からの参照を消すか、「CFN を使わない場合の手動セットアップ用」と位置づけて残すかは別途判断 | 🟢 低 |

**判断済み事項（2026-05-06）**:
- RDS は CFN にそのまま残す（簡素化なし）
- `sre-todo-app` GitHub リポはそのまま残す（改名・アーカイブなし）
- 負荷生成スクリプトの追加は不要

→ **s2-l5 は動画生成・公開まで完了済み**。残る対応は s3-l4 のダッシュボード主役化や s4 系クエリ更新など、後続レクチャー側の反映確認。

---

### A-1. 2026-05-04 時点の構造的修正（旧 `modification_impact_analysis.md` 由来）

| 影響範囲 | 公開リポジトリ側の変更 | 動画側の現状 / 必要対応 | 優先度 |
|---|---|---|---|
| **s2-l5** | アプリ起動ポートを **5000 → 8080** に変更 | ナレ「Running on http://0.0.0.0:**5000**」が古い → **8080 へ修正**、ALB→EC2 のポート説明・curl 例も全て差し替え | 🔴 致命 |
| **s2-l5 / s4 系** | ロググループ名を **`/aws/ec2/sre-handson/webapp`** に統一 | s2-l5: `/sre-handson/app`、s4-l1/l4/l5 でも旧名の可能性 → **新ロググループ名に全置換**（スライド・ナレ・CLI 例） | 🔴 致命 |
| **s2-l5** | **X-Ray daemon を廃止**し、**CloudWatch Agent の `traces` セクション**でトレース送信 | STEP 5 の「X-Ray デーモン起動 (`systemctl start xray`)」を削除、「CW Agent の traces 設定で送る」へ書き換え | 🔴 致命 |
| **s2-l5** | 01-base 実行で TODO アプリ・CW Agent・X-Ray が **自動セットアップ** される構成 | 現動画は STEP 2〜5 で git clone / pip / CW Agent ウィザード / X-Ray SDK 追加を **手動** で実施 → **CFN 一発デプロイ完了型** に再構成、確認手順だけ残す | 🔴 致命 |
| **s2-l5** | DB 名 **`sreapp`** を明記 | env 設定で `DB_NAME` 言及があれば `sreapp` に統一 | 🟢 低 |
| **s2-l5** | アプリログを **JSON 形式** に変更＋意図的なエラー発生機能追加 | ログ形式に触れていない → STEP 4 で「JSON 形式で `/aws/ec2/sre-handson/webapp` に届く」旨を追記 | 🟡 中 |
| **s2-l5** | EC2 IAM ロールに `AWSXRayDaemonWriteAccess` / `AWSXRayReadOnlyAccess` を付与 | CFN 側で完結。動画では「IAM ロールに X-Ray 書き込み・読み取り権限が含まれる」と一言触れる | 🟢 低 |
| **s2-l5** | テンプレート名統一: `sre-handson-base.yml` → **`01-base-infrastructure.yaml`**（旧名は symlink 残） | 「sre-handson-base.yml をアップロード」を **新ファイル名に変更**（symlink で互換取れる旨は補足可） | 🟡 中 |
| **s3-l1 / s7-l4 等** | CW Agent ステータス確認コマンド `-a query` → **`-a status`** | 動画/スライドに `-a query` が出ていれば **`-a status` に修正** | 🟡 中 |

### A-2. 2026-05-04 以降の追加修正（最新コミット群）

| 影響範囲 | 公開リポジトリ側の変更（コミット） | 動画側の現状 / 必要対応 | 優先度 |
|---|---|---|---|
| **s3 系**（カスタムメトリクス） | `03-custom-metrics.yaml` は **Lambda をオプション化**。CLI / boto3 を主とする | Lambda を主にしているなら順序を入れ替え | 🟡 中 |
| **s3 系**（ディスク） | デバイス名 `xvda1` → **`nvme0n1p1`**（モダンEC2向け） | CW Agent / ダッシュボードの説明で旧名を使っていれば差し替え | 🟡 中 |
| **s4-l4**（Logs Insights） | クエリ構文修正（`count_if` 不可 → **`case`** 文）／フィールド拡充／クエリ集追加 | 動画内クエリが古い構文ならスライド差し替え＋ナレ更新 | 🔴 高 |
| **s4 系** | `04-log-metric-filter` を **既存ロググループ参照** に修正 | 「新規ロググループ作成」前提なら文言修正 | 🟡 中 |
| **s5 系** | アラーム名統一: `sre-handson-high-cpu` → **`sre-handson-cpu-high`** | スライド/ナレ/CLI に旧名があれば差し替え | 🟡 中 |
| **s5 系** | ALB 5xx エラー率を **math expression（割合％）** で表現 | 件数で説明している箇所は％換算に統一 | 🟡 中 |
| **s7-l4** | Amazon Linux **2023** 化。`stress` → `stress-ng`（`dnf install`）、`cd ~` 後実行、`killall stress-ng`、`netstat`→`ss`、`/var/log/messages`→`journalctl` | **memo.md の指摘とも合致**。動画は AL2 前提（`amazon-linux-extras install epel`）→ AL2023 仕様に**スライド・コマンド全面書き換え** | 🔴 高 |
| **s9-l4** | `06-cost-alerts.yaml` を **JPY → USD**、Anomaly Subscription を **EMAIL 直送**、しきい値シンプル化 | スライド/ナレで JPY ベースなら USD に。SNS 経由前提の説明は「EMAIL 直送が標準・SNS は拡張」に整理 | 🟡 中 |

> 共通: 動画スライド内でコマンドを短縮表示している箇所は、`udemy/courses/aws-sre-practical/CLI_COMMANDS.md`
> （または公開リポ `aws-sre-cfn-templates/CLI_COMMANDS.md`）への誘導文を必ず添える運用に統一。

---

## B. 動画レビューメモ（`memo.md`）からの修正点

### B-1. ナレーション読み方ルール（横断課題）

- **状態**: 読み方ルールは `skills/narration-writing/SKILL.md` にスキル化済。各 `script.json` への一括反映は未対応。
- **代表的な誤読例**（memo.md より）:
  - `今リリース` → こんりりーす / `上で` → じょうで / `引いた値` → ひいたね
  - `500ms` → ごひゃくむす / `5xx` → ごくす / `重大度` → じゅうたいど
  - `dmesg` → どめすぐ / `一気貫通` → いっきとおりぬき / `killall` → きらる
  - `〇〇さんのミス` → ぜろぜろさんのみす / `Blameless（ブレームレス）` → ぶれーむれす×2
  - `根本原因` → ねもとげんいん / `発報` → はつむくい / `右上` → みぎじょう
  - `Cost Anomaly Detection` → 単語間が空きすぎ → カタカナで連結
- **次のステップ候補**:
  1. `src/voice_generator.py` の `_EN_TO_KANA` / `_JP_READING_FIXES` テーブルを SKILL.md の候補で拡張 → VOICEVOX で聴取確認
  2. `src/script_generator.py` 改修: 新規生成時に `templates/prompts/narration_system.md` を併読
  3. 既存 `script.json` の一括レビュー: 違反検出のドライランレポートをまず出力
- **対応優先度**: **🔴 高**（全レクチャー横断のため、新規生成・既存両方をカバーする仕組みで一気に解決したい）

### B-2. レクチャー別 指摘リスト

| レクチャー | 指摘内容 | 対応案 | 優先度 |
|---|---|---|---|
| **s0-l4** | 「課金アラートは必ず設定する」のナレあり。s9-l4 から「セクション0で予告したBilling Alert」と逆参照されている → s9-l4 から Billing Alert を**削除する場合は s0-l4 の文言も整合修正**が必要 | s0-l4 のナレを「**Budgets で月次予算アラートを設定する**」へ書き換え。Billing Alert という語を使わない | 🔴 高 |
| **s5-l5** | ナレ末尾「次のレクチャーでは複数アラームをまとめる**複合アラーム**を学んでいきましょう」と言っているが、複合アラーム回が存在しない（s6 は SLO に進む） | **複合アラーム回は追加しない方針**（決定済 2026-05-06）。ナレを「次のセクションでは SLI/SLO とエラーバジェットを学んでいきましょう」へ修正＋スライドの「次のレクチャー」予告も連動修正 | 🔴 高（カリキュラム矛盾） |
| **s6-l1** `slides/slide_010.png` | 表のレイアウトが崩れている | スライド再生成（GPT Image 2 で再描画 or HTML テンプレ→PNG） | 🟡 中 |
| **s6-l2** `slides/slide_007.png` | 表のレイアウトが崩れている | 同上 | 🟡 中 |
| **s6-l4** | ナレ「SLOドキュメント**配布している**」と言っているが、配布物が公開リポジトリに無い | `publicRepo/aws-sre-cfn-templates/slo-document-template.md` を新規作成し公開（または該当ナレの修正） | 🔴 高 |
| **s6-l4** `slides/slide_009.png` | 図がつぶれている | スライド再生成 | 🟡 中 |
| **s6-l4 提案** | SLOダッシュボード作成用 CFN テンプレが望ましい | `publicRepo/aws-sre-cfn-templates/cloudformation/07-slo-dashboard.yaml` を追加検討（ALB の可用性 / p99 を Metric Math で可視化） | 🟢 中（追加施策） |
| **s7-l4** | Amazon Linux **2** 前提の手順（`amazon-linux-extras install epel` / `stress`）。AL2023 想定外 | スライド・ナレを AL2023 仕様（`dnf install stress-ng`、`cd ~`、`stress-ng --cpu 4 --timeout 600`、`killall stress-ng`）に置き換え。ハンズオン側 `CLI_COMMANDS.md` を正と扱い、動画では「正確なコマンドはリポジトリ参照」を明記 | 🔴 高（コピペで動かない） |
| **s8-l2** | ナレ「コピーしてそのまま使えるポストモーテムテンプレート」と言っているが、公開リポジトリに該当 MD が無い | `publicRepo/aws-sre-cfn-templates/postmortem-template.md` を新規追加。Udemy リソースでもリンクを既に追加済とのこと | 🔴 高 |
| **s9-l3** | ナレ「**未割り当ての** Elastic IP は月額課金」と言っているが、**EIP は割り当て済みでも課金対象**に AWS 側仕様が変わっている可能性あり | AWS 公式ドキュメント／MCP（`aws-knowledge` / `aws-documentation`）で最新仕様を確認 → 該当ナレ・スライドを最新仕様に修正 | 🔴 高（誤情報リスク） |
| **s9-l4** | Billing Alert（無料枠アラート）は Budgets で完全に代替可能。CFN テンプレ `06-cost-alerts.yaml` も Budgets のみで Billing Alert 未実装 | **動画から Billing Alert 部分を削除**。手順③（Billing Alert + CloudWatch Alarm）スライド・ナレを丸ごと削除し、Budgets + Cost Anomaly Detection の2本立てに再構成。「セクション0で予告した Billing Alert を実装」のナレも削除 | 🔴 高 |
| **s10-l1** | ナレ「このチェックリストは**PDF でもダウンロードできる**ようにしています」が、PDF を用意していない | (a) PDF を生成・公開してリンクを Udemy リソースに追加／ (b) 該当ナレを「Markdown で公開しています」等に修正 | 🟡 中 |

---

## C. アクションアイテム（推奨着手順）

### 進捗（2026-05-08 更新）

**🟢 完了済み（動画生成・公開）**（2026-05-08 反映）
- s2-l5: 新スタブアプリ前提・GPT Image 2 スライド・読み方修正版の動画を生成し、公開済み
  - ローカル確認: `s2-l5/output.mp4`（26,655,640 bytes、2026-05-07 20:18 UTC）
  - 生成元控え: `s2-l5/output_variants/s2-l5-gpt-image2-narrationcheck-20260507.mp4`
  - Drive: `https://drive.google.com/file/d/1WDRWGUklQ3x9ubYjhGnFb4DvFiWh-hqD/view?usp=drivesdk`
- s0-l4: Budgets 前提・読み方修正版の動画を生成し、公開済み
  - ローカル確認: `s0-l4/output.mp4`（19,060,889 bytes、2026-05-07 21:53 UTC）
  - 生成元控え: `s0-l4/output_variants/s0-l4-gpt-image2-narrationcheck-20260507.mp4`
  - Drive: `https://drive.google.com/file/d/1AJKKST2ZIa7bXzY1gzQrpqtOXUKAgajn/view?usp=drivesdk`
- s5-l5: Slack通知ハンズオン修正版を GPT Image 2 スライド・読み方修正済み音声で再生成し、Drive公開済み
  - ローカル確認: `s5-l5/output.mp4`（16,196,480 bytes、2026-05-08 06:18 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1uWdblinDRv6o8DryL8xncwZl1mvvImsp/view?usp=drivesdk`
- s9-l3: コスト削減手法回を GPT Image 2 スライド・最新仕様ナレで再生成し、Drive公開済み
  - ローカル確認: `s9-l3/output.mp4`（19,703,230 bytes、2026-05-08 09:32 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1IRUWwBKjgu5-EYr4ioyuf7zO1eNnoAn9/view?usp=drivesdk`
- s9-l4: コストアラート設定回を GPT Image 2 スライド・修正版音声で再生成し、Drive公開済み
  - ローカル確認: `s9-l4/output.mp4`（28,011,069 bytes、2026-05-08 12:42 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1ZGsFj6h64pcIlmOZkGKIKx-4WOA4HUUE/view?usp=drivesdk`
- s4-l4: Logs Insights クエリ修正版・GPT Image 2 スライドで再生成し、Drive公開済み
  - ローカル確認: `s4-l4/output.mp4`（20,439,074 bytes、2026-05-08 19:09 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1fC0hq_tUTYHXb5Q6CxP6xQD4cfGE7bVU/view?usp=drivesdk`
- s6-l4: SLO 設計回を GPT Image 2 スライドで再生成し、Drive公開済み
  - ローカル確認: `s6-l4/output.mp4`（17,320,701 bytes、2026-05-08 17:01 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1iEIUR51S4LtpLuKl9cUXyXZY3ScT8IOC/view?usp=drivesdk`
- s7-l4: 模擬インシデント対応演習を GPT Image 2 スライドで再生成し、Drive公開済み
  - ローカル確認: `s7-l4/output.mp4`（34,586,012 bytes、2026-05-08 11:17 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/1SNssVmi2C_b6ZuZUakUXU33xnE0KIFqC/view?usp=drivesdk`
- s10-l1: コース総整理回を GPT Image 2 スライド・修正版音声で再生成し、Drive公開済み
  - ローカル確認: `s10-l1/output.mp4`（20,374,872 bytes、2026-05-08 07:52 UTC、faststart済み）
  - Drive: `https://drive.google.com/file/d/11vR2Ekp7RAKPL0i0LRyG_o4fFk-OGiMA/view?usp=drivesdk`

**🟢 追加配布（2026-05-08）**
- s0-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1E9Mp2YibGrqrVuLq39mOVz9GcO5dBTDl/view?usp=drivesdk`
- s0-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1Yo6RjVh6DdlFlpnCUGUpMwmNi9ljeAPO/view?usp=drivesdk`
- s0-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1Kw4pI27AIWX1X4UgwRB7jmWAjATT0YRL/view?usp=drivesdk`
- s1-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1MiHxgK0WsmHjN8mgDd7fJsJP6Qdm_62v/view?usp=drivesdk`
- s1-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1CeqimoqW-i89MBStuuYx2ptBQDHjF7Wu/view?usp=drivesdk`
- s1-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1SpUSMbBFa7YE7vCcIYyQ0W9gWu079t4w/view?usp=drivesdk`
- s1-l4: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1LnVK9NBmgKoKzOWej5AVZYvT1DSCtkSC/view?usp=drivesdk`
- s1-l5: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1mxx1vQQkvM5OGwiqY7bGBWelIRgBE394/view?usp=drivesdk`
- s2-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/12Br8zExdl0m0pN3n70OrrBnavl-08wbL/view?usp=drivesdk`
- s2-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1C1FEwE7IpFphQ3TaDx32WGd97S98b4IO/view?usp=drivesdk`
- s2-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1OIqyGEjsETkPTY3lGEwQQfjS73h7FSfu/view?usp=drivesdk`
- s2-l4: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1P82vm58zh58w76a4fFi5-HR35s5zCvAs/view?usp=drivesdk`
- s3-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1E9ml1LOnM6u9whrRZoXSm034Q-ZVTsqu/view?usp=drivesdk`
- s3-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1VSuTZVzGIuHCgTdOwNJ8BbLzIp9bRAtP/view?usp=drivesdk`
- s3-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1RPHxxeBiE7MlCn1XzZ4cficeXui_ujyt/view?usp=drivesdk`
- s3-l4: Drive公開済み
  - Drive: `https://drive.google.com/file/d/176X7NSnNagZQehTHS_BJgNXVsUsphvEf/view?usp=drivesdk`
- s3-l5: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1Cw7x9PV3h45naJ2XokDigAkkXkCwYNef/view?usp=drivesdk`
- s4-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1-F0nFzX32fKlEJEVMfWqXOby-rjNQVHU/view?usp=drivesdk`
- s4-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/123ratKe0mx-25ety6w36wSgP7nQ_E10f/view?usp=drivesdk`
- s4-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1TRP3yTeMDNUft97MSEKwfg8oT8VBU2ls/view?usp=drivesdk`
- s4-l5: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1nePJpcNUl3V8duQp520NALg3rZfuS_X_/view?usp=drivesdk`
- s5-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1vMgPupZ-SKLBW0OFNF2UKbNcrSm3YIpd/view?usp=drivesdk`
- s5-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1vc8vWlkZjyQzwS6E1OWfSy6nqJqfDcN0/view?usp=drivesdk`
- s5-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1PD_HPZ8a4bk0Xq_9eU6uMpLdC8ibvBJ8/view?usp=drivesdk`
- s5-l4: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1mf8gCJwpecquoAS1IUJSlXYk8EsiMuMz/view?usp=drivesdk`
- s6-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/19B-RUce4jCTybMu1ik6BjgkOXFu3hNwx/view?usp=drivesdk`
- s6-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1qjIVRhnONUDgnY6IsA0GOcoGPttCOzj_/view?usp=drivesdk`
- s6-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1ITwbTkDXUKkAMSzOX0NZvr1bx4xB-UPL/view?usp=drivesdk`
- s7-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1vRoVy_6Ln20oNTFV3h-EEBehHKe4_TzB/view?usp=drivesdk`
- s7-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1lMoDA9QoDScFzrYoPhg7LMbago1c_OZm/view?usp=drivesdk`
- s7-l3: GPT Image 2 でスライドを再構成し、空白読み対策を反映して動画再生成・Drive公開済み
  - Drive: `https://drive.google.com/file/d/1G5Cw_lQC6N1ZJr3ZdDlU3W_BaSXpXzWH/view?usp=drivesdk`
- s8-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1ahzmU8AhfEXguT55kdIpt2YOpS258tb9/view?usp=drivesdk`
- s8-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1ODp5u9HNj-rFyCKiUDKss3-TQpf7D53_/view?usp=drivesdk`
- s8-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/10kAjwP6ATG9MTZ5zosSxbQSp5XAH7eXi/view?usp=drivesdk`
- s9-l1: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1dR8AddRm_iWMR8sFpqjRJnwiET5n2z6R/view?usp=drivesdk`
- s9-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1E2s70k0m2Z_573gbmks3Cq_cELkyq72u/view?usp=drivesdk`
- s10-l2: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1l0tFtFrG1ZHUWoOgnufeX8SpyNammw_k/view?usp=drivesdk`
- s10-l3: Drive公開済み
  - Drive: `https://drive.google.com/file/d/1qfKjQVg0G6xcTpSbcYw4IuaYlA623EJg/view?usp=drivesdk`

**🟢 完了済み（script.json レベル）**
- s2-l5: 新アプリ前提・ポート 8080・ロググループ統一・X-Ray daemon 廃止・`-a status`・CFN 一発デプロイ前提・RDS 後続用に残す説明
- s5-l5: 末尾の「複合アラーム」予告を削除し「次セクションは SLI/SLO」へ修正
- s10-l1: 「PDF でダウンロード」→「Markdown で公開」に変更
- s9-l3: EIP 課金仕様を 2024年2月以降の最新仕様（割り当て状態問わず時間課金）に修正
- s9-l4: Billing Alert スライドを削除し、Budgets + Cost Anomaly Detection の2本立てに再構成
- s7-l4: Amazon Linux 2023 化に合わせて `stress-ng` 前提の演習に再構成
- s0-l4: 課金アラートを「AWS Budgets で予算アラート」と明示、s9 への前振りを更新
- s7-l4: Amazon Linux 2023 化（`stress` → `stress-ng`、`amazon-linux-extras` 削除、`dnf install`、`cd ~`、関連ナレ全箇所も修正）
- s7-l3: Session Manager の SSM Agent 説明を Amazon Linux 2023 前提に修正し、動画再生成・Drive公開済み
- s8-l3: ポストモーテム演習内の旧 `stress` / `stress --cpu 4` 表記を `stress-ng` 前提に修正し、動画再生成・Drive公開済み
- s9-l1: コスト管理の概念説明を `Billing Alert` から `AWS Budgets の予算アラート` に統一し、動画再生成・Drive公開済み

**🟢 完了済み（input.json レベル）**（2026-05-06 追加修正）
- s2-l5/input.json: TODOアプリ前提を新スタブアプリ前提に書き換え（key_points 全面差し替え + ポート8080・JSONログ・CFN自動セットアップ反映）
- s0-l4/input.json: `Billing Alertsの有効化` → `AWS Budgets で月次予算アラートを設定` に修正
- s9-l4/input.json: `Billing Alert の有効化 → CloudWatch Billing Alarm` を削除、notes を Budgets + Cost Anomaly Detection 構成に更新
- s7-l4/input.json: `stress` → `stress-ng`、`amazon-linux-extras / yum install stress` → `dnf install stress-ng -y` (AL2023) に修正

**🟢 完了済み（公開リポジトリ追加物）**
- `publicRepo/aws-sre-cfn-templates/postmortem-template.md`（s8-l2 で配布と言及済の MD）
- `publicRepo/aws-sre-cfn-templates/slo-document-template.md`（s6-l4 で配布と言及済の MD）

**🟡 残: アセット再生成（要 VOICEVOX 起動 / Codex Image rate limit 解除待ち）**
- 上記の script.json 修正済みレクチャーのうち、未公開分の slide PNG / audio WAV / output.mp4 を再生成
- 手順: `/opt/voicevox_engine/linux-cpu-x64/run --host 0.0.0.0 --port 50021 &` → `python -m src.pipeline --section N --lecture M`
- 音声のみ先行する場合: `voice_generator.generate_voice_for_lecture()` を直接呼ぶ（誤読チェック用途）
- 対象: なし
- 完了・公開済みのため対象外: s2-l5, s0-l4, s5-l5, s9-l3, s9-l4, s7-l4, s10-l1

**🟢 完了確認済み（A-2 として「未着手」と記録されていたが script.json 検査で実態は反映済）**（2026-05-06 検証）
- s3 系: ディスクデバイス名 `xvda1` → `nvme0n1p1`（旧名 `xvda1` は全 script.json に残存なし）
- s3-l5: カスタムメトリクス CLI/boto3 優先化（STEP1=boto3、STEP2=CloudShell CLI が主軸。Lambda は EMF 補足と IAM 権限の注意のみ）
- s4-l4: Logs Insights クエリ `count_if` → `case`（s4-l4/script.json:113 で `case(status >= 500, 1, 0)` 使用済み・否定文脈以外で count_if 言及なし）
- s5 系: アラーム名統一 `sre-handson-high-cpu` → `sre-handson-cpu-high`（旧名は全 script.json に残存なし）
- s5 系: ALB 5xx を math expression で割合（％）表示（s5-l5・s3-l4 共に `100 * 5xx / RequestCount` 使用済み）
- s2-l5/構成図ナレ: アプリ JSON ログ形式の言及（script.json:178「JSON形式のアプリログ」明記済み）

**🟢 残: 未着手なし**（実装側 A-2 残タスクは検証時点でゼロ）

**🟢 追加監査メモ（2026-05-09 完了）**
- s8-l3: ポストモーテム演習内の旧 `stress` / `stress --cpu 4` 表記を `stress-ng` 前提に修正し、スライド・音声・動画を再生成して Drive へ公開済み。
- s9-l1: コスト管理の概念説明にあった `Billing Alert` 表記を `AWS Budgets の予算アラート` へ統一し、スライド・音声・動画を再生成して Drive へ公開済み。
- s7-l3: Session Manager の SSM Agent 説明を Amazon Linux 2023 前提に修正し、スライド・音声・動画を再生成して Drive へ公開済み。
- s7-l3: GPT Image 2 版のスライドへ差し替え、Run Command / Incident Manager / Session Manager の空白読みを修正して再生成し、Drive へ公開済み。

**🟢 完了: 横断（B-1 ナレーション読み方ルール）**（2026-05-06）
- `src/voice_generator.py::_EN_TO_KANA` を 33エントリ追加（5xx/4xx, dmesg, killall, stress-ng, Cost Anomaly Detection, Service Level *, Systems Manager, Session Manager, Composite Alarm, Evaluation Periods, Alert Fatigue 等の多語フレーズ＋単独語）
- `src/voice_generator.py::_JP_READING_FIXES` を 7パターン追加（重大度・根本原因・発報・一気貫通・今リリース・右上、+「値」を ひらがな/カタカナ + 助詞 で挟まれているときに『あたい』に変換）
- 既存 script.json 全 38 ファイルを走査し、ルールA（誤読しやすい和語）/C（カッコふりがな）/D（伏字記号）違反を一括修正
  - ルールA: 重大度・根本原因・発報・一気貫通・今リリース・右上 を全置換
  - ルールA: 「値」を文脈判定（ひらがな/カタカナ続きの「この値/どんな値/キーと値/IDの値/高い値/低い値/引いた値/正常な値」など14箇所のみ「あたい」に変換、複合語の「数値・閾値・目標値・現在値・実績値・パーセンタイル値」等は温存）
  - ルールC: 「英語（カタカナ）」表記6件を削除（Toil/Flapping/Window/Blameless×2/Reserved Instances/SLO/SLI/SLA）
  - ルールD: s8-l1 slide3 の「〇〇さん」を「あの担当者」に修正
  - ルールE: 多語英フレーズ23種を script.json 内でカタカナ連結（Cost Anomaly Detection, Service Level Objective 等）

**🟡 残: スライド再生成（B-2 図崩れ）**
- s6-l1 `slides/slide_010.png`、s6-l2 `slides/slide_007.png`、s6-l4 `slides/slide_009.png`

**🟢 任意: 追加施策**
- `publicRepo/aws-sre-cfn-templates/cloudformation/07-slo-dashboard.yaml` 追加（SLO 可視化用 CFN）

**🟢 完了: 公開リポへの commit/push**
- `postmortem-template.md` / `slo-document-template.md` は commit `9dcb2db` で push 済（2026-05-06）

---

## D. 検証チェックリスト（動画修正後の動作確認）

> 旧 `sre-course-validation-results.md` の確認観点を継承

### s2-l5 ハンズオン環境
- [ ] CloudFormation スタック `sre-handson-base` が正常作成
- [ ] **エラー率デモアプリ**（旧 TODO アプリ）が systemd サービスとして自動起動（ポート **8080**）
- [ ] ALB 経由（ポート 80）でアプリにアクセス可能
- [ ] 確率を上げると 5xx エラーが ALB / CW メトリクスで増えることを確認
- [ ] CW Agent が running、`-a status` で確認可能
- [ ] X-Ray コンソールにトレースが届く（CW Agent 経由）
- [ ] ロググループ **`/aws/ec2/sre-handson/webapp`** にログ出力
- [ ] アプリログが **JSON 形式**

### s4-l4 Logs Insights
- [ ] 新クエリ（`case` 文）が動作

### s5 アラーム
- [ ] `sre-handson-cpu-high` 命名でアラーム作成可能
- [ ] 5xx 率が math expression で％表示

### s9 コスト
- [ ] Budgets が **USD** ベースで作成
- [ ] Cost Anomaly Subscription が EMAIL 直送
- [ ] Billing Alert（CloudWatch Alarm）が **存在しない**ことを確認

---

## E. 参考リンク

- 動画レビューメモ: `courses/aws-sre-practical/memo.md`
- 動画用 CLI 参照: `courses/aws-sre-practical/CLI_COMMANDS.md`
- ハンズオン公開リポ: `https://github.com/toma1110/aws-sre-cfn-templates`
  ローカル: `/home/ubuntu/workspace/publicRepo/aws-sre-cfn-templates`
- ナレーション読み方ルール: `skills/narration-writing/SKILL.md`
- 読み方テーブル実装: `src/voice_generator.py::_EN_TO_KANA` / `_JP_READING_FIXES`
- 旧分析（履歴）: `/home/ubuntu/workspace/modification_impact_analysis.md`、`/home/ubuntu/workspace/sre-course-validation-results.md`
