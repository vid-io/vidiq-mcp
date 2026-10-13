---
name: vidiq-video-metadata
description: Apply approved changes to a YouTube video you own through vidIQ (title, description, tags, privacy, scheduled publish time, or thumbnail), with a snapshot and readback. Use when asked 'update my video title', 'change the description', 'add these tags', 'schedule this video', 'make it public or unlisted', or 'apply the new title and thumbnail'. Requires owner authorization and explicit approval of the exact change. For drafting titles or thumbnails first use vidiq-packaging-studio; for keywords use vidiq-youtube-seo.
---

# vidIQ Video Metadata

Read [Live surface notes](references/live-surface-notes.md) first, even when using only supplied evidence.

Apply an explicitly approved change to a YouTube video the connected account owns. Drafting belongs
to other skills; this workflow applies one exact change safely.

## Confirm scope and ownership

1. Confirm the live tool list includes `vidiq_update_video` (title, description, tags, privacy,
   scheduled publish time) or `vidiq_update_video_thumbnail`. If absent, stop: the client may be using
   a directory connector without write tools, or the account may be connected with an API key instead
   of browser sign-in. Route to `vidiq-get-started`; do not improvise with another tool.
2. Resolve the owner with `vidiq_user_channels` and the target video with `vidiq_user_videos` or a
   supplied ID. Require the video's `channelId` to match an authorized ID; a public video on another
   channel cannot be edited.
3. Capture a snapshot of the current title, description, tags, privacy, and publish time with
   `vidiq_get_videos_by_ids`, and read `vidiq_video_change_history` when available.

## Prepare the exact change

1. Use supplied drafts. If the creator wants keyword or scoring help first, run `vidiq-youtube-seo`
   or `vidiq-packaging-studio` and return here with the chosen text.
2. Present a field-by-field diff: current value, proposed value, and unchanged fields. Keep every
   field within YouTube limits (title 100 characters, description 5,000, tags 500 in total).
   `tags` replaces the whole list, and an empty `description` or `tags` clears it. For "add these
   tags", propose the snapshot's tags plus the additions and show any tag that would be removed.
3. For a schedule, `publishAt` takes a UTC time ending in `Z` and applies only to a private video.
   Convert the creator's stated time and timezone, show both, and include `privacyStatus: "private"`
   in the diff. A public or unlisted video cannot be scheduled as it stands; making it private first
   hides it and needs its own explicit approval.
4. Call out consequences: a new title or thumbnail resets viewer expectations, a privacy change is
   visible immediately, and a schedule change can move a launch.
5. Obtain approval of the exact diff and the credit cost. Approval of a draft is not approval to
   publish; ask once, precisely.

## Apply once and verify

1. Immediately before the call, re-read the current values. If they differ from the snapshot, abort,
   show the concurrent difference, and ask for approval again.
2. Call `vidiq_update_video` once with the owning `channelId`, the `videoId`, and only the approved
   fields, or `vidiq_update_video_thumbnail` once with the same IDs and the approved image. Preserve
   the response.
3. A `verification_required` status means the write is waiting on YouTube verification, not that it
   failed. Show the returned verification step, wait until the creator confirms it is complete, then
   repeat the same approved call once; it needs no new approval.
4. Read back with `vidiq_get_videos_by_ids` and compare every approved field. Report any
   discrepancy, partial update, or limit failure; never silently retry, roll back, or resubmit. If
   the readback fails, label the result unverified and distinguish response-confirmed state.

## Deliver

Report the owner and video, the approved diff, the confirmed final values or the exact verification
gap, the charged credits as returned, and anything the creator still needs to do in YouTube Studio.
