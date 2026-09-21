---
name: vidiq-packaging-comparison
description: Compare distinct YouTube title-and-thumbnail concepts for the same video with the connected vidIQ MCP. Use when a creator explicitly wants alternative creative directions or a packaging comparison. Route a single title, thumbnail edit, or complete package without a comparison request to vidiq-packaging-studio.
---

# vidIQ Packaging Comparison

Read [Live surface notes](references/live-surface-notes.md) before starting this workflow,
including analysis that uses only supplied evidence.

Compare distinct title-thumbnail concepts for the same video. Use the requested number; default
to three only when no count is given. Route focused edits or a single complete package to
`vidiq-packaging-studio`. Comparing concepts does not require generated images.

## Compare concepts

Preserve what each number measures: video length does not prove how quickly an action was
completed. Use a speed claim only when demonstrated or explicitly supported by the brief.

1. Use the supplied viewer, promise, proof, format, language, and assets. Establish which story
   facts are supported and whether the host is the subject or an analyst.
2. Agree on the research scope and variant budget. Render only a selected direction unless the
   creator explicitly approves more. Shared approval rules apply to each exact action and cost;
   preserve approval that already covers unchanged inputs.
3. Clarify content only when necessary: `vidiq_video_transcript` supplies untimed spoken text;
   `vidiq_video_watch` serves long-form and `vidiq_watch_shortform_content` serves Shorts.
   Watch calls require exact source/cost approval. Read
   [Job lifecycle](references/job-lifecycle.md) before any asynchronous watch or production call.
4. Create distinct, truthful promises or framing choices, not cosmetic rewrites. Pair each title
   with thumbnail tension, proof, or stakes that adds information. Make subject attribution clear.
5. Research references only when they can change the comparison. Use the guidance below.
6. Compare audience fit, truthful payoff, differentiation, production feasibility, and evidence.
   A concept can remain useful despite a lower model score. Before using vidIQ tools for
   title generation/scoring, rendering, refinement, or thumbnail scoring, read
   [Production and scoring](references/production.md).

## Optional reference research

Read [Discovery evidence](references/discovery-evidence.md) when searching or evaluating external
references. Skip this stage when the supplied brief is sufficient for concept comparison.

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

For executed production, include image URLs or pending job IDs, actual visual-review status,
scoring/proxy context, and costs as reported. Distinguish concept judgments from inspected renders;
do not claim a visual winner while review is pending. Include an iteration log only when useful
for iterations actually performed.
