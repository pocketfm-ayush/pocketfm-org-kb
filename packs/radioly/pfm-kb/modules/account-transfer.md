# Account transfer

Aliases: account merge, move account, old account to new account

## What It Is

An **internal** merge: listening and unlocks on one account are moved
onto another. This is **not** the login “Forgot account?” form (that is
account-recovery) and **not** a listener settings screen.

## Actors

Ops / authenticated internal caller. Two account identities: source and
destination.

## Journey

1. Caller names the old account and the new account.
2. Full merge: start a transfer and record it as initiated.
3. Unlocks-only retry: re-run show unlocks for a pair that already
   transferred; no new transfer record.
4. Status for that pair: initiated, processing, success, or failed.

## User-Visible Invariants

- The listener does not pick “merge” in the app. If they see library or
  unlocks appear after a login change, that is the result — not this
  screen.
- Do not treat a client-supplied “move their id to mine” as a consumer
  feature.

## Security / PII / Compliance

**Sensitive.** Both account ids are identifiers. A hostile pair is
account takeover.

- Requires a server-authenticated internal caller. Reject an
  unauthenticated pair.
- Full merge and unlocks-only retry both move account-scoped listening
  and unlocks. Treat as high-risk.
- Do not invent retention, legal basis, or who may request a merge.

## Client Behavior

Not a consumer fetch. If a merge is in flight, library and unlocks on
the new login may still look empty until status is success.

## Gaps

- Which listener journey (login, support, device switch) starts a merge.
- What copy, if any, the listener sees while it runs or fails.
