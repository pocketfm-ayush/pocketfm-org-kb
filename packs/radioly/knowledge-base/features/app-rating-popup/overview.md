# App rating popup

Aliases: rate app, app rating, in-app review

Product context: `radioly/pfm-kb/modules/app-rating-popup.md`

## What it is

Server/client gate for when to prompt the store rating sheet.

## Graph anchors

CODE SEARCH `app_rating` / `rating_popup` under experience or miscellaneous modules.


## Key product notes

An in-app **rate Pocket FM** sheet (emoji / stars). High scores
can send them to the store. Not the player-minimise NPS survey
(user-survey). Not Support CSAT.

## Risks

- Inventing eligibility thresholds without packed evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "app rating popup" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

