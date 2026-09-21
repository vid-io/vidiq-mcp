# Diagnose failures

Use the narrowest matching branch. Do not repeat expensive research to diagnose a connection.

| Signal | Interpretation and next action |
| --- | --- |
| No vidIQ tools | Check installation, enablement, and authorization through the client; then re-check. |
| Explicit expired/missing authorization or 401 | Reconnect through the client; never request credentials in chat. |
| Unauthorized channel or channel-specific 403 | Compare canonical IDs with `vidiq_user_channels`. Select an authorized target or offer public research; 403 alone does not prove token expiry. |
| Empty or unexpected channel list | Account identity may be unknown. Suggest reconnecting with the intended account when its channel is missing. |
| Insufficient credits or quota | Check `vidiq_balance` within the approved cost boundary; reduce or postpone the scope. |
| Expected tool missing | Reconnect or reload, then trust the refreshed live list; availability can vary by account or client. |
| Invalid input | Re-read the schema and correct only the failing fields. |
| Timeout or transient server error | Retry one zero-cost status read once, or obtain approval for its live retry cost; stop if it repeats. |
| Interrupted media or generation | Follow [Job recovery](job-recovery.md); recover an existing job before considering resubmission. |

Missing `_credits`, including on errors, is unknown rather than zero. A charged or state-changing
retry requires evidence that no job, asset, or mutation was created and approval covering its cost.
Keep raw error details for user-requested debugging.
