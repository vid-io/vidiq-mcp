# vidIQ for Hermes Agent

Install 12 creator workflows for YouTube research, analytics, and packaging.
A vidIQ account is required; hosted tools may consume credits.

## Install

With an up-to-date Hermes installation supporting
[portable plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/#portable-agent-plugins-v1-packages), run:

```bash
hermes plugins install vid-io/vidiq-mcp --no-enable
hermes plugins enable vidiq
hermes mcp add vidiq --url https://mcp.vidiq.com/mcp --auth oauth
```

Complete vidIQ authorization in your browser, then start a new Hermes conversation:

> List the installed vidIQ skills, then use Get Started to check my connection, authorized channels, and credit balance.

The plugin provides the workflows; the separate MCP connection provides the live tools.
If `vidiq` is already configured, use the commands below instead of adding it again.

## Troubleshooting and management

| Task | What to do |
| --- | --- |
| Check the connection | Run `hermes mcp test vidiq`. |
| Sign in again or switch accounts | Run `hermes mcp login vidiq`, choose the intended account in the browser, then confirm the returned authorized channels. Re-running `add` does not force sign-in. |
| Find the workflows | Start a new session and ask Hermes to list its installed vidIQ skills. Plugin skills have namespaced names. |
| Update | Run `hermes plugins update vidiq`, then start a new session. |
| Remove | Run `hermes plugins disable vidiq`, `hermes plugins remove vidiq`, and `hermes mcp remove vidiq`. Removing only the plugin leaves the MCP connection active. |

[vidIQ help](https://support.vidiq.com/en/articles/15082430-vidiq-mcp) ·
[Hermes MCP docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/) ·
[Maintainer checklist](../../references/hermes-release.md)
