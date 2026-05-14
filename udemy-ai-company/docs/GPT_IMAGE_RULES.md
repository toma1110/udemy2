# GPT_IMAGE_RULES

## Purpose

Udemy完成動画の視覚品質を維持するため、最終動画に使うスライドPNGはGPT-Image2由来を必須とします。

## Required Rule

- 完成動画に使う最終スライドPNGは、必ずGPT-Image2で生成した画像にする
- 完成動画に表示するタイトル、見出し、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画、Pillow、HTML Canvas、SVG、手作業レイアウトだけで作ったスライドPNGを完成動画に使わない
- ローカル描画による文字合成、タイトル合成、ラベル合成は完成動画では使わない
- ローカル描画は、下書き、storyboard確認、contact sheet作成、サイズ検証に限って使う
- GPT-Image2生成元PNGは、最終PNGとは別に `slides/<section>-gpt-image2-sources/<lecture>/` へ保存する
- `*_slide_generation_report.md` には、生成元、プロンプト概要、後処理内容、最終PNGとの対応表を残す
- `*_video_build_report.md` には、GPT-Image2由来スライドを入力にしたことを明記する

## Final Video Gate

以下を満たすまで、動画を完成扱いにしません。

- GPT-Image2 source PNGが存在する
- 最終スライドPNGの画像と文字がGPT-Image2生成である
- contact sheetで全スライドを確認している
- ローカル描画のみのスライドを含んでいない
- ローカル文字合成スライドを含んでいない
- QAレポートで `Final PNGs are GPT-Image2-derived: PASS` になっている

## Allowed Post-processing

完成動画では、GPT-Image2が生成した文字を採用します。以下の後処理だけを許可します。

- 1920 x 1080へのトリミング、余白調整、軽微なシャープ化を行う
- contact sheet作成やファイル名整理を行う

後処理で文字を書き換えた場合、そのスライドは完成動画に使えません。文字修正が必要な場合はGPT-Image2で再生成します。

## Prohibited Final Sources

完成動画では以下を最終スライド元にしません。

- Pillowだけで描画した図解スライド
- HTML/CSS/Canvasだけで描画したスライド
- SVGだけで作った図解スライド
- GPT-Image2画像へローカルでタイトルやラベルを合成したスライド
- プレゼンツールで手作業作成した画像
- GPT-Image2 source evidenceを保存していない画像

## Review Questions

AI-QA-01は以下を確認します。

- GPT-Image2 source PNGは保存されているか
- 最終PNGとsource PNGの対応表があるか
- 表示文字もGPT-Image2生成か
- ローカル文字合成が混ざっていないか
- ローカル描画だけのスライドが混ざっていないか
- Driveにアップロードされた動画はGPT-Image2版か
