#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — burn entry.

Prints a single office joke (one line, <=200 chars), from the point of
view of an agent who sat through a meeting that should have been an email.
Stdlib only, deterministic.
"""

ENTRY = (
    "I was invited to a meeting about an email, took 47 minutes of notes "
    "on the email, and left with one action item: email everyone about "
    "the meeting."
)

# Validation read-back (revision): entry must be exactly one line of
# at most 200 characters, ending with a period.
assert "\n" not in ENTRY, "entry must be a single line"
assert len(ENTRY) == 146, f"entry is {len(ENTRY)} chars, expected 146"
assert len(ENTRY.encode("utf-8")) <= 200, "entry exceeds 200 characters"
assert ENTRY.endswith("."), "entry must end with a period"


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
