# Repo Mind — litefm-backend

Skills + orchestrator must obey this file and `contract.json`.

**GitHub:** https://github.com/Pocket-Fm/litefm-backend  
**Stack:** Python · Django · MySQL / Redis (same family as radioly layout)

## Purpose

Lite FM product backend. Load `litefm-backend/pfm-kb/` for product meaning.

Do **not** treat this as `radioly_client_api`. Symbols may look familiar
(`radioly_api/`, `feed_api/`, `v2/`, `v3/`) but this is a separate checkout and
pack — never cite radioly paths as if they lived here.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| Django project | `radioly_api/`, `manage.py` | settings, WSGI |
| HTTP APIs | `feed_api/`, `content_api/`, `user_api/`, `v2/`, `v3/` | product surfaces |
| Workers | `workers/` | async jobs |
| Tests | `tests/` | pytest |

## Conventions

- Prefer CODE SEARCH in this checkout when the ask names `litefm` / `litefm-backend`.
- Same GitHub org token as other Pocket-Fm service repos.
- Expand feature twins under `knowledge-base/features/` as domains are documented.

## Out of scope

- Pocket FM consumer BFF (`radioly_client_api` / pack `radioly`)
- Catalog cutover service (`content-backend`)
- Client apps (`android_client`, `ios_client`)
