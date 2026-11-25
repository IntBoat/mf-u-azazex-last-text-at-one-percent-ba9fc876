#!/usr/bin/env python3
"""Last Text at One Percent — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "1%. Tell the charger I forgive it. Tell the 47 open tabs I never read them. Tell the group chat I died doing what I loved: ignoring it."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
