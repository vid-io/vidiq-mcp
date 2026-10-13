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
| Write tool missing (`vidiq_update_video`, `vidiq_update_video_thumbnail`) | The Claude.ai directory connector and API-key connections expose no write tools; connect `https://mcp.vidiq.com/mcp` as a custom connector with browser sign-in. |
| No YouTube channel connected | Call `vidiq_connect_youtube_channel`, show its widget, wait for the creator, then retry the original request. |
| `status: verification_required` from a write tool | Nothing was changed. Show the verification widget or call `vidiq_authorize_with_youtube`, wait for the creator to confirm, then repeat the same approved call once. |
| Invalid input | Re-read the schema and correct only the failing fields. |
| Timeout or transient server error | Retry a status read once within scope and limits; stop if it repeats. |
| Interrupted media or generation | Follow [Job recovery](job-recovery.md); recover an existing job before considering resubmission. |

Keep raw error details for user-requested debugging.

## Credit usage

Separate estimates from returned charges. Inspect text and structured results for
`_credits.used` without double-counting. Missing charges, including on errors, are unknown.
Balance changes cannot establish a workflow's charge when other usage overlaps.
