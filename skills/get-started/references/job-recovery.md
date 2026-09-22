# Recover an existing job

1. With a supplied job ID, call `vidiq_job_poll` using `mcpJobId`.
   Otherwise use `vidiq_jobs_list` with tool/status filters and `limit` of 1–50; time-window and
   pagination inputs are unsupported.
2. If an in-progress lookup finds no match after an interrupted workflow, make at most one broader
   recent-jobs lookup within scope. Do not guess tool identifiers or match an unidentifiable job.
   Ask the user to select among several plausible matches.
3. For a status-only request, poll once. To wait for or recover a result, follow returned polling
   guidance with a bounded cadence and attempt limit. Respect supplied limits; otherwise state
   reasonable defaults without making the user choose a polling interval.
4. Preserve the original ID; never resubmit the underlying action because it is slow.
   At the limit, return its pending ID and status. Report the terminal result as returned;
   claim a refund only for `refunded: true`.
