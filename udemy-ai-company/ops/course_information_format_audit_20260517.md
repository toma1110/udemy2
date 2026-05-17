# Course Information Format Audit

Date: 2026-05-17

## Scope

CEO指摘により、`aws-cloudwatch-intro-course/course_infomation.md` をSLOコース相当のUdemy登録画面フォーマットへ更新した。
あわせて横展開として、今後の新規・更新講座で同じ抜けが起きないようにテンプレートとチェックツールを追加した。

## Applied Fix

| Course | Result | Notes |
| --- | --- | --- |
| `aws-cloudwatch-intro-course` | Fixed | `course_infomation.md` を `# udemy登録情報` 形式に差し替え。学習成果、前提条件、対象者、紹介ページ文、AI/VOICEVOX表記、コース画像方針、歓迎/お祝いメッセージを追加。 |

## Lateral Rollout

| Area | Action |
| --- | --- |
| Template | `templates/course_infomation_template.md` を追加。SLOコース相当のUdemy登録情報フォーマットを標準化。 |
| QA Tool | `tools/check_course_information.py` を追加。必須見出し、学習成果4件以上、対象者、前提条件、VOICEVOX/GPT-Image2表記、TODO残存を検出。 |
| Quality Gate | `docs/QUALITY_GATE.md` にテンプレート準拠とチェックツール実行を追加。 |
| Existing Courses | 既にGit管理されている公開候補コースの `course_infomation.md` を標準形式へ更新。 |

## All-course Check

Git管理されている `course_spec.md` を持つ公開候補コースのチェック結果は以下。

| Course | Check Result | Required Action |
| --- | --- | --- |
| `aws-cloudwatch-alarm-sns-course` | PASS | 標準形式へ更新済み |
| `aws-cloudwatch-intro-course` | PASS | 今回更新済み |
| `aws-cloudwatch-logs-insights-practical-course` | PASS | 標準形式へ更新済み |
| `aws-cost-safety-course` | PASS | 標準形式へ更新済み |
| `aws-slo-adoption-course` | PASS | 既存のSLO相当形式として維持する |
| `sample-aws-sre-course` | PASS | 前提条件、対象者、GPT-Image2コース画像方針を補完済み |

ローカル作業ツリーには、まだGit管理対象外の将来コース候補も存在する。これらは別チケットでコース本体をコミットする時に同テンプレートへ揃える。

## Prevention

新規講座または公開前更新では、次を必須にする。

```bash
python3 udemy-ai-company/tools/check_course_information.py udemy-ai-company/courses/<course-id>/course_infomation.md
```

全体監査時は次を実行する。

```bash
python3 udemy-ai-company/tools/check_course_information.py
```
