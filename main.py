"""Print the one-line entry from entry.txt (resolved via __file__)."""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
