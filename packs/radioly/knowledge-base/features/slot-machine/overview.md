# Slot machine (Lucky Spin)

Aliases: lucky spin, spin and win, slot machine

Product context: `radioly/pfm-kb/modules/slot-machine.md`

## What it is

Cooldown-gated spin. Server picks the outcome. Zero coins is allowed.

## Graph anchors

| Symbol | Source |
|---|---|
| slot machine | `v3/gamification/slot_machine/` |


## Key product notes

A cooldown-gated spin that can credit coins. Odds are not the same for
every listener. The server returns whether they can spin, when the next
spin is allowed, and what this spin paid.

## Risks

- Client-picking the reel result.
- Treating “spin” as “always pays.”

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "slot machine" --graph $GRAPH
```
