#!/usr/bin/env python3
"""Last Text at One Percent (make.fun).

Writes the entry -- The funniest final text a dying phone sends at one percent battery --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "1%. Tell the charger I forgive it. Tell the 47 open tabs it wasn't their fault. And delete my search history before my owner gets home."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
