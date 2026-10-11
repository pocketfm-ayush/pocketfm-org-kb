# Org KB Slack-thread locator benchmark

Generated: 2026-09-22T19:19:03.881506+00:00

## Purpose
Measure centralized cross-repo knowledge (cerebro-knowledge → LightRAG) on real Slack asks.
Primary score: how fast/accurately we land **repo → file → function**, with low tokens and low maintenance.

## Scoring (production)
| Metric | Pass bar |
|---|---|
| Locator latency p50 | < 3s LightRAG; < 15s with evidence open |
| Repo accuracy | exact match in gold repos |
| Path accuracy | gold path substring OR handbook pointer path |
| Symbol accuracy | gold symbol/handler when known |
| LLM input tokens (locate-only) | < 8k |
| LLM output tokens (locate-only) | < 1.5k |
| Maintenance | knowledge PR delta sync only; no full Graphify rebuild |
| Repo span | each eval run must exercise **≥19 distinct repos** |

## Suite inventory
- Unique Slack threads requested: **76**
- Threads fetched (bot member): **34**
- Threads pending channel invite (`not_in_channel`): **42**
- Synthetic coverage probes: **24**
- Total cases: **100**
- Distinct repos touched by suite: **29**

## Gold-annotated Slack cases (run these first)

### SLACK-GOLD-01 — content-internal-discussions
- URL: https://pocket-fm.slack.com/archives/C09GCH8VA2Z/p1784183063617839?thread_ts=1784126817.760249
- Intent: explain
- Question: iOS: selecting another episode from show details after player navigation plays wrong episode. Which client repo owns this?
- Gold repos: `ios_client`
- Gold symbols/concepts: `show details episode playback`
- Must mention: ios_client, show details, episode

### SLACK-GOLD-02 — going_live
- URL: https://pocket-fm.slack.com/archives/C032XA5TMBK/p1775031360620079?thread_ts=1775031360.620079
- Intent: change_blast
- Question: Where was the production episode seq_number bug fixed (repo + PR lineage) and which TG owns verification?
- Gold repos: `radioly_client_api`
- Gold symbols/concepts: `seq_number`
- Must mention: radioly_client_api, seq_number

### SLACK-GOLD-03 — going_live
- URL: https://pocket-fm.slack.com/archives/C032XA5TMBK/p1775458496561089?thread_ts=1775458496.561089
- Intent: change_blast
- Question: Credit Space bug fix deploy — which repo/PR and related feed TG should agents open?
- Gold repos: `radioly_client_api`
- Gold symbols/concepts: `credit space`
- Must mention: radioly_client_api, credit

### SLACK-GOLD-04 — pod-content
- URL: https://pocket-fm.slack.com/archives/C075MCAP9AL/p1789452422.110269?thread_ts=1789452422.110269
- Intent: debug
- Question: Italy Popular module shows English MVS/Heir in Hiding. Which service owns feed module composition for LATAM/Italian Popular?
- Gold repos: `radioly_client_api, content-backend`
- Gold symbols/concepts: `Popular on pocketfm module, LATAM feed`
- Must mention: Popular, LATAM, module, radioly

### SLACK-GOLD-05 — tech-cs-issues
- URL: https://pocket-fm.slack.com/archives/C05K9PPV0Q7/p1778144715449019?thread_ts=1778138233.870399
- Intent: debug
- Question: Show details shows Resume Episode 273 but user unlocked only 263. Which repo/file/function owns the resume pointer vs unlocked count, and what was the prior fix?
- Gold repos: `radioly_client_api, android_client, ios_client`
- Gold paths: `v2/content_api/models.py`
- Gold symbols/concepts: `start_index clamp / resume pointer`
- Must mention: radioly_client_api, models.py, resume, client

### SLACK-GOLD-06 — sentry_content
- URL: https://pocket-fm.slack.com/archives/C07QHG2SRCM/p1782287110652619?thread_ts=1781953262.332179
- Intent: incident
- Question: content-fm ServerError / connection failures — which repo and data store path should on-call inspect first?
- Gold repos: `content-backend`
- Gold symbols/concepts: `Scylla Session.execute`
- Must mention: content-backend, Scylla, timeout

### SLACK-GOLD-07 — rough-work
- URL: https://pocket-fm.slack.com/archives/C0AQGQTLA67/p1788764693839879?thread_ts=1788763285.914249
- Intent: debug
- Question: Spanish shows appear for users who selected English. Which radioly feed/cache path is the primary suspect and what should be checked about the cache key?
- Gold repos: `radioly_client_api`
- Gold symbols/concepts: `feed cache key, language`
- Must mention: radioly_client_api, feed, language, cache

