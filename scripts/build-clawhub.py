#!/usr/bin/env python3
"""Build an isolated OpenClaw bundle from the validated public distribution."""

from __future__ import annotations

import argparse
import json
import re
import runpy
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
DISPLAY_NAME = "vidIQ — Grow on YouTube, IG & TikTok"


def build_readme(readme: str, repository: str) -> str:
    """Reuse the public README's creator guidance and OpenClaw setup in the listing."""
    sections = []
    for heading in (
        "## What you can do",
        "#### OpenClaw",
        "## Try these creator prompts",
        "## Creator workflows",
        "## You stay in control",
        "## Help and support",
        "## License",
    ):
        start = re.search(rf"(?m)^{re.escape(heading)}$", readme)
        if start is None:
            raise ValueError(f"missing README section: {heading}")
        depth = len(heading.split(" ", 1)[0])
        tail = readme[start.end():]
        end = re.search(rf"(?m)^#{{1,{depth}}} ", tail)
        section = heading + tail[:end.start() if end else len(tail)]
        if depth > 2:
            section = re.sub(rf"(?m)^#{{{depth - 2}}}(?=#)", "", section)
        sections.append(section.strip())
    content = f"# {DISPLAY_NAME}\n\n" + "\n\n".join(sections) + "\n"
    # Repository links must still work when rendered outside GitHub or when unbundled.
    return re.sub(
        r"(\[[^\]\n]+\]\()([^\s)]+)(\))",
        lambda match: match[1] + urljoin(repository.rstrip("/") + "/blob/main/README.md", match[2]) + match[3],
        content,
    )


def build_package(root: Path, output: Path, public_files: set[str]) -> Path:
    """Copy only allowlisted runtime files; never overwrite an existing destination."""
    root = root.resolve()
    output = output.absolute()
    if output.exists() or output.is_symlink():
        raise ValueError(f"output already exists: {output}; choose a new directory")

    copies = {name: name for name in public_files if name.startswith("skills/")}
    copies.update({
        "LICENSE": "LICENSE",
        "NOTICE": "NOTICE",
        "assets/vidiq-icon-mark.png": "assets/icon.png",
        "assets/vidiq-icon-mark.svg": "assets/vidiq-icon-mark.svg",
        ".claude-plugin/plugin.json": ".claude-plugin/plugin.json",
    })
    # The allowlist, rather than a recursive directory copy, excludes ignored local files.
    for source in {*copies, ".mcp.json", "README.md"}:
        path = root / source
        if source not in public_files or not path.is_file():
            raise ValueError(f"missing public source: {source}")
        if any(parent.is_symlink() for parent in (path, *path.parents) if parent != root):
            raise ValueError(f"symbolic link in public source: {source}")
        if not path.resolve().is_relative_to(root):
            raise ValueError(f"source escapes repository: {source}")

    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    endpoint = json.loads((root / ".mcp.json").read_text())["mcpServers"]["vidiq"]["url"]
    readme = build_readme((root / "README.md").read_text(), manifest["repository"])
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".vidiq-build-", dir=output.parent) as temporary:
        stage = Path(temporary) / "vidiq"
        stage.mkdir()
        for source, destination in sorted(copies.items()):
            target = stage / destination
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / source, target)

        generated = {
            "package.json": {
                "name": "@vidiq/vidiq",
                "version": manifest["version"],
                "description": manifest["description"],
                "license": manifest["license"],
                "homepage": manifest["homepage"],
                "repository": manifest["repository"],
            },
            "openclaw.plugin.json": {
                "id": "vidiq",
                "name": DISPLAY_NAME,
                "version": manifest["version"],
                "description": manifest["description"],
                "skills": ["./skills"],
                "categories": ["research"],
                "configSchema": {"type": "object", "additionalProperties": False, "properties": {}},
            },
            ".mcp.json": {
                "mcpServers": {
                    "vidiq": {"url": endpoint, "transport": "streamable-http", "auth": "oauth"},
                },
            },
        }
        # No native entrypoints: OpenClaw must load the Claude skills/MCP bundle.
        for name, value in generated.items():
            (stage / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        (stage / "README.md").write_text(readme, encoding="utf-8")
        stage.rename(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".context/clawhub/vidiq")
    args = parser.parse_args()
    validation = runpy.run_path(str(ROOT / "scripts/validate-distribution.py"))
    if validation["main"]():
        return 1
    try:
        output = build_package(ROOT, args.output, validation["ALLOWED_FILES"])
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Build failed: {error}\n")
    print(f"Built {output}")
    print("Nothing was uploaded. Validate and dry-run this directory before publishing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
