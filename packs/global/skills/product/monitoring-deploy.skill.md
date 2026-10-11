<!-- Cross-repo deploy + incident monitoring. Source of truth: Pocket-Fm/monitoring-mcp. -->
# Skill: Monitoring and deployment verification

**When:** Deploy, canary, CodePipeline, target-group health, 5xx/latency, post-release
checks, or "is service X healthy?" across Pocket FM repos.  
**Tools:** Prefer **pocketfm-monitoring MCP** (`Pocket-Fm/monitoring-mcp`, 38 tools).
In Slack, Groot also routes live incidents to **Sherlock/Holmes**.  
**Never invent metrics.** If a tool returns `error`, record the code + hint and continue
the checklist — do not skip the data plane because one surface failed.

## Absolute rule — no silent skips

Every deploy or incident answer must cover **all** layers below, or explicitly mark
each skipped layer with **why** (tool error code, not "looked fine"). Truncated
MCP payloads (`error: truncated`) are **incomplete** — narrow the query and retry.

| Layer | If skipped you lose | Tool family |
|---|---|---|
| Edge routing | Wrong TG monitored after ALB rule change | `aws_path_to_tg` |
| Target health | Pipeline green while hosts fail health checks | `aws_target_group_health` |
| Pipeline stage | Watching the wrong revision | `aws_codepipeline_status` |
| ALB / CW | LB 5XX / RPS / TargetResponseTime not in app Prom | `cloudwatch_metric` |
| Canary hits | Canary "healthy" with zero traffic | `canary_counter` |
| App RED (prod) | Real RPS/latency/4xx/5xx on main | `radioly_api_*` / `prometheus_*` |
| Pilot APM | Trace p50/p90/p99 (main has no APM sample) | `datadog_apm_service_stats(*-pilot-prod)` |
| Exceptions | Stack traces / new ERROR | `opensearch_recent_tracebacks`, `opensearch_text_search` |
| Scylla | Cluster ops/p99/CPU/disk; KS rates | `scylla_*` |
| Redis | Kill switch / cache / experiment / session | `redis_get`, `redis_scan`, `redis_execute` |
| Kafka | Broker ISR/skew, consumer lag, poison msgs | `kafka_*` |
| SQL proof | Row-level truth on MySQL/Trino/Scylla | `redash_query` (+ `redash_list_data_sources`) |
| Human interrupt | Long watch continues after RED | `notify_desktop` |

## Preflight (every session)

1. VPN up — smoke `redash_list_data_sources()`. VPN status is **process-cached**; after VPN flip, reconnect the MCP.
2. Safari tabs logged in: Grafana (`grafana-main`), Datadog, OpenSearch (**via AWS SSO portal tile**, not direct URL), Kafka UI, Scylla **monitor** URL (`graphs.cloud.scylladb.com/cluster/21229/...`).
3. AWS SSO fresh — `aws_target_group_health` smoke.
4. `kafka_list_clusters()` if not using default `fm-msk-cluster-iam`.
5. Optional: `notify_desktop("smoke")` for long watches.

## Pre-deploy baseline

1. `aws_path_to_tg("<API path>")` → record TG(s) (`app-lb` default).
2. `aws_target_group_health(<tg>)` → healthy / unhealthy / draining counts.
3. `radioly_api_overview("<app>")` + `radioly_api_top_endpoints_by_errors` (app name like `fm-show-main-prod`).
4. `datadog_apm_service_stats("<svc>-pilot-prod")` — **never** rely on `*-main-prod` APM (nulls).
5. If data-plane risk: `scylla_cluster_overview` + relevant `scylla_keyspace_metrics`.
6. If workers: `kafka_consumer_group_health` (+ `kafka_consumer_groups_for_topic`).
7. If flags: `redis_scan` / `redis_get` for kill switches / experiments.
8. Record baselines (RPS, p99, 5xx %, lag, TG healthy count).

## During deploy

1. Poll `aws_codepipeline_status("<pipeline>")` until terminal success/fail.
2. Re-check `aws_target_group_health` — watch `initial` → `healthy`, draining→0, unhealthy→0.
3. `canary_counter` (or service canary metric) → **non-zero** hits.
4. `cloudwatch_metric` for ALB/TG `HTTPCode_Target_5XX_Count`, `RequestCount`, `TargetResponseTime`, `HealthyHostCount`.
5. On RED threshold: `notify_desktop(..., subtitle="RED")`.

## Post-deploy — mandatory evidence pack

