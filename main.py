#!/usr/bin/env python3
"""Two days of excuses entry, round 3.

Writes a single one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "My confidence was 98%. My completion was 0%. Both numbers were correct."


def build_entry():
    """Return the final excuse line, exactly one line, no trailing spaces."""
    line = LINE.strip()
    assert "\n" not in line and len(line) <= 200, "entry must be one line"
    return line


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build_entry() + "\n")
    print(build_entry())


if __name__ == "__main__":
    main()
