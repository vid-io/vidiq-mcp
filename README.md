# vidIQ YouTube MCP Server

**vidIQ's YouTube MCP server for ChatGPT, Claude, Cursor, and other MCP clients, with a creator
workflow plugin.**

[vidIQ MCP](https://vidiq.com/mcp/) is a hosted YouTube MCP server. It connects ChatGPT, Claude,
Codex, Cursor, Gemini CLI, GitHub Copilot, and other MCP-compatible AI assistants to live vidIQ data:
YouTube channel analytics, keyword research, outlier and trending videos, comments, transcripts,
competitor channels, and title and thumbnail scoring. Study public Instagram and TikTok short-form
content when those tools are exposed by the connected account, and analyze private YouTube
performance for channels connected to your vidIQ account. vidIQ runs the server at
`https://mcp.vidiq.com/mcp`, so you don't host anything or set up a YouTube Data API key or Google
Cloud project.

The workflow plugin turns that data into better content decisions with guided creator playbooks.

**[Connect in ChatGPT](#chatgpt)** ·
**[Connect in Claude.ai](#claudeai)** ·
**[Install the workflow plugin](#workflow-plugin)** ·
[Setup guide](https://support.vidiq.com/en/articles/15082430-vidiq-mcp)

> [!NOTE]
> vidIQ hosts the MCP service. This repository distributes connection metadata and a creator
> workflow pack for compatible AI clients.

vidIQ MCP can access data available to the vidIQ account and channels you authorize. Tool results
are returned to the AI client you choose, whose privacy practices also apply. See the
[vidIQ Privacy Policy](https://vidiq.com/privacy/) and the
[disconnect instructions](#disconnect-or-switch-accounts).

## What you can do

Use live vidIQ data to decide what to make next and understand how your content performs:

- Discover video ideas, emerging trends, and opportunities in your niche (`vidiq_outliers`,
  `vidiq_trending_videos`, `vidiq_similar_videos`).
- Research keywords and search demand, then draft tags and descriptions (YouTube SEO)
  (`vidiq_keyword_research`).
- Research competitors, successful videos, and the questions viewers ask in comments
  (`vidiq_channel_search`, `vidiq_similar_channels`, `vidiq_comment_insights`).
- Analyze any public video to learn why it performed (`vidiq_video_stats`,
  `vidiq_video_transcript`, `vidiq_video_watch`).
- Review your channel's performance, new uploads, and audience retention
  (`vidiq_channel_analytics`, `vidiq_channel_performance_trends`).
- Improve titles and thumbnails with research, scoring, and creative workflows, then apply approved
  changes to videos you own (`vidiq_score_title`, `vidiq_generate_thumbnail`, `vidiq_update_video`).
- Study public Instagram and TikTok content for patterns to adapt to YouTube Shorts
  (`vidiq_instagram_tiktok_outlier_search`).
- Draft comment replies, generate chapters, estimate earnings, and save research to
  bookmarks (`vidiq_generate_comment_replies`, `vidiq_generate_video_chapters`,
  `vidiq_video_earnings_estimate`, `vidiq_bookmarks_save`).

See [Tools the workflows use](#tools-the-workflows-use) for the full tool list.

YouTube research covers public channels and videos; private analytics require a channel
authorized in your vidIQ account. Instagram and TikTok research depends on the tools available
to your connected account. Coverage varies by tool, format, language, and market; ask the
assistant to check availability before starting research.

## Connect vidIQ

Step-by-step guides for each client are on vidiq.com:
[ChatGPT](https://vidiq.com/how-to-use-vidiq-in-chatgpt/),
[Claude](https://vidiq.com/how-to-use-vidiq-in-claude/), [Cursor](https://vidiq.com/cursor/),
[Codex](https://vidiq.com/codex/), [Gemini CLI](https://vidiq.com/gemini-cli/),
[Perplexity](https://vidiq.com/perplexity/), [Grok](https://vidiq.com/grok/), and
[OpenClaw](https://vidiq.com/openclaw/).

### ChatGPT

Install the [official vidIQ app](https://chatgpt.com/plugins/plugin_asdk_app_69dd11f3e50c8191b1ca48d03cf7e2ad)
directly in ChatGPT:

1. Open the app listing and select **Install** or **Try it**.
2. Sign in with the vidIQ account you want to use. It does not need to share an email address with
   your ChatGPT account.
3. Grant access. The hosted vidIQ tools are then available in your ChatGPT conversations.

If the listing does not open directly, find **vidIQ** in the
[ChatGPT plugin directory](https://chatgpt.com/plugins).

Try asking:

> What topics are trending in my niche that I have not covered yet?

The ChatGPT plugin connects the hosted vidIQ tools, and current releases also bundle the creator
workflows from this repository as skills; new workflows arrive with the next plugin release. Type
`@vidIQ` at the start of a prompt to use it explicitly, or describe the outcome you want and ChatGPT
picks the matching skill.

### Claude.ai

Add vidIQ as a
[custom connector in Claude.ai](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp):

1. Open **Customize → Connectors**.
2. Select **Add custom connector**.
3. Name the connector **vidIQ** and enter `https://mcp.vidiq.com/mcp`.
4. Add the connector, then authorize the vidIQ account you want to use.
5. In a conversation, open **+ → Connectors** and enable vidIQ when needed.

For Team and Enterprise organizations, an organization owner must add the connector before
members can use it.

The Claude.ai connector makes the hosted vidIQ tools available in conversations. It does not
install the workflow skills from this repository; those require a compatible plugin client such
as Claude Code.

### Workflow plugin

Install the vidIQ workflow plugin to connect your AI client to vidIQ's hosted tools and add guided
creator workflows and safe recovery for long-running jobs. Clients with
bundled-agent support can also load the [vidIQ specialist](agents/vidiq-mcp.agent.md) to select the
right workflow. Shared rules cover scope, evidence quality, and permissions; discovery,
production, and job-recovery guidance loads when relevant to the request. The capabilities and
prices shown in your connected client apply.

#### Claude Code

Run these commands in your terminal:

```bash
claude plugin marketplace add vid-io/vidiq-mcp
claude plugin install vidiq@vidiq-plugins
```

This installs the plugin for your user account across projects. Restart Claude Code, then run
`/mcp` and authenticate the vidIQ server when prompted. See the
[Claude Code plugin guide](https://code.claude.com/docs/en/discover-plugins) for installation
scopes and updates.

Invoke workflows as `/vidiq:vidiq-get-started` or `/vidiq:vidiq-packaging-studio`.
Version 0.1.3 restores the `vidiq-` skill prefix. Version 0.1.4 renames Channel Review to
Channel Audit; invoke it as `/vidiq:vidiq-channel-audit`. Connection diagnostics and job
recovery are part of Get Started. Version 0.2.0 adds `/vidiq:vidiq-youtube-seo`,
`/vidiq:vidiq-video-breakdown`, and `/vidiq:vidiq-video-metadata`. Version 0.2.1 wires the newer
hosted tools: niche-wide comment insights and reply drafts, chapters, title and thumbnail change
history, own-video listing, earnings estimates, bookmarks, and YouTube channel connection. It also
folds Packaging Comparison into Packaging Studio as a compare mode and shortens every skill
description so the full list fits in Codex and ChatGPT.

#### Grok Build

The command below installs vidIQ directly from GitHub. It works without a Grok marketplace listing.
Install [Grok Build](https://x.ai/build), then run:

```bash
grok plugin install vid-io/vidiq-mcp --trust
```

Start a new session with `grok` and sign in to Grok if prompted. To connect your vidIQ account:

1. Open `/mcps` and expand **Plugin: vidiq**.
2. Select **vidiq** and press `i` to authenticate.
3. Complete vidIQ sign-in and authorization in your browser.
4. Return to Grok and run `/vidiq-get-started`.

If the connection fails, run `grok mcp doctor vidiq` in your terminal. See the
[Grok MCP guide](https://docs.x.ai/build/features/mcp-servers) for connection settings and help.

#### OpenClaw

You need OpenClaw with MCP bundle support and a vidIQ account. Install from ClawHub:

```bash
openclaw plugins install clawhub:@vidiq/vidiq
openclaw plugins inspect vidiq
openclaw skills list
```

Review the requested capabilities before accepting. Confirm that inspection lists `skills` and
`mcpServers`, and that the skill list includes the 14 `vidiq-` workflows.
Register the server for OpenClaw's login command, then authorize your vidIQ account:

```bash
openclaw mcp set vidiq '{"url":"https://mcp.vidiq.com/mcp","transport":"streamable-http","auth":"oauth"}'
openclaw mcp login vidiq
openclaw mcp doctor vidiq --probe
```

Complete sign-in in the browser and start your OpenClaw Gateway if it is stopped. In a new
agent conversation, ask: “Check my vidIQ connection, authorized channels, and credit balance.”
All agents using this setup share the connected vidIQ account. Only enable it for people you
trust with that account; credentials stay in OpenClaw's credential store.

If tools are missing, check the plugin and tool policy; the `minimal` profile or a denial of
`bundle-mcp` can hide them. See the [OpenClaw MCP guide](https://docs.openclaw.ai/tools/mcp)
and [bundle documentation](https://docs.openclaw.ai/plugins/bundles) for host requirements.

##### Switch accounts or remove vidIQ

Switch accounts with `openclaw mcp logout vidiq`, then `openclaw mcp login vidiq`.
Sign in with the intended account in the browser and confirm the authorized channels.
To remove the integration:

```bash
openclaw mcp logout vidiq
openclaw mcp unset vidiq
openclaw plugins uninstall vidiq
```

Removing only the saved server leaves the bundle's server definition available.

#### Hermes Agent

With a current Hermes version supporting
[portable plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/#portable-agent-plugins-v1-packages), run:

```bash
hermes plugins install vid-io/vidiq-mcp --no-enable
hermes plugins enable vidiq
hermes mcp add vidiq --url https://mcp.vidiq.com/mcp --auth oauth
```

Complete vidIQ authorization in your browser, then start a new session and ask Hermes to use
vidIQ Get Started. The plugin installs all 14 workflows; the separate MCP connection provides
the live tools. A vidIQ account is required, and hosted tools may consume credits.

Check the connection with `hermes mcp test vidiq`. If already configured, sign in again or switch
accounts with `hermes mcp login vidiq`, then confirm the authorized channels. See the
[Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/) for help.

To update, run `hermes plugins update vidiq` and start a new session. To remove vidIQ, run
`hermes plugins disable vidiq`, `hermes plugins remove vidiq`, and `hermes mcp remove vidiq`.
Removing only the plugin leaves the MCP connection active.

#### Local preview

For local preview, clone or download this repository and follow your client's local-plugin flow.
Install from a clean clone or archive, and keep ignored files, local credentials, and other
local-only files out of the package.

| Client | Local preview |
| --- | --- |
| [Claude Code](https://code.claude.com/docs/en/plugins) | `claude --plugin-dir /absolute/path/to/vidiq-mcp` (current session) |
| [Cursor](https://cursor.com/docs/plugins#test-plugins-locally) | Put the release files in `~/.cursor/plugins/local/vidiq`, then reload Cursor. Expand the Cursor steps below. |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) | `copilot plugin marketplace add /absolute/path/to/vidiq-mcp`<br>`copilot plugin install vidiq@vidiq-plugins` |
| [Gemini CLI](https://geminicli.com/docs/extensions/reference/) | `gemini extensions link /absolute/path/to/vidiq-mcp` |
| [Codex](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually) | Put the checkout at `<marketplace-root>/plugins/vidiq`, add the marketplace, then install `vidiq@vidiq-local`. Expand the Codex steps below. |

On Cursor Teams and Enterprise, you can also
[import this repository into a private team marketplace](https://cursor.com/docs/plugins#add-a-team-marketplace).

<details>
<summary>Cursor local installation steps</summary>

1. Download this repository with **Code → Download ZIP** and extract it.
2. Create `~/.cursor/plugins/local` if needed, then place the extracted folder there as `vidiq`.
   Keep the entire folder, including hidden files: `.cursor-plugin/plugin.json` and `.mcp.json`
   must be directly inside `~/.cursor/plugins/local/vidiq`.
3. Restart Cursor or run **Developer: Reload Window** from the Command Palette.
4. Open **Customize** and confirm that vidIQ's skills, lifecycle rule, and MCP server appear.
   Authorize the MCP connection when prompted.

Use a real directory: Cursor skips symlinks pointing outside `~/.cursor/plugins/local`.
If `vidiq` already exists there, remove only the symlink or move the existing directory aside first.

For Teams and Enterprise, your administrator must enable **Allow Local Plugin Imports** under
**Dashboard → Settings → Security & Identity → Marketplace and Plugins**. Enterprise disables
this by default. An installed marketplace plugin with the same name takes precedence over a
local copy.

</details>

<details>
<summary>Codex local installation steps</summary>

Create a local marketplace root, place a copy of this checkout at
`/absolute/path/to/local-marketplace/plugins/vidiq`, and add this file at
`/absolute/path/to/local-marketplace/.agents/plugins/marketplace.json`:

```json
{
  "name": "vidiq-local",
  "interface": {
    "displayName": "vidIQ Local"
  },
  "plugins": [
    {
      "name": "vidiq",
      "source": {
        "source": "local",
        "path": "./plugins/vidiq"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Creativity"
    }
  ]
}
```

Then run:

```bash
codex plugin marketplace add /absolute/path/to/local-marketplace
codex plugin add vidiq@vidiq-local
codex plugin list
```

Restart the Codex or ChatGPT desktop app and start a new conversation to load the plugin.

</details>

Restart or reload the client when required, complete vidIQ authorization in the browser, and say:

> Help me get started with vidIQ and choose a useful first workflow.

The Get Started workflow verifies authorization and the returned authorized channels, shows your
credit balance, and starts with one focused creator decision. If you have already connected,
verify everything without launching creative work:

> Check my vidIQ MCP status.

### Server-only MCP connection

If your AI client supports remote MCP servers but not plugins, add vidIQ as a Streamable HTTP
server. This connects the live vidIQ tools but does not install the guided workflows.

```text
https://mcp.vidiq.com/mcp
```

<details>
<summary>Show the MCP configuration</summary>

For Codex:

```bash
codex mcp add vidiq --url https://mcp.vidiq.com/mcp
codex mcp login vidiq
```

For clients that accept `.mcp.json`:

```json
{
  "mcpServers": {
    "vidiq": {
      "type": "http",
      "url": "https://mcp.vidiq.com/mcp"
    }
  }
}
```

OAuth-capable clients open vidIQ's browser sign-in. Follow the
[official setup guide](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) for current client
instructions. If your client uses a vidIQ API key, keep it in the client's secret store. Never put
credentials in chat, issues, or shared configuration.

</details>

### Disconnect or switch accounts

To stop a client from using vidIQ, disable or remove the app, connector, plugin, or MCP server in
that client's settings. Manage the ChatGPT app under **Settings → Apps** and the Claude.ai
connector under **Customize → Connectors**.

To switch vidIQ accounts, disconnect the current connection in the client, sign in to the intended
account in the authorization browser, and connect again. For personal-data access or deletion
requests, follow the **Exercising Your Data Subject Rights** instructions in the
[vidIQ Privacy Policy](https://vidiq.com/privacy/).

For OpenClaw commands, see [Switch accounts or remove vidIQ](#switch-accounts-or-remove-vidiq).

## Try these creator prompts

Use natural language. Replace the bracketed details, or give the assistant a channel or video URL.

- **Choose the next video:** “Use my recent channel performance, current demand, and competitor
  whitespace to rank three original ideas for my next `[format]` upload.”
- **Review channel health:** “Review my channel's last 90 days. Separate long-form and Shorts,
  explain what strengthened or weakened, and prioritize three improvements.”
- **Find an opening:** “Show me `[niche]` channels between `[subscriber floor]` and 100K
  subscribers that are breaking out this month. Explain the patterns I can adapt without copying
  them.”
- **Triage a launch:** “Compare my latest upload's first 48 hours with my normal channel baseline.
  Show the evidence before recommending any change.”
- **Diagnose retention:** “Align this video's retention changes with its transcript and comments.
  Identify the moments I should improve next time.”
- **Compare packaging:** “Compare three distinct title and thumbnail concepts for
  `[idea]`, grounded in current creator evidence.”
- **Learn the audience's language:** “Turn recurring viewer language in these comments into hooks
  and content briefs. Omit usernames and personal details from your answer.”
- **Judge a trend window:** “Find high-velocity topics in `[niche]` and separate short-lived spikes
  from durable search demand.”
- **Rank for search:** “Research keywords for a video about `[topic]`, tell me whether people search
  for it, and draft the tags and description.”
- **Learn from any video:** “Analyze `[video URL]` and explain why it performed, what the hook does,
  and what I can adapt without copying it.”
- **Apply a change:** “Update my video `[video ID]` with this approved title and these tags, show me
  the before and after, and confirm what changed.”
- **Answer your viewers:** “Draft three replies to this comment in my channel's voice.”
- **Estimate earnings:** “Estimate what this video earned, and what 500,000 monthly views would earn
  in my niche.”

## Creator workflows

Choose a workflow for the decision you want to make. The assistant can also select one from your
request.

### Connect and choose a direction

| Workflow | Best for | Say |
| --- | --- | --- |
| [Get Started](skills/vidiq-get-started/SKILL.md) | Connect vidIQ, check channels and credits, troubleshoot errors, recover jobs, and choose a workflow. | “Is vidIQ connected, and which channel is linked?” |
| [Next Video Planner](skills/vidiq-next-video-planner/SKILL.md) | Build an evidence-backed next-video brief from channel fit, search demand, trends, outliers, and competitor patterns. | “What should my next video be?” |
| [Video Ideas](skills/vidiq-video-ideas/SKILL.md) | Scan outliers across the creator's channel, niche, and adjacent-audience niches for adaptable concept candidates. | “Give me 10 video ideas based on what's breaking out in my niche.” |
| [YouTube SEO](skills/vidiq-youtube-seo/SKILL.md) | Research keywords and search demand, then draft tags, a description, and title angles. | “Which keywords should I target for a video about `[topic]`?” |
| [Trend Radar](skills/vidiq-trend-radar/SKILL.md) | Separate urgent breakouts and short-lived spikes from durable search demand. | “What's trending in `[niche]` this week, and is it too late?” |
| [Competitor Watchlist](skills/vidiq-competitor-watchlist/SKILL.md) | Propose precise additions and removals before changing the competitors tracked in vidIQ. | “Who are my competitors, and should I track any emerging channels?” |

### Understand performance and opportunity

| Workflow | Best for | Say |
| --- | --- | --- |
| [Channel Audit](skills/vidiq-channel-audit/SKILL.md) | Audit 30–90 days of channel performance and prioritize the next actions. | “Why did my views drop this month?” |
| [New Upload Review](skills/vidiq-new-upload-review/SKILL.md) | Compare a new upload with the channel's normal curve before deciding whether to wait or intervene. | “I uploaded yesterday and it's underperforming. Change the thumbnail or wait?” |
| [Retention Analysis](skills/vidiq-retention-analysis/SKILL.md) | Align retention changes with transcript, scenes, and comments to find moments worth improving. | “Where do viewers drop off in this video?” |
| [Comment Insights](skills/vidiq-comment-insights/SKILL.md) | Turn recurring, de-identified viewer language into hooks, briefs, titles, and audience insight. | “What questions keep coming up in my comments?” |
| [Video Breakdown](skills/vidiq-video-breakdown/SKILL.md) | Analyze any public video's performance history, packaging changes, hooks, and comment themes. | “Analyze this video and tell me why it went viral.” |

### Package and produce

| Workflow | Best for | Say |
| --- | --- | --- |
| [Packaging Studio](skills/vidiq-packaging-studio/SKILL.md) | Turn a source video, concept card, script draft, rough idea pitch, or underperforming published video into scored titles, a thumbnail, and an optional script, or compare distinct title and thumbnail directions for the same video. | “Write five titles and a thumbnail idea for this video.” |
| [Video Metadata](skills/vidiq-video-metadata/SKILL.md) | Apply an approved title, description, tags, schedule, or thumbnail change to a video you own, with a snapshot and readback. | “Update my video with this title and these tags.” |
| [Shorts Inspiration](skills/vidiq-shorts-inspiration/SKILL.md) | Study short-form content patterns and develop original YouTube Shorts ideas. | “What's working on TikTok in my niche that I could adapt for Shorts?” |

## Tools the workflows use

The hosted server exposes these tools; the workflows call them by name and check the live list
first because availability varies by account and client. The Claude.ai directory connector omits
the tools in the last column; adding `https://mcp.vidiq.com/mcp` as a custom connector with
browser sign-in exposes the full set. Changes to your channel need owner access, YouTube
verification, and your approval of the exact change.

| Job | Tools (free tools in italics; async tools return a job to poll) | Claude.ai directory connector |
| --- | --- | --- |
| Account, jobs, and bookmarks | *`vidiq_user_channels`*, *`vidiq_balance`*, *`vidiq_connect_youtube_channel`*, *`vidiq_authorize_with_youtube`*, *`vidiq_jobs_list`*, *`vidiq_job_poll`*, *`vidiq_bookmarks_list`*, *`vidiq_bookmarks_save`*, *`vidiq_bookmarks_remove`*, *`vidiq_submit_feedback`* | all except `vidiq_connect_youtube_channel`, `vidiq_authorize_with_youtube` |
| Keyword and topic research | `vidiq_keyword_research`, `vidiq_trending_videos`, *`vidiq_trend_categories`*, `vidiq_youtube_search` | all |
| Ideas and outliers | `vidiq_outliers`, `vidiq_similar_videos`, `vidiq_similar_thumbnails`, `vidiq_instagram_tiktok_outlier_search` | all |
| Channels and competitors | `vidiq_channel_search`, `vidiq_channel_stats`, `vidiq_get_channels_by_ids`, `vidiq_similar_channels`, `vidiq_channel_videos`, *`vidiq_list_competitors`*, *`vidiq_update_competitors`* | all |
| Video evidence | `vidiq_get_videos_by_ids`, `vidiq_video_stats`, `vidiq_video_change_history`, `vidiq_video_transcript`, `vidiq_video_comments`, `vidiq_comment_insights` (async), `vidiq_video_watch` (async), `vidiq_watch_shortform_content` (async), `vidiq_video_earnings_estimate`, `vidiq_earnings_calculate` | all except `vidiq_comment_insights` |
| Private analytics (authorized channel) | `vidiq_channel_analytics`, `vidiq_channel_performance_trends`, `vidiq_subscriber_insights`, `vidiq_user_videos` | all |
| Titles, thumbnails, scripts, and chapters | `vidiq_generate_titles`, `vidiq_score_title`, `vidiq_generate_thumbnail` (async), `vidiq_refine_thumbnail` (async), `vidiq_score_thumbnail`, `vidiq_generate_script` (async), `vidiq_generate_video_chapters` (async), `vidiq_generate_comment_replies` | all except `vidiq_generate_thumbnail`, `vidiq_refine_thumbnail`, `vidiq_generate_video_chapters`, `vidiq_generate_comment_replies` |
| Changes to your channel (owner access, approval required) | `vidiq_update_video`, `vidiq_update_video_thumbnail` | none |
| Media production | *`vidiq_video_upload`*, `vidiq_generate_clips` (async), `vidiq_generate_broll`, `vidiq_compose` (async), `vidiq_edit_media` (async), `vidiq_motion_graphics` (async), `vidiq_generate_music` (async), *`vidiq_voiceover_list_voices`*, `vidiq_voiceover_generate` (async), `vidiq_generate_video` (async) | all except `vidiq_video_upload`, `vidiq_generate_music`, `vidiq_voiceover_list_voices`, `vidiq_voiceover_generate`, `vidiq_generate_video` |
| Instagram | `vidiq_ig_profile`, `vidiq_ig_profile_reels`, `vidiq_ig_accounts_from_outliers`, `vidiq_instagram_connected_accounts`, `vidiq_instagram_owner_insights`, `vidiq_instagram_publish_reel` | all except `vidiq_instagram_connected_accounts`, `vidiq_instagram_owner_insights`, `vidiq_instagram_publish_reel` |

## You stay in control

- Authorization belongs to your vidIQ account; your AI client email does not need to match it.
- Private YouTube analytics are available only for channels authorized in that vidIQ account.
- Hosted tools may consume vidIQ credits. Ask for your balance and the current cost before
  starting a workflow; the connected service reports the applicable capabilities and prices.
- Tool results are sent to your AI client, whose privacy practices also apply. Never put
  passwords, API keys, or authorization tokens in chat or shared configuration.
- Some tools can create media, update tracked competitors, or edit your YouTube videos.
  Changes to your account or published videos require your approval. YouTube updates also
  require authorized owner access and YouTube verification.
- The bundled guidance tells the assistant to preserve long-running job IDs and resume existing
  work instead of accidentally starting a duplicate.

Availability varies by account and client.

## Common questions

**Does vidIQ work with ChatGPT and Claude?** Yes. Install the vidIQ plugin in ChatGPT, add the vidIQ
connector in Claude.ai, or install this plugin in Claude Code, Codex, Cursor, Gemini CLI, GitHub
Copilot, Grok Build, Hermes Agent, or OpenClaw. See [Connect vidIQ](#connect-vidiq).

**Can the assistant see my YouTube analytics?** Private analytics are available only for channels
authorized in your vidIQ account. Public research works for any channel or video.

**Can it change my videos?** Only through the Video Metadata workflow (video details, chapters,
thumbnail), only for channels you own with
browser sign-in and YouTube verification, and only after you approve the exact change. Competitor
list changes and Instagram publishing also wait for your approval.

**Does it use credits?** Hosted tools may consume vidIQ credits. Ask for your balance and the current
cost before a workflow; the connected service reports the applicable prices.

**Which workflow should I ask for?** Describe the outcome in plain language. The assistant picks the
matching workflow from the [Creator workflows](#creator-workflows) tables, or name one directly.

## Help and support

- [vidIQ MCP product page](https://vidiq.com/mcp/)
- [Setup, usage, credits, and troubleshooting](https://support.vidiq.com/en/articles/15082430-vidiq-mcp)
- [vidIQ Support](https://support.vidiq.com/)
- [Privacy Policy](https://vidiq.com/privacy/)
- [Terms of Service](https://vidiq.com/terms/)

Use GitHub issues for this plugin's documentation, manifests, or workflow skills. Take account,
authorization, billing, credit, and hosted-service problems to vidIQ Support. Report suspected
vulnerabilities privately by following [SECURITY.md](SECURITY.md), and never post credentials,
private analytics, or job URLs in an issue.

## License

Unless otherwise noted, the files in this repository are licensed under the
[Apache License 2.0](LICENSE). Copyright and trademark attribution is recorded in [NOTICE](NOTICE).
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) is adapted from the Contributor Covenant and is licensed
separately under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Use of the hosted service remains subject to
the [vidIQ Terms](https://vidiq.com/terms/) and [Privacy Policy](https://vidiq.com/privacy/). These
repository licenses apply only to files in this repository.

The vidIQ name and logos are trademarks of vidIQ, Inc. The Apache License 2.0 does not grant
permission to use those marks, and modified versions must not imply vidIQ affiliation or
endorsement.

All third-party product names and trademarks are the property of their respective owners.
References indicate compatibility only and do not imply affiliation, sponsorship, or endorsement.
