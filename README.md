# Pocket FM Org KB

**Organization-owned knowledge brain for Pocket FM.**

This is the **org KB instance** (config, memory, handbook, evaluation, policies).
It is not the Org Brain engine — that lives in
[`ayushgarg2702/org-kb`](https://github.com/ayushgarg2702/org-kb).

```text
org-kb (engine) ──init/bootstrap──▶ pocketfm-org-kb (this repo)
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    ▼                      ▼                      ▼
           content-knowledge-base    cerebro-knowledge         live ops
           (Groot packs / skills)    (cross-repo graph)     (Sherlock/MCP)
```

## Why this repo exists

| Layer | Repo | Answers |
|---|---|---|
| **Engine** | `org-kb` | How to ingest, index, query, evaluate |
| **Org instance (this)** | `pocketfm-org-kb` | Which repos, policies, memory, golden Qs, handbook SoT |
| **Agent packs** | `content-knowledge-base` | Per-service CONTRACT / features / skills for Groot |
| **Cross-repo semantics** | `cerebro-knowledge` | Interfaces, events, multi-service relationships |
| **Agent runtime** | `groot` | Slack / Deep Agents / locate / tools |

Today those layers are split. This repo is the **single org control plane**:
what is in scope, what is trusted, what we remember, and how we measure quality.

## Quick start

```bash
# 1. Clone
git clone https://github.com/ayushgarg2702/pocketfm-org-kb.git
cd pocketfm-org-kb

# 2. Point Org Brain at this instance (engine installed separately)
export ORG_BRAIN_INSTANCE="$(pwd)"
export ORG_BRAIN_DATABASE_URL="${ORG_BRAIN_DATABASE_URL:-sqlite+pysqlite:///./var/orgbrain.db}"

# 3. Validate handbook + config
make validate

# 4. When org-kb engine is available:
#    org-brain preflight && org-brain bootstrap && org-brain query "…"
```

## Layout

```text
pocketfm-org-kb/
├── org.yaml                 # org id, sources, indexing, query budgets
├── policies.yaml            # ACL profiles
├── connectors/              # connector enablement
├── handbook/                # meaning + evidence (Lane A SoT)
│   ├── SCHEMA.md
│   ├── catalog.yaml
│   └── repositories/        # per-repo entity markdown
├── memory/                  # human/ops durable memory
│   ├── incidents/
│   ├── decisions/
│   └── lessons/
├── packs/                   # pointers + sync contract to Groot packs
├── evaluation/              # golden questions + baselines
├── schemas/                 # entity / evidence contracts
├── docs/                    # architecture, layers, gap plan
└── scripts/                 # validate, sync helpers
```

## Design principles (from Org Brain)

1. Never equate plausible inference with verified fact.
2. Every material claim needs an evidence pointer (`repo@sha:path#symbol`).
3. Permissions enforced at query time; secrets never indexed.
4. Partial maps must be labeled incomplete.
5. Retrieve the smallest sufficient evidence set.

## Related

- Engine: https://github.com/ayushgarg2702/org-kb
- Groot packs: https://github.com/Pocket-Fm/content-knowledge-base
- Cerebro: https://github.com/Pocket-Fm/cerebro-knowledge (or local checkout)
- Groot: https://github.com/Pocket-Fm/groot