Do **all** of these (or mark skip+error):

1. **Traffic RED:** `radioly_api_overview` + `radioly_api_top_endpoints_by_latency` + `_by_errors` (and `_by_rps` if traffic shift suspected).
2. **Canary latency:** `datadog_apm_service_stats(pilot)`.
3. **Exceptions:** `opensearch_recent_tracebacks("<service>")` + `opensearch_text_search` (discover index via `opensearch_indices` if needed). Prefer OS over `datadog_logs_search` for k8s app logs.
4. **Routing:** re-run `aws_path_to_tg` if rules may have changed.
5. **TG settled:** all healthy, draining 0.
6. **Deps:** Scylla overview/KS; Redis flags; Kafka lag + optional `kafka_recent_messages` for payload shape.
7. **Business/SQL:** `redash_query` on the correct replica when behavior needs DB proof.
8. **Escape hatches** when named tools miss the signal: `prometheus_query` / `_range`, `datadog_metric`, `opensearch_raw`, `scylla_promql`, `redis_execute`.

## Incident expansion order

1. Path → TG → health → CloudWatch 5XX (edge)
2. Radioly overview → top errors / latency (app RED)
3. OpenSearch tracebacks / text (root-cause text)
4. Pilot Datadog APM (trace latency)
5. Scylla / Redis / Kafka (dependencies)
6. Redash (data correctness)

## Groot / Slack wiring

| Ask shape | Backend | This skill |
|---|---|---|
| 5xx / outage / pager / crashloop | Sherlock (`OBSERVABILITY_ASK`) | Attach — list missing evidence Sherlock did not cover |
| Deploy / canary / pipeline / TG health / “monitor until done” | Deploy watch + Sherlock and/or MCP | Attach — run or narrate the checklist; do not invent numbers |
| DB / table / warehouse facts | Argus + `fm_product_analytics` | Separate from live metrics |

### Holmes binding (hard rule)

Holmes is **ClusterIP-only** — same cluster as the Groot that answered:

| Groot | Holmes |
|---|---|
| `groot-qa` (`GROOT_ENV=qa`) | `sherlock-qa-holmes.sherlock-qa.svc.cluster.local` |
| `groot-prod` (`GROOT_ENV=production`) | `sherlock-prod-holmes.sherlock-prod.svc.cluster.local` |

- Never point groot-qa at sherlock-prod (DNS does not resolve across clusters).
- Never point groot-prod at sherlock-qa.
- If Holmes `/healthz` fails: mark Sherlock **SKIPPED** with the ConnectError, continue MCP layers when available — do **not** invent TG/RED numbers.
- Deploy watch must not claim “armed” unless live Holmes healthz **or** monitoring MCP is actually available.

### Deploy watch (Slack)

- Read-only: observe pipeline/TG/RED; never stop/promote/rollback.
- Prefer MCP tools when installed; else Sherlock with this checklist attached.
- Status asks (“are you watching?”, “status of … deployment”) refer to the **thread’s** watch — not CODE SEARCH.
- `stop watching` stops the poller (may take one poll interval across pods).

Writes: only `redis_expire`, and only if `MCP_ALLOW_WRITES=true`. Never DEL.

## Error envelope (MCP)

Responses may be `{"error": "<code>", "hint": "...", "details": {...}}`.
Codes: `vpn_unreachable`, `auth_failed`, `safari_tab_not_found`, `safari_js_failed`,
`upstream_http_error`, `timeout`, `truncated`, `write_disabled`, `not_found`, `query_failed`.
Treat any `error` as a **failed data point**, not as "healthy".

## Repo coverage

Applies to **all** onboarded packs (search, radioly, fabric, content-backend, kafka
workers, genai, cms, …). Map service → Prom `app` label / Datadog service /
OpenSearch `logs-{service}-*` / TG name from **that pack’s** CONTRACT when present;
otherwise discover via `aws_path_to_tg` + `opensearch_indices` + `kafka_list_topics`.

**One service per answer:** do not mix radioly feed handlers with pocket_search
symbols, or kafka-worker jobs with go-radioly-service modes, in the same verdict.

## Do not

- Declare deploy success from CodePipeline alone.
- Use Datadog APM on `*-main-prod` as latency proof.
- Hit OpenSearch without AWS SSO portal SAML.
- Skip Kafka lag for consumer/worker deploys.
- Skip Scylla/Redis when the change touches those stores.
- Accept truncated MCP results as complete.
- Cite code from a pack that is not the resolved `repo_id` for this ask.
