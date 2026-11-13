# Run and recover a background job

Read this for tools that return `mcpJobId`, including watch, generation, refinement, and
YouTube-source import jobs.

Use the returned ID with the matching tool: `mcpJobId` goes to `vidiq_job_poll`; waiting or
processing uploads with `uploadId` are checked through `vidiq_video_upload`; post delivery uses
`vidiq_social_post_status` with `postId`. These IDs are not interchangeable.

1. Submit an approved action once and save its `mcpJobId`. Poll that same job.
2. For a status-only request, poll once. When waiting for completion, follow returned polling
   guidance within a bounded plan. Respect supplied limits; otherwise state reasonable defaults.
   At the limit, return the pending ID and status so work can resume.
3. If `message` says the job is waiting for another action, stop polling and use that action's
   workflow within the approved scope. Obtain any missing approval before acting. A job can stay
   `inprogress` while awaiting this handoff; polling itself never publishes anything.
4. On completion, read `result` and preserve the returned asset IDs and URLs for the next stage.
   Report failures from the returned status, message, and `errorCode` when present. Claim a refund
   only when `refunded: true`.

Recover interrupted work using a known `mcpJobId` first; otherwise use `vidiq_jobs_list`.
Use `vidiq-get-started` when available for an unresolved lookup.

Before retrying a submission, confirm it created no job, asset, or mutation and the retry stays
within approved scope and limits. Never resubmit an existing job because it is slow or its result
is missing.
