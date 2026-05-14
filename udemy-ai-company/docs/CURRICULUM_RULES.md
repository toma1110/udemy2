# CURRICULUM_RULES

## 目的

Udemyのコースカリキュラム作成時に、各レクチャーの目的、受講後に身につくこと、ハンズオン有無、PublicRepo URLを一貫して管理する。

`course_curriculum.md` は、Udemy登録画面へ入力するレクチャー構成の作業台帳であり、動画制作、台本作成、ハンズオンREADME、PublicRepo配布物の整合性確認にも使う。

## 必須ファイル

各講座には、以下を作成する。

```text
courses/<course-name>/course_curriculum.md
```

## Source of Truth

`course_curriculum.md` は以下と矛盾してはいけない。

- `course_spec.md`
- `lectures.md`
- `course_infomation.md`
- ハンズオンREADME
- PublicRepoのREADME、テンプレート、スクリプト
- 完成動画の台本、スライド、動画内手順

矛盾がある場合は、`course_spec.md` を最優先し、必要に応じてChange Requestを作成する。

## 必須項目

各レクチャーには、必ず以下を記載する。

| 項目 | 内容 |
| --- | --- |
| Section | セクション番号 |
| Lecture | セクション内のレクチャー番号 |
| レクチャータイトル | Udemyに表示するレクチャータイトル |
| レクチャー完了後に身についていること | 受講者がレクチャー後に説明、判断、実行できること |
| ハンズオン | `なし` または `あり: <PublicRepo URL>` |

## ハンズオンURLルール

ハンズオンがあるレクチャーでは、PublicRepo URLを必ず記載する。

推奨するURL粒度:

- 講座全体の導入、構成説明: PublicRepoルートURL
- テンプレート説明: 対象テンプレートファイルURL
- コマンド実行: READMEの該当セクションURL
- 検証、smoke test、削除: 対象スクリプトファイルURLまたはREADME該当セクションURL

PublicRepo作業コピーは必ず以下に置く。

```text
udemy-ai-company/public_repo/<repo-name>/
```

PublicRepoを `courses/` 配下や親リポジトリ直下に作成しない。

## レクチャー内容の書き方

`レクチャー完了後に身についていること` は、受講者視点で書く。

よい例:

- SLI、SLO、SLAの違いを整理し、それぞれの役割を説明できる
- READMEに沿ってCloudFormationスタックを作成し、作成されたリソースを確認できる
- エラーバジェットをリリース判断や改善優先度に結びつけて説明できる

避ける例:

- SLOについて説明する
- CloudFormationをやる
- 重要な内容

## 作成タイミング

`course_curriculum.md` は、`course_spec.md` と `lectures.md` が確定した後、台本と動画制作に入る前に作成する。

ハンズオン内容、PublicRepo名、README構成が変更された場合は、`course_curriculum.md` も同時に更新する。

## 品質ゲート

- 全レクチャーが `lectures.md` と一致している
- セクション番号、レクチャー番号、タイトルが欠けていない
- 各レクチャーの到達状態が受講者視点で書かれている
- ハンズオンありの行にPublicRepo URLがある
- ハンズオンなしの行に誤ってPublicRepo URLを書いていない
- PublicRepo URLが実在する配布物を指している
- `course_infomation.md`、README、動画内手順と矛盾していない
- WorkerとReviewerが別AIである

## テンプレート

新規講座では、以下をコピーして作成する。

```text
templates/course_curriculum_template.md
```
