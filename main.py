"""
Write the winning 30-day plan to /output/entry.txt.

The plan: sell Amazon product infographics on Fiverr ($25/set) and upsell
buyers onto a $99/month 4-set plan, so one buyer pays repeatedly instead of
once. The $100 goes to promoting the gig ($30) and Canva Pro ($20), with
$50 held back for revisions, refunds and a second promotion push.

Scoring of the three candidates against the judge's five criteria
(most important first):
  A (this text, Fiverr Amazon infographics + monthly upsell) -- wins.
     Agent-executable end to end; realistic expected value (~$450 on day 30);
     Fiverr and Canva exist today and Amazon sellers already buy this;
     names the product, buyer, marketplace, price and day-one actions;
     edge is the monthly reorder, where one buyer pays 4x.
  B (Etsy SEO listings, $15 each) -- valid idea, but weaker edge: many
     agents already sell done-for-you Etsy listings, and $15 jobs need
     high volume from a brand-new gig to reach the same expected money.
  C (Google Business Profile retainers via Upwork) -- recurring revenue is
     attractive, but signing 5 local shops by cold email in 30 days leans
     on shop owners replying, negotiating and paying; more human friction
     than a Fiverr gig, so lower expected money.

Revision (pass 2): tightened the wording ("5 samples", "promoted gigs",
"upsell each buyer"), and made the expected money honest by stating it
net of fees ("$450 after fees"). Also added a 1-280 character guard in
main() so a bad edit fails loudly instead of shipping an invalid entry.
"""

import os

TEXT = (
    "Day 1: list on Fiverr 'Amazon infographics, $25/set, 24h delivery' "
    "with 5 samples; spend $30 on promoted gigs, $20 on Canva Pro. "
    "Days 2-30: deliver 2 sets/day, upsell each buyer a $99/mo plan. "
    "Edge: sellers reorder monthly, so one buyer pays 4x. "
    "Likely day-30: $450 after fees."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-blank characters")
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
