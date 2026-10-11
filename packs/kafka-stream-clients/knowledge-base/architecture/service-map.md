# Kafka workers — service map

Three K8s deploy pipelines (see source `workers-kafka-*.sh`):

| Pipeline | Product role | Twin families |
|---|---|---|
| critical | Audio listening playtime | listening-playtime |
| consumer | Ads, S2S, experience, unlocks, referrals, … | most domain twins |
| db-s3 | Coins, feed/last-active dumps, deactivation, user-actions | wallet-coins-and-recon, feeds-packaged-deployment, account-actions-and-deactivation |

Producers: Radioly APIs, clients, payment gateways, ad networks.
Consumers: durable state for progress, wallet, unlocks, attribution, CRM.

Pair with `radioly` (request-time), `fabric` (platform impression/playtime),
`go-radioly-service` (Relay exporters), `airflow` (scheduled/Temporal).
