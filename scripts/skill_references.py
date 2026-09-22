#!/usr/bin/env python3
"""Synchronize the shared references required by each independently installable skill."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parent.parent
SKILLS = frozenset(
    (
        "channel-review", "comment-insights", "competitor-watchlist", "get-started",
        "new-upload-review", "next-video-planner", "packaging-comparison", "packaging-studio",
        "retention-analysis", "shorts-inspiration", "trend-radar", "video-ideas",
    )
)
SHARED_REFERENCES = {
    "live-surface-notes.md": SKILLS,
    "discovery-evidence.md": frozenset(
        (
            "comment-insights", "competitor-watchlist", "next-video-planner",
            "packaging-comparison", "packaging-studio", "shorts-inspiration",
            "trend-radar", "video-ideas",
        )
    ),
    "job-lifecycle.md": frozenset(
        (
            "packaging-comparison", "packaging-studio", "retention-analysis",
            "shorts-inspiration",
        )
    ),
}


def bundles(root: Path = ROOT) -> Iterator[tuple[Path, Path]]:
    for filename, skills in sorted(SHARED_REFERENCES.items()):
        for skill in sorted(skills):
            yield root / "references" / filename, root / "skills" / skill / "references" / filename


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check copies without writing (default).")
    mode.add_argument("--write", action="store_true", help="Update bundled copies from authoring sources.")
    args = parser.parse_args()
    changed = []
    for source, destination in bundles():
        expected = source.read_bytes()
        if not destination.is_file() or destination.read_bytes() != expected:
            changed.append(destination)
            if args.write:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(expected)
    for path in changed:
        print(f"{'Updated' if args.write else 'Out of sync:'} {path.relative_to(ROOT)}")
    if not changed:
        print("Shared skill references are synchronized.")
    return 1 if changed and not args.write else 0


if __name__ == "__main__":
    raise SystemExit(main())
