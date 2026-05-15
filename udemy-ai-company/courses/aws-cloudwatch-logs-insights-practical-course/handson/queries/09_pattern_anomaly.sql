fields @timestamp, @message
| filter @message like /(?i)(error|exception|timeout)/
| pattern @message
| anomaly
