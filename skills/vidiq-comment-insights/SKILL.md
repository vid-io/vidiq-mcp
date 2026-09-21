---
name: vidiq-comment-insights
description: Mine de-identified viewer language from YouTube comments and transcripts with the connected vidIQ MCP. Use when a creator needs authentic phrases for hooks, briefs, titles, scripts, offers, or audience research; wants recurring questions and objections; or needs to distinguish creator language from the words viewers actually use.
---

# vidIQ Comment Insights

Read [Live surface notes](references/live-surface-notes.md) before starting this workflow,
including analysis that uses only supplied evidence.

Extract reusable audience language from comments while protecting commenter identity.
Keep viewer wording distinct from the creator's transcript and from original copy.

## Sample the requested audience

1. Establish topic, intended use, language/market, and period; agree on the live-cost sample.
   Use supplied videos. Discover additional sources only when needed and approved.
2. For discovery, use `vidiq_channel_videos`, `vidiq_youtube_search`, or `vidiq_outliers` to
   include typical, recent, and breakout examples. Catalog calls require matching
   `videoFormat: long`, `short`, or `live`; use `popular: false` for recent uploads.
   YouTube search needs `type: ["video"]` so channels/playlists do not enter comment calls.
   Keep language/format explicit where supported; outliers cannot discover non-English Shorts.
3. Read [Discovery evidence](references/discovery-evidence.md) when discovering source videos or
   asserting a recurring pattern. Inspect thumbnails only
   if visual context changes source selection; missing image access does not invalidate comment
   analysis. Fetch independent samples in parallel only after agreeing on scope.
4. Start `vidiq_video_comments` with `videoId`, explicit `order`, and singular `maxResult`
   (1–100 threads per page). Report the sample cap and selection bias. Count actual returned
   replies; `replyCount` is not the number inspected. When the live tool returns `nextPageToken`,
   continue within the agreed budget using `pageToken` and the same source, `order`, and
   `minLikes`. Like filtering can leave a page short or empty while more pages remain.
   Filter dates locally; undated comments have unknown recency.
5. Use representative `vidiq_video_transcript` results only when useful; `transcription` is
   untimed creator language, not viewer evidence.

## Deidentify and count accurately

Verify the video's owner channel from metadata, using `vidiq_get_videos_by_ids` only when needed.
Compare `authorChannelUrl` in the same identifier form: `/channel/ID` against the owner ID,
or `/@handle` against a verified owner handle. If the handle is missing, one budgeted
`vidiq_channel_search` with `channelTitleMatch: "exact"` can resolve it; require the returned
`channelId` to match the video's owner before trusting its handle.

An ID/handle mismatch or display name does not establish non-owner status. Without a comparable
owner identity, all affected authors remain unverified: paraphrase separately, exclude them from
verified viewer counts, and use no verbatim fragments. Exclude matched owner comments and replies.
Use author IDs and handles transiently, never in the language bank or evidence trail.

Decode entities, strip HTML, URLs and handles, and normalize whitespace. Drop sensitive or
identifying fragments instead of trying to salvage them by partial redaction. Prefer paraphrases.
For useful verbatim evidence, take one contiguous deidentified fragment of at most eight
whitespace-delimited words, shorter than the full cleaned comment. Otherwise paraphrase or omit.
Never stitch fragments or reproduce full comments, even short ones.

Cluster questions, desired outcomes, objections, misconceptions, and emotional language.
Count support by videos: N of M with usable sampled comments, with M out of all selected videos.
Multiple replies in one thread are not independent video support. Preserve per-video caps,
returned/retained threads and replies, exclusions, and date coverage. Empty, disabled, or missing
comments are coverage gaps, not absence of audience concerns.

Use `vidiq_keyword_research` only to test a requested or decision-relevant search-demand
hypothesis; conversational phrasing does not establish search intent. Do not infer demographics
or sensitive traits from wording.

## Deliver

Return the requested language bank or audience findings with meaning, support, recency, source-video
labels, limitations, and suggested use. Label paraphrases, verbatim evidence, creator language,
and original copy distinctly.

Add hooks or content briefs only when requested, using the requested count. Keep all examples
original and the evidence trail deidentified.
