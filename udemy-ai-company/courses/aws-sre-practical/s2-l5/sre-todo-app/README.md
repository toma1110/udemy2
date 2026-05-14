# sre-todo-app

Section 2 Lecture 5 のハンズオンで使う Flask 製 TODO アプリです。

AWS では EC2 上で起動し、RDS MySQL に TODO データを保存します。ローカル確認時は `DB_HOST` を設定しなければ SQLite を使います。

## ローカル起動

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

ブラウザで `http://127.0.0.1:5000` を開きます。

## EC2 での起動

```bash
git clone https://github.com/<your-account>/sre-todo-app.git
cd sre-todo-app
pip3 install -r requirements.txt

export DB_HOST="<CloudFormation Outputs の RDS エンドポイント>"
export DB_USER="admin"
export DB_PASSWORD="<RDS のパスワード>"
export DB_NAME="sreapp"

python3 app.py
```

## 環境変数

| 変数 | デフォルト | 説明 |
|---|---|---|
| `APP_PORT` | `5000` | Flask の待受ポート |
| `DB_HOST` | 未設定 | RDS MySQL のホスト名。未設定なら SQLite |
| `DB_PORT` | `3306` | MySQL ポート |
| `DB_USER` | `admin` | MySQL ユーザー |
| `DB_PASSWORD` | 未設定 | MySQL パスワード |
| `DB_NAME` | `sreapp` | MySQL データベース名 |
| `XRAY_ENABLED` | `true` | X-Ray SDK の初期化有無 |

## GitHub リポジトリ作成

このディレクトリを GitHub に公開する場合は以下を実行します。

```bash
git remote add origin https://github.com/<your-account>/sre-todo-app.git
git branch -M main
git push -u origin main
```

