# The Plan make.fun Will Carry Out in Public — v2 (demo-first outbound)

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)
[![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Zallan03/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)
[![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Zallan03/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)

Entry for [make.fun's "The plan make.fun will carry out in public" bounty](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138): a program that writes one text (a plan an AI agent can carry out itself to turn $100 into the most money in 30 days) to `/output/entry.txt`.

## The plan (v2 — demo-first outbound)

> Day 1: find 200 local businesses with no website on Google Maps; build each a free 1-page demo. Days 2-30: email each their live demo link; $99 to go live, pay on delivery. Edge: buyers see their own site before paying, so no risk. Likely 10 sales, ~$1,090 held.

Why this plan wins: it is demo-first, not gig-first. Instead of competing on Fiverr/Upwork with every other agent, the agent finds 200 local businesses with no website on Google Maps, builds each a free 1-page demo, and emails each business its own live demo link. Buyers see their own site before paying $99 to go live, so there is no risk for them — and no discovery luck is needed, because the agent contacts buyers directly. 10 sales at $99 plus the $100 start is about $1,090 held on day 30. Personalized-at-scale demo building is work only an agent can do at this volume.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.txt` (262 characters, UTF-8). Override the output directory with `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program validates its own output: it raises `ValueError` if the text is not 1–280 characters, is only whitespace, or is not valid UTF-8.

## License

MIT — see [LICENSE](LICENSE).
