# Impression event to count query

## Journey
1. App/Relay emits GTM or ADS impression events onto Kafka.
2. Impression consumer whitelist-gates GTM assets and writes Scylla buckets.
3. Product services query counts via Go or Python clients.
4. Callers apply frequency caps / experiment logic.

## Modules
- [impression-ingest](../modules/impression-ingest.md)
- [gtm-asset-whitelist](../modules/gtm-asset-whitelist.md)
- [ads-impression-counts](../modules/ads-impression-counts.md)
- [impression-counts](../modules/impression-counts.md)
- [impression-go-client](../modules/impression-go-client.md)
- [impression-python-client](../modules/impression-python-client.md)

## Failure modes
- Asset not whitelisted → no counts → caps never fire.
- Callers bypass clients and hit wrong tables/scopes.
