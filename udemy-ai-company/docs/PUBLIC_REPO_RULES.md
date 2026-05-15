# PUBLIC_REPO_RULES

## 目的

Publicリポジトリ用の作業コピーを一箇所に集約し、講座制作素材、内部運用ファイル、公開配布物が混ざらないようにする。

## 標準配置

Publicリポジトリ用のフォルダは必ず以下に作成する。

```text
udemy-ai-company/public_repo/<repo-name>/
```

例:

```text
udemy-ai-company/public_repo/sre-slo-introduction-cfn-templates/
```

## 禁止配置

以下にPublicリポジトリの作業コピーを直接作成しない。

- `udemy2/<repo-name>/`
- `udemy-ai-company/courses/<course>/`
- `udemy-ai-company/infrastructure/`
- `udemy-ai-company/tools/`

`courses/` は講座のSource of Truth、制作素材、QAレポートを置く場所であり、Publicリポジトリそのものを置く場所ではない。

## 親リポジトリとの関係

`public_repo/` 配下の各Publicリポジトリは、それぞれ独立したGitリポジトリとして扱う。

親の `udemy2` リポジトリには、Publicリポジトリ本体のファイルを取り込まない。親リポジトリへ残すのは、この運用ルールと必要な参照情報だけにする。

## 作業ルール

- Publicリポジトリ作業もGitHub Issueに紐づける
- 作業前に対象講座の `course_spec.md`、ハンズオンREADME、関連QAレポートを確認する
- 公開用README、テンプレート、検証スクリプトは受講者が単体で理解できる内容にする
- PublicリポジトリのREADMEは原則として日本語で書く
- CloudFormationテンプレートを公開する場合は、コスト注意、作成手順、検証手順、削除手順、トラブルシューティングを含める
- README、CLI、補助ドキュメントは実テンプレートと一致させる。スタック名、Outputs、Parameters、アラーム名、ロググループ名、アプリ名、systemdサービス名、ポート番号、環境変数、手動/自動セットアップの違いを古い説明のまま残さない
- CloudFormation UserData等でアプリを自動作成する場合、Publicリポジトリには不要な `git clone`、手動依存ライブラリ導入、古いサンプルアプリ名を手順として残さない
- `git push`、release作成、外部公開状態変更を行った場合は、対象Issueにcommit SHA、公開URL、実行ログ、検証結果を記録する

## 補助図解ルール

Publicリポジトリでハンズオン理解を助ける図解を置く場合は、完成動画素材とは別物として扱う。

- Publicリポジトリの補助資料では、Markdown、draw.io、PNGを使ってよい
- draw.ioを置く場合は、GitHub上で直接確認できるようPNGを書き出し、該当Markdownに埋め込む
- draw.ioソースとPNGの両方をcommitし、図解の更新時は両方を同期する
- draw.io XMLのwell-formedness、可能なら専用validator、Markdown相対リンク、PNG表示を確認する
- 図解内のリソース名、データフロー、スタック番号、CLI手順は実テンプレートと矛盾させない
- 図解の線ラベルや注釈が多すぎて読めない場合は、Markdown本文へ説明を逃がす
- Publicリポジトリに、内部制作向け注意書きやレビューメモを公開しない。例: 「完成動画へ流用する場合はGPT-Image2由来PNGで作り直す」といった制作会社向け注意はIssue、QAレポート、社内docsへ記録する
- Publicリポジトリの補助図解を完成動画へ使う場合は、そのまま流用せず、`docs/GPT_IMAGE_RULES.md` に従ってGPT-Image2由来PNGとして作り直す

## 検証ルール

Publicリポジトリへ反映する前に、少なくとも以下を確認する。

- shellスクリプトがある場合は `bash -n`
- CloudFormationテンプレートがある場合は `aws cloudformation validate-template`
- READMEの手順と実ファイル名、環境変数、スタック名が一致している
- README、CLI、補助ドキュメントに、古いアプリ名、古いアラーム名、古いOutput名、不要な手動セットアップ手順が残っていない
- draw.io図解を追加した場合は、PNGがMarkdownに埋め込まれておりGitHub上で確認できる
- 課金リソースを作成するフル検証を実行した場合は、作成、更新、削除の結果を検証レポートに残す
- 課金リソースを作成する検証を省略した場合は、省略理由と代替検証結果を明記する

## 現在のPublicリポジトリ

| リポジトリ | ローカル配置 | 用途 |
| --- | --- | --- |
| `toma1110/sre-slo-introduction-cfn-templates` | `udemy-ai-company/public_repo/sre-slo-introduction-cfn-templates/` | SLO入門講座のCloudFormationハンズオン公開テンプレート |
