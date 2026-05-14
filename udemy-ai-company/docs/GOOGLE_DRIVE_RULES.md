# GOOGLE_DRIVE_RULES

Google Driveにアップロードした動画成果物の管理ルールです。

## 基本方針

- Google Driveには、CEO確認またはQA確認に必要な動画だけを残す。
- CEO確認またはQA確認に必要な動画は、ローカルQA通過後に事前承認を求めずGoogle Driveへアップロードする。
- Google Driveへのレビュー用アップロードは公開ではなく確認導線であり、Issueコメントと `drive_upload.json` に必ず記録する。
- レビュー用アップロードでは、CEOがブラウザで見られるように `anyone reader` 共有を付ける。
- NG判定、品質ゲートBlocked、取り違え、重複アップロードの動画は、原因と対象IDを記録してから削除する。
- 削除は原則としてDrive APIの `trashed=true` によるゴミ箱移動とする。
- 完全削除はCEOが明示した場合だけ行う。
- 新しい修正版をアップロードする前に、古いNG版の扱いをIssueに記録する。

## レビュー用アップロード

AI-Production-01またはAI-Ops-01は、動画ビルドと最低限のデコード確認が通った時点で、CEOに確認を求める前にGoogle Driveへアップロードする。

アップロード後に以下を記録する。

- Drive file ID
- Drive URL
- ファイル名
- サイズ
- `trashed: false`
- `anyone reader` 共有
- ローカルMP4パス
- `drive_upload.json` パス

Udemyへの公開、外部投稿、最終承認済みDrive成果物の差し替えや削除は、引き続きCEO承認を必要とする。

## NG動画の削除条件

以下のいずれかに該当する動画は、Google Driveから削除対象にする。

- CEOがNGと判断した
- 品質ゲートでBlockedになった
- 誤った生成方法、誤った音声、誤ったスライド、誤ったファイル名でアップロードされた
- 同じ講義の古い版で、最新版と混同するリスクがある
- Drive URLをIssueに出した後、最終成果物ではないことが確定した

## 削除前チェック

AI-Ops-01は削除前に以下を確認する。

- 削除対象のDrive file ID
- ファイル名
- 講義ID
- 削除理由
- 関連Issue
- 代替となる最新版の有無

## 削除後チェック

削除後は以下をQAレポートに残す。

- `trashed: true` が確認できたこと
- 削除実行日時
- 実行者AI
- 対象ファイルID
- 関連IssueへのコメントURL

## 禁止事項

- ID確認なしでDriveファイルを削除しない
- 同名ファイル検索だけで削除しない
- 最終承認済み動画をCEO承認なしに削除しない
- ゴミ箱移動と完全削除を混同しない
