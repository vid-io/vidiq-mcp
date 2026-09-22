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

By submitting a contribution, you represent that you have the right to submit it. Except for
contributions to `CODE_OF_CONDUCT.md`, which are licensed under CC BY 4.0, your contribution is
licensed under the [Apache License 2.0](LICENSE).

Files under `LICENSES/` contain authoritative license texts and must not be edited except by
replacing them byte-for-byte from the authoritative upstream source.

Participation in this project is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
