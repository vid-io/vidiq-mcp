# Hermes plugin release

The repository root is a skills-only Agent Plugins v1 package. Release the shared `skills/`
and root `plugin.json` together; no generated copy or custom runtime is needed. The native
Hermes MCP connection remains a separate browser OAuth setup step.

## Validate

Run distribution validation and the Agent Plugins v1 schema check from the repository CI.
CI also runs `scripts/validate-hermes.py` against the pinned Hermes revision, checking that
all 12 skills load without diagnostics and no portable MCP server is registered.
When upgrading the Hermes pin, update the workflow, validation script, and compatibility note
in the [user guide](../integrations/hermes/README.md) together.

Before catalog submission, use a clean committed checkout and run:

```bash
hermes plugins validate /absolute/path/to/vidiq-mcp --json
```

Review scanner warnings and complete these checks in a separate Hermes profile:

1. Install the exact published commit with
   `hermes plugins install vid-io/vidiq-mcp --ref <full-commit-sha> --no-enable`.
2. Enable `vidiq`, then confirm all 12 namespaced workflows are discoverable in a new session.
3. Follow the [connection guide](../integrations/hermes/README.md). Verify missing authorization
   is reported honestly, browser OAuth completes, and `hermes mcp test vidiq` discovers tools.
4. Use Get Started to verify authorized channels and balance after inspecting live tool prices.
   Do not generate media or change account state as part of the connection test.
5. Remove the MCP connection and confirm authenticated tools are unavailable in a new session.
   Reconnecting should restore access. Removing only the plugin should leave the separately
   configured MCP connection intact.

The local loader check and public OAuth discovery metadata do not prove authenticated access.

## Submit to the Plugin Catalog

After the package is published in `vid-io/vidiq-mcp` and the acceptance checks pass, a repository
owner or major contributor can submit a PR to `NousResearch/hermes-agent` adding
`plugin-catalog/vidiq.yaml`. Use the public release commit, not a local or placeholder SHA.
The catalog requires human review and an exact 40-character commit pin.

Use these entry values, filling in the actual release commit and matching plugin version:

```yaml
name: vidiq
repo: https://github.com/vid-io/vidiq-mcp
sha: <full-release-commit-sha>
version: "<plugin.json version>"
description: >-
  Twelve vidIQ creator workflows for YouTube research, channel analytics, video planning,
  and packaging. Skills-only plugin; connect the hosted vidIQ MCP service separately with
  hermes mcp add and browser OAuth. Requires a vidIQ account; hosted tools may consume credits.
maintainer: vid-io
tier: community
category: tools
docs_url: https://github.com/vid-io/vidiq-mcp/blob/<full-release-commit-sha>/integrations/hermes/README.md
readme: true
capabilities:
  provides_tools: []
  provides_hooks: []
  provides_middleware: []
  requires_env: []
```

The capability arrays are empty because this package provides workflow instructions; the
separately configured hosted server provides the live tools. `community` identifies the Hermes
catalog tier, even though vidIQ maintains the integration. Do not claim a catalog listing or
advertise `hermes plugins install vidiq` until the entry is accepted and discoverable.

Subsequent catalog updates require a new reviewed PR changing the pinned SHA and version.
Follow the current [catalog submission rules](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugin-catalog#submitting-a-plugin-to-the-catalog)
and [catalog README](https://github.com/NousResearch/hermes-agent/blob/main/plugin-catalog/README.md).
