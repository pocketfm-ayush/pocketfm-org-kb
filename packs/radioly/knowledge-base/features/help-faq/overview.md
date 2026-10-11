# Help / FAQ

Aliases: help, FAQ, faq

Product context: `radioly/pfm-kb/modules/help-faq.md`

## What it is

In-app help articles and categories served from campaign FAQ models.

## Graph anchors

| Symbol | Source |
|---|---|
| `Faq` / `FaqCategory` | `v2/campaigns/faqs/models.py` (`faq`, `faq_categories`) |
| FAQ views / serializers | `v2/campaigns/faqs/` |

## Stores

- MySQL: `faq`, `faq_categories`, `faq_feedback`, `faq_top_searches`.


## Key product notes

The **Help** list: categories, articles, search, related, top
searches. Not History FAQ (wallet). Not subscription FAQ.

## Risks

- Inventing article copy; CMS owns content.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "help faq" --graph $GRAPH
```
