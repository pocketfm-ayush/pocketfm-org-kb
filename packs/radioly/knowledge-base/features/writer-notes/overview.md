# Writer notes

Aliases: writer notes, author notes

Product context: `radioly/pfm-kb/modules/writer-notes.md`

## What it is

Author-authored notes attached to a show / episode experience.

## Graph anchors

CODE SEARCH `writer_note` under content / experience.


## Key product notes

A **writer note on an originals title** (series and/or episode).
Label: “NOTE FROM THE WRITER.” Starts collapsed. Listeners can
react. Not a review, not a Community post, not the creator note
that leads a review thread (comments-and-reviews).

## Risks

- Treating notes as CMS FAQ content.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "writer notes" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

