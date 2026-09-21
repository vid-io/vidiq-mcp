---
name: vidiq-video-ideas
description: Discover adaptable video concepts from outlier title mechanisms across adjacent-audience niches, using own-channel and competitor diagnostics with the connected vidIQ MCP. Use when a creator asks what is working right now, wants breakout inspiration, wants a recurring idea scan, or needs concept candidates to feed into packaging.
---

# vidIQ Video Ideas

Read [Live surface notes](references/live-surface-notes.md) before starting this workflow,
including analysis that uses only supplied evidence.

Find adaptable concepts in videos that overperform on their source channels. Use the creator's
own channel and competitors as context; look across adjacent niches for title mechanisms serving
the same viewer motivation. Hand off full packaging to `vidiq-packaging-studio`.

## Establish the scan

Read [Discovery evidence](references/discovery-evidence.md) before evaluating concept sources,
including supplied examples.

Use supplied channel, niche, viewer, format, language, and market context. Ask only when missing
information changes the scan. Agree on a small research budget; one or two outlier calls per
mechanism lane is a useful starting point, including the shared bounded correction.

Resolve canonical channel IDs from supplied context, `vidiq_user_channels`, or exact-handle
`vidiq_channel_search`. Authorized IDs do not supply niche classifications. Reuse a supplied
niche; otherwise search a known handle/title and verify the returned `channelId` before using
`niche` or `subNiches`. Use `vidiq_get_channels_by_ids` for a missing title only if necessary
and approved. Missing classification stays unknown or needs creator input.

Keep these evidence lanes distinct:

- **Own channel:** use matching-format `vidiq_channel_videos` and authorized analytics when useful.
  Catalog calls require `videoFormat: long`, `short`, or `live`. For sampled per-video analytics,
  use `dimensions: ["video"]` and `filters: "video==ID1,ID2"` in batches of at most 150.
  Missing requested rows are unknown.
- **Exact niche:** use an existing `vidiq_list_competitors` result or `vidiq_similar_channels`.
  Canonical `channelId` mode permits optional `size`/`sort`; manual `niche` mode has separate
  filters and no `subNiches` input. Country may affect ranking rather than eligibility.
  Exclude self, known siblings, and unrelated channels from analysis; disclose uncertainty and
  leave the saved list unchanged.
- **Adjacent niches:** use audience-focused semantic `vidiq_channel_search` and known creators.
  Verify returned market fit. Shared viewer motivation, not topical similarity alone, supports
  transfer; a small scan cannot prove the creator's audience has never seen a concept.

## Discover and judge concepts

1. Search `vidiq_outliers` with mechanism-shaped `keyword` queries, such as “I analyzed 100…”.
   Use `requireAllTitleTerms: false` for semantic discovery and strict `true` phrases as support;
   verify exact wording locally. Reserve own/competitor `channelIds` scans for separate context
   (up to 50 IDs). Set recent `publishedWithin`, matching `contentType`, and `sort: breakoutScore`.
2. Check the format/language combination. Outliers rejects non-English Shorts and has no live-only
   lane. For non-English outliers, `all` narrows to long-form and discovery is capped at six months.
   Pass a supported `language` explicitly; omission means English. A supported
   `vidiq_trending_videos` alternative uses `videoFormat` and `videoTitleLanguage`, but measures
   absolute velocity rather than channel-relative breakout. Disclose unavailable coverage.
3. Use `vidiq_similar_videos` selectively for independent executions of a seed. Choose the live
   `matchOn`, set `excludeSeedChannel: true` when appropriate, and inspect `signalsUsed`,
   `signalsFailed`, and `matchedBy` before relying on matches.
4. Apply the shared relevance/independence rule to inspected titles and images. Test whether the
   promise survives adaptation, audience overlap is credible, and production is feasible.
   Exclude fame-dependent or unaffordable mechanisms from feasible adaptations.
5. Name each surviving mechanism and explain its transfer. Rank with an editorial rubric for
   audience fit, originality, truthful payoff, and feasibility; label the rubric result separately
   from evidence confidence. Consider views, channel size, publication age, baseline stability,
   and market. Nonpositive or tiny baselines cannot establish reliable relative uplift.
   Favor feasible small-channel examples without excluding larger sources.
   Parse outlier `videoPublishedAt` as epoch seconds before comparing ages with ISO dates.
   Validate adapted-topic demand with `vidiq_keyword_research`, `mode: research`, only if useful.

For recurring scans, exclude previously shown video IDs; persist lanes and the seen list in a
client file/project note only when the creator wants a standing workflow.

## Deliver

Return concept cards with source/link and lane, actual performance context, inspected thumbnail
evidence or its limitation, the adapted concept, mechanism/transfer reasoning, and a working title,
hook, and format direction. Include separate rubric judgments and evidence confidence.

Report scan coverage, exclusions, and costs once for the scan rather than on every card.
These are research candidates, not performance predictions. Generate no assets or tool-based
scores; use original wording and hand eligible concepts to packaging.
