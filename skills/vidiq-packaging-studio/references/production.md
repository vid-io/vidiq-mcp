# Produce and score packaging

Use only the requested production stages. Before an asynchronous call, read
[Job lifecycle](job-lifecycle.md).

## Titles

Pass the confirmed `type` and `language` to `vidiq_generate_titles`. Omitted values can produce
long-form English titles for an unpublished Short. Check generation's language codes separately
from discovery.

Generation already returns scores. Use `vidiq_score_title` for new/changed candidates or necessary
comparable context, with confirmed `type: long` or `short` and the creator's `channelId` when
available. Do not rescore unchanged text in the same context.

Treat scores as directional, not predicted CTR; preserve an honest, strategically strong option
despite a lower score. A payoff within roughly 55 characters is a preview heuristic, not a
universal truncation rule. Inspect the title-thumbnail pair at small display size when possible;
otherwise mark the preview unverified.

## Thumbnails

Before rendering or refining, establish rights to the source assets and any depicted likeness;
preserve required attribution. Reuse established rights and ask only about missing permissions
relevant to the requested image.

Build from the brief, brand, and authorized assets. An external reference is optional; identify
its abstract contribution and the original changes when used. Let the thumbnail complement the
title. Use channel evidence for host-led versus object-led design, not a universal performance
rule. A host covering someone else's story must not appear to have lived it.
Use creator-supplied imagery for an authorized host likeness.

Set `orientation: "landscape"` for a standard long-form asset or `"portrait"` for a Shorts asset,
respecting a different supported target explicitly requested by the creator.

Call `vidiq_generate_thumbnail` once for each approved render and preserve its job ID. Return the
completed `imageUrl`. Inspect actual pixels with host vision or explicit human review: small-size
legibility, text, numbers, units, objects, labels, logos, likeness, and subject attribution.
An unseen image remains an unverified draft. Factual and visual review outrank scores.

## Separate thumbnail scoring

`vidiq_score_thumbnail` requires a real published `videoId`, intended `title`, and image via
`image`; it scores the pair. For unpublished work, verify a relevant own-channel video as a
proxy and disclose its identity and reference role before scoring. Keep the proxy and title
context consistent for comparisons. Never invent an ID or use an unrelated proxy.

Without a suitable proxy, report separate scoring unavailable and use returned self-critique
plus labeled qualitative review. Generator self-scores and separate scorer results are not
interchangeable, and neither establishes factual authenticity.

## Refinement

Use `vidiq_refine_thumbnail` for the requested edit. Preserve the intended orientation explicitly;
masked edits retain source dimensions. Default to one refinement unless more iterations are
requested; keep them bounded. Change one variable for a controlled comparison.

Save and poll the refinement job, inspect the image, and use returned critique before requesting
additional scoring. Missing score/feedback remains missing; separately score only when needed.
Keep the best eligible result for the brief, not merely the highest score.

## Optional script

Use `vidiq_generate_script` only for a requested long-form script, with the selected topic, title,
concept, length, tone, and verified research. For Shorts, offer a brief grounded conversation
draft or an exposed tool that supports Shorts; do not pad it to the long-form tool's one-minute
minimum. Preserve any asynchronous script job and flag facts the creator still needs to verify.
