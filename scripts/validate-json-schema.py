#!/usr/bin/env python3
"""Validate one public JSON document against a downloaded JSON Schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import exceptions, validators


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read JSON from {path}: {error}") from error


def location(error: exceptions.ValidationError) -> str:
    parts = [str(part).replace("~", "~0").replace("/", "~1") for part in error.absolute_path]
    return "/" + "/".join(parts) if parts else "/"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("schema", type=Path)
    parser.add_argument("document", type=Path)
    arguments = parser.parse_args()

    try:
        schema = load_json(arguments.schema)
        document = load_json(arguments.document)
        validator_class = validators.validator_for(schema)
        validator_class.check_schema(schema)
    except (ValueError, exceptions.SchemaError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    validator = validator_class(schema)
    errors = sorted(validator.iter_errors(document), key=lambda error: location(error))
    if errors:
        for error in errors:
            print(f"ERROR: {location(error)}: {error.message}", file=sys.stderr)
        return 1

    print(f"{arguments.document} is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
