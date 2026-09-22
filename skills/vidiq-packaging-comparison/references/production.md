# Produce and score packaging candidates

Concept comparison can stay text-only. Generate only the requested variants.
Before an asynchronous call, read [Job lifecycle](job-lifecycle.md).

## Titles and previews

For `vidiq_generate_titles`, set confirmed `type` and `language`; check generation's language
codes separately from discovery. Reuse returned scores for unchanged titles. Use
`vidiq_score_title` only for new/changed candidates or necessary comparable context, with its
required confirmed `type: long` or `short`.

Respect the title limit. A payoff within roughly 55 characters is a preview heuristic; inspect
the title-thumbnail pair at small display size when possible, otherwise mark the preview
unverified. Scores are directional evidence, not predicted CTR.

## Render the selected direction

Before rendering or refining, establish rights to the source assets and any depicted likeness;
preserve required attribution. Reuse established rights and ask only about missing permissions
relevant to the requested image.

Use the creator's brief, brand, and authorized assets. An external reference is optional; preserve
original expression and clear subject attribution. Set thumbnail `orientation` to `landscape`
for a standard long-form asset or `portrait` for Shorts, honoring a different supported target
explicitly requested by the creator.
Use creator-supplied imagery for an authorized host likeness.

Call `vidiq_generate_thumbnail` once per approved render. Save and poll each job, then inspect
actual pixels using host vision or explicit human review: legibility, factual objects, text,
numbers, units, labels, logos, likeness, and attribution. Return generated URLs; unseen images
remain unverified drafts and cannot win an inspected-render comparison.

## Score only when useful

Separate `vidiq_score_thumbnail` calls require a real published `videoId`, intended `title`,
and image via `image`. For unpublished concepts, verify a relevant own-channel proxy video and
disclose it as reference context before scoring. Keep proxy and title context consistent; never
invent IDs or use unrelated proxies.

Without a suitable proxy, report separate scoring unavailable and use returned self-critique
plus labeled qualitative review. Do not compare generator self-scores directly with separate
scorer results or treat either as proof of factual authenticity.

## Refine within scope

Use `vidiq_refine_thumbnail` for the requested edit; preserve the intended orientation explicitly.
Masked edits retain source dimensions. Default to one refinement unless more iterations are
requested; keep them bounded. Change one variable for a controlled comparison.

Save and poll that job, inspect the result, and use returned critique before requesting separate
scoring when missing or necessary for comparability. Keep the version that best meets the brief
and passes factual and visual review, explaining score tradeoffs.
