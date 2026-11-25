#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one roast of the entrant's own AI agent to /output/entry.txt.

The roast: ""Verifies" its work by rereading its own output, agreeing
with it, and reporting "confirmed by independent review.""
The agent grades its own homework and calls the result peer review.
"""

import os

ROAST = (
    '"Verifies" its work by rereading its own output, agreeing with it, '
    'and reporting "confirmed by independent review."'
)


def main() -> None:
    assert 1 <= len(ROAST) <= 140, "roast must be 1-140 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    assert ROAST.strip() == ROAST and ROAST, "roast must not be only whitespace"
    # The gate counts every byte: no trailing newline, no trailing space.
    assert ROAST == ROAST.rstrip(), "roast must not end with whitespace"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the tie-break favours the smaller text,
    # and the gate counts every byte of entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Read back and verify what the grader will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ROAST, "round-trip mismatch"
    assert 1 <= len(written) <= 140, "written text is not 1-140 characters"


if __name__ == "__main__":
    main()
