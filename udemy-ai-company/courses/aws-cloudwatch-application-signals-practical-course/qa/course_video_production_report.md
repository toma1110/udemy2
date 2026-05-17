# Course Video Production Report

Course: `aws-cloudwatch-application-signals-practical-course`
Date: 2026-05-17
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01
Status: Pass for runtime-remediated normal lecture videos

## Summary

- 通常レクチャー動画: 11本
- プロモーション動画: 既存2026-05-16版を維持
- GPT-Image2由来完成PNG: 通常レクチャー66枚を使用
- VOICEVOX音声: 通常レクチャー66本を2026-05-17に再生成
- 通常レクチャー合計動画時間: 2049.580秒、約34.16分
- 全MP4: faststart true
- 全MP4: decode check OK during build
- AWS CloudFormation create/update/delete/fullは未実行

## Produced Normal Lecture Videos

| Lecture | Title | Audio Count | Audio sec | Video sec | Video mm:ss | Faststart | MP4 Size bytes |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: |
| `s1-l1` | Application Signalsで何が見えるか | 6 | 200.427 | 200.448 | 3:20 | True | 8501365 |
| `s1-l2` | ハンズオン構成とコスト安全策 | 6 | 201.984 | 202.005 | 3:22 | True | 8512150 |
| `s2-l1` | テンプレート全体を読む | 6 | 196.064 | 196.085 | 3:16 | True | 8285049 |
| `s2-l2` | サンプルアプリと低頻度トラフィックをデプロイする | 6 | 193.760 | 193.781 | 3:14 | True | 8258186 |
| `s2-l3` | 正常、遅延、エラーのシナリオを切り替える | 6 | 185.216 | 185.237 | 3:05 | True | 8076219 |
| `s3-l1` | Servicesで状態を見る | 6 | 178.315 | 178.336 | 2:58 | True | 7826041 |
| `s3-l2` | Application Mapで依存関係を見る | 6 | 177.045 | 177.066 | 2:57 | True | 7901163 |
| `s3-l3` | Service detailでLatency、Fault、Errorを読む | 6 | 169.003 | 169.025 | 2:49 | True | 7777067 |
| `s4-l1` | Application Signals SLOを作る | 6 | 185.259 | 185.280 | 3:05 | True | 8103003 |
| `s4-l2` | SLO RecommendationsとPerformance Reportの前提 | 6 | 183.136 | 183.157 | 3:03 | True | 8082164 |
| `s4-l3` | 後片付け、停止、コスト確認 | 6 | 179.136 | 179.157 | 2:59 | True | 7930085 |

## Verification

| Check | Result |
| --- | --- |
| `tools/narration_checker.py scripts` | PASS |
| Voice files for all normal lecture script slides | PASS |
| Final slide PNG count for normal lectures | PASS: 66 |
| Normal lecture video count | PASS: 11 |
| Main lecture runtime over 30 minutes | PASS |
| FFmpeg decode validation for all rebuilt MP4 | PASS |
| `build_report.json` exists for all normal lecture MP4 | PASS |
| AWS resource mutation | PASS: not performed |

## Notes

- 完成動画用スライドは既存GPT-Image2由来PNGを使用した。
- ローカル文字合成スライドは使用していない。
- プロモーション動画は30分要件に含めていない。
- 本レポートは制作担当の完了報告であり、Worker/Reviewer分離のためAI-QA-01レビュー扱いの証跡を別途Driveレポートにも残す。
