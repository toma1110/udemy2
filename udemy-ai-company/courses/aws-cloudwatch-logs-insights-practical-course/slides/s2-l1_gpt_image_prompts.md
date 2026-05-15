# GPT-Image2 Prompts: s2-l1

Use a premium AWS/SRE educational visual style. 16:9 slide, clean log-analysis and incident-investigation aesthetic, white and pale blue background, navy, teal, green, amber, and restrained red accents, readable Japanese text generated directly inside the image, no logos, no watermark, no local text overlay.

## Production Rules

- All visible text must be generated directly by GPT-Image2.
- Do not use local text overlay.
- Keep one clear message per slide.
- Prefer diagrams, query cards, timelines, and troubleshooting flows over decorative art.

## slide_001.png

Create a Japanese course slide. Large title: `エラー検索`. Subtitle: `まず異常らしいログを集める`. Visual: Error search over logs; ERROR, Exception, timeout, 5xx labels. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_002.png

Create a Japanese course slide. Large title: `levelを見る`. Subtitle: `構造化ログならERRORで絞る`. Visual: JSON field level = ERROR; Structured log table. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_003.png

Create a Japanese course slide. Large title: `messageを見る`. Subtitle: `非構造ログは文字列で探す`. Visual: @message text search; regex style filter. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_004.png

Create a Japanese course slide. Large title: `5xxとtimeout`. Subtitle: `HTTP失敗と待ち時間の失敗を見る`. Visual: API 5xx card and timeout card; statusCode >= 500. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_005.png

Create a Japanese course slide. Large title: `フィールド名を合わせる`. Subtitle: `クエリは現場ログへ調整する`. Visual: Template query adapted to real log fields; Field mapping table. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.

## slide_006.png

Create a Japanese course slide. Large title: `結果から行動へ`. Subtitle: `時間、対象、種類を次の確認へつなげる`. Visual: Result table branching to trend and request trace; Time, service, error type. Use large readable Japanese text, a clear operations diagram or query card layout, and leave generous margins. Do not add extra marketing copy, logos, or watermarks.
