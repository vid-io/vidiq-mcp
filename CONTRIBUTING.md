# Contributing to vidIQ MCP

Thanks for helping improve the public vidIQ MCP plugin repository.

This repository publishes an installable multi-client plugin, connection metadata, and Registry
metadata for the [hosted vidIQ MCP service](https://vidiq.com/mcp/).

**In scope:** corrections and improvements to the public README, client manifests, MCP and Registry
metadata, workflow skills, routing agent, lifecycle rule, issue forms, and related public-facing
material.

**Out of scope:** hosted-service behavior, authentication, accounts, plans, billing, and credits.
Report those through [vidIQ Support](https://support.vidiq.com/).
Report suspected vulnerabilities privately by following [SECURITY.md](SECURITY.md).

Before opening a pull request:

1. Use current production behavior and public or synthetic data.
2. Remove credentials, account identifiers, personal information, and private analytics.
3. Keep the machine identifier and installable version synchronized across all client manifests.
   The client-manifest version tracks this plugin bundle. `server.json.version` tracks the active
   MCP Registry descriptor and may differ from the client-manifest version.
4. Confirm that every added visual or third-party asset is licensed for redistribution.
5. Test the affected client installation or usage flow, or explain why that is not applicable, then
   describe the public user need in the pull request.

Run the repository release check before submitting:

```bash
python3 -m pip install --requirement requirements-dev.txt
python3 scripts/validate-distribution.py
```

The same invariant and client-schema checks run in GitHub Actions. If a new public artifact or
workflow is intentional, update the validator's file or skill inventory in the same pull
request.

CI also loads all skills with a pinned Hermes checkout. When upgrading it, update the workflow
checkout and `HERMES_COMMIT` in `scripts/validate-hermes.py` together; the loader check verifies
the actual revision. Hermes catalog submissions follow the upstream
[catalog rules](https://github.com/NousResearch/hermes-agent/blob/main/plugin-catalog/README.md)
and must reference a published, tested commit. Keep the GitHub installation command in the README
until the catalog entry is accepted.

The repository-root [live surface notes](references/live-surface-notes.md) contain the universal
operating rules. Keep discovery evidence and asynchronous procedures in their separate files in
`references/`; put tool-specific guidance in the skills that use it. Link optional references at
the relevant workflow stage so ordinary requests load only the guidance they need.

Each skill bundles the references it needs so it can be installed independently. Edit the
repository-root authoring source, then synchronize its copies:

```bash
python3 scripts/skill_references.py --write
```

The mapping in that script defines which skill receives each shared reference. Its default mode
checks without writing. CI rejects missing or divergent copies and runtime links outside the
skill directory. Keep the specialist and client rules focused on routing rather than repeating
the shared references or individual workflows.

## OpenClaw bundle

Build `@vidiq/vidiq` from the shared skills and manifests. The generated bundle includes the
skill references, icons, license, and notices, with OpenClaw's OAuth configuration.
Publish this bundle, not the repository root or individual skills.

After installing the development requirements above, run from the repository root:

```bash
python3 -m unittest discover -s scripts -p 'test_clawhub_package.py'
python3 scripts/build-clawhub.py
npx --yes clawhub@0.23.3 package validate .context/clawhub/vidiq \
  --openclaw-version 2026.9.6 --out "$PWD/.context/clawhub-reports"
npx --yes clawhub@0.23.3 package publish .context/clawhub/vidiq \
  --family bundle-plugin --owner vidiq \
  --source-repo https://github.com/vid-io/vidiq-mcp \
  --source-commit "$(git rev-parse HEAD)" --source-path . \
  --topics youtube,instagram,tiktok,video-research,creator-analytics --dry-run --json
```

The package name is `@vidiq/vidiq`; its version comes from `.claude-plugin/plugin.json`.
Builds refuse to overwrite an existing directory. For another build, use `--output` with a fresh
directory under `.context/` and pass that path to subsequent commands. To replace an installed
bundle, run `openclaw plugins install /absolute/path/to/new-bundle --force` after reviewing it.
Keep the validator's absolute `--out` directory outside the bundle so reports are not packaged.

ClawHub requires `openclaw.plugin.json`. Keep the Claude bundle marker and omit native
entrypoints so OpenClaw loads the bundled skills and MCP connection. When upgrading the
pinned host or CLI, recheck bundle loading and the [README setup flow](README.md#openclaw),
including authorization, channel access, logout, and login. For isolated tests, set
`OPENCLAW_STATE_DIR` and `OPENCLAW_CONFIG_PATH` to private temporary paths.

Release from a clean checkout of a commit merged and pushed to `main`, with access to `@vidiq`.
Review the generated files and retain Apache-2.0 and its notices. After approval of the exact
package and version, rerun the publish command without `--dry-run`, adding `--wait`.
Verify security review and public installation before announcing availability. See
[ClawHub publishing](https://docs.openclaw.ai/clawhub/publishing) for registry requirements.

## Contribution terms

By submitting a contribution, you represent that you have the right to submit it. Except for
contributions to `CODE_OF_CONDUCT.md`, which are licensed under CC BY 4.0, your contribution is
licensed under the [Apache License 2.0](LICENSE).

Files under `LICENSES/` contain authoritative license texts and must not be edited except by
replacing them byte-for-byte from the authoritative upstream source.

Participation in this project is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
