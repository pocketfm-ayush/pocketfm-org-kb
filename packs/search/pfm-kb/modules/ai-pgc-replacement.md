# AI / PGC replacement (Search)

Aliases: AI PGC, AI/PGC, AI<>PGC, PGC replacement, PGC show selection, user_tg pgc

## What It Is

Some titles exist as an AI version and a human-produced (PGC) version.
Search shows **one** of the pair for this listener.

## Actors

Listener. Marketing can pin PGC via campaign attribution (`pgc_<show>`).
CS can force a version (override). Ops can turn routing off.

## Journey

1. Results contain one or both IDs of a known pair.
2. If the listener has meaningfully played one side, that side wins
   (about three minutes). Recency breaks ties.
3. If both sides are cold, a campaign pin can force live PGC.
4. If still cold, default is PGC unless the pair is flagged to keep AI.
5. Unavailable side is not shown.

## User-Visible Invariants

- The listener should not see both members of the pair as two different
  shows in one search list.
- Playtime beats a marketing pin.
- After the swap, campaign-only / ME / override / disabled rules still apply
  to the ID that remains.
- Feed/library uses the same pair idea on Radioly — do not describe Search
  handlers when the ask is the home feed.

## Client Behavior

Decision is server-side on both cache hit and miss.

## Gaps

Which titles are paired is CMS-owned and changes. Do not hardcode show IDs.
