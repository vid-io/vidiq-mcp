---
name: vidiq-packaging-comparison
description: Compare distinct YouTube title-and-thumbnail concepts for the same video when alternative creative directions are explicitly requested. Route single titles, thumbnail edits, or complete packages without a comparison request to vidiq-packaging-studio.
---

# vidIQ Packaging Comparison

Read [Live surface notes](references/live-surface-notes.md) first, even when using only supplied evidence.

Compare the requested number of distinct title-thumbnail concepts for the same video, defaulting
to three if unspecified. Use `vidiq-packaging-studio` for focused edits or one package. Generated
images are optional.

## Compare concepts

Preserve what each number measures: video length does not prove how quickly an action was
completed. Use a speed claim only when demonstrated or explicitly supported by the brief.

1. Use the supplied viewer, promise, proof, format, language, and assets. Establish which story
   facts are supported and whether the host is the subject or an analyst.
2. Keep research within scope. Generate images only when requested, using the selected direction
   or the requested number of variants.
3. Clarify content only when necessary: `vidiq_video_transcript` supplies untimed spoken text;
   `vidiq_video_watch` serves long-form and `vidiq_watch_shortform_content` serves Shorts.
   Verify the source before watching. Read
   [Job lifecycle](references/job-lifecycle.md) before any asynchronous watch or production call.
4. Create distinct, truthful promises or framing choices, not cosmetic rewrites. Pair each title
   with thumbnail tension, proof, or stakes that adds information. Make subject attribution clear.
5. Research references only when they can change the comparison. Use the guidance below.
6. Compare audience fit, truthful payoff, differentiation, production feasibility, and evidence.
   A concept can remain useful despite a lower model score. Before using vidIQ tools for
   title generation/scoring, rendering, refinement, or thumbnail scoring, read
   [Production and scoring](references/production.md).

## Optional reference research

Read [Discovery evidence](references/discovery-evidence.md) before searching or evaluating external
references. Skip research when the supplied brief suffices.

For long-form visual conventions, `vidiq_similar_thumbnails` takes exactly one of `description`
or `videoId`; it does not support Shorts. Description retrieval is approximate and may be
irrelevant. Inspect actual images before claiming visual similarity or saturation.

For title mechanisms, use `vidiq_outliers` with semantic `requireAllTitleTerms: false`; strict
`true` phrases provide supporting evidence only. Preserve format and language: outliers rejects
non-English Shorts, has no live-only lane, narrows non-English `all` to long-form, and caps
non-English discovery at six months. Pass a supported `language` explicitly; use a supported
alternative or disclose missing coverage.
Normalize outlier `videoPublishedAt` epoch seconds and ISO dates before comparing publication ages.

Exclude the story's originating video/creator and sources of material adapted for the story from
the packaging reference set, even if licensed. Without image access, mark visual relevance unverified.

A reference is optional design evidence, not permission to copy another creator's distinctive
expression. Preserve the creator's authorized assets and name any reference's abstract contribution.

## Deliver

Return the agreed concepts, their matched titles and thumbnail directions, evidence and
limitations, and the recommended choice with its strongest counterargument. Honor a request for
comparison without forcing a winner.

For executed production, report image URLs or pending job IDs, visual-review status, and score/proxy
context. Separate concept judgments from inspected renders; never claim a
visual winner before inspection. Log only useful iterations actually performed.
