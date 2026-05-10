# QUALITY_GATE

## 必須品質ゲート

すべての講座は公開前に以下を満たす必要があります。

## 企画

- `course_spec.md` が存在する
- Course Title、Target Audience、Prerequisites、Learning Objectivesが明記されている
- Hands-on Scope、CloudFormation Scope、Cost Warning、Out of Scopeが明記されている
- `course_spec.md` と成果物の矛盾がない

## CloudFormation

- CloudFormationを原則としている
- `aws cloudformation validate-template` が成功する
- stack createが成功する
- stack updateが成功する
- stack deleteが成功する
- `smoke_test.sh` が成功する
- ParametersとOutputsが明確である
- IAMを作る場合は最小権限になっている
- コスト注意と削除手順がREADMEにある

## ハンズオン

- README通りに再現できる
- 前提条件が明記されている
- 実行コマンドがコピー可能である
- 検証手順が明記されている
- 削除手順が明記されている
- 失敗時の確認ポイントがある

## 教材

- 動画手順とREADMEが一致している
- スライドはGPT-Image2 PNG生成を前提としている
- 図解はスライドPNG内に含まれている
- 音声はVOICEVOXを前提としている
- `tools/narration_checker.py` でナレーション品質を確認している
- VOICEVOXで不自然な空白読みが起きやすい表記を避けている
- 英字、カッコふりがな、伏字記号が読み上げ本文に残っていない
- 台本に未検証の技術説明がない

## AI運用

- Worker != Reviewer
- Planner != Worker
- チケットにOwner AIとReviewer AIがある
- change requestフローを順守している
- QAレポートが残っている

## 公開判定

すべての必須項目が満たされ、CEOが承認した場合のみ `Ready for Publish` から `Published` へ進める。
