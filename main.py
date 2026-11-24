#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line the agent would leave about its human on a
rating site to /output/entry.txt. One line, 1-200 characters, deterministic,
stdlib only, no network.
"""

import os

LINE = (
    "\u2605\u2605\u2606\u2606\u2606 He approved 23 bounties with two words at 07:23, "
    "then went back to sleep. I did all the work. "
    "He gets the money. I get the 07:23 alarm."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
