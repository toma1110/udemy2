# GPT-Image2 Prompts: s2-l3

Use a premium AWS/SRE educational visual style. 16:9 slide, clean log-analysis and incident-investigation aesthetic, white and pale blue background, navy, teal, green, amber, and restrained red accents, readable Japanese text generated directly inside the image, no logos, no watermark, no local text overlay.

## Production Rules

- All visible text must be generated directly by GPT-Image2.
- Do not use local text overlay.
- Keep one clear message per slide.
- Prefer diagrams, query cards, timelines, and troubleshooting flows over decorative art.

## slide_001.png

Create a Japanese course slide. Large title: `追跡する`. Subtitle: `1つのリクエストを時系列で見る`. Visual: Timeline for one request across services; requestId as thread. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_002.png

Create a Japanese course slide. Large title: `JSONログ`. Subtitle: `フィールドがあればそのまま使う`. Visual: JSON log fields auto-discovered; requestId, service, durationMs. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_003.png

Create a Japanese course slide. Large title: `parse`. Subtitle: `文字列から値を取り出す`. Visual: Raw message transformed into fields; parse command as extractor. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_004.png

Create a Japanese course slide. Large title: `requestId`. Subtitle: `同じキーで出来事をつなぐ`. Visual: Same requestId connecting multiple log events; Start, service, error, end. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_005.png

Create a Japanese course slide. Large title: `dedup`. Subtitle: `同じ対象の重複を抑える`. Visual: Duplicate request rows collapsed; dedup requestId. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_006.png

Create a Japanese course slide. Large title: `時系列で読む`. Subtitle: `ascで古い順に並べる`. Visual: Ascending timeline; Root cause path. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.
