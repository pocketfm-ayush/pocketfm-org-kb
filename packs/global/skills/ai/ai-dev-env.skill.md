---
name: ai-dev-env
description: Index of discrete AI Dev Env skills — engineering, stack, and agent/MCP/eval. Load one skill per job; never collapse into a mega-skill.
triggers: [ai dev env, which skill, skill tree, engineering skills, stack skills]
intent: general
priority: 95
---

# YOUR AI DEV ENV (index only)

Load **one** skill for the job. Do not replace this tree with a single mega-skill.

```
YOUR AI DEV ENV
                 │
    ┌────────────┴────────────┐
    │                         │
CORE ENGINEERING          AI / AGENTS
    │                         │
┌───┼───┐                ┌────┼────┐
│   │   │                │    │    │
Plan Review Debug      Agent MCP Eval
│   │   │                │
└───┼───┘                │
    │                    │
┌───┼─────────┐          │
│   │         │          │
Test Refactor Security   │
│                        │
└──────────┬─────────────┘
           │
      Documentation
           │
    ┌──────┴───────┐
    │              │
  README          API
    │              │
Architecture     PRD
```

## Core engineering (01–15)

| # | Skill | Use when |
|---|---|---|
| 01 | `repo-explorer` | Map repo before changing it |
| 02 | `planner` | Ordered implementation plan |
| 03 | `architecture` | Boundaries, flows, trade-offs |
| 04 | `code-review` | Diff / PR review |
| 05 | `debugger` | Reproduce + root-cause |
| 06 | `test-engineer` | Design / add tests |
| 07 | `refactoring` | Behavior-preserving cleanup |
| 08 | `security-review` | Authz, secrets, abuse paths |
| 09 | `performance-review` | Latency, N+1, cost |
| 10 | `documentation` | README / runbooks / notes |
| 11 | `api-design` | HTTP/RPC contracts |
| 12 | `database-sql` | Schema, SQL, migrations |
| 13 | `github` | Branch, PR, CI hygiene |
| 14 | `agent-builder` | New agents / skills / tools |
| 15 | `prd` | Requirements + acceptance |

## Stack (load with engineering skills)

`mysql` · `redis` · `kafka` · `docker` · `kubernetes` · `slack` · `python` · `typescript` · `golang`

## AI / Agents

| Skill | Use when |
|---|---|
| `agent` | Runtime loop / stop conditions |
| `mcp` | MCP tool discovery and calls |
| `eval` | Golden sets / agent regressions |

## Also keep (not collapsed)

- Harness: `harness-*`
- Roles: `role-*`
- AGENTS sections: `agents-*`
- Product: `prd-*`, `phantom-*`, `monitoring-deploy`, …

## Rule

**Multiple skills, one job each.** Compose (`debugger` + `mysql` + `harness-evidence-audit`), do not merge into one file.
