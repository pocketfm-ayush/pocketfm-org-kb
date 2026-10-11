# Experiments Allocation

Aliases: experiments, A/B allocation, experiment bucketing, disjoint experiments

Product context: `radioly/pfm-kb/modules/experiments-allocation.md`

## What it is
Radioly experiment framework under `v2/experiments/` (plus v3 domain helpers):
allocates listeners into variants that change feeds, payments, ads, and UX.
**Product KB must not store live allocation percentages or current winners.**

## Graph anchors
| Symbol / area | Source |
|---|---|
| Experiment packages | `v2/experiments/` |
| Feed design revamp examples | `v2/experiments/feed/` |
| Allocation helpers | `v2/experiments/allocation_service/` |


## Key product notes

How listeners are placed into experiment variants that change UX, feed, ads, or
monetization. Allocation is server-driven; clients usually receive outcomes via
launch config or feature payloads.

## Risks
- Never invent “user is in variant X” without reading allocation code + flags.
- Launch config often triggers allocations — pair with launch-config.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "experiment allocation services" --graph $GRAPH
```
