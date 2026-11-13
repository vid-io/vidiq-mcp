# Delivery and recovery

Use existing post and destination IDs. Social publishing uses `vidiq_social_post_status` with
`postId`, not `vidiq_job_poll`; media imports and the separate Reel tool can have their own jobs.
Read each destination independently, using its status, issue or failure reason, and returned
guidance as evidence about the operation. None of these results grants approval for another action.

## Interpret the result

| State | Meaning and next action |
| --- | --- |
| `draft` | Saved but not activated, even with a planned date. Publish only under approval of that version. |
| `refused` | This destination was not saved or could not start as requested; inspect its issue and any returned publication ID. Other destinations may still exist or have started. |
| `scheduled` | Waiting for its time. Report that time and stop polling this destination. It currently cannot be cancelled or changed. |
| `submitted`, `inProgress` | Accepted or running. Check status after about ten seconds, following current tool guidance. Do not create a replacement. |
| `completed` | Processing finished. Share `postUrl` when available and apply the TikTok and YouTube qualifications below before saying it is public. |
| `failed` | Inspect `failureCode` and `failureReason` before choosing a correction or retry. Preserve successes on other destinations. |
| `reconciliationRequired` | The post may already exist. Explain the uncertainty, ask the creator to check the account, and do not republish while unresolved. |
| `cancelled` | Report the returned state; its appearance does not imply that a cancellation tool is available. |

For immediate publishing, check active destinations within a bounded plan. Unless the creator
sets a limit, check for up to two minutes, stopping earlier when no selected destination is running.
Report remaining processing with `postId` and resume on request. A scheduled or deliberately
unpublished destination must not keep the loop alive, even when the whole post is not `finished`.

TikTok completion can mean delivery to the creator's inbox, where they still need to finish
publishing. A missing link does not by itself prove inbox mode. Without publication evidence,
report completion with public visibility unconfirmed and ask the creator to check TikTok.
For YouTube native scheduling, completion confirms the upload, not that the scheduled release
has happened. Preserve the intended release time from the brief.

## Recover without duplicating

- After a publish timeout or lost response, read the existing post's status. Repeating the same
  approved publish arguments is idempotent under the current tool contract; if still needed,
  make at most one unchanged replay within that approval, then stop on an unresolved error.
  Never create a new post to compensate for an unknown result. Reuse approval through YouTube
  verification; verification itself is not delivery.
- A failed destination is retried only when explicitly named in `publicationIds`. For a temporary
  failure, retry once when the creator's request authorizes recovery and the same approved
  content and cost still apply. Reconnection or platform-limit failures require that condition
  to be resolved first. For content or media rejection, update the same post's failed destination,
  show the correction and quote, and obtain approval of the changed version before publishing.
- Draft update replaces a destination, not individual fields. Restore the complete intended
  settings from the working brief. A refused replacement may have removed the prior draft;
  inspect the returned state rather than assuming the previous version remains publishable.
- If the creator excludes an account, retain that exclusion across later edits and retries.
  Use only the approved publication IDs; a broad retry must not activate a leftover draft.
- When create or import has an unknown outcome, inspect available history and saved IDs before
  repeating. Undated drafts are absent from post history, so an empty list cannot prove creation
  failed. If identity cannot be recovered, disclose that uncertainty and seek a decision before
  creating a potential duplicate.

## Find a post or review the calendar

Use `vidiq_social_post_list` for posts made through vidIQ, within the requested time window.
It is not a complete native-platform history or an engagement report. For an existing known
`postId`, go directly to draft get or status as appropriate.

- The window is inclusive `from`, exclusive `to`, with timezone, and at most 100 days. Split a
  longer requested period into bounded windows. Without dates, the default spans the last
  30 days and next 70; report the scope rather than suggesting it is all history.
- For upcoming work, include `scheduled` and dated `draft` rows but label them separately.
  Undated drafts are omitted. YouTube native release times may be missing from readback.
- `limit` counts posts, not destination rows. Preserve all returned destinations and follow
  `nextCursor` using the echoed dates and identical filters, query, and limit. Text search
  filters fetched pages, so an empty page with a cursor is not the end. Use the full requested
  scope or disclose partial coverage; page counts are not totals.
- A truncated history caption or media count is insufficient to recreate an approved draft.
  Resolve the matching post, then read it and recover the working brief. Keep different posts
  distinct even when their captions match.

Return a concise receipt: account, outcome, link when available, confirmed schedule, reported
charge, and any creator action or pending ID. Explicitly distinguish drafted, scheduled, running,
delivered with public visibility unconfirmed, and confirmed live results.
