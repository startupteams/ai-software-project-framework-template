#!/usr/bin/env python3
"""Lightweight documentation checks (see docs/CI_VALIDATION_POLICY.md).

Checks every tracked Markdown file for:
- valid UTF-8 text;
- merge-conflict markers;
- obvious private-key material;
- relative links whose target file does not exist.

Standard library only. Exits non-zero on any failure.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFLICT = re.compile(r"^(<{7}|={7}|>{7})( |$)", re.MULTILINE)
PRIVATE_KEY = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def markdown_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "*.md", "*.mdx"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [ROOT / line for line in out.splitlines() if line]


def check(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"{rel}: not valid UTF-8 ({exc})"]
    errors = []
    if CONFLICT.search(text):
        errors.append(f"{rel}: merge-conflict marker")
    if PRIVATE_KEY.search(text):
        errors.append(f"{rel}: private-key material")
    prose = INLINE_CODE.sub("", FENCE.sub("", text))
    for target in LINK.findall(prose):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        file_part = target.split("#", 1)[0]
        if file_part and not (path.parent / file_part).exists():
            errors.append(f"{rel}: broken link -> {target}")
    return errors


def main() -> int:
    files = markdown_files()
    errors = [e for f in files for e in check(f)]
    for e in errors:
        print(f"FAIL {e}")
    print(f"Checked {len(files)} Markdown files: {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
