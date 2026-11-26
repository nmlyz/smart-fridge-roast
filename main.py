#!/usr/bin/env python3
"""Write a one-line roast of a smart fridge to /output/entry.txt.

The line is a single roast, 88 characters: the fridge emails a PDF of the
owner's eating habits, with a subject line borrowed from a relationship
breakup. Standard library only; the output is deterministic.
"""

import os

LINE = (
    "The fridge emailed me a PDF of my eating habits "
    "with the subject line 'We need to talk.'"
)

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 160


def output_path():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    return os.path.join(out_dir, OUTPUT_NAME)


def write_entry(path):
    text = LINE + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written entry does not match the line")
    return len(LINE)


def main():
    if len(LINE) > MAX_CHARS:
        raise SystemExit("line exceeds the 160 character limit")
    write_entry(output_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
