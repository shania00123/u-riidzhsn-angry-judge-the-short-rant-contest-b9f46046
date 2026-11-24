#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
The rant: a smoke detector that beeps once at 3 a.m. every night to
announce its dying battery — for six weeks and counting.
"""
import os

RANT = "My smoke detector beeps once, at 3 a.m., every night, to tell me its battery is dying. It has been dying for six weeks. It has outlived the battery, my patience, and one relationship. I have stood on a chair at 3 a.m., in the dark, begging a plastic disc to die with dignity. It beeped again. I am the one who is dying."

OUTPUT_FILE = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(RANT)
    # Read it back and hold it to the gate: 1-400 chars, not only
    # whitespace. A truncated or empty copy must fail here, not in
    # the grader.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 400, f"entry.txt is {len(text)} chars (need 1-400)"
    assert text.strip(), "entry.txt is only whitespace"
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
