# Comments and reviews

Aliases: show reviews, episode comments, my reviews

Product context: `radioly/pfm-kb/modules/comments-and-reviews.md`

## What it is

Series review or episode comment. Not Community posts. Not Discover
shorts comments. A second series review updates the first.

## Graph anchors

| Symbol | Source |
|---|---|
| comments | `v2/social/` |


## Key product notes

Talk on a **series** (review + optional 1–5 stars) or an **episode**
(comment and replies). Not Community posts. Shorts comments are
Discover. The show-page “NOTE FROM THE WRITER” is writer-notes, not
a review. The creator note that can lead the review list is this
product.

## Risks

- Using this list for shorts.
- Leaving another login’s “my reviews” after logout.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "comments and reviews" --graph $GRAPH
```
