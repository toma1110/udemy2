fields @timestamp, service, errorType, statusCode, @message
| filter level = "ERROR" or statusCode >= 500 or ispresent(errorType)
| stats count(*) as count by service, errorType
| sort count desc
| limit 20
