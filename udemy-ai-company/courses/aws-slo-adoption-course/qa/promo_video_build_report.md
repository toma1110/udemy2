# Promo Video Build Report

## Summary

- Course: AWSで学ぶSLO導入実践：SLI設計・エラーバジェット・SRE運用レビュー
- Asset ID: `promo`
- Output: `courses/aws-slo-adoption-course/video/promo/promo.30fps.mp4`
- Current version: GPT Image2 regenerated version from TASK-0120
- Purpose: Udemy course promotional video
- Structure: 1本構成、約90秒

## Effective Promo Structure

1. Hook: SLOを、説明できる状態から運用できる状態へ
2. Problem: 監視はあるが、判断基準が説明できない
3. Value: SLI、SLO、エラーバジェット、バーンレートを一気通貫で扱う
4. AWS implementation: CloudFormationでCloudWatch、SNS、Dashboardを作り、SLOの計測、可視化、通知を具体化する
5. Current AWS: Application Signals SLOの使いどころと制約を扱う
6. Audience: SRE志向、インフラ、バックエンド、運用改善担当
7. Outcome: 自分のサービスで最初のSLOを設計し、説明できる

## Generated Assets

- Script JSON: `courses/aws-slo-adoption-course/scripts/promo_video_script.json`
- Script Markdown: `courses/aws-slo-adoption-course/scripts/promo_video_script.md`
- Slide PNGs: `courses/aws-slo-adoption-course/slides/promo/slide_001.png` to `slide_007.png`
- Contact sheet: `courses/aws-slo-adoption-course/slides/promo/contact_sheet.png`
- VOICEVOX audio: `courses/aws-slo-adoption-course/audio/promo/slide_001.wav` to `slide_007.wav`
- Video: `courses/aws-slo-adoption-course/video/promo/promo.30fps.mp4`
- Frame check: `courses/aws-slo-adoption-course/video/promo/frame_check_30fps_43s.png`
- Google Drive metadata: `courses/aws-slo-adoption-course/video/promo/drive_upload.json`
- Google Drive URL: https://drive.google.com/file/d/1L4rjbl2zXEE0z3fML-xlttIBZxO_ghRy/view?usp=drivesdk
- New Google Drive metadata: `courses/aws-slo-adoption-course/video/promo/drive_upload_gpt_image2.json`
- New Google Drive URL: https://drive.google.com/file/d/15IlfcpRWIxstWpieUOuSHRkQsj3HU_xw/view?usp=drivesdk

## Validation

- JSON syntax: pass
- Renderer syntax: pass
- Narration risk check: pass, 0 issues
- VOICEVOX Engine: pass, version `0.25.1`
- Slide count: 7
- Audio count: 7
- Duration: 87.933333 seconds
- Resolution: 1920x1080
- Aspect ratio: 16:9
- Motion: subtle zoom, encoded as 30 fps
- Video codec: H.264
- Audio codec: AAC stereo
- File size: 9415237 bytes
- Faststart: true
- Decode validation: pass

## Notes

- Udemy公式情報では、プロモーション動画はコース紹介ページの Promotional video セクションへアップロードする単一動画として扱われます。
- Udemyのビデオ基準に合わせ、HD以上、16:9、音声と連動したカスタム映像で作成しています。
- 30 fpsの直接動的エンコードはEC2上で途中終了したため、6 fpsで軽いズーム付き動画を生成し、最終ファイルを30 fpsへ再エンコードしています。
- CEO確認用にGoogle Driveへアップロード済みです。
- TASK-0120でGPT Image2版スライドへ再生成済みです。
- TASK-0121で、コースタイトルとpromo台本をSLO導入・運用主語へ更新しました。既存MP4は自動更新されないため、旧タイトルが画面表示されるpromo動画は公開前に再レンダリング対象です。
- 現時点ではUdemyへのアップロードは未実施です。

## Official References

- https://support.udemy.com/hc/en-us/articles/229232387
- https://support.udemy.com/hc/en-us/articles/229232767-Video-Standards
- https://support.udemy.com/hc/en-us/articles/229604988-Udemy-Course-Quality-Checklist
