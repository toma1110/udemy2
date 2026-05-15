fields @timestamp, service, path, durationMs
| filter ispresent(durationMs)
| stats
    count(*) as requests,
    avg(durationMs) as avgMs,
    pct(durationMs, 95) as p95Ms,
    pct(durationMs, 99) as p99Ms,
    max(durationMs) as maxMs
  by service, path
| sort p99Ms desc
| limit 20
