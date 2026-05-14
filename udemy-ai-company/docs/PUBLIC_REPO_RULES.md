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
- `git push`、release作成、外部公開状態変更を行った場合は、対象Issueにcommit SHA、公開URL、実行ログ、検証結果を記録する

## 検証ルール

Publicリポジトリへ反映する前に、少なくとも以下を確認する。

- shellスクリプトがある場合は `bash -n`
- CloudFormationテンプレートがある場合は `aws cloudformation validate-template`
- READMEの手順と実ファイル名、環境変数、スタック名が一致している
- 課金リソースを作成するフル検証を実行した場合は、作成、更新、削除の結果を検証レポートに残す
- 課金リソースを作成する検証を省略した場合は、省略理由と代替検証結果を明記する

## 現在のPublicリポジトリ

| リポジトリ | ローカル配置 | 用途 |
| --- | --- | --- |
| `toma1110/sre-slo-introduction-cfn-templates` | `udemy-ai-company/public_repo/sre-slo-introduction-cfn-templates/` | SLO入門講座のCloudFormationハンズオン公開テンプレート |
