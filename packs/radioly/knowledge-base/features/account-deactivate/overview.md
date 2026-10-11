# Account deactivate

Aliases: deactivate account, deactivate

Product context: `radioly/pfm-kb/modules/account-deactivate.md`

## What it is

Temporary deactivation path. Distinct from permanent delete and from recovery.

## Graph anchors

Search CODE SEARCH for `deactivate` under user APIs. Confirm before naming handlers.


## Key product notes

The listener **pauses** this login for a while, or until they sign in
again. Not delete (30-day remove), not recovery, not transfer.

## Risks

- Treating deactivate as delete.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "account deactivate" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

