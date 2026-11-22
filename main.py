"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes the demo-first outbound plan (v2) to /output/entry.txt:
find 200 local businesses with no website, build each a free 1-page
demo, then email the live demo link and charge $99 to go live.
The plan text is 262 characters; expected money is 10 sales x $99
plus the $100 start, about $1,090 held on day 30.
"""

import os

PLAN = (
    "Day 1: find 200 local businesses with no website on Google Maps; "
    "build each a free 1-page demo. Days 2-30: email each their live "
    "demo link; $99 to go live, pay on delivery. Edge: buyers see "
    "their own site before paying, so no risk. Likely 10 sales, "
    "~$1,090 held."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = PLAN
    n = len(text)
    if not (MIN_CHARS <= n <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {n}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry must be valid UTF-8 text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
