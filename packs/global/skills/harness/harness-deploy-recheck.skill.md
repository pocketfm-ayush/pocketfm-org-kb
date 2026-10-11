<!-- After deploy claims — full monitoring pack. -->
# Skill: Harness deploy recheck

**When:** After deploy/canary/release claims.
**Delegates to:** `monitoring-deploy.skill.md` (full MCP checklist).

## Minimum

Re-state each layer as OK|WARN|FAIL|SKIPPED(error): path→TG, TG health,
pipeline, CloudWatch, canary hits, Radioly RED, pilot APM, OpenSearch,
Scylla/Redis/Kafka as relevant, Redash if data proof needed.

`DEPLOY_RECHECK: PASS` only if no FAIL and no silent skip.
CodePipeline green alone is **FAIL**.
