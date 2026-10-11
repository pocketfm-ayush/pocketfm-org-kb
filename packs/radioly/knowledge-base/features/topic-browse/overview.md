# Topic browse

Aliases: topic, browse topic, genre topic

Product context: `radioly/pfm-kb/modules/topic-browse.md`

## What it is

Topic / genre browse rails outside typed Search. Subject to feed visibility + AI↔PGC helpers.

## Graph anchors

| Symbol | Source |
|---|---|
| `filter_duplicate_shows_from_topic_entities` | `v2/feed_api/helpers.py` |


## Key product notes

A **one-topic (or one-tag) list of titles**. Tap a rail, theme,
or collection and land here. Not For You. Not Discover shorts.
Not Stage.

The old Hindi “explore topics” directory is this same browse, not
a fourth tab.

## Risks

- Confusing topic browse with Search `show-filter` / genre-trope discovery.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "topic browse" --graph $GRAPH
```
