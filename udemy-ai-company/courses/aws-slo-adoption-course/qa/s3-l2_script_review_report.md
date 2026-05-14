# S3-L2 Script Review Report

## Target

- Lecture: Section 3 Lecture 2「可用性、レイテンシ、エラー率を設計する」
- Script: `scripts/s3-l2_script.md`
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01

## Review Result

Pass.

## Checks

- 可用性、レイテンシ、エラー率をユーザー体験の3分解として説明している
- 分母、分子、対象リクエスト、目標水準の設計順序が明確である
- 4系、5系、パーセンタイルはVOICEVOX向けに読み下している
- 8スライド構成で、S3-L3のパーセンタイル講義へ接続している

## Validation

```bash
python3 udemy-ai-company/tools/narration_checker.py \
  udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l2_script.md \
  --warnings-ok
```

Result: OK.

## Notes

- Worker: AI-Production-01
- Reviewer: AI-QA-01
- Worker and Reviewer are separated.
