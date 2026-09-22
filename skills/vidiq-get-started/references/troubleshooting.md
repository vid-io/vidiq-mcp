# Diagnose failures

Use the narrowest matching branch. Do not start creator research to diagnose a connection.

| Signal | Interpretation and next action |
| --- | --- |
| No vidIQ tools | Check installation, enablement, and authorization through the client; then re-check. |
| Explicit expired/missing authorization or 401 | Reconnect through the client; never request credentials in chat. |
| Unauthorized channel or channel-specific 403 | Compare canonical IDs with `vidiq_user_channels`. Select an authorized target or offer public research; 403 alone does not prove token expiry. |
| Empty or unexpected channel list | Account identity may be unknown. Suggest reconnecting with the intended account when its channel is missing. |
| Insufficient credits or quota | Check `vidiq_balance`; reduce or postpone the scope. |
| Expected tool missing | Reconnect or reload, then trust the refreshed live list; availability can vary by account or client. |
| Invalid input | Re-read the schema and correct only the failing fields. |
| Timeout or transient server error | Retry a status read once within scope and limits; stop if it repeats. |
| Interrupted media or generation | Follow [Job recovery](job-recovery.md); recover an existing job before considering resubmission. |

Keep raw error details for user-requested debugging.

## Credit usage

Separate estimates from returned charges. Inspect text and structured results for
`_credits.used` without double-counting. Missing charges, including on errors, are unknown.
Balance changes cannot establish a workflow's charge when other usage overlaps.
