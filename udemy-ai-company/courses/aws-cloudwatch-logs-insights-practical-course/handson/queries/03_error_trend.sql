fields @timestamp, level, statusCode, @message
| filter level = "ERROR"
    or statusCode >= 500
    or @message like /(?i)(error|exception|timeout)/
| stats count(*) as errorCount by bin(5m)
| sort errorCount desc
