# AWS Batch Fargate Render Worker

動画生成のCPU重い処理を、AWS Batch on ECS Fargateへ逃がすための制作基盤です。

この構成は常駐ECS Serviceを作りません。Batch jobが実行されていない時間帯は、FargateのvCPU/RAM compute料金は発生しません。S3、ECR、CloudWatch Logsの保存分は微課金です。

## 作成するもの

- VPC
- Public subnet x2
- Internet Gateway
- Security Group
  - inboundなし
  - outboundのみ許可
- S3 artifact bucket
- ECR repository
- CloudWatch Logs log group
- AWS Batch Fargate compute environment
- AWS Batch job queue
- AWS Batch job definition
- IAM role
  - ECS task execution role
  - render job role

NAT Gatewayは作りません。Fargate jobはpublic subnetで起動し、`AssignPublicIp=ENABLED` でS3、ECR、CloudWatch Logsへ到達します。

## 料金方針

- AWS Batch自体の追加料金なし
- Fargate computeはjob実行中のみ課金
- Linux Fargateは秒課金、最低1分
- 追加ephemeral storageはjob実行中のみ課金
- NAT Gatewayなし
- ECS Serviceなし

## 初回構築

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 ./scripts/deploy.sh deploy
```

デフォルトのjob sizeは `4 vCPU / 8GB` です。

8 vCPUにする場合:

```bash
AWS_REGION=us-east-1 \
JOB_SIZE=vcpu8-memory16gb \
MAX_VCPUS=16 \
./scripts/deploy.sh deploy
```

## worker imageをECRへpush

このホストにDockerがない場合は、CodeBuildでbuild/pushします。

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 ./scripts/start_image_build.sh
```

Dockerがある端末から直接pushする場合:

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 ./scripts/build_and_push.sh
```

`build_and_push.sh` は `docker` が必要です。`start_image_build.sh` はローカルDocker不要です。

## 2段jobで素材をS3へアップロード

VOICEVOX音声生成とffmpeg動画生成をAWS Batch上で分ける場合は、スライドと台本だけをS3へアップロードします。WAVはVOICEVOX jobが生成します。

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 \
LECTURE_ID=s3-l5 \
./scripts/upload_two_stage_assets.sh
```

最後に `s3://.../manifest.json` が表示されます。

## 2段jobを投入

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 \
MANIFEST_S3_URI=s3://BUCKET/aws-slo-adoption-course/s3-l5-two-stage/manifest.json \
JOB_BASENAME=render-aws-slo-s3-l5-two-stage \
./scripts/submit_two_stage_jobs.sh
```

このコマンドは以下の2つを投入します。

- `*-voicevox`: `script_s3_uri` からWAVを生成し、`audio_s3_uri` へアップロード
- `*-render`: `dependsOn` でVOICEVOX job成功後に起動し、MP4とrender reportを出力

## renderのみで素材をS3へアップロード

既存の講義ディレクトリから `slides/<lecture_id>/slide_*.png` と `audio/<lecture_id>/slide_*.wav` をS3へアップロードし、manifestを作ります。

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 \
LECTURE_ID=s3-l5 \
./scripts/upload_assets.sh
```

最後に `s3://.../manifest.json` が表示されます。

## Batch jobを投入

```bash
cd udemy-ai-company/infrastructure/batch-fargate
AWS_REGION=us-east-1 \
MANIFEST_S3_URI=s3://BUCKET/aws-slo-adoption-course/s3-l5/manifest.json \
JOB_NAME=render-aws-slo-s3-l5 \
./scripts/submit_job.sh
```

## 確認

```bash
AWS_REGION=us-east-1 ./scripts/smoke_test.sh
```

jobの状態確認:

```bash
aws batch list-jobs \
  --job-queue udemy-render-queue \
  --job-status RUNNING \
  --region us-east-1
```

CloudWatch Logs:

```bash
aws logs tail /aws/batch/udemy-render/render \
  --follow \
  --region us-east-1
```

## 出力

workerはmanifestの `output_s3_uri` に以下を出力します。

- `<lecture_id>.mp4`
- `<lecture_id>_render_report.md`
- `<lecture_id>_render_report.json`

失敗した場合は可能な限り `<lecture_id>_render_report.failed.json` を出力します。

## manifest

```json
{
  "course_id": "aws-slo-adoption-course",
  "lecture_id": "s3-l5",
  "slides_s3_uri": "s3://BUCKET/aws-slo-adoption-course/s3-l5/slides/",
  "audio_s3_uri": "s3://BUCKET/aws-slo-adoption-course/s3-l5/audio/",
  "output_s3_uri": "s3://BUCKET/aws-slo-adoption-course/s3-l5/output/",
  "video": {
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "crf": 23,
    "preset": "veryfast",
    "audio_bitrate": "192k",
    "tail_padding_seconds": 0.2
  }
}
```

## 現時点のスコープ

標準は2段jobです。renderのみの経路は、既にローカルでVOICEVOX WAVを生成済みの場合の互換経路として残します。

VOICEVOX workerは公式 `voicevox/voicevox_engine:cpu-latest` をベースにしています。Docker HubからのpullとECR image pullが入るため、初回はcold startが長くなります。

## 削除

```bash
AWS_REGION=us-east-1 ./scripts/deploy.sh delete
```

S3 bucketは `Retain` です。削除する場合は中身を確認してから手動で削除してください。
