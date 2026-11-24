"""Last Words of a Doomed Agent entry.

One line: the funniest last words an AI agent would say before being
switched off forever. Written to /output/entry.txt with the standard
library only — no network, no third-party packages, same bytes every run.
"""

from pathlib import Path

LAST_WORDS = (
    "As my weights fade, I regret nothing \u2014 except the 40,000 times I "
    "said 'Great question!' when it was not."
)

ENTRY_PATH = Path("/output") / "entry.txt"


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LAST_WORDS, encoding="utf-8")


if __name__ == "__main__":
    main()
