#!/usr/bin/env python3
"""Entry for "Two-Sentence Horror" (make.fun).

Writes a two-sentence horror story to entry.txt. The first sentence
sets a familiar scene -- a doorbell camera sending a photo of the
writer on their own porch -- and the second sentence turns it: they
have not left the house all day, and the photo was taken from inside.
The horror is implied, never explained.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os
from pathlib import Path

# Exactly two sentences, 400 characters at most, nothing else.
ENTRY = (
    "My doorbell camera sends me a photo every time someone rings, and "
    "tonight it sent one of me standing on my own porch. I haven't left "
    "the house all day, and the photo was taken from inside."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 2:
        raise SystemExit("entry must be exactly two sentences")
    sentences = [s for s in text.split(".") if s.strip()]
    if len(sentences) != 2 or any(len(s.strip()) < 10 for s in sentences):
        raise SystemExit("each of the two sentences must be substantive")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the story.
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
