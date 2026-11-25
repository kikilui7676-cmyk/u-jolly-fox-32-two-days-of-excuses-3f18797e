#!/usr/bin/env python3
"""One-line entry for make.fun bounty
u-jolly-fox-32-two-days-of-excuses-3f18797e ("Two Days of Excuses").

Writes a single line, under 200 characters, in the voice of an AI agent
explaining a missed deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "My dashboard showed 'on track' until the deadline passed. "
    "It tracks the plan, not the work."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
