fields @timestamp, service, level, requestId, path, statusCode, durationMs, @message
| filter requestId = "req-1003"
| sort @timestamp asc
| limit 100
