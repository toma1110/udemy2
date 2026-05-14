# S3-L4 Script Review Report

## Target

- Lecture: Section 3 Lecture 4「AWSサービス別SLI選定ガイド」
- Script: `scripts/s3-l4_script.md`
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01

## Review Result

Pass.

## Checks

- course_spec の対象サービスである ALB、API Gateway、ECS、Lambda、RDS を扱っている
- サービス名からではなく、ユーザー操作からSLIを選ぶ方針が明確である
- Application Signalsは有力な入口として扱い、計装やデータ期間の制約も明記している
- ナレーションではAWSサービス名を読み上げ用カタカナにしている
- 初回チェックで出た「上で」の読みリスクは「環境で」に修正済み

## Validation

```bash
python3 udemy-ai-company/tools/narration_checker.py \
  udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l4_script.md \
  --warnings-ok
```

Result: OK.

## Notes

- Worker: AI-Production-01
- Reviewer: AI-QA-01
- Worker and Reviewer are separated.
