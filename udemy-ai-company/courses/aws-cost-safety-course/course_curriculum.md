# AWS課金事故防止入門 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-cost-safety-course`
- Course Title: `AWS課金事故防止入門: Budgets・Cost Explorer・削除チェックリスト`
- Course Information: `course_infomation.md`
- Target Lecture Count: 12
- Target Main Lecture Runtime: 36〜48分
- Current Audit Result: 2026-05-17時点で通常レクチャーMP4は未作成。プロモーション動画は通常レクチャーの30分要件に含めない。

## Curriculum Review Gate

- 動画生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で生成してよい。
- AWS実行、Billing API実行、CloudFormation stack作成、更新、削除はCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: 課金事故が起きる理由

Section Learning Goal: 従量課金、削除漏れ、無料枠誤解、データ反映遅延を理解し、本コースで作る安全柵を説明できる。

Hands-on Resource Title: `課金事故防止ハンズオン`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | AWS課金事故防止の地図 | 課金事故の典型パターンと、この講座で作る安全柵を説明できる | 課金事故防止ハンズオン | 3〜4分 | Not produced |
| `s1-l2` | コストデータの遅れと無料枠の誤解 | BudgetsやCost Explorerがリアルタイムではないことと、無料枠の誤解を説明できる | 実行前チェック | 3〜4分 | Not produced |

## Section 2: Budgetsで最初の安全柵を作る

Section Learning Goal: AWS Budgetsで月次予算、Actual通知、Forecasted通知、通知先確認を扱える。

Hands-on Resource Title: `Budgets月次予算チェック`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | 月次予算を作る | AWS Budgetsで学習用の月次コスト予算を作る流れを説明できる | Budgets月次予算チェック | 3〜4分 | Not produced |
| `s2-l2` | 実績アラートと予測アラート | Actual通知とForecasted通知の違い、通知確認の必要性を説明できる | 通知確認チェック | 3〜4分 | Not produced |

## Section 3: Cost Explorerでコストを見る

Section Learning Goal: Cost Explorerでサービス別、期間別、タグ別に費用源を絞る入口を作れる。

Hands-on Resource Title: `Cost Explorer確認手順`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | サービス別コストを読む | Cost Explorerでサービス別コストを見て、主な費用源を探せる | Cost Explorer確認手順 | 3〜4分 | Not produced |
| `s3-l2` | 期間、タグ、フィルターで原因を絞る | 期間比較、タグ、フィルターで原因候補を絞る考え方を説明できる | タグ・フィルター確認 | 3〜4分 | Not produced |

## Section 4: Cost Anomaly Detectionで異常に気づく

Section Learning Goal: Cost Anomaly Detectionの役割、限界、モニター、通知設計を説明できる。

Hands-on Resource Title: `Cost Anomaly Detection設計メモ`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s4-l1` | 異常コスト検知の考え方 | Cost Anomaly Detectionの役割と限界を説明できる | Cost Anomaly Detection設計メモ | 3〜4分 | Not produced |
| `s4-l2` | モニター、サブスクリプション、通知設計 | モニター、通知頻度、しきい値、通知先を設計できる | 通知設計チェック | 3〜4分 | Not produced |

## Section 5: タグと削除チェックリスト

Section Learning Goal: ハンズオン後に残りやすい課金源を確認し、タグと命名で学習用リソースを追跡できる。

Hands-on Resource Title: `削除チェックリスト`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s5-l1` | ハンズオン後の削除チェック | 削除漏れしやすいAWSリソースをチェックリストで確認できる | 削除チェックリスト | 3〜4分 | Not produced |
| `s5-l2` | タグとスタック名で見失わない | 学習用リソースをタグ、名前、メモで追跡する方法を説明できる | タグ確認チェック | 3〜4分 | Not produced |

## Section 6: 月次コスト確認ルーティン

Section Learning Goal: 毎月短時間で確認する画面と記録項目を決め、CloudWatch/SRE学習へ安全につなげる。

Hands-on Resource Title: `月次レビュー記録テンプレート`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s6-l1` | 毎月15分のコストレビュー | 月次で確認する画面、記録項目、判断基準を説明できる | 月次レビュー記録テンプレート | 3〜4分 | Not produced |
| `s6-l2` | 次に学ぶAWS/SRE講座への接続 | 課金安全策を前提に、CloudWatch/SRE学習へ進む順番を説明できる | 次講座接続メモ | 3〜4分 | Not produced |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| 課金事故防止ハンズオン | `handson/README.md` | 任意 | 標準はコンソール中心 |
| Budgets月次予算チェック | `handson/README.md#budgets` | AWS Budgets | CEO承認後に実行 |
| Cost Explorer確認手順 | `handson/README.md#cost-explorer` | Cost Explorer | データ反映遅延を説明 |
| Cost Anomaly Detection設計メモ | `handson/README.md#cost-anomaly-detection` | 任意 | 料金、権限、通知先確認を扱う |
| 削除チェックリスト | `handson/README.md#削除チェックリスト` | なし | 他講座にも流用できる |
| 月次レビュー記録テンプレート | `qa/` | なし | 制作時に追加予定 |

## Definition of Done

- 通常レクチャー12本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを生成する。
- 料金、無料枠、反映遅延、API課金を断定せず、公式情報確認を前提にする。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
