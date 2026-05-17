# Runbook Template

## Runbook Info

| Field | Value |
| --- | --- |
| Runbook ID | RUN-XXX |
| Service |  |
| Trigger |  |
| Desired Outcome |  |
| Owner |  |
| Severity |  |
| Required Tools | CloudWatch Alarm, Dashboard, Logs, deploy history, AWS Health |
| Required Permissions | Read-only investigation first. Write/rollback requires explicit approval according to team policy. |
| Last Updated |  |
| Escalation POC |  |

## First Checks

1. Confirm the alarm name, state change time, and affected service.
2. Check customer impact: error rate, latency, availability, and affected operation.
3. Check dashboard trend before and after the alert.
4. Check recent deploys, configuration changes, or scheduled jobs.
5. Check relevant logs for repeated error patterns.
6. Check AWS Health or dependency status if external impact is suspected.

## Mitigation

| Condition | Action | Approval |
| --- | --- | --- |
| Recent deploy likely caused the issue | Prepare rollback or disable the feature flag | Team policy |
| Traffic spike or throttling suspected | Apply documented scaling or throttling mitigation | Team policy |
| Dependency issue suspected | Use fallback or degradation mode if available | Team policy |

## Escalation

- 5 minutes: owner confirms impact and starts first checks.
- 15 minutes: escalate to service lead if impact continues.
- 30 minutes: open incident channel and assign incident commander if user impact is material.

## Communication

- Internal channel:
- Stakeholder update owner:
- Customer-facing update owner:
- Update interval:

## Recovery Confirmation

- Alarm returns to OK.
- Error rate and latency return to normal range.
- User-facing operation succeeds.
- Mitigation is recorded.

## Postmortem Link

- Postmortem issue/document:
- Follow-up actions:
- Runbook updates:
