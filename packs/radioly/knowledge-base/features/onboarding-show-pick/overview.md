# Onboarding show pick

Aliases: onboarding shows, first shows, pick shows

Product context: `radioly/pfm-kb/modules/onboarding-show-pick.md` · flow `radioly/pfm-kb/flows/first-run.md`

## What it is

First-run show selection after language / ATT. Distinct from ongoing Home personalization.

## Graph anchors

CODE SEARCH `onboarding` under `v2/` / `v3/experience/` — confirm handlers before naming.


## Key product notes

The first-run screens where a new listener picks starter titles (sometimes
as trailers). This is **not** AI/PGC pair routing.

## Risks

- Mixing first-run pick with Discover or Home genre chips.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "onboarding show pick" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

