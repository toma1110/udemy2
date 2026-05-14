# CLI_COMMANDS

このファイルは、動画内では長くて表示しきれない CLI コマンドの参照用です。

セクション2 レクチャー5のハンズオンでは、CloudWatch Agent と X-Ray の設定コマンドもここにまとめています。動画内の図では一部を短縮表示しているため、実際に実行する場合はこのファイルのコマンドを確認してください。

## Section 2 Lecture 5: Flask TODO App

EC2 に SSH 接続したあと、GitHub からサンプルアプリを取得して起動します。

```bash
# サンプルアプリを取得
cd /home/ec2-user
git clone https://github.com/toma1110/sre-todo-app.git
cd sre-todo-app

# 依存ライブラリをインストール
pip3 install -r requirements.txt

# CloudFormation Outputs の RDS エンドポイントを指定
export DB_HOST="<RDSエンドポイント>"
export DB_PORT="3306"
export DB_USER="admin"
export DB_PASSWORD="<RDSのパスワード>"
export DB_NAME="sreapp"

# Flaskアプリを起動
python3 app.py
```

ブラウザから ALB の DNS 名にアクセスして TODO アプリが表示されれば成功です。

動作確認用のエンドポイントです。

```bash
curl http://localhost:5000/health
```

## Section 2 Lecture 5: CloudWatch Agent

`01-base-infrastructure.yaml` で作成する EC2 には、CloudWatch Agent 用の IAM ポリシーと Agent 設定が含まれています。手動で確認・再設定する場合は以下を使います。

```bash
# Agent の状態確認
sudo systemctl status amazon-cloudwatch-agent --no-pager

# 設定ファイル確認
sudo cat /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

# 設定を再読み込みして Agent を起動
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
  -s

# ログ確認
sudo tail -f /opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log
```

CloudWatch 側では、名前空間 `CWAgent` に `mem_used_percent` と `disk_used_percent` が届いているか確認します。

## Section 2 Lecture 5: X-Ray

X-Ray を使う場合は、EC2 の IAM ロールに X-Ray 送信用ポリシーを付けたうえで、アプリ側に X-Ray SDK の計装を追加します。

```bash
# EC2 ロールに X-Ray 書き込み権限を付与
aws iam attach-role-policy \
  --role-name sre-handson-app-role \
  --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess

# Python アプリで使う SDK をインストール
pip3 install aws-xray-sdk

# アプリ再起動後、X-Ray のサービスグラフを確認
aws xray get-service-graph \
  --start-time "$(date -u -d '15 minutes ago' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --region ap-northeast-1
```

Flask アプリに追加する最小の計装例です。

```python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_recorder.configure(service="sre-todo-app")
XRayMiddleware(app, xray_recorder)
```
