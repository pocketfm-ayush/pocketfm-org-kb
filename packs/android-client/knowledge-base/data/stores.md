# android-client local stores

| Store | Role |
|---|---|
| SharedPreferences / DataStore via PreferenceKeys | Device flags, session-ish client state |
| Room / database modules | Offline/local persistence where used |
| Media downloads | Offline episode packs (player/download ownership) |
| In-memory MVI state | Screen state — not product source of truth |

Server catalogs, wallet balances, and entitlements are backend-owned (Radioly/payments).
Reuse PreferenceKeys — do not invent parallel key constants.
