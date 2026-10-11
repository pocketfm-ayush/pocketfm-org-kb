# fabric source folder map

| Folder | Product meaning |
|---|---|
| `impression/server` | Kafka consumer writing impression counts |
| `impression/clientgo` | Go query SDK |
| `impression/clientpy` | Python query SDK |
| `playtime/` | Playtime Kafka consumers (modes) |
| `playtime/feedshowexclusion` | Threshold → Content exclusion |
| `playtime/aipgcsync` | AI↔PGC progress sync |
| `playtime/audioplaytime` | Core ingest mode (verify completeness) |
| `playtime/externalservices` | Content client for exclusion |
| `temporal-namespaces/` | Declarative Temporal namespace ops config |
| `infra/` | Local/dev dependencies |

Query graph before inventing ownership. Temporal *workflows* are not authored here.
