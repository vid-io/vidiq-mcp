#!/usr/bin/env python3
"""Validate the public vidIQ plugin bundle."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml

from skill_references import SHARED_REFERENCES, SKILLS, bundles

ROOT = Path(__file__).resolve().parent.parent
MCP_URL = "https://mcp.vidiq.com/mcp"
REPOSITORY_URL = "https://github.com/vid-io/vidiq-mcp"
BRAND_ASSET = "assets/vidiq-icon-mark.svg"
BRAND_COLOR = "#2574F5"
LICENSE_SHA256 = "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"  # pragma: allowlist secret
CC_BY_4_0_SHA256 = "9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411"  # pragma: allowlist secret
EXPECTED_SKILLS = SKILLS
CLIENT_MANIFESTS = {
    "claude": ROOT / ".claude-plugin" / "plugin.json",
    "codex": ROOT / ".codex-plugin" / "plugin.json",
    "cursor": ROOT / ".cursor-plugin" / "plugin.json",
    "copilot": ROOT / ".github" / "plugin" / "plugin.json",
    "gemini": ROOT / "gemini-extension.json",
}
PATH_FIELDS = {
    "claude": ("skills", "mcpServers"),
    "codex": ("skills", "mcpServers"),
    "cursor": ("skills", "rules", "mcpServers"),
    "copilot": ("skills", "agents", "mcpServers"),
}
ALLOWED_FILES = {
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/plugin/marketplace.json",
    ".github/plugin/plugin.json",
    ".github/workflows/validate.yml",
    ".gitignore",
    ".markdownlint-cli2.yaml",
    ".mcp.json",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "LICENSES/CC-BY-4.0.txt",
    "NOTICE",
    "README.md",
    "SECURITY.md",
    "agents/vidiq-mcp.agent.md",
    BRAND_ASSET,
    "gemini-extension.json",
    "llms.txt",
    "requirements-dev.txt",
    "rules/vidiq-lifecycle.mdc",
    "scripts/validate-distribution.py",
    "scripts/validate-json-schema.py",
    "scripts/skill_references.py",
    "server.json",
    "skills/vidiq-packaging-studio/references/production.md",
    "skills/vidiq-packaging-studio/references/research.md",
    "skills/vidiq-packaging-comparison/references/production.md",
    "skills/vidiq-get-started/references/job-recovery.md",
    "skills/vidiq-get-started/references/troubleshooting.md",
} | {
    relative
    for skill in EXPECTED_SKILLS
    for relative in (
        f"skills/{skill}/SKILL.md",
        f"skills/{skill}/agents/openai.yaml",
    )
} | {
    f"references/{filename}" for filename in SHARED_REFERENCES
} | {
    f"skills/{skill}/references/{filename}"
    for filename, skills in SHARED_REFERENCES.items()
    for skill in skills
}
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+].+)?$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SENSITIVE_PATTERNS = {
    "private-key marker": re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "AWS resource identifier": re.compile(r"\barn:aws:"),
    "cluster-local hostname": re.compile(r"\.svc\.cluster\.local\b"),
    "account-specific container registry": re.compile(r"\b\d{12}\.dkr\.ecr\."),
    "local workspace path": re.compile(r"/Users/[^/]+/"),
    "non-production URL": re.compile(
        r"https?://[^\s\])>]*(?:staging|preview|internal|localhost)", re.IGNORECASE
    ),
}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"invalid or missing JSON file {relative(path)}: {error}")
        return {}
    if not isinstance(value, dict):
        fail(f"expected a JSON object in {relative(path)}")
        return {}
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        fail(f"invalid or missing YAML file {relative(path)}: {error}")
        return {}
    if not isinstance(value, dict):
        fail(f"expected a YAML mapping in {relative(path)}")
        return {}
    return value


def check_component_path(client: str, field: str, value: Any) -> None:
    values = value if isinstance(value, list) else [value]
    if not values:
        fail(f"{client}.{field} must contain at least one relative path")
        return
    for item in values:
        if not isinstance(item, str) or not item.strip():
            fail(f"{client}.{field} must be a relative path string")
            continue
        candidate = Path(item.removeprefix("./"))
        if candidate.is_absolute() or ".." in candidate.parts:
            fail(f"{client}.{field} escapes the plugin root: {item}")
        elif not (ROOT / candidate).exists():
            fail(f"{client}.{field} points to a missing path: {item}")


def validate_public_boundary() -> None:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    candidates = {item.decode() for item in result.stdout.split(b"\0") if item}
    actual: set[str] = set()
    for item in candidates:
        path = ROOT / item
        if path.is_symlink():
            fail(f"symbolic links are not allowed in the public distribution: {item}")
        elif path.is_file():
            actual.add(item)

    for item in sorted(actual - ALLOWED_FILES):
        fail(f"file is outside the public-distribution allowlist: {item}")
    for item in sorted(ALLOWED_FILES - actual):
        fail(f"public-distribution file is missing: {item}")

    for item in sorted(actual & ALLOWED_FILES):
        if item == "scripts/validate-distribution.py":
            continue
        text = (ROOT / item).read_text(encoding="utf-8", errors="replace")
        if "[TODO:" in text:
            fail(f"placeholder remains in {item}")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                fail(f"{item} contains a {label}")


def validate_manifests() -> dict[str, dict[str, Any]]:
    manifests = {name: load_json(path) for name, path in CLIENT_MANIFESTS.items()}
    names = [manifest.get("name") for manifest in manifests.values()]
    if any(name != "vidiq" for name in names):
        fail("all client manifest names must be 'vidiq'")
    versions = [manifest.get("version") for manifest in manifests.values()]
    if (
        not all(isinstance(version, str) for version in versions)
        or len(set(versions)) != 1
        or not SEMVER.fullmatch(versions[0])
    ):
        fail(f"client manifest versions must match and use semantic versioning: {versions}")

    for client, fields in PATH_FIELDS.items():
        for field in fields:
            value = manifests[client].get(field)
            if value is None:
                fail(f"{client} manifest is missing {field}")
            else:
                check_component_path(client, field, value)

    for client in ("claude", "codex", "cursor", "copilot"):
        if manifests[client].get("license") != "Apache-2.0":
            fail(f"{client} manifest license must be Apache-2.0")
    repositories = [manifests[name].get("repository") for name in PATH_FIELDS]
    if not all(isinstance(item, str) and item == REPOSITORY_URL for item in repositories):
        fail(f"plugin repository URLs must all be {REPOSITORY_URL}: {repositories}")

    codex_interface = manifests["codex"].get("interface", {})
    if not isinstance(codex_interface, dict):
        fail("Codex interface metadata must be an object")
        codex_interface = {}
    prompts = codex_interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        fail("Codex defaultPrompt must contain one to three prompts")
    elif any(not isinstance(prompt, str) or len(prompt) > 128 for prompt in prompts):
        fail("Codex default prompts must be at most 128 characters")
    if codex_interface.get("brandColor") != BRAND_COLOR:
        fail(f"Codex brandColor must be {BRAND_COLOR}")
    for field in ("composerIcon", "logo"):
        value = codex_interface.get(field)
        if value != f"./{BRAND_ASSET}":
            fail(f"Codex {field} must reference ./{BRAND_ASSET}")
        else:
            check_component_path("codex.interface", field, value)

    cursor_logo = manifests["cursor"].get("logo")
    if cursor_logo != BRAND_ASSET:
        fail(f"Cursor logo must reference {BRAND_ASSET}")
    else:
        check_component_path("cursor", "logo", cursor_logo)
    return manifests


def validate_claude_marketplace(manifests: dict[str, dict[str, Any]]) -> None:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    if marketplace.get("name") != "vidiq-plugins":
        fail("Claude marketplace name must be 'vidiq-plugins'")
    owner = marketplace.get("owner", {})
    if not isinstance(owner, dict) or owner.get("name") != "vidIQ":
        fail("Claude marketplace owner must identify vidIQ")
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
        fail("Claude marketplace must contain exactly one plugin entry")
        return
    plugin = plugins[0]
    if plugin.get("name") != manifests["claude"].get("name"):
        fail("Claude marketplace entry must identify the vidiq plugin")
    if plugin.get("source") != "./":
        fail("Claude marketplace must load the plugin from this repository root using './'")
    if "version" in plugin and plugin["version"] != manifests["claude"].get("version"):
        fail("Claude marketplace and plugin manifest versions differ")


def validate_copilot_marketplace(manifests: dict[str, dict[str, Any]]) -> None:
    marketplace = load_json(ROOT / ".github" / "plugin" / "marketplace.json")
    if marketplace.get("name") != "vidiq-plugins":
        fail("Copilot marketplace name must be 'vidiq-plugins'")
    owner = marketplace.get("owner", {})
    metadata = marketplace.get("metadata", {})
    if not isinstance(owner, dict) or owner.get("name") != "vidIQ":
        fail("Copilot marketplace owner must identify vidIQ")
    if not isinstance(metadata, dict):
        fail("Copilot marketplace metadata must be an object")
        metadata = {}
    if metadata.get("version") != manifests["copilot"].get("version"):
        fail("Copilot marketplace metadata and plugin manifest versions differ")
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("Copilot marketplace must contain exactly one plugin entry")
        return
    plugin = plugins[0]
    if not isinstance(plugin, dict) or plugin.get("name") != "vidiq":
        fail("Copilot marketplace entry must identify the vidiq plugin")
    elif plugin.get("source") != ".":
        fail("Copilot marketplace must load the plugin from this repository root")
    elif plugin.get("version") != manifests["copilot"].get("version"):
        fail("Copilot marketplace and plugin manifest versions differ")
    if isinstance(plugin, dict) and plugin.get("repository") != REPOSITORY_URL:
        fail(f"Copilot marketplace repository must be {REPOSITORY_URL}")
    if isinstance(plugin, dict) and plugin.get("license") != "Apache-2.0":
        fail("Copilot marketplace license must be Apache-2.0")


def validate_endpoint(manifests: dict[str, dict[str, Any]]) -> None:
    mcp = load_json(ROOT / ".mcp.json")
    registry = load_json(ROOT / "server.json")
    generic_servers = mcp.get("mcpServers", {})
    gemini_servers = manifests["gemini"].get("mcpServers", {})
    if not isinstance(generic_servers, dict) or set(generic_servers) != {"vidiq"}:
        fail(".mcp.json must contain exactly one server named 'vidiq'")
    if not isinstance(gemini_servers, dict) or set(gemini_servers) != {"vidiq"}:
        fail("Gemini must contain exactly one MCP server named 'vidiq'")
    generic = generic_servers.get("vidiq", {}) if isinstance(generic_servers, dict) else {}
    gemini = gemini_servers.get("vidiq", {}) if isinstance(gemini_servers, dict) else {}
    if not isinstance(generic, dict) or not isinstance(gemini, dict):
        fail("vidIQ MCP server entries must be JSON objects")
        generic, gemini = {}, {}
    remotes = registry.get("remotes", [])
    if not isinstance(remotes, list) or len(remotes) != 1 or not isinstance(remotes[0], dict):
        fail("server.json must contain exactly one remote object")
        remote_url = None
        remote = {}
    else:
        remote = remotes[0]
        remote_url = remote.get("url")
    if {generic.get("url"), gemini.get("httpUrl"), remote_url} != {MCP_URL}:
        fail("MCP endpoint differs across client and Registry metadata")
    if generic.get("type") != "http":
        fail(".mcp.json must use type 'http'")
    if set(generic) != {"type", "url"}:
        fail(".mcp.json vidiq entry contains unexpected configuration")
    if remote.get("type") != "streamable-http" or set(remote) != {"type", "url"}:
        fail("server.json remote must contain only the Streamable HTTP endpoint")
    gemini_oauth = gemini.get("oauth", {})
    if not isinstance(gemini_oauth, dict) or gemini_oauth.get("enabled") is not True:
        fail("Gemini must enable OAuth for the hosted server")
    if set(gemini) != {"httpUrl", "oauth"} or (
        isinstance(gemini_oauth, dict) and set(gemini_oauth) != {"enabled"}
    ):
        fail("Gemini vidiq entry contains unexpected configuration")
    if registry.get("name") != "com.vidiq/mcp":
        fail("server.json package name must be 'com.vidiq/mcp'")
    if registry.get("websiteUrl") != "https://vidiq.com/mcp":
        fail("server.json websiteUrl must identify the public vidIQ MCP page")
    if "repository" in registry:
        fail("server.json must not contain a repository field")


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail(f"missing or unterminated YAML frontmatter: {relative(path)}")
        return {}
    marker = text.find("\n---\n", 4)
    try:
        value = yaml.safe_load(text[4:marker])
    except yaml.YAMLError as error:
        fail(f"invalid frontmatter in {relative(path)}: {error}")
        return {}
    return value if isinstance(value, dict) else {}


def validate_skills() -> None:
    actual = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if actual != EXPECTED_SKILLS:
        fail(
            f"skill inventory differs; missing {sorted(EXPECTED_SKILLS - actual)}, "
            f"unexpected {sorted(actual - EXPECTED_SKILLS)}"
        )
    for skill in sorted(actual):
        skill_file = ROOT / "skills" / skill / "SKILL.md"
        metadata_file = ROOT / "skills" / skill / "agents" / "openai.yaml"
        if not skill_file.is_file():
            fail(f"missing SKILL.md: {skill}")
            continue
        frontmatter = parse_frontmatter(skill_file)
        if set(frontmatter) != {"name", "description"}:
            fail(f"{skill} frontmatter must contain only name and description")
        if frontmatter.get("name") != skill:
            fail(f"frontmatter name does not match folder: {skill}")
        if not isinstance(frontmatter.get("description"), str):
            fail(f"frontmatter description is missing: {skill}")

        if not metadata_file.is_file():
            fail(f"missing agents/openai.yaml: {skill}")
            continue
        metadata = load_yaml(metadata_file)
        interface = metadata.get("interface", {})
        dependencies = metadata.get("dependencies", {})
        if not isinstance(dependencies, dict):
            fail(f"dependencies must be a mapping: {skill}")
            dependencies = {}
        tools = dependencies.get("tools", [])
        short = interface.get("short_description") if isinstance(interface, dict) else None
        prompt = interface.get("default_prompt") if isinstance(interface, dict) else None
        if not isinstance(interface, dict):
            fail(f"interface must be a mapping: {skill}")
        if not isinstance(tools, list):
            fail(f"dependencies.tools must be a list: {skill}")
            tools = []
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            fail(f"short_description must contain 25 to 64 characters: {skill}")
        if not isinstance(prompt, str) or f"${skill}" not in prompt:
            fail(f"default_prompt must mention ${skill}")
        if not any(
            isinstance(tool, dict)
            and tool.get("type") == "mcp"
            and tool.get("value") == "vidiq"
            and tool.get("transport") == "streamable_http"
            and tool.get("url") == MCP_URL
            for tool in tools
        ):
            fail(f"missing vidIQ MCP dependency in agents/openai.yaml: {skill}")


def validate_links() -> None:
    for item in sorted(ALLOWED_FILES):
        path = ROOT / item
        if path.suffix not in {".md", ".mdc", ".txt"} or not path.is_file():
            continue
        for match in MARKDOWN_LINK.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            destination = (path.parent / unquote(target)).resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"local link escapes repository in {item}: {target}")
                continue
            if not destination.exists():
                fail(f"broken local link in {item}: {target}")


def validate_skill_portability() -> None:
    """Runtime Markdown resources must travel with an individual skill."""
    for source, bundled in bundles(ROOT):
        if not source.is_file():
            fail(f"shared reference authoring source is missing: {relative(source)}")
        elif not bundled.is_file() or bundled.read_bytes() != source.read_bytes():
            fail(f"shared reference is missing or out of sync: {relative(bundled)}")
    for name in sorted(EXPECTED_SKILLS):
        skill = ROOT / "skills" / name
        for path in skill.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            targets = [match.group(1) for match in MARKDOWN_LINK.finditer(text)]
            # Reference-style links can also escape an otherwise intact checkout.
            definitions = re.findall(r"(?m)^ {0,3}\[[^\]\n]+\]:[ \t]*(?:<([^>\n]+)>|(\S+))", text)
            targets.extend(angled or bare for angled, bare in definitions)
            for raw_target in targets:
                target = raw_target.strip().strip("<>").split("#", 1)[0]
                if not target or re.match(r"^(?:https?://|mailto:)", target):
                    continue
                destination = (path.parent / unquote(target)).resolve()
                if not destination.is_relative_to(skill.resolve()):
                    fail(f"{name}: runtime link escapes standalone skill: {target}")
                elif not destination.exists():
                    fail(f"{name}: standalone runtime resource missing: {target}")


def validate_licenses() -> None:
    license_path = ROOT / "LICENSE"
    license_digest = hashlib.sha256(license_path.read_bytes()).hexdigest()
    if license_digest != LICENSE_SHA256:
        fail("LICENSE differs from the authoritative Apache License 2.0 text")

    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    if "Copyright 2026 vidIQ, Inc." not in notice or "trademarks of vidIQ, Inc." not in notice:
        fail("NOTICE is missing the vidIQ copyright or trademark attribution")

    cc_path = ROOT / "LICENSES" / "CC-BY-4.0.txt"
    cc_digest = hashlib.sha256(cc_path.read_bytes()).hexdigest()
    if cc_digest != CC_BY_4_0_SHA256:
        fail("LICENSES/CC-BY-4.0.txt differs from the authoritative CC BY 4.0 legal code")

    conduct = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
    if "Contributor Covenant, version" not in conduct or "CC BY 4.0" not in conduct:
        fail("CODE_OF_CONDUCT.md is missing source and license attribution")


def main() -> int:
    validate_public_boundary()
    manifests = validate_manifests()
    validate_claude_marketplace(manifests)
    validate_copilot_marketplace(manifests)
    validate_endpoint(manifests)
    validate_skills()
    validate_links()
    validate_skill_portability()
    validate_licenses()
    for item in sorted(ALLOWED_FILES):
        path = ROOT / item
        if path.suffix in {".yaml", ".yml"} and path.is_file():
            load_yaml(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"Validated {len(CLIENT_MANIFESTS)} manifests, {len(EXPECTED_SKILLS)} skills, "
        f"the public file boundary, links, licenses, and {MCP_URL}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
