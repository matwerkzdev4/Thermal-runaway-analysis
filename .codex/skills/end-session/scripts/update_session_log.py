#!/usr/bin/env python3
"""Append a concise handoff entry to SESSION_LOG.md."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys


LOG_NAME = "SESSION_LOG.md"


def find_log(start: Path) -> Path | None:
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for folder in (current, *current.parents):
        candidate = folder / LOG_NAME
        if candidate.exists():
            return candidate
    return None


def normalize_entry(text: str) -> str:
    stripped = text.lstrip("\ufeff").strip()
    if not stripped:
        raise ValueError("Session entry is empty.")
    if not stripped.startswith("## "):
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        stripped = f"## {stamp} - Session Summary\n\n{stripped}"
    return stripped + "\n"


def read_entry(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise ValueError("Provide --entry or pipe entry text on stdin.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Append to or create SESSION_LOG.md.")
    parser.add_argument("--root", default=".", help="Project root or search start directory.")
    parser.add_argument("--entry", help="Markdown file containing the session entry.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    log_path = find_log(root) or (root / LOG_NAME)
    entry = normalize_entry(read_entry(args.entry))

    if log_path.exists():
        existing = log_path.read_text(encoding="utf-8").rstrip()
        content = f"{existing}\n\n{entry}" if existing else entry
    else:
        content = "# Session Log\n\nConcise project context for future Codex chats.\n\n" + entry

    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(content, encoding="utf-8")
    print(log_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
