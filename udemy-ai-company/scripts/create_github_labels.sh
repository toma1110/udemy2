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

create_or_update_label "high" "b60205" "高優先度"
create_or_update_label "medium" "fbca04" "中優先度"
create_or_update_label "low" "0e8a16" "低優先度"

create_or_update_label "blocked" "b60205" "ブロッカーあり"
create_or_update_label "review" "d93f0b" "レビュー待ち"
create_or_update_label "ready" "1d76db" "次工程へ進められる"
create_or_update_label "done" "0e8a16" "完了"

echo "GitHub labels are ready."
