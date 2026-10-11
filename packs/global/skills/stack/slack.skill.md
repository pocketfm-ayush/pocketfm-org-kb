---
name: slack
description: Slack notifications and bot messages — clear, actionable, low noise.
triggers: [slack, notify slack, slack message, slack bot]
intent: implement
priority: 70
---

# Slack

## Do
- Short alerts with what/where/severity/link to evidence.
- Prefer existing notify integrations (e.g. monitoring-mcp notify tools).
- Route to the right channel; avoid paging everyone for info-level.

## Do not
- Dump raw PII or secrets into channels.
- Spam retries that duplicate the same alert without dedupe.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
