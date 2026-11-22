"""Write the chosen 30-day money plan to /output/entry.txt.

Deterministic: the same text is written on every run. Stdlib only,
no network. OUTPUT_PATH env var overrides the output path for local
testing only; the sandbox default is /output/entry.txt.
"""

import os
from pathlib import Path

TEXT = (
    "Day 1: list a $49 same-day landing-page gig on Fiverr, with 3 free "
    "demo pages as portfolio. Days 2-30: build one page a day in code; "
    "buyer pays on delivery. Spend $100 on promoted gigs. Edge: agencies "
    "charge $500 and take a week; I deliver today. Likely 20 sales, "
    "~$700 net."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
