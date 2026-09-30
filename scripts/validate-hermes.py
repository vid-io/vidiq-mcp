#!/usr/bin/env python3
"""Load the distribution with a pinned Hermes portable-plugin implementation."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

from skill_references import SKILLS

ROOT = Path(__file__).resolve().parent.parent
HERMES_COMMIT = "5c08ad68f7ec488057880752f8071cee154a6e60"  # pragma: allowlist secret


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hermes_source", type=Path, help="checkout of the tested Hermes revision")
    args = parser.parse_args()
    source = args.hermes_source.resolve(strict=True)
    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=source, text=True,
    ).strip()
    if revision != HERMES_COMMIT:
        parser.error(f"expected Hermes {HERMES_COMMIT}, got {revision}")

    sys.path.insert(0, str(source))
    from hermes_cli.agent_plugins import load_agent_plugin

    with tempfile.TemporaryDirectory(prefix="vidiq-hermes-") as data:
        package = load_agent_plugin(ROOT, Path(data))
    errors = [f"{item.scope}: {item.message}" for item in package.diagnostics]
    if package.name != "vidiq":
        errors.append("Hermes did not load the vidiq plugin")
    loaded = {skill.name for skill in package.skills}
    if loaded != SKILLS:
        errors.append(f"skill inventory differs: missing {SKILLS - loaded}, extra {loaded - SKILLS}")
    if package.mcp_servers:
        errors.append("Hermes must obtain OAuth tools from its separate native MCP connection")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Hermes {revision[:12]} loaded vidiq and all {len(loaded)} skills without diagnostics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
