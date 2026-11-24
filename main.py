"""The Robot Vacuum's Best Excuse — make.fun entry (Python 3.13, stdlib only).

Writes one line to /output/entry.txt: the funniest excuse a robot vacuum
gives for missing a spot, 140 characters or fewer. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

ENTRY = (
    "My sensors flagged it as load-bearing dust. "
    "Removing it could collapse the whole room, and I am not insured."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry() -> None:
    """Fail loudly before writing if the entry breaks the gate.

    The gate refuses empty/whitespace-only text and anything over
    140 characters, so refuse to write such a text instead of
    submitting a dead entry.
    """
    if not ENTRY.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(ENTRY) > 140:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the 140 cap")


def write_entry() -> Path:
    """Write the entry text, then read it back and verify it in full."""
    check_entry()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != ENTRY:
        raise IOError("read-back text does not match the entry")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
