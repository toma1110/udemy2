# AWS CloudWatch Application Signals実践 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-cloudwatch-application-signals-practical-course`
- Course Title: `AWS CloudWatch Application Signals実践: サンプルアプリで学ぶAPM・Service Map・SLO監視`
- Course Information: `course_infomation.md`
- Target Lecture Count: 11
- Target Main Lecture Runtime: 33〜44分
- Current Audit Result: 2026-05-17時点で通常レクチャー11本、合計約13.2分。Udemy標準コースの30分要件を満たしていない。

## Curriculum Review Gate

- 動画再生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で再生成してよい。
- CloudFormation stack作成、更新、削除、Application Signals有効化、AWS実行はCEO承認後にだけ実行する。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: Application Signalsの地図

Section Learning Goal: Application Signalsで何が見えるか、ハンズオン構成、コスト安全策を説明できる。

Hands-on Resource Title: `Application Signalsハンズオン構成とコスト安全策`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | Application Signalsで何が見えるか | Services、Application Map、Service detail、Latency、Availability、Fault、Errorの関係を説明できる | Application Signals画面地図 | 3〜4分 | Produced - regenerate for runtime |
| `s1-l2` | ハンズオン構成とコスト安全策 | サンプルアプリ、低頻度トラフィック、停止、削除、料金注意を説明できる | コスト安全策チェック | 3〜4分 | Produced - regenerate for runtime |

## Section 2: CloudFormationでサンプルアプリを作る

Section Learning Goal: CloudFormationテンプレートを読み、サンプル通信、低頻度トラフィック、シナリオ切替を理解できる。

Hands-on Resource Title: `Application Signals CloudFormationハンズオン`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | テンプレート全体を読む | Lambda、IAM、Logs、Scheduler、Application Signals関連リソースの役割を説明できる | CloudFormationテンプレート読解 | 3〜4分 | Produced - regenerate for runtime |
| `s2-l2` | サンプルアプリと低頻度トラフィックをデプロイする | READMEに沿った作成手順と、低頻度トラフィックの目的を説明できる | Stack作成手順 | 3〜4分 | Produced - regenerate for runtime |
| `s2-l3` | 正常、遅延、エラーのシナリオを切り替える | 正常、遅延、エラーの通信を発生させ、画面変化につなげて説明できる | シナリオ切替手順 | 3〜4分 | Produced - regenerate for runtime |

## Section 3: Application Signalsで見る

Section Learning Goal: Services、Application Map、Service detailからサービス状態、依存関係、Latency/Fault/Errorを読み取れる。

Hands-on Resource Title: `Application Signals画面確認手順`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | Servicesで状態を見る | Services一覧でサービス状態、呼び出し量、Latency、Availabilityを確認できる | Services確認手順 | 3〜4分 | Produced - regenerate for runtime |
| `s3-l2` | Application Mapで依存関係を見る | Application Mapで呼び出し関係と障害箇所の入口を説明できる | Application Map確認手順 | 3〜4分 | Produced - regenerate for runtime |
| `s3-l3` | Service detailでLatency、Fault、Errorを読む | Service detailでLatency、Fault、Error、ログへの深掘りを説明できる | Service detail確認手順 | 3〜4分 | Produced - regenerate for runtime |

## Section 4: SLOと運用判断につなげる

Section Learning Goal: Application Signals SLO、Recommendations、Performance Report、停止、削除、コスト確認の前提を説明できる。

Hands-on Resource Title: `Application Signals SLOと後片付け手順`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s4-l1` | Application Signals SLOを作る | Application Signals SLOを1つ作成し、SLIとSLOの関係を説明できる | SLO作成手順 | 3〜4分 | Produced - regenerate for runtime |
| `s4-l2` | SLO RecommendationsとPerformance Reportの前提 | 30日データや実運用データが必要な機能を短時間ハンズオンと分けて説明できる | Recommendations前提メモ | 3〜4分 | Produced - regenerate for runtime |
| `s4-l3` | 後片付け、停止、コスト確認 | 自動トラフィック停止、stack delete、ログ、SLO、料金確認を説明できる | 停止・削除・コスト確認手順 | 3〜4分 | Produced - regenerate for runtime |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Application Signalsハンズオン構成とコスト安全策 | `handson/README.md` | なし | 実行前に読む |
| Application Signals CloudFormationハンズオン | `cloudformation/README.md` | Lambda、IAM、Logs、Scheduler、Application Signals | CEO承認後のみ実行 |
| Application Signals画面確認手順 | `handson/README.md` | 作成済みサンプルアプリ | 短時間・低頻度で確認 |
| Application Signals SLOと後片付け手順 | `handson/README.md` | Application Signals SLO | 停止と削除を必須にする |

## Definition of Done

- 通常レクチャー11本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを再生成し、短尺版をそのまま完成扱いにしない。
- CloudFormation validate、create、update、smoke test、deleteの結果をQAに残す。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
