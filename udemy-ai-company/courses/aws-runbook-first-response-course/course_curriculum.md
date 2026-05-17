# AWS障害対応Runbook入門 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-runbook-first-response-course`
- Course Title: `AWS障害対応Runbook入門: アラートから初動対応へ`
- Course Information: `course_infomation.md`
- Target Lecture Count: 6
- Target Main Lecture Runtime: 30〜36分
- Current Audit Result: 2026-05-17時点で通常レクチャーMP4は1本、合計約2.8分。`s1-l2`、`s2-l1`、`s2-l2`、`s3-l1`、`s3-l2` が未作成。

## Curriculum Review Gate

- 動画生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で生成してよい。
- 標準範囲ではAWSリソースを作成しない。追加検証でAWS実行する場合はCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: Runbookの地図

Section Learning Goal: Runbookに書くべき項目と、Playbook/Runbookの違いを説明できる。

Hands-on Resource Title: `Runbookテンプレート記入演習`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | Runbookに何を書くか | Trigger、Owner、Severity、Scope、First Checks、Mitigation、Escalationを書く理由を説明できる | Runbookテンプレート記入演習 | 5〜6分 | Produced - regenerate for runtime |
| `s1-l2` | PlaybookとRunbookの違い | 調査手順としてのPlaybookと、既知の緩和・復旧手順としてのRunbookを区別できる | Playbook/Runbook比較表 | 5〜6分 | Not produced |

## Section 2: アラートから初動確認へ

Section Learning Goal: CloudWatch Alarmを受け取った直後に、5分以内に確認する対象を絞れる。

Hands-on Resource Title: `初動確認チェックリスト`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | CloudWatch Alarmから5分で確認すること | 影響範囲、対象サービス、直近変更、メトリクス、ログの初動確認を説明できる | 5分初動確認チェック | 5〜6分 | Not produced |
| `s2-l2` | Dashboard、Logs、Recent deploy、AWS Healthを見る | Dashboard、Logs、Recent deploy、AWS Healthを順番に見る理由を説明できる | Dashboard/Logs/AWS Health確認 | 5〜6分 | Not produced |

## Section 3: 緩和とエスカレーション

Section Learning Goal: Mitigation、Rollback、Escalation、Communication、PostmortemをRunbookへつなげられる。

Hands-on Resource Title: `緩和・連絡・振り返りテンプレート`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | Mitigation、Rollback、Escalationを決める | 一次緩和、ロールバック、権限外対応、エスカレーション条件を分けて書ける | Mitigation/Escalation設計 | 5〜6分 | Not produced |
| `s3-l2` | CommunicationとPostmortemへつなげる | 障害連絡、ステータス更新、ポストモーテムへの接続をRunbookへ入れられる | Communication/Postmortemテンプレート | 5〜6分 | Not produced |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Runbookテンプレート記入演習 | `handson/runbook_template.md` | なし | 標準は文書作成演習 |
| 初動確認チェックリスト | `handson/README.md` | なし | CloudWatch画面例は読解中心 |
| 緩和・連絡・振り返りテンプレート | `handson/README.md` | なし | 実AWS操作は扱わない |

## Definition of Done

- 通常レクチャー6本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを生成し、既存の短尺 `s1-l1` だけを完成扱いにしない。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
