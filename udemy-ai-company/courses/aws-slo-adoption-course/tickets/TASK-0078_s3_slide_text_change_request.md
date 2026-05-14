# Task Summary
Task ID: TASK-0078
Title: aws-slo-adoption-course Section 3 スライド文字量修正の変更要求と影響分析を行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Strategy-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- GitHub Issue #77 CEO comment
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section3_completion_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s2-l*/contact_sheet.png
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l*/contact_sheet.png
Dependencies:
- TASK-0077 CEO review comment

# Deliverables
Expected Output:
- Section 3 slide revision scope
- Impact analysis note
- Approval state

# Quality Gate
Definition of Done:
- CEOコメントの内容を確認している
- S2とS3のスライド印象差分を確認している
- 修正対象がSection 3全5講義のスライド・動画・Driveであることを明確にしている
- 音声は問題なしとして再生成対象外にしている
- change request → impact analysis → approve の状態を記録している

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 修正は直接変更禁止
- CEOコメントを承認根拠として扱う

# Blocking
Blocked By:
Notes:
- 2026-05-10 Issue #77 コメント: S3-L1音声は問題なし。スライドに文字がなくS2と印象が変わるため、S2相当に修正する。
- Impact: S3全5講義のスライドPNG、動画MP4、Driveアップロード、QAレポートを更新する。音声WAVと台本は変更しない。
