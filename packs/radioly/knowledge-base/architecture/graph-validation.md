# Graph validation — radioly_client_api

After extract + cluster:

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
grep "Built from commit" radioly/graphify/graphify-out/GRAPH_REPORT.md
graphify query "what are the main entrypoints?" --graph $GRAPH --budget 4000
```

If `graph.json` is missing, the pack is incomplete — run the rebuild commands in CONTRACT.md.
