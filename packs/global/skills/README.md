# Groot skills

Skills are markdown Groot attaches to Madeye or a graph node. Pack overlays
live at `<pack>/skills/<name>.skill.md` (flat or nested) and replace the global
file of the same **stem** (filename without folders). Facts never merge — only
skills do.

Root **`AGENTS.md`** is always-on. Skills are progressive disclosure — load via
`agents-index`, `ai-dev-env`, or by name. **One skill = one job**; compose, do
not collapse into a mega-skill.

## Layout (segregated)

```
global/skills/
  README.md
  OPEN_POINTS.md
  agents-md/       # AGENTS.md section skills
  harness/         # question-everything + recheck ladder
  roles/           # Planner / Researcher / Reviewer / …
  engineering/     # AI Dev Env core 01–15
  stack/           # mysql redis kafka docker k8s slack languages
  ai/              # agent · mcp · eval · ai-dev-env index
  product/         # PRD / Phantom / deploy / explain-flow / …
```

Lookup is by **skill name** (`planner`), not folder. Groot searches
`global/skills/**/<name>.skill.md` then pack overlay.

## How Groot invokes skills

1. Classify Slack/`/groot` ask → `Intent` (`groot/api/intents.py`).
2. Map intent → **one** skill name (`SKILL_FOR_INTENT` in `groot/knowledge/skills.py`).
3. `read_skill(name)` loads markdown → `_attach_skill` puts `# SKILL \`<name>\`` into the system prompt.
4. Graph nodes (`implement`, `evals`, `analyze`) may load named skills from the pack.

**Today only product intents are auto-wired** (PRD, evals, implement, tests, Argus,
investigate/deploy, explain-flow). Engineering / stack / harness / role skills are
loaded when an agent or future router asks for them by name (Cursor, Madeye stage,
or explicit compose). They are not all attached on every turn.

| Intent | Skill |
|---|---|
| `general` | `explain-flow` |
| `analyze_prd` | `prd-analysis` |
| `normalize_prd` | `prd-normalize` |
| `write_prd` | `prd-writer` |
| `write_evals` | `eval-writer` |
| `implement` | `implementation` |
| `write_tests` | `phantom-tests` |
| `confidence` | `confidence` |
| `argus` | `argus-kb` (builtin) |
| `investigate` / `deploy` | `monitoring-deploy` |
| `review` | composed: `role-reviewer` + `code-review` + stack language + pack overlay |

### Review skill composition (Deep Agent `reviewer`)

For `Intent.REVIEW`, Groot does **not** attach only `role-reviewer`. It resolves:

1. Role: `role-reviewer`, `harness-review-recheck` (+ `atlassian-docs` on the role)
2. Engineering: `code-review`, `agents-pr`
3. Language from pack `contract.json` → `python` / `golang` / `kotlin` / `swift` / `typescript`
4. Optional second language from PR file extensions
5. Pack overlay: `<pack>/skills/code-review.skill.md` replaces global `code-review`
6. Capped companions from `framework` / `external_systems` (e.g. `database-sql`, `mysql`)

Stack skills: `python` · `typescript` · `golang` · `kotlin` · `swift` (+ infra stack as companions)

## YOUR AI DEV ENV

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
      Documentation → README · Architecture · API · PRD
```

Index: `ai/ai-dev-env.skill.md`

### Core engineering → `engineering/`

| # | Skill |
|---|---|
| 01 | `repo-explorer` |
| 02 | `planner` |
| 03 | `architecture` |
| 04 | `code-review` |
| 05 | `debugger` |
| 06 | `test-engineer` |
| 07 | `refactoring` |
| 08 | `security-review` |
| 09 | `performance-review` |
| 10 | `documentation` |
| 11 | `api-design` |
| 12 | `database-sql` |
| 13 | `github` |
| 14 | `agent-builder` |
| 15 | `prd` |

### Stack → `stack/`

`mysql` · `redis` · `kafka` · `docker` · `kubernetes` · `slack` · `python` · `typescript` · `golang` · `kotlin` · `swift`

### AI / Agents → `ai/`

`agent` · `mcp` · `eval` (+ index `ai-dev-env`)

## AGENTS.md sections → `agents-md/`

| Section | Skill |
|---|---|
| Project overview | `agents-overview` |
| Architecture | `agents-architecture` |
| Repository rules | `agents-repo-rules` |
| Coding standards | `agents-coding` |
| Testing requirements | `agents-testing` |
| Database rules | `agents-database` |
| Security rules | `agents-security` |
| Git rules | `agents-git` |
| PR rules | `agents-pr` |
| Deployment rules | `agents-deploy` |
| Agent behavior | `agents-behavior` |
| Index | `agents-index` |

## Harness → `harness/`

| Skill | Level |
|---|---|
| `harness-loop` | Meta stage machine |
| `harness-intake` | Clarify before inventing |
| `harness-response-recheck` | **Every** assistant turn |
| `harness-plan-critique` | After planner |
| `harness-evidence-audit` | After researcher |
| `harness-diff-recheck` | After implement |
| `harness-test-recheck` | After tests |
| `harness-review-recheck` | After reviewer |
| `harness-deploy-recheck` | After deploy claims |

## Roles → `roles/`

| Skill | Role |
|---|---|
| `role-planner` | Phased plans + acceptance + validation |
| `role-researcher` | Evidence-backed briefs |
| `role-reviewer` | Severity-tagged review only |
| `role-implementer` | Execute approved plan |
| `role-verifier` | Rubric freeze + re-grade |
| `role-scout` | Fast read-only paths |
| `role-architect` | Cross-service design |
| `role-adversary` | Red-team assumptions |

## Product / stage → `product/`

| Skill | Slack / stage |
|---|---|
| `prd-format` | Contract every PRD skill emits or consumes |
| `prd-normalize` | "convert / reformat this PRD" |
| `prd-writer` | "write / draft a PRD" |
| `prd-analysis` | "analyse this PRD", `/groot` analyze |
| `eval-writer` | "write evals", `/groot` evals |
| `implementation` | "implement", `/groot` implement |
| `repair` | `/groot` failed tests/checks |
| `knowledge-update` | `/groot` refresh CONTRACT Current API |
| `explain-flow` | "how does X work" |
| `confidence` | `/groot` score; "why no PR" |
| `phantom-tests` | "write tests on this PR", `@phantom` |
| `phantom-pytest` | Tests **inside** Pocket-Fm/phantom repo |
| `monitoring-deploy` | Deploy, canary, TG health, 5xx, post-release |

## Still required (not skills, but the loop fails without them)

1. **Pack** — `CONTRACT.md` + `contract.json` + `features/*/overview.md`.
2. **Per-pack `CONTEXT_BUILDER.md`** and explain-flow overlays.
3. **Sherlock** for live 5xx + **monitoring-deploy** evidence pack.
4. **Human gates** — product answers, mind-update, merge.
5. **Harness** — no stage promotion without PASS evidence.

## Do not add

- A skill that invents architecture when the pack is missing.
- A second confidence formula.
- A "call Sherlock Slack bot" skill (Holmes is the HTTP API).
- A skill that invents latency or 5xx numbers without evidence.
- A role that skips `harness-response-recheck`.
- A mega-skill that replaces this folder tree.
