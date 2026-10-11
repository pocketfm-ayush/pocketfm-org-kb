# Interactive story

Aliases: choice story, tap to choose, branching story

Product context: `radioly/pfm-kb/modules/interactive-story.md`

## What it is

Choose-your-path story. Next beat is server-owned. Not the title picker
and not story-evolution cards.

## Graph anchors

| Symbol | Source |
|---|---|
| interactive | `v3/experience/interactive/` |


## Key product notes

A choose-your-path story, not a normal episode list. Home can show a
banner; tap starts or **resumes**. Ending is “to be continued,” with
Notify Me — not a finished catalog title.

## Risks

- Inventing a branch on the client.
- Folding this into onboarding show-pick.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "interactive story" --graph $GRAPH
```
