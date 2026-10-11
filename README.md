# Pocket FM Org KB

**Organization-owned knowledge brain for Pocket FM** — handbook, Groot packs,
Cerebro peer maps, memory, evaluation, and Org Brain phase 7–8 instance config.

Engine (not this repo): [`ayushgarg2702/org-kb`](https://github.com/ayushgarg2702/org-kb).

## What’s in here

| Path | Contents |
|---|---|
| `handbook/` | Lane A SoT — **217** entities from CKB org-handbook; evidence SHAs refreshed from local clones |
| `packs/` | Full Groot packs (CONTRACT, features, pfm-kb, skills) for 10 services + `global/` |
| `peers/cerebro/` | Domain resource YAMLs from cerebro-knowledge |
| `memory/` | Incidents / ADRs / lessons |
| `evaluation/` | Golden questions + Cerebro P0/correctness suites + evidence refresh report |
| `org.yaml` | Full P0–P3 source inventory (matches handbook catalog) |
| `docs/PHASE_7_CONNECTORS.md` | Connectors + MCP |
| `docs/PHASE_8_PRODUCTION.md` | Security + ops acceptance |

## Quick start

```bash
pip install -r requirements-dev.txt
make validate
make refresh-evidence   # after git pull on app repos
```

## Trust ranking

1. Source at pinned SHA  
2. Handbook entity with evidence  
3. Pack CONTRACT / features / pfm-kb  
4. Cerebro resources  
5. Memory notes  
6. Live ops (Sherlock) — ephemeral  

## Sync sources

- Upstream handbook/packs: `../content-knowledge-base`
- Upstream cerebro resources: `../cerebro-knowledge/resources`
- App code for SHA refresh: sibling clones under `../`

## Related

- https://github.com/ayushgarg2702/org-kb  
- https://github.com/Pocket-Fm/content-knowledge-base  
- https://github.com/Pocket-Fm/groot  
