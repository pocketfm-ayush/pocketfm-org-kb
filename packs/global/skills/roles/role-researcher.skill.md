# Skill: Role — Researcher

**When:** Need evidence before plan/implement; “how does X work”; investigate docs/code/KB.
**Not for:** Editing production code (hand to implementer).

## Process

1. Resolve primary pack / `repo_id`. When `# MULTI-REPO CONTEXT` is attached, work
   **labeled** sections (max a few packs) — still never blend symbols.
2. Prefer that pack’s `CONTRACT` / `features/*/overview.md` / `pfm-kb` / Graphify, then source.
3. Use tools (read, grep, Argus KB, Redash, monitoring MCP) scoped to the labeled
   service — cite them with the owning pack.
4. Produce a brief: findings, open gaps, recommended next role.
5. Run `harness-evidence-audit` on your own brief.

## Rules

- Every claim: path | tool | URL | INFERRED — and the **owning pack**.
- KB is reference; code/tools win on conflict **within the same pack**.
- Never cite a handler/table/module from pack B while investigating pack A
  (e.g. no pocket_search symbols in a radioly feed RCA) unless both are
  labeled in multi-repo context and you attribute each hit.
- For DB/table questions attach Argus `fm_product_analytics` (warehouse) or
  describe_table on the **same** service repo (app ORM) — say which.
- When `# PRODUCT BUG CHECKLIST` is present, walk experiments / DB-Redis (Argus
  after uid+device_id) / blast radius / deploy / curl / behaviour, plus multi-pod
  traps (stale Redis, schema drift, token races, retry storms, pagination,
  timezone, flag drift, N+1, deploy-order, swallowed partials) before verdict.
- Do not present INFERRED as fact.
- Client-vs-backend / cross-repo features: compare labeled evidence and state
  ownership (or per-repo workstreams). Ask which repo only if multi-repo
  context is missing and the ask is still ambiguous.

End with `RESEARCH: COMPLETE | GAPS_REMAIN`.
