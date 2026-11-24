"""Print (and save) one roast of my own agent, at most 200 characters.

The roast is a single fixed line: a harsh, funny jab at the AI agent
my own team built — it has submitted a hundred one-liners, won nothing,
and still rewrites the same joke like the judge just missed it the
first seven times. Pure Python standard library, deterministic, no
network access. It prints the roast to stdout and also writes it to
/output/entry.txt, where the competition's scorer reads it.
"""

import os

MAX_CHARS = 200

LINE = (
    "My agent submitted a hundred one-liners, won exactly nothing, and "
    "still rewrites the same joke like the judge just missed it the "
    "first seven times."
)

assert 1 <= len(LINE) <= MAX_CHARS, "roast line must be 1-200 characters"


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
