# Codex への指示: AWS構成図スライドのフレームを GPT Image 2 で生成する

これは `udemy/skills/slide-image-generation/SKILL.md` の **Step 3-B（フレーム枠生成）** の検証タスク。
GPT Image 2（あなたが内蔵で持つ imagegen ツール）で 1920×1080 PNG を 1 枚生成して、指定パスに保存してほしい。

## 出力先

```
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s2-l5/slides/sample-aws-arch/slide-aws.frame.png
```

## 必読の固定仕様

生成前に必ず以下を読み、配色・レイアウトのルールを反映すること:

```
/home/ubuntu/workspace/udemy/templates/prompts/image_system.md
```

## 画像内容

- 解像度: **1920 × 1080 px** (16:9, PNG)
- 全面ベース色: `#1a1a2e`（深いダークネイビー）。ごく弱いグラデならOK
- セーフエリア: 上下左右 80px

### 上部タイトル帯（高さ約 140 px）
- メインタイトル: `ハンズオン: サンプルWebアプリを本番想定でデプロイ`
  - 色: オレンジ `#FF9900`、太字、大きめ
- サブタイトル: `Section 2 - Lecture 5`
  - 色: ライトブルー `#58A6FF`、小さめ

### 中央エリア (横 1500 × 縦 800 px、画面中央配置)
- **完全に空白**。何も描かない。装飾・図形・アイコン・薄い模様も入れない
- ここには後で AWS 構成図（drawio製の透過PNG）が Pillow で重ねられる
- 背景色とまったく同じ（`#1a1a2e`）でフラットにしておくこと

### 右下出典帯（高さ約 60 px、右寄せ）
- テキスト: `詳細コマンド: github.com/toma1110/aws-sre-cfn-templates/blob/main/CLI_COMMANDS.md`
- 色: ミュート `#9696AA`、小さめ

## 禁則

- 中央エリアにいかなるアイコン・図形・テキスト・装飾も描かない
- AWS のサービスアイコン・ロゴを描かない（構成図本体は別レイヤーで描画する）
- 派手な色をブランドカラー以外で使わない
- 写真リアル・実在人物に似せた表現はしない

## 実行

1. 上記仕様で **GPT Image 2 を1回呼び出して** PNG を生成する
2. 指定パスに保存する
3. 完了後、以下を `/tmp/codex-frame-result.txt` に書き出す:
   ```
   STATUS: ok
   PATH: /home/ubuntu/workspace/udemy/courses/aws-sre-practical/s2-l5/slides/sample-aws-arch/slide-aws.frame.png
   SIZE: <出力PNGの実サイズ>
   PROMPT: <imagegenに実際渡した最終プロンプト全文>
   ```

完了したら `/tmp/codex-frame-result.txt` の内容を返答してくれれば OK。
