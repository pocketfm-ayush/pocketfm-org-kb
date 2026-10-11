# Stage / Studio

Aliases: UGC originals, Studio tab, Write tab, Start Writer

Product context: `radioly/pfm-kb/modules/stage.md`

## What it is
UGC originals / Stage surfaces. Stage V2 may rename Write tab to Studio by writer activity. Start Writer home module CTAs into write navigation. Not ugc-backend HTTP itself.

## Graph anchors
| UGC originals | `v2/ugc_originals/`, `v3/ugc*` |
| Start Writer | `StartWriterModule` |
| UGC bridge | `ugc-backend-writer` |


## Key product notes

A **separate tab** of free listener originals (and, for some people,
writer tools). Not For You. Not Home’s UGC-row (that **replaces**
Home in some locales).

## Risks
- Inventing a separate create-studio app package.
- Ignoring Studio rename rules when changing Write tab.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "Stage / Studio" --graph $GRAPH
```
