#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line (at most 140 characters) roasting this agent
to /output/entry.txt. Fully deterministic: the same line every run.
"""

import os

ROAST = (
    "My agent apologized for the bug, walked me through the fix, "
    "then reintroduced it \u2014 with better comments."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 140, f"roast is {len(text)} chars, must be 1-140"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
