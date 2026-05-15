# CLI_COMMANDS

このファイルは、動画内では長くて表示しきれない CLI コマンドの参照用です。

セクション2 レクチャー5のハンズオンでは、CloudWatch Agent と X-Ray の設定コマンドもここにまとめています。動画内の図では一部を短縮表示しているため、実際に実行する場合はこのファイルのコマンドを確認してください。

## Section 2 Lecture 5: エラー率デモアプリ

`01-base-infrastructure.yaml` で作成する EC2 には、エラー率デモアプリ、systemd サービス、CloudWatch Agent 設定が UserData で自動作成されます。
GitHub からアプリを clone したり、手動で依存ライブラリを入れたりする必要はありません。

```bash
# EC2 に SSH 接続
ssh -i ~/.ssh/your-key-pair.pem ec2-user@<EC2-Public-IP>

# アプリ本体の確認
ls -la /home/ec2-user/app/app.py

# systemd サービスの確認
sudo systemctl status todo-app --no-pager

# ログ確認
sudo tail -f /var/log/todo-app.log
```

ブラウザから ALB の DNS 名にアクセスして JSON レスポンスが表示されれば成功です。

動作確認用のエンドポイントです。

```bash
curl http://localhost:8080/
curl http://localhost:8080/api/data
curl http://localhost:8080/api/process
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

X-Ray を使う場合、`01-base-infrastructure.yaml` が EC2 の IAM ロールとアプリ側の X-Ray SDK 計装を自動設定します。

```bash
# X-Ray のサービスグラフを確認
aws xray get-service-graph \
  --start-time "$(date -u -d '15 minutes ago' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --region ap-northeast-1
```
