"""Funniest lost sock status update.

Writes the entry sentence to /output/entry.txt, one line, no extra output.
The sentence itself is the entry and must not be changed.
"""

TEXT = "Left the dryer for a life behind the couch cushions. The remote and I are engaged. Tell my partner I'm not coming back."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write TEXT plus a trailing newline to path."""
    # Entry limit is 120 characters; the sentence must stay within it.
    assert len(TEXT) <= 120, "entry text exceeds 120 characters"
    with open(path, "w") as f:
        f.write(TEXT + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
