# VIDEO_QUALITY_BASELINE

## Purpose

完成動画の見た目と制作品質を、VID-001のGPT-Image2版と同等以上に保つための基準です。

## Current Reference

- Reference course: `aws-cloudwatch-intro-course`
- Reference lecture: `s1-l1`
- Reference Drive file: `vid001-cloudwatch-intro-s1-l1-gptimage2-text-20260514.mp4`
- Reference Drive URL: https://drive.google.com/file/d/1JzSBq-AtW2JkA96w8AQWTLuU_B2gZwsv/view?usp=drivesdk
- Reference report: `courses/aws-cloudwatch-intro-course/qa/s1-l1_slide_generation_report.md`
- Reference contact sheet: `courses/aws-cloudwatch-intro-course/slides/s1-l1/contact_sheet.png`

## Mandatory Baseline

- 最終スライドPNGはGPT-Image2由来である
- タイトル、見出し、短いラベル、図解内テキストもGPT-Image2生成である
- ローカル文字合成、Pillow文字描画、HTML/SVG/Canvas文字合成を完成動画に使わない
- GPT-Image2 source PNGを `slides/<section>-gpt-image2-sources/<lecture>/` に保存する
- 最終PNGは1920 x 1080で、contact sheetを作る
- 文字修正が必要な場合はローカル編集ではなくGPT-Image2で再生成する
- Driveアップロード後、anyone-reader共有とURLをQAレポートへ残す

## Visual Quality Checks

AI-QA-01は以下を確認します。

- VID-001基準と比べて、情報密度、余白、コントラスト、色の深みが明らかに落ちていない
- タイトルは一目で読める
- ラベルは小さすぎず、動画視聴サイズでも読める
- 画面が単調な一色に寄りすぎていない
- 図解が講義内容を補助している
- 不要なロゴ、透かし、意味不明な文字列が目立たない
- contact sheetで全体トーンがそろっている

## Regeneration Rules

以下の場合、そのスライドは完成動画に使わず、GPT-Image2で再生成します。

- タイトルが崩れている
- 重要ラベルが読めない
- ローカルで文字を書き換える必要がある
- 図解の意味が台本と矛盾している
- VID-001基準より明らかに品質が低い

## Reporting

各Lectureの `*_slide_generation_report.md` には以下を記録します。

- GPT-Image2 prompt file
- GPT-Image2 source PNG directory
- Final PNG directory
- Source to final mapping
- Contact sheet path
- VID-001 baseline comparison result
- Local text overlay absent: PASS/FAIL
