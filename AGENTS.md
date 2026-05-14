あなたは、AWS/SRE関連のUdemy動画を量産するための「AI制作会社 v1」のリポジトリ構成と初期ファイル一式を構築するシニアエンジニアです。

目的:
私（人間）はCEOとして最終判断のみを行い、AIがチケット駆動で自律的に実装・制作・レビューを進められる土台を作ること。

重要:
これは「AI制作会社 v1」です。
完全自律ではなく、GitHub Issueベースで半自律運用できる構成を作ってください。

========================================
前提
========================================

- AWS/SRE関連のUdemy講座を量産する
- 教材ハンズオンでは、受講者が追加ツールなしで再現しやすい場合に CloudFormation を使う
- 実運用のIaC推奨は CDK または Terraform とする
- 音声は当面 VOICEVOX を使う
- 完成動画に使うスライドは必ず GPT-Image2 由来のPNGにする
- 完成動画に表示する文字も必ず GPT-Image2 に生成させる
- ローカル描画のみのスライドは下書き・検証用に限り、完成動画には使わない
- ローカル文字合成したスライドは完成動画には使わない
- 図解はスライドPNG内に含める
- 動画アップロードは Google Drive 一括アップロード方式
- course_spec.md を唯一の真実（Source of Truth）とする
- AIの局所修正で全体崩壊しない設計にする
- ハンズオンは「動いた」ではなく「README通り再現できる」が合格条件

========================================
AI組織ルール
========================================

必ず以下を守る:

- Planner ≠ Worker
- Worker ≠ Reviewer
- 実装AIが自分でレビューしてはいけない
- 全作業はチケット駆動
- チケットには担当AIとレビュアーAIを必ず書く
- チケットなし作業は禁止
- GitHub Issueの自動実行はAI-PM-01が検知・判定する
- AWS環境構築、CloudFormation stack作成/更新/削除、Fargate/Batch/ECR等の課金影響がある作業はCEO承認後にのみ実行する
- 修正は直接変更禁止
- change request → impact analysis → approve → implementation → QA の順
- Publicリポジトリ用の作業コピー、公開テンプレート、公開配布物は必ず `udemy-ai-company/public_repo/<repo-name>/` に作成・配置する
- Publicリポジトリを `/home/ubuntu/workspace/udemy2/<repo-name>` や `udemy-ai-company/courses/` 配下に直接作成しない
- Publicリポジトリ運用の詳細は `udemy-ai-company/docs/PUBLIC_REPO_RULES.md` を参照する
- 動画制作ルールの詳細は `udemy-ai-company/docs/GPT_IMAGE_RULES.md` を参照し、最終動画はGPT-Image2由来スライドだけで作る

========================================
AI社員
========================================

以下のAI社員を前提に構成する:

AI-Strategy-01
役割:
企画
高性能モデル

AI-PM-01
役割:
GitHub Issue変更検知
自動実行可否判定
課金影響があるAWS作業のCEO承認ゲート管理

AI-Engineer-01
役割:
CloudFormation実装
ハンズオン構築
CLI検証
Codex/ClaudeCode想定

AI-Production-01
役割:
教材化
PNGスライド生成
台本生成
VOICEVOX素材生成

AI-QA-01
役割:
技術レビュー
教材レビュー
整合性レビュー

AI-Ops-01
役割:
Issue監視
進捗管理
Blocked検知
運用管理

========================================
作成する構成
========================================

現在のディレクトリ配下に以下を作成してください。

udemy-ai-company/
  README.md
  AGENTS.md
  .github/
    ISSUE_TEMPLATE/
      task.md
      change_request.md
  docs/
    PROJECT.md
    STYLE_GUIDE.md
    WORKFLOW.md
    QUALITY_GATE.md
    AI_ORG_CHART.md
    TASK_MANAGEMENT.md
    CLOUDFORMATION_RULES.md
  templates/
    course_spec_template.md
    impact_analysis_template.md
    qa_report_template.md
    handson_validation_report_template.md
  courses/
    sample-aws-sre-course/
      course_spec.md
      README.md
      cloudformation/
        README.md
        validate.sh
        smoke_test.sh
        template.yaml
      slides/
        README.md
      scripts/
        README.md
      audio/
        README.md
      video/
        README.md
      qa/
        README.md

