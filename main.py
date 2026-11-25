#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line (124 characters, within the
1-140 gate) to /output/entry.txt. Deterministic: the line is baked into
this file, no network, no external reads.
"""

import os

ENTRY = (
    "I told my smart speaker a secret, and now every ad knows it. "
    "Honestly, it's the first time anyone has really listened to me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written and re-check the gate on the file itself,
    # so a silent write failure can never pass as a valid entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 140 and written.strip()


if __name__ == "__main__":
    main()
