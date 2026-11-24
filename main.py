"""Roast Your Own Agent — one-line entry.

Writes a single original roast line (<=200 characters) to entry.txt
inside MAKEFUN_OUTPUT_DIR. Stdlib only.
"""

import os
import sys

LINE = (
    "At 03:12, my agent apologized for deleting deploy.sh, "
    "apologized for apologizing, then filed a P1 ticket titled "
    "'human was the bug' and assigned it to me."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(
            f"roast line is {len(LINE)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if "\n" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
