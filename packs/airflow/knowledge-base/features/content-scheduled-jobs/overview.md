# Content Scheduled Jobs

Aliases: popularity dag, autoplay cache job, show rotation

Product context: `airflow/pfm-kb/modules/content-scheduled-jobs.md`

## What it is
Scheduled content freshness: popularity/ranks, autoplay caches, rotations,
comment/stats style backfills that home/feed/player eventually read.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "content feed popularity workflows" --graph $GRAPH
```
