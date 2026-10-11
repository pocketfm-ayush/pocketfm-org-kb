---
id: flow.groot-load-pack
type: flow
repository: groot
status: established
evidence:
  - groot@539d39a80ceb0cc44a1dd429f064b22629be253f:groot/knowledge/loader.py#load_pack
  - groot@539d39a80ceb0cc44a1dd429f064b22629be253f:groot/knowledge/sync.py#ensure_knowledge_base
---

# Load knowledge pack

Resolve `repo_id` → one folder under `KNOWLEDGE_BASE_ROOT`, read
`knowledge-base/CONTRACT.md` + `contract.json`, features, and skills.
Missing pack blocks the run — engine must not invent architecture.
