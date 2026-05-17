# AWS SRE入門 サンプル講座 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `sample-aws-sre-course`
- Course Title: `AWS SRE入門：CloudFormationで作る監視基盤ハンズオン`
- Course Information: `course_infomation.md`
- Target Lecture Count: 6
- Current Status: AI制作会社v1のサンプル講座。公開用の本番制作対象ではなく、構成、品質ゲート、CloudFormationハンズオンの雛形確認に使う。

## Curriculum Review Gate

- サンプル講座であっても `course_spec.md` をSource of Truthとする。
- CloudFormation validate以外のstack create、update、delete、smoke testはCEO承認後にだけ実行する。
- 公開用動画を作る場合は、動画生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: SREと監視基盤の全体像

Section Learning Goal: SREにおける監視基盤の役割と、CloudWatch/SNS/Dashboardの最小構成を説明できる。

Hands-on Resource Title: `監視基盤ハンズオン全体像`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s1-l1` | SREと監視基盤の全体像 | SREにおける監視、通知、可視化の位置づけを説明できる | 監視基盤ハンズオン全体像 | Sample only |
| `s1-l2` | CloudWatch Alarm、SNS、Dashboardの役割 | Alarm、SNS Topic、Dashboardの役割を分けて説明できる | 最小監視構成チェック | Sample only |

## Section 2: CloudFormationで作る

Section Learning Goal: CloudFormationテンプレートを読み、README通りにvalidate、create、smoke testへ進む流れを説明できる。

Hands-on Resource Title: `CloudFormationテンプレート読解`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s2-l1` | CloudFormationテンプレートの読み方 | Parameters、Resources、Outputsを読み、作成される監視リソースを説明できる | CloudFormationテンプレート読解 | Sample only |
| `s2-l2` | スタック作成と検証 | READMEに沿って作成、smoke test、存在確認へ進む流れを説明できる | Stack作成とsmoke test手順 | Sample only |

## Section 3: 更新、削除、運用改善

Section Learning Goal: stack update/deleteと、運用で見るべき改善ポイントを説明できる。

Hands-on Resource Title: `更新・削除・改善ポイント確認`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s3-l1` | スタック更新と削除 | stack updateとdeleteを行い、課金源を残さない手順を説明できる | 更新・削除手順 | Sample only |
| `s3-l2` | 運用で見るべき改善ポイント | 最小監視構成からSLO、Runbook、アラート設計へ広げる観点を説明できる | 運用改善チェック | Sample only |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| 監視基盤ハンズオン全体像 | `README.md` | なし | サンプル講座の入口 |
| CloudFormationテンプレート読解 | `cloudformation/template.yaml` | なし | 実行前に読む |
| Stack作成とsmoke test手順 | `cloudformation/README.md` | CloudWatch Alarm、SNS、Dashboard | CEO承認後のみ実行 |
| 更新・削除手順 | `cloudformation/validate.sh` | 作成済みStack | 削除確認まで必須 |

## Definition of Done

- サンプルとして `course_spec.md`、`course_infomation.md`、`course_curriculum.md` の関係が確認できる。
- CloudFormationテンプレート、README、validate script、smoke test scriptが存在する。
- AWS実行を伴う検証はCEO承認後に実施し、結果をQAへ残す。
- WorkerとReviewerが別AIである。
