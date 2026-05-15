filter @type = "REPORT" and @duration > 1000
| fields @timestamp, @requestId, @duration, @billedDuration, @memorySize, @maxMemoryUsed
| sort @duration desc
| limit 20
