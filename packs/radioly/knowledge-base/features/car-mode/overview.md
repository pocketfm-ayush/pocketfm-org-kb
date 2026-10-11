# Car mode

Aliases: car mode, in-car, bluetooth car

Product context: `radioly/pfm-kb/modules/car-mode.md`

## What it is

Classify Bluetooth name, then a short recents row. iOS is gated on;
Android is present but not enabled. Earphones are not a car.

## Graph anchors

| Symbol | Source |
|---|---|
| car mode | `v3/car_mode/` |


## Key product notes

A simplified in-car listen: classify the Bluetooth name, then show
a short recents row.

## Risks

- Treating earphones as a car.
- Inventing popular titles when recents are empty.
- Assuming Android car mode is live.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "car mode" --graph $GRAPH
```
