# vidIQ MCP Plugin

**Live creator intelligence, in your AI assistant.**

[vidIQ MCP](https://vidiq.com/mcp/) connects MCP-compatible AI assistants to live vidIQ data.
Research YouTube channels, videos, trends, and comments; study public Instagram
and TikTok short-form content when those tools are exposed by the connected account; and analyze
private YouTube performance for channels connected to your vidIQ account.

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

## Connect vidIQ

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

The ChatGPT app connects the hosted vidIQ tools. It does not install the workflow skills from this
repository; use the workflow plugin below in a compatible plugin client when you want those
guided playbooks.

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

## Creator workflows

Choose a workflow for the decision you want to make. The assistant can also select one from your
request.

In Claude Code, invoke skills as `/vidiq:vidiq-get-started` or `/vidiq:vidiq-packaging-studio`.
Version 0.1.3 restores the `vidiq-` skill prefix. Connection diagnostics and job recovery
are part of Get Started.

### Connect and choose a direction

| Workflow | Best for |
| --- | --- |
| [Get Started](skills/vidiq-get-started/SKILL.md) | Connect vidIQ, check channels and credits, troubleshoot errors, recover jobs, and choose a workflow. |
| [Next Video Planner](skills/vidiq-next-video-planner/SKILL.md) | Build an evidence-backed next-video brief from channel fit, search demand, trends, outliers, and competitor patterns. |
| [Video Ideas](skills/vidiq-video-ideas/SKILL.md) | Scan outliers across the creator's channel, niche, and adjacent-audience niches for adaptable concept candidates. |

### Understand performance and opportunity

| Workflow | Best for |
| --- | --- |
| [Channel Review](skills/vidiq-channel-review/SKILL.md) | Review 30–90 days of channel performance and prioritize the next actions. |
| [New Upload Review](skills/vidiq-new-upload-review/SKILL.md) | Compare a new upload with the channel's normal curve before deciding whether to wait or intervene. |
| [Retention Analysis](skills/vidiq-retention-analysis/SKILL.md) | Align retention changes with transcript, scenes, and comments to find moments worth improving. |
| [Comment Insights](skills/vidiq-comment-insights/SKILL.md) | Turn recurring, de-identified viewer language into hooks, briefs, titles, and audience insight. |
| [Trend Radar](skills/vidiq-trend-radar/SKILL.md) | Separate urgent breakouts and short-lived spikes from durable search demand. |
| [Competitor Watchlist](skills/vidiq-competitor-watchlist/SKILL.md) | Propose precise additions and removals before changing the competitors tracked in vidIQ. |

### Package and produce

| Workflow | Best for |
| --- | --- |
| [Packaging Comparison](skills/vidiq-packaging-comparison/SKILL.md) | Compare distinct title and thumbnail concepts for the same video using creator evidence. |
| [Packaging Studio](skills/vidiq-packaging-studio/SKILL.md) | Turn a source video, concept card, script draft, rough idea pitch, or underperforming published video into scored titles, a thumbnail, and an optional script for the creator's channel. |
| [Shorts Inspiration](skills/vidiq-shorts-inspiration/SKILL.md) | Study short-form content patterns and develop original YouTube Shorts ideas. |

## You stay in control

- Authorization belongs to your vidIQ account; your AI client email does not need to match it.
- Private YouTube analytics are available only for channels authorized in that vidIQ account.
- Some tools can create media, update tracked competitors, or edit your YouTube videos.
  Changes to your account or published videos require your approval. YouTube updates also
  require authorized owner access and YouTube verification.
- The bundled guidance tells the assistant to preserve long-running job IDs and resume existing
  work instead of accidentally starting a duplicate.

Availability varies by account and client.

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