### SLACK-GOLD-08 — sentry_content
- URL: https://pocket-fm.slack.com/archives/C07QHG2SRCM/p1789462758822409?thread_ts=1782118431.047329
- Intent: incident
- Question: content-fm OperationTimedOut against Scylla :19042 — which service owns the client and what evidence pointer should KB return?
- Gold repos: `content-backend`
- Gold symbols/concepts: `OperationTimedOut, Session.execute_async`
- Must mention: content-backend, OperationTimedOut, Scylla

### SLACK-GOLD-09 — ios_reviews
- URL: https://pocket-fm.slack.com/archives/C02TNA1R2R0/p1789798582556759?thread_ts=1789794060.915659
- Intent: locate
- Question: Continue Playing module unexpectedly changes ranking/contents. Which repo owns Continue Playing construction vs DS ranking?
- Gold repos: `radioly_client_api`
- Gold symbols/concepts: `continue playing module`
- Must mention: radioly_client_api, continue playing

### SLACK-GOLD-10 — tech-cs-issues
- URL: https://pocket-fm.slack.com/archives/C05K9PPV0Q7/p1781856303534109?thread_ts=1781856303.534109
- Intent: debug
- Question: WhatsApp notifications toggle does not persist. Which client API and IAM endpoint/field own this preference?
- Gold repos: `radioly_client_api, iam, android_client, ios_client`
- Gold symbols/concepts: `user.update, POST /v1/profile, is_whatsapp`
- Must mention: iam, is_whatsapp, user.update

## Coverage probes (force ≥19 repos)
Ask each coverage case; answer must name the target repo and at least one real path/symbol from handbook evidence.

### COV-01-RADIOLY_CLIENT_API
Across the org KB, locate repo `radioly_client_api`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-02-IAM
Across the org KB, locate repo `iam`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-03-NEXUS
Across the org KB, locate repo `nexus`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-04-ANDROID_CLIENT
Across the org KB, locate repo `android_client`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-05-IOS_CLIENT
Across the org KB, locate repo `ios_client`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-06-APOLLO
Across the org KB, locate repo `apollo`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-07-IMPRESSION
Across the org KB, locate repo `impression`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-08-AIRFLOW
Across the org KB, locate repo `airflow`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-09-KAFKA_STREAM_CLIENTS
Across the org KB, locate repo `kafka-stream-clients`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-10-GO_COMMON
Across the org KB, locate repo `go-common`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-11-PYTHON_COMMON
Across the org KB, locate repo `python-common`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-12-EXPERIENCE
Across the org KB, locate repo `experience`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-13-CONTENT_BACKEND
Across the org KB, locate repo `content-backend`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-14-ADS
Across the org KB, locate repo `ads`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-15-UGC_BACKEND
Across the org KB, locate repo `ugc-backend`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-16-UGC_TTS_WORKER
Across the org KB, locate repo `ugc-tts-worker`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-17-WRITERS_BACKEND
Across the org KB, locate repo `writers-backend`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-18-CMS_DASHBOARD_BACKEND
Across the org KB, locate repo `cms-dashboard-backend`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-19-INFRA_DEPLOYMENTS_K8S
Across the org KB, locate repo `Infra_deployments_k8s`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-20-INFRA_K8S
Across the org KB, locate repo `Infra_k8s`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-21-MEDIA_FORGE
Across the org KB, locate repo `media-forge`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-22-RAVEN
Across the org KB, locate repo `raven`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-23-FABRIC
Across the org KB, locate repo `fabric`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

### COV-24-GO_RADIOLY
Across the org KB, locate repo `go-radioly`: primary module paths and the top 1–3 handler/functions an agent should open for a production bug in that service.

## Pending Slack threads (invite `prd_agent` bot)
Bot lacks `channels:join` / membership. Invite bot to these channels then re-run fetch to promote to gold.

- `#C05GRDP9US1`
- `#C07DZC0MKN2`
- `#bug-discussions-cms`
- `#bugbash-2026`
- `#cms-sentry-alerts-prod`
- `#comics-business-analytics`
- `#comics-s2s-reports`
- `#content-pr-reviews`
- `#creator-payments-sentry-alerts`
- `#ios-agent-development`
- `#mau-qualification`
- `#phantom-use`
- `#pocket-toons-cs`
- `#product-leads`
- `#qa`
- `#sentry-ugc-kafka-workers`
- `#tech`
- `#tts-ugc-prod-alerts`
- `#ugc-prod-alerts-critical`
- `#ugc-tamil`
- `#writer_contests`
