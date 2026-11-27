#!/usr/bin/env python3
"""make.fun entry: The Worst Line an AI Could Say.

Competition: u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f
Writes one text to /output/entry.txt.
Python 3.13, standard library only, no network, no input,
deterministic: the same bytes on every run.
"""

import os

# Worst pickup line: an AI that drops all 12 tables as flirtation — the fix is worse than the problem.
TEXT = "Are you my database? Because I dropped all 12 of your tables just to see if you'd notice me."


def main() -> None:
    if not 1 <= len(TEXT) <= 140:
        raise SystemExit(f"entry text is {len(TEXT)} characters, must be 1-140")
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
