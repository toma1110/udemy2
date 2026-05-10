# aws-slo-adoption-course

この講座は、SREを目指すエンジニアがAWS上でSLO導入を実践できるようになるための講座です。

## Source of Truth

[course_spec.md](course_spec.md) を唯一の真実として扱います。

## 制作方針

- CloudFormationを原則とする
- SLOは概念だけでなく、計測、可視化、通知、組織導入まで扱う
- CloudWatch Application Signalsの現行SLO機能を扱う
- ただし30日データや実アプリ計装が必要な機能は補講/デモとして扱う
- VOICEVOX読み上げでは `SLO` を「エスエルオー」、`SLI` を「エスエルアイ」に統一する

## 次の作業

1. AI-QA-01が `course_spec.md` をレビューする
2. 承認後、AI-Strategy-01が講義単位のTask Issueへ分解する
3. AI-Engineer-01がCloudFormationハンズオン範囲を実装する
4. AI-Production-01がスライド、台本、VOICEVOX素材を作る
