# AGENTS.md — Pocket FM Org KB

You are editing the **organization-owned knowledge brain**, not application code
and not the Org Brain engine.

## Product split

| Repo | Role |
|---|---|
| `ayushgarg2702/org-kb` | Reusable engine (do not put Pocket FM secrets/indexes here) |
| **this repo** | Org config, handbook, memory, evaluation, policies |
| `Pocket-Fm/content-knowledge-base` | Groot per-pack CONTRACT / skills / pfm-kb |
| `cerebro-knowledge` | Cross-repo distilled semantics |
| `Pocket-Fm/groot` | Agent runtime that consumes packs + handbook |

## Hard rules

1. Prefer `unknown` / `uncertain` over inventing ownership or production state.
2. Every established fact needs evidence: `<repo_id>@<40-hex>:<path>#<symbol>`.
3. No secrets, tokens, `.env` values, PII, or production credentials in any file.
4. Facts do not silently merge across services — label by `repository_id`.
5. Handbook entities (`handbook/repositories/`) are the meaning SoT for Lane A.
6. Pack overlays live in content-knowledge-base; this repo only **points** via
   `packs/manifest.yaml` unless explicitly dual-homed.
7. Run `make validate` before marking a catalog repo `ready`.
8. Partial knowledge must say it is incomplete.

## When to edit what

| Ask | Edit |
|---|---|
| New service in scope | `org.yaml` + `handbook/catalog.yaml` |
| Meaning / flow / capability | `handbook/repositories/<id>/…` |
| Incident / lesson / ADR | `memory/` |
| Golden eval question | `evaluation/` |
| ACL / write power | `policies.yaml` |
| Groot pack content | `packs/<pack>/` (mirror upstream CKB) |
| Evidence after app merges | `make refresh-evidence` |
| Engine bug / connector | org-kb master |

## Non-goals

- Shipping production app code from this repo
- Claiming full understanding after one green bootstrap job
- Bypassing source evidence with model prose
