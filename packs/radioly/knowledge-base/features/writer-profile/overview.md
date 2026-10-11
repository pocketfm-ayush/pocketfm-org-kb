# Writer profile

Aliases: writer profile, author profile

Product context: `radioly/pfm-kb/modules/writer-profile.md`

## What it is

Author / writer page. Distinct from listener profile.

## Graph anchors

CODE SEARCH `writer` / `author` profile under content APIs.


## Key product notes

The **writer’s person page**: live titles, reviews those titles got,
and (when they are a writer) social links and a completion bar.

Not the listener person page (listener-profile). Not Stage. Not
“my reviews” (that is comments-and-reviews — reviews **this login**
wrote).

## Risks

- Mixing with listener profile or writer-notes.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "writer profile" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

## Related
- `stage`
- `ugc-backend-writer`
- `writer-notes`
