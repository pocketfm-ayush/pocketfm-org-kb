# Graph validation — content-backend

After extract + cluster:

```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
grep "Built from commit" content-backend/graphify/graphify-out/GRAPH_REPORT.md
graphify query "what are the main entrypoints?" --graph $GRAPH --budget 4000
```

If `graph.json` is missing, the pack is incomplete — run the rebuild commands in CONTRACT.md.
