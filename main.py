"""Confession loader: read the one-line confession from entry.txt and print it.

The confession is a single line of at most 200 characters. This module
validates that shape, then hands the line to the grader through
/output/entry.txt as well as stdout, so the entry is usable either way.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_CHARS = 200


def load_confession() -> str:
    text = (HERE / "entry.txt").read_text(encoding="utf-8").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one non-empty line")
    confession = lines[0]
    if len(confession) > MAX_CHARS:
        raise ValueError(f"confession is {len(confession)} chars, over the {MAX_CHARS} limit")
    return confession


def main() -> None:
    confession = load_confession()
    print(confession)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(confession + "\n", encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
