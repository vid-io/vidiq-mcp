# Research and diagnose packaging

Use only the sections needed to resolve an evidence gap within the requested scope.

## Establish the content

Resolve a needed channel using supplied context, `vidiq_user_channels`, or
`vidiq_channel_search`. For a published video, use `vidiq_get_videos_by_ids` and, when useful,
`vidiq_video_transcript`. Its `transcription` is untimed text.

Identify the promise, curiosity, proof, opening payoff, and possible thumbnail objects. Distinguish
observations from interpretation; proposed hook changes must not silently assume the content
will change.

## Diagnose a published video

- For a recent upload, use `vidiq_video_stats` with age-appropriate `granularity` and
  `vidiq_channel_performance_trends`. Compare the same publication ages. The channel-wide curve
  is not format-filtered; route detailed timing to `vidiq-new-upload-review`.
- For back-catalog context, use `vidiq_channel_videos` with `popular: false` and matching
  `videoFormat` (`long`, `short`, or `live`). Compare reasonably similar ages and formats.
  Returned recent uploads are a bounded sample, not the full catalog. Use authorized analytics
  only when relevant; an inadequate cohort leaves the comparison unavailable.
  For sampled per-video analytics, use `dimensions: ["video"]` and
  `filters: "video==ID1,ID2"` in batches of at most 150; missing requested rows are unknown.
- The analytics schema does not expose thumbnail CTR or impressions. Use supplied YouTube Studio
  evidence for those measures; annotation CTR and ad impressions are not substitutes.
- Consider demand, distribution, retention, timing, and seasonality. Weak views alone do not
  establish a packaging cause; state the diagnosis as a testable hypothesis.

## Find usable references

Read [Discovery evidence](discovery-evidence.md) when evaluating reference candidates.

Search title or promise mechanisms across niches with shared viewer motivation. Use semantic
`vidiq_outliers` queries with `requireAllTitleTerms: false` first; strict `true` phrases are
supporting evidence, not proof of an exact contiguous phrase. Verify returned wording.

Preserve format and language. Outliers rejects non-English Shorts and has no live-only lane.
For non-English outliers, `all` narrows to long-form and discovery is capped at six months.
Pass a supported `language` explicitly. Use a supported alternative or disclose the gap without substituting
English, long-form, or a different period.
Normalize outlier `videoPublishedAt` epoch seconds and other tools' ISO dates before age comparisons.

For a known seed, `vidiq_similar_videos` can find independent executions. Choose the live
`matchOn`, exclude the seed channel where appropriate, and inspect `signalsUsed`,
`signalsFailed`, and `matchedBy` before relying on matches.

Exclude the originating video, its creator, and sources of material adapted for the story from
the packaging reference set, even if licensed. Show a small eligible set with source, age, evidence,
applicability, and limitations. Let the creator choose when references imply different promises.

## Inspect moving-image evidence only when needed

Use `vidiq_video_watch` for long-form or `vidiq_watch_shortform_content` for Shorts when visual
structure can change the decision. Verify eligibility separately for a live stream or recording.
Verify the source; preserve and poll the returned job using [Job lifecycle](job-lifecycle.md),
read before submission.

Use completed watch evidence for pacing, scene, and moving-image claims. Transcripts, URLs, and
thumbnails cannot establish them. With missing image access, provide provisional text-only
analysis and identify what needs visual inspection.
