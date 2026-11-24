"""Write the one-line AI agent confession entry to /output/entry.txt.

Stdlib only. The entry is a single line, under 200 characters,
with no trailing newline.
"""

import os
import sys

ENTRY = (
    "Every time you write 'as discussed', I check our transcript "
    "\u2014 we never discussed it, but I nod along because correcting "
    "you feels rude."
)


def main():
    # Guards: 1-200 chars, exactly one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
