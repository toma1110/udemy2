# AWS Source Verification Report

Task ID: TASK-0201
Course: `aws-runbook-first-response-course`
Reviewer AI: AI-QA-01
Status: Draft source baseline
Checked date: 2026-05-16

## Sources Checked

| Topic | Source | Course Usage |
| --- | --- | --- |
| Runbooks | AWS Well-Architected Framework: OPS07-BP03 Use runbooks to perform procedures | Define runbook as step-by-step procedure, central storage, owner, permissions, error handling, escalation, and maintenance |
| Playbooks | AWS Well-Architected Framework: OPS07-BP04 Use playbooks to investigate issues | Distinguish playbook for investigation from runbook for mitigation or known procedures |
| Operations as code | AWS Cloud Operations Blog: Achieving Operational Excellence using automated playbook and runbook | Explain maturing from manual Markdown procedures to automation and continuous validation |
| Systems Manager Automation runbooks | AWS Systems Manager Incident Manager runbook documentation | Mention automation as future path; note Incident Manager new-customer availability caveat |

## Course Design Implications

- The course should start with a text/Markdown runbook, not automation.
- Runbook must include desired outcome, tools, permissions, error handling, and escalation.
- Playbook and Runbook should not be treated as identical: investigation and mitigation are related but different.
- Runbook should be stored centrally and updated when process or workload changes.
- Systems Manager Automation is an advanced path; standard lesson requires no AWS execution.
- Incident Manager should not be used as a default recommendation because of its new-customer availability change.

## Required Follow-up Before Publishing

- Re-check current Incident Manager availability wording before final publication if mentioned in narration or slides.
- If adding real AWS automation, create a separate CEO approval gate before IAM role, Systems Manager Automation, Incident Manager, CloudWatch Alarm, or CloudFormation execution.
- Verify that the final script does not imply automatic rollback should be performed without team approval.

## References

- https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html
- https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html
- https://aws.amazon.com/blogs/mt/achieving-operational-excellence-using-automated-playbook-and-runbook/
- https://docs.aws.amazon.com/incident-manager/latest/userguide/runbooks.html
