"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Holds one original one-line review of planet Earth, written as an alien
tourist, and writes it to /output/entry.txt when run with `python3 main.py`.

Gate (from the kit's RULES.txt): the output file must be UTF-8 text of
1 to 200 characters, not only white space.
"""

import os

ENTRY = (
    "Earth review: the locals pay rent to sleep indoors, drink bean juice "
    "to stay awake, and stare at glowing rectangles for fun. "
    "2/5 \u2014 but the sunsets nearly saved it."
)

MAX_CHARS = 200


def gate_check(text):
    """Enforce the entry gate exactly. Raises ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing padding")
    text.encode("utf-8")  # must be encodable UTF-8 text
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote /output/entry.txt (%d characters)" % len(ENTRY))


if __name__ == "__main__":
    main()
