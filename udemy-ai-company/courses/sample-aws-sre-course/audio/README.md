# audio

VOICEVOXで生成した音声素材を配置します。

## ルール

- 台本と音声の対応を崩さない
- 再生成時は対象レッスンと理由を記録する
- 技術用語の読み方をQAで確認する
- VOICEVOX起動確認後に生成する
- gTTSなど別音声フォールバックを本番成果物に使わない

## 命名規則

```text
lesson_001.wav
lesson_002.wav
```

## 注意

音声だけを修正した場合も、動画手順や台本との整合性を確認します。

## VOICEVOX起動確認

```bash
curl -s http://localhost:50021/version
```
