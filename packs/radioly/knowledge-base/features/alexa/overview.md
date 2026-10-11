# Alexa

Aliases: Alexa, Pocket FM skill, voice command

Product context: `radioly/pfm-kb/modules/alexa.md`

## What it is

Voice play / resume / next / unlock-next. Device is enough to play.
Coin unlock needs a login. Insufficient coins is spoken, not a mobile
paywall sheet.

## Graph anchors

| Symbol | Source |
|---|---|
| Alexa | `v3/experience/alexa/` |


## Key product notes

Voice play / resume / next / previous / start-over / play episode N,
plus “unlock next” with coins and “recommend a series.”

## Risks

- Letting a guest spend coins.
- Opening the mobile paywall from a voice unlock miss.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "alexa" --graph $GRAPH
```
