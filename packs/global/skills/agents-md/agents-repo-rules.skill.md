# Skill: AGENTS — Repository rules

## Pack isolation (hard rule)

Facts **never silently merge across packs**. Every claim cites the owning
`repo_id` / pack. Use only names that appear in **that** pack’s
`CONTRACT.md`, `features/*/overview.md`, `pfm-kb/`, `slug-map.yaml`, and
CODE SEARCH hits from **that** service checkout.

| Ask about | Pack / repo | Do not pull from |
|---|---|---|
| Feed, home, show APIs, wallet, ads, unlocks | `radioly` (`radioly_client_api`) | `search`, kafka workers, clients |
| Universal / show / user search, ranking, ES | `search` (`pocket_search`) | radioly feed handlers |
| Async workers / dumps / MoEngage jobs | `kafka-stream-clients` | radioly HTTP views |
| Go relay / providers | `go-radioly-service` | Python radioly modules |
| CMS / catalog APIs | `content-backend` | consumer radioly |
| Impression / fabric ingest | `fabric` | radioly unless CONTRACT says so |
| Temporal workers / workflows | `airflow` | fabric; radioly HTTP |
| Android / iOS shell | `android-client` / `ios-client` | backend file paths as “the app” |

## Same product name, different code

Several domains exist in **more than one** pack with **different** modules:

- **AI↔PGC:** Radioly feed selection ≠ Search `apply_pgc_show_replacement` — cite the pack that owns the surface.
- **Playtime / listening:** warehouse (Argus) ≠ fabric ingest ≠ kafka dumps ≠ radioly APIs — name which plane you mean.
- **“Feed” vs “Search”:** home/explore feed is radioly; query search is pocket_search.
- **Player-feed rail titles (Next Series / New Releases):** radioly `radioly_client_api`. Not `content-backend`, not `go-radioly-service`. Clients display the server title.
- **“Shows” TG deploy:** monitor `fm-show` / shows catalog — not search, not kafka.

## Labeled multi-repo (when `# MULTI-REPO CONTEXT` is present)

Groot may attach **2–3** packs for:

- Two+ named services in the ask
- **Blank feed/home/library/screen product bugs** — auto-scan backend + clients
  (users often do not know client vs backend; do not quiz for repo first)
- Client-vs-backend / “which layer?” when the user already named a platform
- New features that clearly span client + API (or two backends)

Rules when multi-repo evidence is attached:

1. Compare **labeled** `# REPO \`…\`` / `# CODE SEARCH (\`…\`)` sections only.
2. Also weigh redis/cache gates, auth/token failures, and Sherlock pod health /
   one-uid vs many-users signal.
3. Verdict must name which layer is most likely (client / backend / both / unclear)
   from evidence — or list **per-repo workstreams** for features.
4. Never paste a symbol from section A as if it lived in section B.
5. Do **not** ask “which service?” when multi-repo sections are already present —
   use them. Ask only if a critical unknown remains after comparing.

If the ask is ambiguous and **no** multi-repo context was attached, ask which
service / layer — do **not** blend symbols and do **not** invent ownership.

## Product bugs (when `# PRODUCT BUG CHECKLIST` is attached)

For mindless per-user bugs (history/library/module/ads/unlock/coins/disabled
show/discover/…), walk the checklist before a verdict:

1. Experiments that could cause this behaviour
2. DB / Redis — **only** for per-user data symptoms (history/library/unlock/
   coins/module/disabled show/discover/purchase) after `uid` + `device_id`
   (prefer **Argus**). Skip Argus for blank feed/screen/audio/billboard/app-load.
3. Blast radius — other users? Sherlock pod + API health
4. Recent deploy / change (incl. deploy-order / backward-compat)
5. Curl / API vs app
6. User behaviour
7. Different responses (another uid / locale / A/B)

When intermittent, cross-screen, or load-related, also check multi-pod traps:
stale/shared Redis keys, schema drift, auth/token refresh races, retry storms,
pagination/cursor mismatches, timezone/locale, experiment config drift, N+1
fan-out, deploy-order breaks, swallowed partial failures.

Do not invent DB rows or redis values. If ids are missing, share Sherlock + code
findings first, then ask for `uid` + `device_id` (and show/episode id).

## Grounding

1. Resolve `repo_id`(s) (user named them, sticky, alias, API path, or multi expand).
2. Load only the attached pack(s): CONTRACT → matching feature → matching `pfm-kb`.
3. CODE SEARCH / describe_table / sandbox `/repo/` target the labeled checkout only.
4. Respect `allowed_edit_paths` / `protected_paths` in that pack’s `contract.json`.
5. Pack overlays replace global skills **by name** for that pack only.
6. No inventing handlers, tables, cache keys, or packages that are not in the
   selected pack or tool output.

## Product KB vs code KB

- `pfm-kb/` = product meaning (actors, journey, invariants) — no file/function encyclopedias.
- `knowledge-base/features/` + CONTRACT = code-grounded twins for that repo.
- Never answer a radioly code question from search `pfm-kb` alone (or the reverse).
