# Run an asynchronous action

Read this before submitting or polling an asynchronous watch, generation, or refinement job.

Submit an approved action once, save its job ID, and poll it with `vidiq_job_poll`.
Recover interrupted work with `vidiq_jobs_list`; use `get-started` when available.
Follow returned polling guidance within a bounded plan. Respect supplied limits; otherwise state
reasonable defaults. At the limit, return the pending ID and status.

Before retrying a submission, confirm it created no job, asset, or mutation and the retry stays
within approved scope and limits. Never resubmit an existing job because it is slow or its result
is missing. Report terminal status and refunds only from results.
