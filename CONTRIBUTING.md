# Contributing

1. Branch: `feature/<TICKET-ID>-short-name` (or `feature/kb-…` for KB-only work).
2. Prefer evidence-backed handbook edits over prose-only docs.
3. Run `make validate` before opening a PR.
4. Do not commit secrets, embeddings, or `var/` database files.
5. Pack content (CONTRACT, features, skills) belongs in
   `content-knowledge-base` — update `packs/manifest.yaml` here instead.
