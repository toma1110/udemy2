# GPT-Image2 Prompts: s1-l3

Use a premium AWS/SRE educational visual style. 16:9 slide, clean log-analysis and incident-investigation aesthetic, white and pale blue background, navy, teal, green, amber, and restrained red accents, readable Japanese text generated directly inside the image, no logos, no watermark, no local text overlay.

## Production Rules

- All visible text must be generated directly by GPT-Image2.
- Do not use local text overlay.
- Keep one clear message per slide.
- Prefer diagrams, query cards, timelines, and troubleshooting flows over decorative art.

## slide_001.png

Create a Japanese course slide. Large title: `基本構文`. Subtitle: `表示、絞り込み、並べ替え、件数制限`. Visual: Query pipeline with four commands; fields filter sort limit. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_002.png

Create a Japanese course slide. Large title: `fields`. Subtitle: `見たい列を選ぶ`. Visual: Select columns from log event; @timestamp, @message, @logStream. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_003.png

Create a Japanese course slide. Large title: `filter`. Subtitle: `必要な行だけに絞る`. Visual: Many rows filtered into error rows; ERROR, statusCode >= 500, timeout. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_004.png

Create a Japanese course slide. Large title: `sortとlimit`. Subtitle: `新しい順に、小さく見る`. Visual: Latest logs first; limit 50 as guardrail. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_005.png

Create a Japanese course slide. Large title: `pipeでつなぐ`. Subtitle: `クエリは左から順に処理される`. Visual: Pipe character between command blocks; Left to right processing. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_006.png

Create a Japanese course slide. Large title: `最初のクエリ`. Subtitle: `直近ログを見る型を持つ`. Visual: Query card for recent events; Result table preview. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.
