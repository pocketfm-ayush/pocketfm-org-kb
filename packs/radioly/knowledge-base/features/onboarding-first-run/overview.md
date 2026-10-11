# Onboarding first-run

Aliases: language screen, name screen, gender screen, ATT, notification permission

Product context: `radioly/pfm-kb/modules/onboarding-first-run.md` · flow `radioly/pfm-kb/flows/first-run.md`

## What it is

Launch screens before or around the title picker. The picker itself is
`onboarding-show-pick`. Trailer-code is a different prompt.

## Graph anchors

| Symbol | Source |
|---|---|
| onboarding experience | `v3/experience/onboarding/` |

## Risks

- Folding language / ATT / name into the title picker.
- Inventing Android ATT.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "onboarding" --graph $GRAPH
```
