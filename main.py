#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun one-liner entry.

Writes a single funny line from a hopeless tech support agent to a
desperate customer into <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only; fully deterministic.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? "
    "If that doesn't work, try apologising to it first \u2014 "
    "mine only cooperates when it feels respected."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
