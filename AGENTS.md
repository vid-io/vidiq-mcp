# vidIQ MCP agent guide

This repository packages connection metadata and creator-workflow skills for the hosted vidIQ MCP
service across Claude, Codex, Cursor, GitHub Copilot, Gemini, Grok Build, Hermes Agent, and OpenClaw.

Apply this guide to vidIQ requests and vidIQ MCP calls. Do not start onboarding, account checks,
or creator research for an unrelated task. Read
[Live surface notes](references/live-surface-notes.md), including when analyzing supplied evidence.
Load only the selected skill and references relevant to the request.

## Connect

Follow the client-specific flow in [README.md](README.md). The hosted Streamable HTTP endpoint is
`https://mcp.vidiq.com/mcp`; compatible clients open a browser for vidIQ authorization. Never ask
the user to paste credentials into chat or save them in shared configuration.

If vidIQ tools are not visible, help the user confirm that the plugin or MCP connection is enabled
and authorized. If the wrong account or channel appears, suggest reconnecting with the intended
vidIQ account.

## Route by what the creator asks

| Creator asks | Skill |
| --- | --- |
| Connect vidIQ or a YouTube channel, check channels or credits, fix errors, recover a job | `vidiq-get-started` |
| What should I post next for my channel | `vidiq-next-video-planner` |
| Video ideas, what's working in my niche, outliers | `vidiq-video-ideas` |
| Keywords, search volume, tags, description, YouTube SEO | `vidiq-youtube-seo` |
| What's trending, is this trend worth it, timing | `vidiq-trend-radar` |
| Who are my competitors, similar channels, watchlist changes | `vidiq-competitor-watchlist` |
| How is my channel doing, views dropped, 30-, 60-, or 90-day review | `vidiq-channel-audit` |
| I just uploaded and it is underperforming | `vidiq-new-upload-review` |
| Where viewers drop off, retention, watch time | `vidiq-retention-analysis` |
| What viewers say or want in the comments, niche-wide audience requests, draft a comment reply | `vidiq-comment-insights` |
| Analyze this video, why did it go viral | `vidiq-video-breakdown` |
| Titles, thumbnails, scripts, repackage a video, compare packaging directions | `vidiq-packaging-studio` |
| Update a video's title, description, tags, chapters, schedule, or thumbnail | `vidiq-video-metadata` |
| Shorts ideas from Reels and TikTok | `vidiq-shorts-inspiration` |

For end-to-end "find an idea and package it" requests, run `vidiq-video-ideas` first and feed its
concept cards into `vidiq-packaging-studio`. When the creator already has a script draft, a rough idea
pitch, or a published video that needs repackaging, go straight to `vidiq-packaging-studio`; it handles
diagnosis and reference discovery itself. For a focused title or thumbnail edit, use only the relevant
studio stage; its compare section handles distinct creative directions. Apply approved changes to an
owned video only through `vidiq-video-metadata`.

## Calls without a dedicated workflow

Read [Discovery evidence](references/discovery-evidence.md) before recurring discovery-pattern
claims, and [Job lifecycle](references/job-lifecycle.md) before asynchronous work.

Tools with no workflow of their own, and the rule for each:

- **Earnings:** `vidiq_earnings_calculate` is a what-if calculator (`subject`, `monthlyViews`,
  `category`, `format`); `vidiq_video_earnings_estimate` prices one real video. Both are estimates
  that assume a monetized channel.
- **Clips and uploads:** `vidiq_generate_clips` turns a long video into vertical clips as an
  asynchronous job and charges per minute of the selected range, so confirm the range and cost
  first. `vidiq_video_upload` imports an MP4 or public URL and returns a hosted `videoUrl` at no
  charge.
- **Instagram publishing:** `vidiq_instagram_publish_reel` publishes a vidIQ-hosted video to a
  connected account with `publishingAvailable: true` after approval of the exact video, account,
  caption, and settings. Keep `containerId` and `platformAccountId` across calls and stop on any
  error.
- **Media generation:** `vidiq_generate_broll`, `vidiq_compose`, `vidiq_edit_media`,
  `vidiq_motion_graphics`, `vidiq_generate_music`, the `vidiq_voiceover_*` tools, and
  `vidiq_generate_video` are asynchronous jobs; confirm the cost before starting.
- **Bookmarks:** `vidiq_bookmarks_save`, `vidiq_bookmarks_list`, and `vidiq_bookmarks_remove` keep
  the creator's saved research; save or remove only on an explicit request.
- **Deprecated aliases:** `vidiq_breakout_channels`, `vidiq_ig_reel_watch`, and
  `vidiq_ig_outlier_reels_search` are replaced by `vidiq_channel_search` with
  `breakoutChannel: true`, `vidiq_watch_shortform_content`, and
  `vidiq_instagram_tiktok_outlier_search`.

For media generation, confirm only the source, likeness, and speaker rights relevant to that
medium; preserve required attribution. Reuse rights already established for the supplied assets.
Voice cloning requires explicit speaker consent. Keep temporary or signed media URLs within the
user's requested workflow.
