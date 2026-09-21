---
name: vidiq-status
description: Check and diagnose a vidIQ MCP connection without starting creative work. Use when a user asks whether vidIQ MCP is connected or working, wants to verify authorization, authorized channels, credit balance, available capabilities, or asynchronous jobs, needs to recover an interrupted job, or reports authorization, quota, missing-tool, input, timeout, or server errors.
---

# vidIQ Status & Troubleshooting

Read [Live surface notes](references/live-surface-notes.md) before starting this workflow,
including analysis that uses only supplied evidence.

Diagnose the requested connection, account, credit, or job issue without starting research,
generation, or mutations. Infer the mode from the request:

- For an existing job, read [Job recovery](references/job-recovery.md).
- For a reported error, read [Troubleshooting](references/troubleshooting.md).
- For a general connection check, use the health check below.

## Health check

1. If vidIQ tools are missing, report **not connected** and route to `vidiq-get-started`.
   Tool visibility alone does not establish authorization.
2. Inspect the costs of `vidiq_user_channels`, `vidiq_balance`, and `vidiq_jobs_list`.
   Free independent checks may run in parallel. Obtain approval before any nonzero-cost check,
   quoting the aggregate for multiple calls; pause a check if its live price is unavailable.
3. Report the returned authorized channel IDs. An account label is optional; an empty or
   unexpected list does not prove an outage or expired authorization. Ask for channel selection
   or enrich names only when it affects the requested check.
4. Report the balance, distinguishing renewable and add-on credits and preserving `unlimited`
   and `null`. List active jobs with `status: "inprogress"`.
5. Summarize currently exposed capabilities by outcome, without reproducing a static catalog.

For a specific check, run only its relevant steps. Do not claim the connected channel is the
intended one unless the user established that target.

## Report

For connection checks, lead with **healthy** when requested checks succeed, **degraded** for partial or transient failure,
**action required** for authorization/account/credit intervention, or **not connected** when tools
are absent. Include relevant results, each issue's evidence, and its next corrective action.

Translate errors into plain language. Keep account information, job IDs, and result URLs private;
never ask the user to put them in a public issue.
For job recovery, report the actual job state, result or pending ID, and next action.
