# Platforms and media

Read only the sections needed for the selected destinations and source. Use the live schemas for
accepted inputs, limits, and prices; a platform appearing in history does not mean it is available
as a new destination.

## Import and reuse

- Reuse an existing `imageId` or video `uploadId`. `vidiq_upload_image` adds an image to the
  library; `vidiq_video_upload` imports a video. Importing a file does not publish to a platform.
  Use the returned ID as the corresponding image or video entry in a draft's media.
- Choose the input supported by the client: an accessible URL, an accepted attachment, or an
  advertised local-file input. Do not put a local path in a URL field or assume a chat attachment
  is readable by the server. When an attachment cannot be passed directly and `vidiq_file_upload`
  is available, show its picker and wait for the returned upload IDs. Reuse an image ID directly;
  check a video's upload with `vidiq_video_upload` as directed by the result.
- A YouTube source import can return `mcpJobId`. Poll it with `vidiq_job_poll`, following
  [Job lifecycle](job-lifecycle.md), and keep the resulting `uploadId`. For waiting or processing
  uploads, call `vidiq_video_upload` with the existing `uploadId` rather than transferring again.
  Never publish a known unready asset.
- Use a one-time transfer link only when the tool offers it and the local environment can send
  the file. Keep signed links private and unchanged. Preserve transfer IDs on interruptions;
  an uncertain import is not permission to create another copy.
- A converted or edited image is a distinct library asset. Upload it with `parentImageId` and
  a meaningful `variant` when supported, then use it only on the destination that needs it.
  Media overrides replace the inherited list; preserve intended order. An empty list means
  no media, which is invalid for destinations requiring it.
- A thumbnail or generated image URL is not a library ID. Import it if needed. New generation,
  clipping, or edits require the relevant scope, rights, and cost approval; reuse established
  rights for supplied assets.

## Destination choices

| Destination | Decisions that affect preparation |
| --- | --- |
| YouTube | Requires a title and a video. The creator chooses privacy. Put `thumbnailImageId` on the YouTube destination only, so the thumbnail is not posted elsewhere. A publish time uses YouTube's native schedule: the upload happens now and stays private until release. Do not combine an unlisted choice with a schedule. |
| Instagram | Regular posts, carousels, and Reels use the social draft workflow. Supply media and preserve its order. Use a compatible image variant when needed; do not silently turn a requested carousel into separate posts. |
| TikTok | The creator chooses privacy, comments, and applicable music settings. Ask for any missing choices or music confirmation; never assert their consent. Preserve disclosure choices for branded or AI-generated content and resolve applicable missing facts. Account-specific allowed privacy values may only become clear from a refusal. |
| X | Review the actual destination text and quoted credits, especially after adding a link. Link posts cost more; even a bare domain can affect pricing. Preserve supplied reply and disclosure settings. |
| Facebook Pages | Select the actual Page, not a personal Facebook profile. Connection covers Pages the user manages through their own profile; an expected Page reached only through a business portfolio may be absent. |

TikTok photo posts currently use JPEGs of at most 1080p, with 1–20 images; video posts use one
video. Check known dimensions before submission: a draft can pass and later fail for image size.
Use the destination's validation issue to resolve other limits rather than maintaining a second
copy of every platform's rules. Keep the original asset for platforms that accept it.

A YouTube destination has no switch that forces Shorts classification. For a Shorts request,
check the source's format and current eligibility; identify uncertainty rather than promising
that any uploaded clip will appear as a Short.

## Instagram Trial Reels and AI labels

`vidiq_instagram_publish_reel` is the separate path when the request requires a Trial Reel or its
AI-generated label. Select the Instagram account through `vidiq_social_account_list`; this tool
uses `videoUrl`, such as the hosted URL from `vidiq_video_upload`, rather than a library ID.
Inspect its current contract and publishing eligibility. Prepare and show the
exact account, video, caption, regular/Trial setting, and label choice before approval: this tool
publishes directly, not through the social draft review.

If combined with other platforms, keep this Instagram destination out of the regular social draft
and explain the separate submission. Preserve the tool's `mcpJobId` or `containerId` and account
across continuations. Follow its job/container protocol, not social-post status; a preparation job
finishing alone does not publish. Stop on an error and inspect the outcome before any retry.

## Scheduling and cost boundaries

An already uploaded YouTube video using YouTube's native schedule is the exception to the
skill's scheduling restrictions: its metadata may be changed through `vidiq-video-metadata` when available,
with the exact video and change approved. Confirm that it is an existing upload first.

Use returned draft quotes for the proposed destinations. Currently only X publishing costs
credits; edits and replacements can change the amount. An X failure after submission does not
automatically refund its charge. A correction on the same post can receive credit for an earlier
paid attempt, so use the new quote instead of calculating a refund. Report actual charges from
`_credits.used` once per call as required by the shared surface notes.
