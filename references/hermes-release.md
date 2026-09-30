# Hermes release checklist

The root `plugin.json` packages the existing 12 skills. OAuth uses Hermes's native MCP setup
because portable MCP entries cannot declare `auth: oauth`.

## Validate the release

- Keep all client versions aligned. CI checks the schema, public files, and all 12 skills using
  Hermes commit `5c08ad68f7ec488057880752f8071cee154a6e60`. Update this pin, the workflow, and
  `scripts/validate-hermes.py` together when upgrading.
- Run `hermes plugins validate /absolute/path/to/vidiq-mcp --json` on a clean checkout and review
  any scanner warnings.
- In a separate Hermes profile, install the published commit with
  `hermes plugins install vid-io/vidiq-mcp --ref <full-commit-sha> --no-enable`, then enable `vidiq`.
- Follow the [setup guide](../integrations/hermes/README.md). Confirm all 12 skills are discoverable,
  browser OAuth completes, and `hermes mcp test vidiq` discovers tools. Check authorized channels
  and balance after inspecting tool prices; do not generate media or change account state.
- Remove the MCP connection and check that authenticated tools are unavailable in a new session;
  reconnect and verify access returns. Removing only the plugin should leave MCP connected.

Packaging checks pass; live browser authorization and authenticated tool discovery remain untested.

## Submit the catalog entry

After publishing the package and completing the checks, an owner or major contributor submits
`plugin-catalog/vidiq.yaml` to `NousResearch/hermes-agent`, following the
[catalog rules and schema](https://github.com/NousResearch/hermes-agent/blob/main/plugin-catalog/README.md).
Use `name: vidiq`, `repo: https://github.com/vid-io/vidiq-mcp`, the exact 40-character release SHA,
and the version from `plugin.json`. Set `maintainer: vid-io`, `tier: community`, `category: tools`,
and link `docs_url` to the setup guide at that commit. Describe the 12 workflows, separate OAuth
setup, account requirement, and possible credit usage. Keep the tools, hooks, middleware, and
required-environment capability arrays empty: this package provides skills only.

Advertise `hermes plugins install vidiq` only after catalog acceptance. Each later catalog update
requires a reviewed PR with a new SHA and version.
