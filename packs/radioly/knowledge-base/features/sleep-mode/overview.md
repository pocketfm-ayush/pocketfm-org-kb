# Unwind (sleep mode)

Aliases: Unwind, sleep mode, sleep stories

Product context: `radioly/pfm-kb/modules/sleep-mode.md`

## What it is

Evening catalog. User-facing name is Unwind. English only. Hindi is a
reject, not an empty English feed.

## Graph anchors

| Symbol | Source |
|---|---|
| sleep mode | `v3/experience/sleep_mode/` |


## Key product notes

An evening catalog of calm stories and soundscapes. User-facing name
is **Unwind**. English only. Distinct from any older sleep-stories
partnership.

## Risks

- Serving Hindi Unwind as empty English.
- Time-gating the Unwind feed itself (only Home/profile/nudges are).

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "sleep mode" --graph $GRAPH
```
