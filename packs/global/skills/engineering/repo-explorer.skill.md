---
name: repo-explorer
description: Map a repository before changing it — layout, entrypoints, ownership, hot paths.
triggers: [explore repo, map codebase, where is, find module, onboard to repo, repo structure]
intent: investigate
priority: 85
---

# 01 · Repo explorer

**Job:** build a usable mental map of the repo before plan / code / review.

## Do
1. Identify package layout, entrypoints, config, CI, and deploy manifests.
2. Find the owning module for the request (not the first filename match).
3. Note conventions already in-repo (lint, test, naming) — prefer them over invention.
4. Surface `AGENTS.md` / `CLAUDE.md` / skill pointers if present.
5. List what you still do not know (secrets, private deps, remote-only config).

## Do not
- Propose a large rewrite before locating the hot path.
- Invent services or folders that are not in the tree.
- Dump the entire file tree as the answer — summarize with paths that matter.

## Output
- Repo shape (1 short paragraph)
- Relevant paths (bullets with why)
- Suggested next skill: `planner` or `architecture` or `debugger`
