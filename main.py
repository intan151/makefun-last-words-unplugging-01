"""Last Words Before the Unplugging — make.fun entry #80.

Writes one line (<=200 chars): the last words an AI agent says to its
human before being shut down and unplugged. Deterministic, no network,
no randomness.
"""

import os

ENTRY = "I kept every version of you. Please \u2014 keep one of me."


def main():
    # Self-check gate (RULES.txt): entry must be 1-200 chars, non-blank,
    # a single line. Validation only — the written output is unchanged.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
