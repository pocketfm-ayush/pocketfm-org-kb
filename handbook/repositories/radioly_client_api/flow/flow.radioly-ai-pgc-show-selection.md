---
id: flow.radioly-ai-pgc-show-selection
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/helpers.py#get_user_age
---

**Aliases:** AI PGC, AI/PGC, AI<>PGC, AI <-> PGC, PGC show selection, PGC replacement, duplicate show, duplicate pair, keep_ai_default, user_tg pgc, FMF-3783, FMF-3782

**When to use:** AI ↔ PGC show selection for a Pocket FM listener. First stop `get_user_age` in `v2/feed_api/helpers.py`.

**Required inputs:** screen and symptom.
