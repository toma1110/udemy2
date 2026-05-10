# scripts

動画台本を配置します。

## ルール

- VOICEVOXで自然に読める日本語にする
- コマンドやリソース名は聞き取りやすく説明する
- READMEと異なる手順を書かない
- 技術的な断定はCloudFormationテンプレートと照合する
- `docs/VOICEVOX_RULES.md` に従い、英字、空白付きサービス名、カッコふりがなを避ける
- 音声生成前に `tools/narration_checker.py` を実行する

## 命名規則

```text
lesson_001_script.md
lesson_002_script.md
```

## レビュー観点

- `course_spec.md` の学習目標に対応している
- 初学者が置いていかれない
- 手順と説明が一致している
- 読み上げに不自然な長文がない
- `ステップ 5` ではなく `ステップ5` になっている
- `AWS CLI` などの英字語が読み上げ用に処理されている

## チェックコマンド

```bash
python3 ../../../tools/narration_checker.py .
```
