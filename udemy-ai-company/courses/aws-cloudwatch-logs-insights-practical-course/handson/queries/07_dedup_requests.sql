fields @timestamp, requestId, service, errorType, @message
| filter level = "ERROR" or @message like /(?i)(error|exception|timeout)/
| sort @timestamp desc
| dedup requestId
| limit 50
