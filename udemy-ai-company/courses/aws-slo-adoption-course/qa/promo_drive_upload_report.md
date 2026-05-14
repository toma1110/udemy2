# Promo Drive Upload Report

## Target

- Issue: #126 / TASK-0119
- Asset: Promo video
- Local file: `video/promo/promo.30fps.mp4`
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## Result

Pass.

## Google Drive

- File name: `promo_slo_course_20260513.mp4`
- File ID: `1L4rjbl2zXEE0z3fML-xlttIBZxO_ghRy`
- URL: https://drive.google.com/file/d/1L4rjbl2zXEE0z3fML-xlttIBZxO_ghRy/view?usp=drivesdk
- Size: 41083237 bytes
- Trashed: false
- Sharing: anyone reader true
- Metadata verified: 2026-05-13

## Notes

- `video/promo/drive_upload.json` にDriveメタデータを保存済み。
- CEO ReviewはローカルMP4では成立しないため、Google Drive URLをレビュー入力として扱う。
- Worker != Reviewer: pass.
