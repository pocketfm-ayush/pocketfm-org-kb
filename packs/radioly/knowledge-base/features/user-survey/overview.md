# User survey

Aliases: NPS, in-app survey, player minimise survey

Product context: `radioly/pfm-kb/modules/user-survey.md`

## What it is

Short in-app feedback, typically on player minimise. One survey at a
time. Resume must not re-ask skipped questions.

## Graph anchors

| Symbol | Source |
|---|---|
| user survey | `v3/user_survey/` |


## Key product notes

A short in-app feedback survey. Typical trigger: they minimise the
player. One survey at a time; a newer form replaces the older one on
newer apps.

## Risks

- Inventing question text.
- Re-asking skipped or already-answered questions.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "user survey" --graph $GRAPH
```
