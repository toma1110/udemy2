# GPT-Image2 Prompts: s2-l2

Use a premium AWS/SRE educational visual style. 16:9 slide, clean log-analysis and incident-investigation aesthetic, white and pale blue background, navy, teal, green, amber, and restrained red accents, readable Japanese text generated directly inside the image, no logos, no watermark, no local text overlay.

## Production Rules

- All visible text must be generated directly by GPT-Image2.
- Do not use local text overlay.
- Keep one clear message per slide.
- Prefer diagrams, query cards, timelines, and troubleshooting flows over decorative art.

## slide_001.png

Create a Japanese course slide. Large title: `傾向を見る`. Subtitle: `件数を時間帯でまとめる`. Visual: Error count trend chart; stats and bin blocks. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_002.png

Create a Japanese course slide. Large title: `count by bin`. Subtitle: `5分ごとの件数を見る`. Visual: count(*) by bin(5m); Time buckets with bars. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_003.png

Create a Japanese course slide. Large title: `上位エラー`. Subtitle: `多い種類から見る`. Visual: Top error types table; service and errorType columns. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_004.png

Create a Japanese course slide. Large title: `遅延を見る`. Subtitle: `平均だけでなくp95とp99を見る`. Visual: Latency percentile chart; p95 and p99 highlighted. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_005.png

Create a Japanese course slide. Large title: `binの注意`. Subtitle: `300sではなく5mを使う`. Visual: Correct bin(5m), avoid bin(300s); Small warning callout. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_006.png

Create a Japanese course slide. Large title: `読み方`. Subtitle: `いつ、何が、どれだけ増えたか`. Visual: Aggregate result to request trace transition; When, what, how much. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.
