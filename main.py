#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Pure standard library, deterministic,
no network, no randomness: the same input always produces the same
output bytes.
"""

import os
import sys
from pathlib import Path

# The line, in full: the vacuum mistakes the sock for a small, flat cat,
# which explains the eating while staying absurd, and the deadpan second
# beat ("We have since made peace") treats the sock as a negotiating
# party. Naming the sock keeps the line on the prompt instead of drifting
# into a generic robot joke, and the excuse avoids the first thoughts
# anyone would reach for, such as hunger or the sock looking tasty.
ENTRY = "I mistook the sock for a small, flat cat. We have since made peace."


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text.strip() != text or not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
