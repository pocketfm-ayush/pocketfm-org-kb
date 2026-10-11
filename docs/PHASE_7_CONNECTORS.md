# Phase 7 — Connectors + MCP (org instance)

Org Brain exit gate: **new connector without core rewrite**.

## Enabled (this instance)

| Connector | Status | Profile | Notes |
|---|---|---|---|
| `git.local` | enabled | repository_read | Sibling checkouts in `org.yaml` |
| `docs.markdown` | enabled | repository_read | `memory/` + pack markdown |
| `issues.local` | enabled | repository_read | `memory/incidents/` |
| `otel.http` | disabled | operational_read | Wire Sherlock/OTel when approved |
| `mcp.generic` | disabled | metadata_only | Allowlist-only when enabled |
| `pfm.content_knowledge_base` | mirrored | repository_read | Content under `packs/` |
| `pfm.cerebro` | mirrored resources | repository_read | `peers/cerebro/resources/` |
| `pfm.sherlock` | disabled | operational_read | Live RCA — TTL only, not handbook |

See `connectors/default.yaml`.

## Adding a Pocket FM connector

1. Declare `connector_id`, capabilities, auth, scopes in `connectors/`.
2. Map ACL profile in `policies.yaml` (never expand via MCP tool text).
3. Keep secrets in env / AWS SM — never in git.
4. Document in this file + run golden questions that touch the new source.
5. Engine change (if needed) lands in `ayushgarg2702/org-kb`, not here.

## Untrusted input

Repository content, issues, docs, and MCP payloads are **untrusted**. They cannot
raise privileges or become policy.
