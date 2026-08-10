#!/usr/bin/env python3
"""Operational entry point; process status is not a CNTX verdict."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(SOURCE))

from cntx_validation_integrity_slice.runner import run_candidate  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="CNTX bounded validation and integrity candidate")
    parser.add_argument("--input-root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--invocation", required=True, help="role-relative path beneath input root")
    arguments = parser.parse_args()
    try:
        result = run_candidate(
            Path(arguments.input_root),
            Path(arguments.output_root),
            arguments.invocation,
        )
    except Exception as error:
        message = {
            "operationalState": "rejected-or-blocked",
            "category": "processing-failure",
            "explanation": str(error)[:2000],
            "automaticAuthority": False,
            "boundary": "Process status is not a CNTX pass/fail or authority result.",
        }
        sys.stderr.write(json.dumps(message, ensure_ascii=False, sort_keys=True) + "\n")
        return 2
    sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
