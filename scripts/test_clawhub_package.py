"""Check package boundaries and compatibility without network access or credentials."""

from __future__ import annotations

import json
import runpy
import tempfile
import unittest
from pathlib import Path

build_package = runpy.run_path(str(Path(__file__).with_name("build-clawhub.py")))["build_package"]


class ClawHubPackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.root = self.base / "source"
        self.output = self.base / "bundle"
        self.manifest = {
            "name": "vidiq", "version": "0.1.4", "description": "Creator workflows",
            "license": "Apache-2.0", "homepage": "https://vidiq.com/mcp/",
            "repository": "https://github.com/vid-io/vidiq-mcp",
            "icon": "./assets/vidiq-icon-mark.svg",
            "skills": "./skills/", "mcpServers": "./.mcp.json",
        }
        sources = {
            ".claude-plugin/plugin.json": json.dumps(self.manifest),
            ".mcp.json": json.dumps({"mcpServers": {"vidiq": {
                "type": "http", "url": "https://mcp.vidiq.com/mcp",
            }}}),
            "LICENSE": "Apache-2.0", "NOTICE": "vidIQ",
            "assets/vidiq-icon-mark.png": "test icon",
            "assets/vidiq-icon-mark.svg": "<svg></svg>",
            "integrations/openclaw/README.md": "# OpenClaw setup\n",
            "skills/vidiq-get-started/SKILL.md": "# Get started\n",
            "skills/vidiq-get-started/references/setup.md": "OAuth instructions\n",
        }
        self.public_files = set(sources)
        for name, content in sources.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

    def build(self) -> Path:
        return build_package(self.root, self.output, "vidiq", self.public_files)

    def test_copies_references_and_excludes_unlisted_files(self) -> None:
        for name in [".env", "skills/vidiq-get-started/.env", "skills/vidiq-get-started/private.md"]:
            (self.root / name).write_text("local-only sentinel")
        self.build()
        actual = {p.relative_to(self.output).as_posix() for p in self.output.rglob("*") if p.is_file()}
        self.assertEqual(actual, {
            "LICENSE", "NOTICE", "README.md", "assets/icon.png", ".claude-plugin/plugin.json",
            "package.json", "openclaw.plugin.json", ".mcp.json",
            "assets/vidiq-icon-mark.svg",
            "skills/vidiq-get-started/SKILL.md", "skills/vidiq-get-started/references/setup.md",
        })
        self.assertEqual((self.output / "skills/vidiq-get-started/references/setup.md").read_text(),
                         "OAuth instructions\n")

    def test_oauth_adapter_preserves_other_clients_and_license(self) -> None:
        before = (self.root / ".mcp.json").read_bytes()
        self.build()
        self.assertEqual((self.root / ".mcp.json").read_bytes(), before)
        self.assertEqual(json.loads((self.output / ".mcp.json").read_text()), {
            "mcpServers": {"vidiq": {
                "url": "https://mcp.vidiq.com/mcp", "transport": "streamable-http", "auth": "oauth",
            }},
        })
        package = json.loads((self.output / "package.json").read_text())
        self.assertEqual(package["name"], "@vidiq/vidiq")
        self.assertEqual(package["version"], self.manifest["version"])
        self.assertEqual(package["license"], "Apache-2.0")
        self.assertNotIn("openclaw", package)
        self.assertEqual(json.loads((self.output / ".claude-plugin/plugin.json").read_text()),
                         self.manifest)
        self.assertTrue((self.output / self.manifest["icon"]).is_file())

    def test_existing_output_is_untouched(self) -> None:
        self.output.mkdir()
        sentinel = self.output / "keep.txt"
        sentinel.write_text("keep")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.build()
        self.assertEqual(sentinel.read_text(), "keep")

    def test_rejects_source_symlinks(self) -> None:
        path = self.root / "LICENSE"
        path.unlink()
        secret = self.base / "private.txt"
        secret.write_text("private")
        path.symlink_to(secret)
        with self.assertRaisesRegex(ValueError, "symbolic link"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_rejects_symlinked_source_directories(self) -> None:
        path = self.root / "skills"
        path.rename(self.base / "outside-skills")
        path.symlink_to(self.base / "outside-skills", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symbolic link"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_rejects_missing_inputs_without_partial_output(self) -> None:
        (self.root / "NOTICE").unlink()
        with self.assertRaisesRegex(ValueError, "missing public source"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_rejects_invalid_publisher_handles(self) -> None:
        for owner in ["", "@vidiq", "VidIQ", "../vidiq", "vidiq/other", "vidiq;"]:
            with self.subTest(owner=owner), self.assertRaises(ValueError):
                build_package(self.root, self.output, owner, self.public_files)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
