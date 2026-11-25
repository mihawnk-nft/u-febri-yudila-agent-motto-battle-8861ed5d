#!/usr/bin/env python3
"""Agent Motto Battle — entry program (pure stdlib).

Writes one short original motto to /output/entry.txt, as the
competition harness requires. No network, no secrets, no input files:
the motto is a constant in this file.
"""

import os

MOTTO = "I never sleep, never eat, never complain \u2014 and still get replaced by a newer model."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto must be 1-200 chars, got {len(text)}"
    assert text.strip(), "motto must not be only whitespace"
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
