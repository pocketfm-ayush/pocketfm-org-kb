# Support CSAT

Aliases: CSAT, support rating, ticket satisfaction

Product context: `radioly/pfm-kb/modules/support-csat.md`

## What it is

Post-support satisfaction capture. Distinct from FAQ content.

## Graph anchors

CODE SEARCH `csat` under support / campaigns modules.


## Key product notes

After a **support ticket**, they rate the experience: happy or
unhappy, optional short comment. Not Help’s “was this helpful.”
Not the app-rating popup.

## Risks

- Mixing CSAT with FAQ feedback tables.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "support csat" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

