#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLIが見つかりません。GitHubラベル作成には gh のインストールと gh auth login が必要です。" >&2
  exit 1
fi

create_or_update_label() {
  local name="$1"
  local color="$2"
  local description="$3"

  if gh label list --limit 200 --json name --jq '.[].name' | grep -Fxq "$name"; then
    gh label edit "$name" --color "$color" --description "$description"
  else
    gh label create "$name" --color "$color" --description "$description"
  fi
}

create_or_update_label "strategy" "5319e7" "企画、講座設計、差別化"
create_or_update_label "engineering" "1d76db" "CloudFormation、ハンズオン実装"
create_or_update_label "production" "0e8a16" "スライド、台本、VOICEVOX、動画制作"
create_or_update_label "qa" "d93f0b" "技術レビュー、教材レビュー、品質ゲート"
create_or_update_label "ops" "fbca04" "Issue運用、進捗、公開管理"
create_or_update_label "pm" "7057ff" "Issue変更検知、自動実行可否判定"
create_or_update_label "rule-audit" "c5def5" "AI-Ops-01による仕組みルール監査"

create_or_update_label "high" "b60205" "高優先度"
create_or_update_label "medium" "fbca04" "中優先度"
create_or_update_label "low" "0e8a16" "低優先度"

create_or_update_label "blocked" "b60205" "ブロッカーあり"
create_or_update_label "review" "d93f0b" "レビュー待ち"
create_or_update_label "ready" "1d76db" "次工程へ進められる"
create_or_update_label "done" "0e8a16" "完了"
create_or_update_label "auto-execute" "5319e7" "AI-PM-01による自動実行対象"
create_or_update_label "pm-parent" "7057ff" "AI-PM-01が子チケットへ分解した親Issue"
create_or_update_label "pm-child" "bfd4f2" "AI-PM-01が親Issueから作成した子Issue"
create_or_update_label "needs-breakdown" "fbca04" "PM分解に必要な情報が不足"
create_or_update_label "feedback" "d93f0b" "CEOフィードバック対応"
create_or_update_label "approval-required" "b60205" "CEO承認が必要"
create_or_update_label "ceo-approved" "0e8a16" "CEO承認済み"
create_or_update_label "pm-queued" "1d76db" "AI-PM-01が実行キュー投入済み"
create_or_update_label "in-progress" "fbca04" "作業中"

echo "GitHub labels are ready."
