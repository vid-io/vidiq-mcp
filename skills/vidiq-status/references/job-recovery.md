# Recover an existing job

1. Inspect live list/poll costs. Obtain exact approval for nonzero-cost calls and pause if price
   metadata is missing.
2. With a supplied job ID, call `vidiq_job_poll` using `mcpJobId`.
   Otherwise use `vidiq_jobs_list`, filtering only by exact tool/status values supported by the
   live schema. Its bounded `limit` is 1–50; do not invent time-window or pagination inputs.
3. If an in-progress lookup finds no match after an interrupted workflow, make at most one broader
   recent-jobs lookup when free or approved. Do not guess tool identifiers or match an
   unidentifiable job. Ask the user to select among several plausible matches.
4. For a status-only request, poll once. To wait for or recover a result, follow returned polling
   guidance with a bounded cadence and attempt limit. Respect supplied limits; otherwise state
   reasonable defaults without making the user choose a polling interval.
5. Continue only while calls are free or their total is approved. Preserve the original ID;
   never resubmit the underlying action because it is slow. At the limit, return its pending ID
   and status. Report the terminal result as returned; claim a refund only for `refunded: true`.
