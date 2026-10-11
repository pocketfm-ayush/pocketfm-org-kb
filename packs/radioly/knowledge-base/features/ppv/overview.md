# PPV testing (catalog)

Aliases: PPV test, pay-per-view test, LDAU cap, feed exclusion

Product context: `radioly/pfm-kb/modules/ppv.md`

## What it is

CMS test that can pull a title off Home after enough unique listeners.
Not listener checkout. Not a PPV pass.

## Graph anchors

| Symbol | Source |
|---|---|
| PPV | `v3/ppv/` |


## Key product notes

How CMS decides whether a title should become paid / PPV — **not** the
listener checkout. A title in test can disappear from Home after enough
unique listeners.

Do not confuse this with a PPV subscription pass (unproven here).

## Risks

- Treating this as “the listener bought PPV.”
- Stitching a cap-hit title back onto Home from a local catalog.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "ppv" --graph $GRAPH
```
