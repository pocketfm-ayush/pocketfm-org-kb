# Support ticket

Aliases: support ticket, help ticket, zendesk

Product context: `radioly/pfm-kb/modules/support-ticket.md`

## What it is

Create / track support tickets. Distinct from FAQ and CSAT.

## Graph anchors

CODE SEARCH support ticket / zendesk integration under user or campaigns.


## Key product notes

In-app **chat → support ticket**. Not Help articles. Not
“Forgot account?” (account-recovery).

## Risks

- Inventing SLA or ticket fields without packed evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "support ticket" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