========================================
詳細要件
========================================

1. README.md

以下を書く:

- このAI制作会社の目的
- 組織構成
- AI社員一覧
- 基本ワークフロー
- CEO（人間）の役割
- 最初の使い方
- GitHub Issueベース運用方法

----------------------------------------

2. AGENTS.md

各AI社員について定義:

- 役割
- 入力
- 出力
- 禁止事項
- Definition of Done
- 参照必須ファイル

Codex/ClaudeCodeが読んでそのまま動ける内容にする

----------------------------------------

3. GitHub Issue Template

task.md

必須項目:

# Task Summary
Task ID:
Title:

# Ownership
Department:
Owner AI:
Reviewer AI:

# Execution
Priority:
Status:

# Inputs
Input Files:
Dependencies:

# Deliverables
Expected Output:

# Quality Gate
Definition of Done:

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth

# Blocking
Blocked By:
Notes:

----------------------------------------

change_request.md

変更時テンプレート:

- Change Summary
- Why Change
- Scope
- Impact
- Risks
- Approval
- Implementation Plan

----------------------------------------

4. docs/WORKFLOW.md

以下の状態遷移を書く:

Backlog
→ Planning
→ Engineering
→ Engineering Review
→ Production
→ Content Review
→ Ready for Publish
→ Published
→ Analytics Review

各フェーズで:
- 担当AI
- 入力
- 出力
- 完了条件

を書く

----------------------------------------

5. docs/TASK_MANAGEMENT.md

GitHub Issueベースで定義

含める:

- チケット駆動の目的
- 1チケット1成果物
- Owner AI 必須
- Reviewer AI 必須
- Blocked時の対応
- stale issue対応
- GitHub labels案

labels:

strategy
engineering
production
qa
ops

high
medium
low

blocked
review
ready
done

----------------------------------------

6. docs/QUALITY_GATE.md

必須品質ゲート:

- course_spec.md が存在
- CloudFormation validate success
- create success
- update success
- delete success
- smoke test success
- README再現成功
- 動画手順とREADME一致
- Worker != Reviewer
- change requestフロー順守

----------------------------------------

7. docs/CLOUDFORMATION_RULES.md

必須:

- CloudFormationは教材ハンズオン向けの再現手段
- 実運用IaCはCDKまたはTerraform推奨
- 初学者が読めるテンプレート
- Parameters明確
- Outputs明確
- IAM最小権限
- コスト注意
- 削除手順必須
- validate.sh必須
- stack naming rule

----------------------------------------

8. templates/course_spec_template.md

項目:

- Course Title
- Target Audience
- Prerequisites
- Learning Objectives
- Course Promise
- Differentiation
- Chapter Structure
- Hands-on Scope
- CloudFormation Scope
- Cost Warning
- Definition of Done
- Out of Scope

----------------------------------------

9. サンプル講座

sample-aws-sre-course/course_spec.md

テーマ:

AWS SRE入門：CloudFormationで作る監視基盤ハンズオン

低コスト構成:

- CloudWatch Alarm
- SNS
- Dashboard

----------------------------------------

10. cloudformation/template.yaml

最低限動く簡易テンプレートを作る

----------------------------------------

11. validate.sh

以下を想定:

- cfn validate
- stack create
- stack update
- smoke test
- stack delete

実用雛形にする

----------------------------------------

12. smoke_test.sh

以下確認:

- alarm exists
- sns exists
- dashboard exists

----------------------------------------

実装ルール:

- 日本語
- Markdown中心
- bashは実行権限
- 既存ファイル破壊禁止
- TODOコメント歓迎
- 実際に使える内容

========================================
最後に必ずやること
========================================

セルフレビュー:

- AIが自律的に動けるか
- Worker/Reviewer分離されているか
- CloudFormationをハンズオン用途に限定し、実運用IaCはCDK/Terraform推奨になっているか
- GPT-Image2前提か
- VOICEVOX前提か
- GitHub Issueだけで運用できるか
- ハンズオン品質ゲートが明確か

最後に表示:

- 作成ファイル一覧
- 次にCEOがやるべきこと
