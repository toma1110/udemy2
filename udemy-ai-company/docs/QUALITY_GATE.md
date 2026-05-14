# QUALITY_GATE

## 必須品質ゲート

すべての講座は公開前に以下を満たす必要があります。

## 企画

- `docs/MISSION_VISION_VALUES.md` のミッション、ビジョン、バリューと矛盾していない
- `course_spec.md` が存在する
- Course Title、Target Audience、Prerequisites、Learning Objectivesが明記されている
- Hands-on Scope、Hands-on IaC Scope、Production IaC Positioning、Cost Warning、Out of Scopeが明記されている
- `course_spec.md` と成果物の矛盾がない

## AWS技術仕様

- AWSサービス仕様、制約、廃止予定、ベストプラクティスに関わる説明は `awsknowledge` で確認している
- `awsknowledge` の検索語、確認結果、参照URLをQAレポートまたはIssueに残している
- `awsknowledge` が利用できない場合は、未使用理由と代替確認元をQAレポートまたはIssueに明記している
- AWS最新仕様に影響される内容を、モデルの記憶だけで承認していない

## ハンズオンIaC

- CloudFormationを使う場合、それが教材ハンズオン向けの再現手段であることを説明している
- 実運用IaCはCDKまたはTerraform推奨であることを必要に応じて補足している
- CloudFormationハンズオンの場合、`aws cloudformation validate-template` が成功する
- CloudFormationハンズオンの場合、利用可能なら `awsiac` によるCloudFormationテンプレート検証が成功する
- `awsiac` が利用できない場合は、未使用理由と代替検証結果をハンズオン検証レポートまたはIssueに明記している
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

- 動画制作前に対象講座の `course_infomation.md` が存在する
- `course_infomation.md` にUdemy登録時に必要なコースタイトル、サブタイトル、説明、学習目標、前提条件、対象者、コース画像方針が記載されている
- `course_infomation.md` の内容が `course_spec.md`、動画内容、ハンズオン範囲、VOICEVOX/AI利用表記と矛盾していない
- 動画手順とREADMEが一致している
- スライドはGPT-Image2 PNG生成を前提としている
- 完成動画に使う最終スライドPNGは必ずGPT-Image2由来である
- 完成動画に表示する文字、タイトル、短いラベルもGPT-Image2生成である
- GPT-Image2 source PNGを `slides/<section>-gpt-image2-sources/<lecture>/` に保存している
- `*_slide_generation_report.md` に Generation Mode、GPT-Image2出力元、プロンプト概要、後処理内容、contact sheet確認結果を記録している
- `docs/VIDEO_QUALITY_BASELINE.md` に従い、VID-001基準と比較した品質確認結果を記録している
- ローカル描画（Pillow、HTML Canvas、SVG、手作業レイアウト等）は、下書き、storyboard確認、contact sheet作成、サイズ検証に限定している
- ローカル描画のみのスライドPNGを完成動画に使っていない
- ローカル文字合成したスライドPNGを完成動画に使っていない
- `*_video_build_report.md` にGPT-Image2由来スライドを入力にしたことを記録している
- 動画生成前に、直近承認済みセクションまたは指定リファレンスとのcontact sheet比較を行い、品質差があればBlockedにする
- 図解はスライドPNG内に含まれている
- 音声はVOICEVOXを前提としている
- `tools/narration_checker.py` でナレーション品質を確認している
- VOICEVOXで不自然な空白読みが起きやすい表記を避けている
- 英字、カッコふりがな、伏字記号が読み上げ本文に残っていない
- 台本に未検証の技術説明がない

## AI運用

- Worker != Reviewer
- Planner != Worker
- PM != Worker
- PM != Reviewer
- チケットにOwner AIとReviewer AIがある
- change requestフローを順守している
- `auto-execute` IssueはAI-PM-01が実行可否を判定している
- AWS課金につながる作業はCEO承認の証跡がIssueに残っている
- QAレポートが残っている

## 公開判定

すべての必須項目が満たされ、CEOが承認した場合のみ `Ready for Publish` から `Published` へ進める。
