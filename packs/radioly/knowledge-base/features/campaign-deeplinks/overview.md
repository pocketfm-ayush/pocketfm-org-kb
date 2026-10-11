# Campaign deeplinks

Aliases: deeplink, deep link, campaign link

Product context: `radioly/pfm-kb/modules/campaign-deeplinks.md` · flow `radioly/pfm-kb/flows/open-from-campaign.md`

## What it is

Campaign URLs that land the listener on a show / offer / tab.

## Graph anchors

CODE SEARCH `deeplink` / campaign routing under campaigns / experience.


## Key product notes

A campaign / ad / install link that **resolves to a title or episode
and opens it playing**. This is not trailer-code, not a launch overlay
deeplink, and not a Discover share pin.

## Risks

- Inventing landing rules per campaign without config evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "campaign deeplinks" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

