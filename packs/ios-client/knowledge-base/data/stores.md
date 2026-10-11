# ios-client local stores

| Store | Role |
|---|---|
| AppState path arrays | Navigation stack / modal routes |
| PocketDB / Realm (Data layer) | Local persistence where used |
| Downloads on device | Offline episode packs |
| UserDefaults / keyed caches | Client flags and small state |

Server catalogs, wallet balances, and entitlements are backend-owned.
Decoding belongs in DataTransferService — never in ViewModels.
