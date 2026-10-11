# Graph validation — kafka-stream-clients

After extract + cluster:

```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
grep "Built from commit" kafka-stream-clients/graphify/graphify-out/GRAPH_REPORT.md
graphify query "what are the main entrypoints?" --graph $GRAPH --budget 4000
```

If `graph.json` is missing, the pack is incomplete — run the rebuild commands in CONTRACT.md.
