# Task Summary
Task ID: TASK-0156
Title: aws-sre-cfn-templatesにハンズオン理解を助ける図解ドキュメントを追加する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/README.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/CLI_COMMANDS.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/01-base-infrastructure.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/02-cloudwatch-dashboard.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/04-log-metric-filter.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/05-alarms-sns.yaml`
- `udemy-ai-company/docs/PUBLIC_REPO_RULES.md`
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`
Dependencies:
- TASK-0155
- 受講者レビュー指摘: ハンズオンの全体像と操作意図が把握しづらい

# Deliverables
Expected Output:
- CloudFormationで作成されるAWSリソース構成図
- CloudWatch Alarm / Logs Insights / Dashboard の見方を説明する概念図
- 正常系・異常系のログやメトリクスの読み取りイメージ
- ハンズオン全体の流れを示すステップ図
- 公開リポジトリREADMEから各図解への導線

# Quality Gate
Definition of Done:
- 図解がCloudFormationテンプレートの実リソースと矛盾していない
- AWS構成図は `aws-architecture-diagram` ルールに従い、draw.io形式で作成する
- GitHub上で受講者が読めるMarkdown説明を併設する
- 図解内で動画と異なる手順、存在しないファイル、存在しないリソースを案内しない
- CLI_COMMANDS.md と README の手順にリンクされている
- 完成動画へ転用する場合はGPT-Image2由来PNGにする。Publicリポジトリの補助資料としてはMarkdown/draw.ioを許可する
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- Publicリポジトリ配布物は `udemy-ai-company/public_repo/aws-sre-cfn-templates/` 配下で作成する
- AWSリソース作成、CloudFormation stack作成/更新/削除は行わない
- CloudFormationは教材ハンズオン用途に限定し、実運用IaC推奨はCDKまたはTerraformとする

# Proposed Files
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/docs/architecture.drawio`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/docs/ARCHITECTURE.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/docs/CLOUDWATCH_GUIDE.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/docs/SIGNAL_EXAMPLES.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/docs/HANDSON_FLOW.md`

# Impact Analysis
Scope:
- Publicリポジトリの補助ドキュメント追加とREADMEリンク追加
Risks:
- 図解がテンプレート実体とずれると受講者を混乱させる
- 動画スライドへ流用する場合、GPT-Image2ルールを満たさない素材を完成動画に使ってはいけない
QA:
- CloudFormationテンプレートから作成リソースを棚卸しする
- README、CLI_COMMANDS、図解のファイル名、スタック名、リソース名を照合する
- 図解ファイルのXML/Markdownリンクを静的検証する

# Blocking
Blocked By:
- TASK-0155
Notes:
- GitHub Issue: #156 https://github.com/toma1110/udemy2/issues/156
- `courses/aws-sre-practical/course_spec.md` は現時点で未配置。図解整備時は公開リポジトリREADME、CLI_COMMANDS、CloudFormationテンプレートを事実ソースとして扱い、course_spec整備は別途必要。
