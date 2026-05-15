# JOIN example: correlate API logs and application logs by requestId.
# This is an advanced read-through query. Keep time range short if you run it.
filter statusCode >= 500
| join type=inner left=api right=app
    where api.requestId = app.requestId
    (SOURCE '/aws/lambda/example-app')
| fields api.requestId, api.path, api.statusCode, app.errorType
| sort api.requestId desc
| limit 50

# Subquery example: find upstream requests that had downstream timeout records.
filter requestId in (
    SOURCE '/aws/lambda/payment-service'
    | filter errorType = "PaymentTimeout"
    | fields requestId
)
| fields @timestamp, requestId, service, path, statusCode, @message
| sort @timestamp desc
| limit 50

# SOURCE tag example: CLI/API only, not CloudWatch console.
SOURCE logGroupTags([{"key":"Application","values":["checkout"]}])
| fields @timestamp, @message, @log
| sort @timestamp desc
| limit 50
