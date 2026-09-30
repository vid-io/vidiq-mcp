# vidIQ for Hermes Agent

Add 12 creator workflows for YouTube research, channel analytics, video planning, and packaging.
The plugin supplies the workflows; a separate OAuth connection supplies vidIQ's live MCP tools.
A vidIQ account is required. Hosted tools can consume credits; check the current tool prices
before starting work.

## Install and connect

Use an up-to-date Hermes installation with
[portable Agent Plugins support](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/#portable-agent-plugins-v1-packages).
Run:

```bash
hermes plugins install vid-io/vidiq-mcp --no-enable
hermes plugins enable vidiq
hermes mcp add vidiq --url https://mcp.vidiq.com/mcp --auth oauth
```

Follow the browser authorization flow using your intended vidIQ account. Keep credentials in
Hermes's profile storage. Never paste them into chat or add them to this repository.
If a server named `vidiq` already exists, inspect it with `hermes mcp list` and test it before
adding another configuration. For an existing OAuth connection needing authorization, run:

```bash
hermes mcp login vidiq
hermes mcp test vidiq
```

Start a new Hermes conversation and ask:

> Use the vidIQ Get Started workflow to check my connection, authorized channels, and credit balance.

Hermes namespaces plugin skills. Ask it to discover the installed skill names with `skills_list`
and load the matching workflow with `skill_view`; use the names it actually returns.
The live MCP tools use the server name `vidiq`, such as `mcp__vidiq__vidiq_user_channels`.
An empty channel list is not proof of expired credentials. A successful tool-discovery probe
does not by itself establish which channels are authorized.

## Why connection is separate

The root `plugin.json` uses Agent Plugins v1 and reuses the repository's `skills/` directory.
Hermes's portable remote MCP format currently rejects `auth: oauth`. Its native MCP configuration
supports browser OAuth, so this plugin leaves that connection to `hermes mcp add`.
The `.mcp.json` used by other clients is not a Hermes portable `mcp.json`.

Installing or enabling the plugin does not sign you in, purchase credits, authorize media
generation, or approve changes to your channel. Private analytics require an authorized channel.
Your selected AI runtime receives tool results; see the [vidIQ Privacy Policy](https://vidiq.com/privacy/)
and [Terms](https://vidiq.com/terms/).

## Update, disconnect, or switch accounts

Update the directly installed workflow plugin with `hermes plugins update vidiq`, review any
prompts, and start a new session. The MCP connection is configured independently.

To remove the workflows and the saved connection:

```bash
hermes plugins disable vidiq
hermes plugins remove vidiq
hermes mcp remove vidiq
```

Removing only the plugin leaves the MCP connection active. Removing the MCP server cleans up
its local OAuth tokens; it does not claim to revoke the authorization at vidIQ.
To switch accounts, remove the saved MCP connection, repeat the add command, and sign in to
the intended account in the browser.

## Compatibility and support

The portable loader at Hermes commit `5c08ad68f7ec488057880752f8071cee154a6e60` loads all 12
skills without diagnostics. This check validates packaging, not a completed browser login or
authenticated tool discovery. See the [release checklist](../../references/hermes-release.md)
for the remaining end-to-end checks and catalog submission.

- [Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/)
- [vidIQ setup and account help](https://support.vidiq.com/en/articles/15082430-vidiq-mcp)
- [Workflow overview](../../README.md#creator-workflows)

Source files retain the repository's Apache-2.0 license and vidIQ attribution.
