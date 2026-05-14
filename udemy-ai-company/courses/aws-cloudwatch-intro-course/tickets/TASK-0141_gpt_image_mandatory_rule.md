# Task Summary
Task ID: TASK-0141
Title: 完成動画のスライドをGPT-Image2由来必須にする制作ルールへ更新する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `AGENTS.md`
- `udemy-ai-company/README.md`
- `udemy-ai-company/AGENTS.md`
- `udemy-ai-company/docs/QUALITY_GATE.md`
- `udemy-ai-company/docs/STYLE_GUIDE.md`
- `udemy-ai-company/docs/WORKFLOW.md`
- `udemy-ai-company/templates/slide_generation_report_template.md`
Dependencies:
- CEO request: 動画は必ずGPT-Imageで作る

# Deliverables
Expected Output:
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`
- GPT-Image2必須ルールの各運用ドキュメント反映
- PM自動生成チケットのQuality Gate更新

# Quality Gate
Definition of Done:
- 完成動画に使う最終スライドPNGがGPT-Image2由来必須と明記されている
- 完成動画に表示する文字もGPT-Image2生成必須と明記されている
- ローカル描画のみのスライドを完成動画に使わないことが明記されている
- ローカル文字合成したスライドを完成動画に使わないことが明記されている
- GPT-Image2 source evidence保存が必須になっている
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止

# Blocking
Blocked By:
- none
Notes:
- CEO承認済み方針として扱う。
- GitHub Issue: #148 https://github.com/toma1110/udemy2/issues/148
- 完成動画のスライドPNG、表示文字、図解内テキストをGPT-Image2生成必須に更新済み。
- ローカル文字合成は禁止し、下書き、contact sheet、サイズ検証のみ許可する運用に更新済み。
