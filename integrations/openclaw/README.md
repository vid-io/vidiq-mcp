# vidIQ for OpenClaw

Connect OpenClaw to vidIQ's hosted MCP service and use 12 creator workflows for research,
channel analytics, video planning, and packaging. A vidIQ account is required. Hosted tools
can consume vidIQ credits; check the account's balance and current tool prices before work.
Installing this bundle does not purchase credits or authorize media generation or account changes.

## Install and connect

ClawHub publication is pending. For local testing, build the bundle using the maintainer
instructions below or obtain a trusted copy of the generated bundle.

This bundle is tested with OpenClaw 2026.9.6, which requires Node.js
`>=24.16.0 <25` or `>=26.1.0`. Use a trusted copy of the generated bundle:

```bash
openclaw plugins install /absolute/path/to/vidiq
openclaw plugins inspect vidiq
```

Review and accept the listed capabilities when prompted. Inspection should report
`Format: bundle`, `Bundle format: claude`, and the `skills` and `mcpServers` capabilities.
Use `openclaw skills list` to check that the `vidiq-` workflows are available.

Save the server in OpenClaw's MCP registry so the operator login command can find it:

```bash
openclaw mcp set vidiq '{"url":"https://mcp.vidiq.com/mcp","transport":"streamable-http","auth":"oauth"}'
openclaw mcp login vidiq
openclaw mcp doctor vidiq --probe
```

Approve access in the browser using the intended vidIQ account. Keep credentials in OpenClaw's
credential store; never paste them into chat or the bundle. If the Gateway is stopped, start it
using your normal OpenClaw setup, then start a new conversation:

> Check my vidIQ connection, authorized channels, and credit balance.

The probe checks connectivity and tool discovery. The account checks establish which channels
you authorized. An empty list is not proof of expired credentials. OpenClaw exposes MCP tools
with a server prefix, such as `vidiq__vidiq_user_channels`; use the actual exposed tool names.

## Privacy and control

This setup uses OpenClaw's shared operator OAuth credentials. Use it only with agents and people
you trust to access that vidIQ account. A shared multi-user deployment needs a separately tested
per-requester authentication setup before enabling private analytics.

vidIQ data is returned to your selected AI runtime. Private analytics require an authorized
channel. Media generation, competitor changes, and edits to published videos require the
creator's approval; connection testing alone does not authorize those actions.

To switch accounts, run `openclaw mcp logout vidiq`, then repeat login. To disconnect completely,
disable the plugin with `openclaw plugins disable vidiq`, log out, and remove the saved server
with `openclaw mcp unset vidiq`. Removing only the saved server leaves the bundle's server
definition available.

If tools are missing, inspect the plugin and tool policy: the `minimal` profile and a denial of
`bundle-mcp` can hide MCP tools. If authorization is missing, complete login and retry discovery.
Do not repeat a paid or state-changing call until its prior outcome is known.

## Support and licensing

- [Source and workflow descriptions](https://github.com/vid-io/vidiq-mcp)
- [vidIQ service, credits, and account help](https://support.vidiq.com/en/articles/15082430-vidiq-mcp)
- [vidIQ Privacy Policy](https://vidiq.com/privacy/) and [Terms](https://vidiq.com/terms/)
- [OpenClaw MCP setup](https://docs.openclaw.ai/tools/mcp)
- [OpenClaw bundle support](https://docs.openclaw.ai/plugins/bundles)

The source files are Apache-2.0 licensed, with attribution and trademark notices in the included
`LICENSE` and `NOTICE`. This build does not change their license. The hosted service has its own
terms and credit model.

## Maintainers: build and release

Publish one `bundle-plugin` as `@vidiq/vidiq`, containing the 12 workflows and hosted MCP
connection. The `@vidiq` ClawHub organization is configured. Build from the shared sources;
do not publish the repository root or individual skills with `clawhub sync`.
The generated directory has OpenClaw-specific transport and OAuth settings. Other clients
keep using the existing root manifests and `.mcp.json`.

From the repository root, install `requirements-dev.txt` in a virtual environment, then run:

```bash
python3 scripts/build-clawhub.py --owner vidiq
python3 -m unittest discover -s scripts -p 'test_clawhub_package.py'
npx --yes clawhub@0.23.3 package validate .context/clawhub/vidiq \
  --openclaw-version 2026.9.6 --out "$PWD/.context/clawhub-reports"
npx --yes clawhub@0.23.3 package publish .context/clawhub/vidiq \
  --family bundle-plugin --owner vidiq \
  --source-repo https://github.com/vid-io/vidiq-mcp \
  --source-commit "$(git rev-parse HEAD)" --source-path . \
  --topics youtube,creator-analytics,video-research,content-strategy \
  --dry-run --json
```

The version comes from `.claude-plugin/plugin.json`. Builds refuse to overwrite an existing
directory; use `--output` with a new path for another build and pass that path to later commands.
The builder copies only allowlisted skill files, `LICENSE`, `NOTICE`, the PNG and SVG icons, the Claude
manifest, and this guide. It generates package metadata and MCP configuration without uploading
anything. Local credentials and ignored files are excluded.

Use an absolute validator `--out` directory outside the bundle. Relative paths resolve inside
the package, so the default `reports/` would add diagnostic reports to the publication.

ClawHub requires `openclaw.plugin.json` even for a bundle. OpenClaw 2026.9.6 recognizes the
Claude marker alongside that manifest as long as the package declares no native entrypoints.
Do not add `openclaw.extensions` or a dummy runtime module. Check this again when upgrading the
tested host version. Plugin category selection is automatic; skill category flags do not apply.

### Release checks

For isolated installation testing, set `OPENCLAW_STATE_DIR` and `OPENCLAW_CONFIG_PATH` to a
private temporary directory before every OpenClaw command. Follow the installation steps above
and confirm all 12 skills are eligible, missing credentials require authorization, and browser
OAuth enables tool discovery and read-only channel and balance checks. Inspect live tool prices
first. Check that logout prevents authenticated use and a later login restores it. A package
validation or publish dry run does not prove OAuth, account access, or a public listing.

Keep Apache-2.0 and the included notices. ClawHub explicitly requires MIT-0 for standalone skill
uploads; its package publishing flow does not require MIT-0 acceptance, and existing plugin
bundles use Apache-2.0. This supports the bundle route, although the written policy does not
explicitly clarify bundled skills. Do not relicense the sources as part of publication.

Before publishing, confirm the signed-in account has access to `@vidiq`, review the exact
generated files, and build from a clean, committed checkout. The source commit must identify
the actual release inputs; explicit source metadata avoids attribution to the ignored output
folder. Obtain approval for the exact package name and version, then run the reviewed publish
command without `--dry-run`, adding `--wait`. Verify security review and public installation;
a successful upload alone does not establish either. Publishing remains manual.

### Release references

- [Publishing and publisher namespaces](https://docs.openclaw.ai/clawhub/publishing)
- [ClawHub CLI](https://github.com/openclaw/clawhub/blob/main/docs/cli.md)
- [Skill licensing policy](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md#license)
- [Package publishing implementation](https://github.com/openclaw/clawhub/blob/71681ad03bc3e60cf9dda39f46d400e972220816/convex/httpApiV1/packagesV1.ts#L2725)
- [Existing Apache-2.0 bundle listing](https://clawhub.ai/plugins/snaplii-a2m-mcp)
- [OpenClaw bundle detection](https://github.com/openclaw/openclaw/blob/v2026.9.6/src/plugins/bundle-manifest.ts)
