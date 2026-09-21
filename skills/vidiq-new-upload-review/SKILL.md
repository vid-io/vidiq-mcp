---
name: vidiq-new-upload-review
description: Triage a newly published YouTube video against its channel's normal performance curve with the connected vidIQ MCP. Use when a creator asks whether an upload is ahead, on track, or behind; whether to wait or inspect packaging; or when to reassess performance during the first hours or days after publication.
---

# vidIQ New Upload Review

Read [Live surface notes](references/live-surface-notes.md) before starting this workflow,
including analysis that uses only supplied evidence.

Judge a new upload against the channel's performance at the same publication age. Recommend
whether to hold, inspect, or prepare a packaging change; do not change YouTube metadata/settings.

## Compare the trajectory

1. Establish video, channel, goal, format, publication time, and current age from supplied context.
   Agree on the bounded evidence plan and live cost.
2. For “my channel” or private analytics, resolve the authorized target with `vidiq_user_channels`.
   For “my newest upload,” use `vidiq_channel_videos` with `popular: false` and confirmed
   `videoFormat: long`, `short`, or `live`, then confirm the returned video.
3. Use `vidiq_get_videos_by_ids` for context, `vidiq_video_stats` for history, and
   `vidiq_channel_performance_trends` for the recent-video post-publication curve.
   Stats requires `granularity`: prefer `hourly` for early launches; use coarser intervals only
   when age/window warrants them.
4. Compare cumulative `views` at equivalent `minutesSincePublication`. Use returned
   `views.perc30`, median, and `views.perc70`; missing percentiles are unavailable, not replaceable
   by min/max. VPH is not cumulative views. Disclose age mismatch and mixed-format limitations
   of the channel-wide curve. Do not manufacture checkpoints or extrapolate beyond observations.

## Choose the next action

- **Hold:** evidence is sparse, incomparable, or insufficient to justify intervention.
- **Inspect:** repeated weakness against an age-matched baseline warrants investigation.
  A percentile crossing alone cannot identify packaging as the cause.
- **Prepare a change:** weakness has corroboration from supported analytics, supplied Studio
  data, or qualitative comments, with competing explanations and confidence stated.
  Without corroboration, keep the decision at hold or inspect.

Inspect only decision-relevant evidence within scope: authorized `vidiq_channel_analytics`,
supplied Studio CTR/impressions, or `vidiq_video_comments`. Thumbnail CTR/impressions are not in
the analytics metric enum; annotation CTR and ad impressions are not substitutes. Comments and
scores cannot prove low CTR or its cause. Use `vidiq_score_title`/`vidiq_score_thumbnail` only
when useful and after exact action/cost approval.

A known factual or formatting error can warrant correction at any age, independently of
performance. Choose a reassessment point from the observed channel curve, with no universal
waiting period or fixed checkpoint count.

## Deliver

Report publication age, evidence window, observed trajectory/bands and their gaps, and the
count/ages of checkpoints used. Give the decision, strongest evidence for and against it,
confidence, and next measurement/checkpoint. An unresolved video or channel prevents a trajectory
claim; a recommendation does not mean a change was applied.
