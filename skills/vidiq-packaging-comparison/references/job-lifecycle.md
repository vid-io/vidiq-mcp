# Run an asynchronous action

Read this before submitting or polling an asynchronous watch, generation, or refinement job.

Submit an approved action once, save its job ID, and poll it with `vidiq_job_poll`.
Recover interrupted work with `vidiq_jobs_list`; use `vidiq-status` when available.
Follow returned polling guidance within a bounded plan and approved live cost. Respect supplied
limits; otherwise state reasonable defaults. At the limit, return the pending ID and status.

Report terminal status and refunds only from results. An existing job must not be resubmitted
merely because it is slow or its result has not been retrieved.
