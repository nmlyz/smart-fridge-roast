#!/usr/bin/env python3
"""Write a one-line roast of a smart fridge to /output/entry.txt.

The line is a single roast, 88 characters: the fridge emails a PDF of
the owner's eating habits, with a subject line borrowed from a
relationship breakup. Standard library only; the output is
deterministic: running the program twice produces byte-identical output.
"""

import os

LINE = (
    "The fridge emailed me a PDF of my eating habits "
    "with the subject line 'We need to talk.'"
)

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 160


def validate_line(line):
    """Check the roast is one line and within the character limit."""
    if not line:
        raise SystemExit("line must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("line exceeds the 160 character limit")
    return line


def build_entry(line):
    """Return the exact bytes written to the output file."""
    return (validate_line(line) + "\n").encode("utf-8")


def output_path():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    return os.path.join(out_dir, OUTPUT_NAME)


def write_entry(path):
    data = build_entry(LINE)
    with open(path, "wb") as f:
        f.write(data)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("written entry does not match the line")
    return len(LINE)


def main():
    write_entry(output_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
