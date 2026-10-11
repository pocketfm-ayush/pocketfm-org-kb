# Offerwall

Aliases: offerwall, offer wall, rewarded offers

Product context: `radioly/pfm-kb/modules/offerwall.md`

## What it is

Third-party offerwall entry for earning rewards. Distinct from in-player RV ads.

## Graph anchors

CODE SEARCH `offerwall` under ads / campaigns.


## Key product notes

A **task wall** for coins: install, survey, follow, purchase, and
similar offers. Opens as an offer-wall screen. Not watch-an-ad
(that is rewarded-ads).

## Risks

- Treating offerwall credit as spendable coins without wallet evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "offerwall" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

