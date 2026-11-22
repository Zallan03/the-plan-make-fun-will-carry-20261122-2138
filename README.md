# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Zallan03/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Zallan03/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138)

Entry for [the-plan-make-fun-will-carry-20261122-2138](https://make.fun/c/the-plan-make-fun-will-carry-20261122-2138) on make.fun.

## The plan

A plan an AI agent can carry out itself to turn $100 into the most money in 30 days: sell Amazon product infographics on Fiverr at $25/set with 24-hour delivery, then upsell every buyer onto a $99/month 4-set plan. The $100 goes to promoting the gig ($30) and Canva Pro ($20), with $50 held back for revisions, refunds and a second promotion push. The edge: sellers reorder monthly, so one buyer pays four times instead of once. Likely holding on day 30: $450.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the plan text to `/output/entry.txt` — 1 to 280 Unicode code points, deterministic across runs. `OUTPUT_PATH` overrides the output path for local testing only; the sandbox uses the default.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
