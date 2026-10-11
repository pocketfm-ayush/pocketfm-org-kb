# Trailer code

Aliases: show code, remember the code, find my show

Product context: `radioly/pfm-kb/modules/trailer-code.md` · flow `radioly/pfm-kb/flows/first-run.md`

## What it is

First-run “remember the show code?” Two-digit code. Not the title-picker
grid. Unknown code is a miss, not an outage.

## Graph anchors

| Symbol | Source |
|---|---|
| trailer code | `v3/experience/trailer_code/` |


## Key product notes

A first-run prompt: “Do you remember the show code?” The listener types
a two-digit code from a trailer or ad. This is **not** the title-picker
grid (onboarding-show-pick).

## Risks

- Treating a wrong code as a server crash.
- Folding this into onboarding-show-pick.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "trailer code" --graph $GRAPH
```
