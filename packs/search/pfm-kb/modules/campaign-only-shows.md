# Campaign-only shows

Aliases: campaign show, restricted show, hidden campaign, AppsFlyer show

## What It Is

Some shows are only for users in a campaign. Everyone else must not see
them in search.

## User-Visible Invariants

- Non-campaign users never see a campaign-only title.
- Campaign membership can be stale for a short window — treat as a
  visibility risk, not a ranking bug.
- An incident kill switch can turn this filter off; that is ops, not a
  product default.

## Client Behavior

Server-side. Attribution failures must hide rather than leak.
