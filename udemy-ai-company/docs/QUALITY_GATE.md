# QUALITY_GATE

## 必須品質ゲート

すべての講座は公開前に以下を満たす必要があります。

## 受講者レビュー指摘の横展開

- CEOレビュー、受講者レビュー、QAで出た指摘は、個別修正だけで終わらせず、再発防止のために該当ルール文書へ反映するか、反映不要の理由をIssueに残す
- 読み方指摘は `docs/VOICEVOX_RULES.md` と音声生成/チェック系ツールへ反映する
- ハンズオンの分かりにくさ、手順不一致、Publicリポジトリの不足は、README、CLI、補助ドキュメント、Public repoルールへ反映する
- 完成動画素材に関する指摘は `docs/GPT_IMAGE_RULES.md` と `docs/VIDEO_QUALITY_BASELINE.md` へ反映する
- 同じ種類の指摘が2回以上出た場合は、次回以降のQAチェック項目として必ず明文化する

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
- 動画内手順、PublicリポジトリREADME、CLIコマンド、補助ドキュメントが一致している
- PublicリポジトリのREADME/CLIに、古いアプリ名、古いアラーム名、古いOutput名、不要な手動セットアップ手順、存在しないファイル名が残っていない
- CloudFormation Outputsや後続スタックのParametersは、受講者がコピーできる形で取得手順が書かれている
- ハンズオン全体像が分かりにくい場合は、少なくとも構成図、操作フロー、確認観点、正常系/異常系の読み取り例をPublicリポジトリに追加する
- draw.io等の補助図解をPublicリポジトリへ置く場合は、GitHub上で直接確認できるPNGをMarkdownに埋め込んでいる
- Publicリポジトリに内部制作向け注意書き、未公開レビュー事情、完成動画素材向けの社内注意を載せていない

## 教材

- 動画制作前に対象講座の `course_infomation.md` が存在する
- 動画制作前に対象講座の `course_curriculum.md` が存在する
- `course_infomation.md` は `templates/course_infomation_template.md` のUdemy登録情報フォーマットに準拠している
- `course_infomation.md` にUdemy登録時に必要なコースタイトル、サブタイトル、説明、学習目標、前提条件、対象者、コース画像方針、歓迎メッセージ、修了/お祝いメッセージが記載されている
- `course_infomation.md` の内容が `course_spec.md`、動画内容、ハンズオン範囲、VOICEVOX/AI利用表記と矛盾していない
- `tools/check_course_information.py` で対象講座の `course_infomation.md` がPASSしている
- `course_curriculum.md` に全レクチャーのセクション番号、レクチャー番号、タイトル、レクチャー完了後に身についていること、ハンズオン有無が記載されている
- ハンズオンがあるレクチャーでは `course_curriculum.md` にPublicRepo URLが記載され、READMEまたは配布物と一致している
- `course_curriculum.md` が `docs/CURRICULUM_RULES.md` に従っている
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
- 完成MP4の末尾には、Udemy終端切れ対策として最終スライドの短い無音保持が入っている
- 末尾の無音保持は約1秒を標準とし、長すぎる空白として目立たない
- 台本に未検証の技術説明がない

## プロモーション動画

- 公開対象コースでは通常レクチャーとは別にプロモーション動画が存在する
- `course_spec.md` に `Promotion Video Scope` が明記されている
- プロモーション動画台本が `course_spec.md`、`course_infomation.md`、`course_curriculum.md` と矛盾していない
- 通常レクチャー動画をプロモーション動画の代用にしていない
- 解決する悩み、対象者、受講後の状態、主要トピック、ハンズオン有無が短く伝わる
- Out of Scopeを超える成果、未検証の収益表現、保証表現を含まない
- 完成動画に使う最終スライドPNGと表示文字はGPT-Image2由来である
- VOICEVOX音声、MP4、Drive URL、共有状態、QAレポートが存在する
- `build_report.json` に末尾余白秒数が記録されている
- `docs/PROMOTION_VIDEO_RULES.md` に従っている

## 量産判断

初回動画や新しい制作方式では問題が出る前提で、品質ゲートは「無限に磨く」ためではなく、量産可能な最低ラインを安定させるために使う。

- ハンズオン再現性、技術的正確性、VOICEVOXの明確な誤読、GPT-Image2由来スライド要件、動画とREADMEの手順一致はBlockingにする
- 受講者からハンズオン以外の重大指摘が出ておらず、VID-001基準の見た目と音声品質を満たす場合は、単品の微修正を続けず次の制作へ進む
- 単品改善に時間を使う場合は、同じ改善が次の動画にも効くルール、テンプレート、チェックリスト、スクリプトへ変換する
- CEOが量産優先を指示した場合、AI-QA-01は「量産へ進んでよい残リスク」をQAレポートに短く記録する

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
