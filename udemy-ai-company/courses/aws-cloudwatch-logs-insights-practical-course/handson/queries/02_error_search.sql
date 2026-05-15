fields @timestamp, service, level, requestId, statusCode, errorType, @message
| filter level = "ERROR"
    or statusCode >= 500
    or @message like /(?i)(error|exception|timeout)/
| sort @timestamp desc
| limit 100
