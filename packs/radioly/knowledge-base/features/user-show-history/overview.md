# User show history API

Aliases: show.history, user.show.history, UserShowHistoryView, listening history

Product context: `radioly/pfm-kb/modules/user-show-history.md`

**Repo:** `radioly_client_api`  
**URL:** `user.show.history/(?P<pk>…)` in `v2/user_api/urls.py`  
**View:** `UserShowHistoryView` in `v2/user_api/viewsets.py`

## Limit

`get_listening_history(..., max_records=5)` — default returns at most **5**
recent shows (sorted by `max_updated`, slice `[:max_records]`).

Evidence lives in code as the default argument `max_records=5`, not in Argus.

## Data plane

Reads Scylla playtime (`device_story_playtime` / `user_story_playtime`) via
`get_query_meta`, then enriches last-played story.

## How to answer “was it always 5?”

1. Open `UserShowHistoryView.get_listening_history` default.
2. `git log -p` / `git blame` on `max_records=5` in that file.
3. Do **not** ask Argus unless a warehouse table is named.

## Graph anchors

| Symbol | Source |
|---|---|
| `UserShowHistoryView` | `v2/user_api/viewsets.py` |
| `get_listening_history` | same view (`max_records=5`) |

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "user show history" --graph $GRAPH
```
