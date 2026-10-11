# Packs

Mirrored Groot knowledge packs from `content-knowledge-base` (no Graphify blobs).

```text
packs/
  global/           # catalog, conventions, kb-coverage, skills
  radioly/          # knowledge-base + pfm-kb + skills
  search/
  fabric/
  …
  contracts/        # thin CONTRACT.md mirrors
  manifest.yaml     # repo_id → pack folder
```

Refresh from upstream:

```bash
# from Work/Repo
rsync -a --exclude graphify --exclude graphify-out \
  content-knowledge-base/radioly/ pocketfm-org-kb/packs/radioly/
```
