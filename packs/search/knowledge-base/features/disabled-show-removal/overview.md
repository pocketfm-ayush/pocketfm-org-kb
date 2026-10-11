# Disabled Show Removal

Aliases: disabled show, hidden show, take down

Product context: `search/pfm-kb/modules/disabled-show-removal.md`

## What it is
Remove shows the user (or system) has disabled from search results. Cross-cutting filter on
v2/v3 orchestration.

## Graph anchors
| Symbol | Source | Notes |
|---|---|---|
| `UserDisabledShowRemovalService` | `v2/search/services/user_disabled_show_removal_service.py` | Used by `QueryRouter` [INFERRED] |

## Key edges
- Imported in `v3/search/views.py` (with ME/override) [EXTRACTED]
- Stubbed heavily in v3 BDD `_stub_infra_modules()` — tests mock this path carefully

## Tests
- Covered indirectly via universal-search / ME / UX BDD suites
- Content moderation adjacent: `test_content_moderation_bdd.py` (Community 7)

## Risks
- Order in the personalize/finalize pipeline: disabled removal must still apply after
  replacements that introduce new show IDs.
- Easy to “lose” in v3 stubs — prefer integration-style BDD when changing behavior.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "UserDisabledShowRemovalService" --graph $GRAPH
```
