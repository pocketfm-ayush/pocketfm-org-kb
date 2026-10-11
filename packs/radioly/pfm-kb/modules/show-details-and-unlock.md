# Show open and episode unlock

Aliases: show details, show page, unlock episodes, locked episode, how many free

## What It Is

Opening a title: which show to play (region, pair, hidden), how far the
listener already is, and how many episodes are open right now.

## Actors

Listener. Subscription / VIP / campaign / battle-pass can raise the open
count. Daily unlock can add more once per day.

## Journey

1. App opens the show.
2. Server picks the visible ID (hidden and pair rules apply).
3. If the title has an AI/PGC counterpart, progress on both is compared;
   the listener keeps the side they are further into.
4. Open-episode count is computed and stored as durable unlock state.
5. Daily unlock skips a second write if it already ran today.
6. Each episode is marked locked or open for the player.

## User-Visible Invariants

- Unlock count is not a short-lived Home cache. Losing it looks like
  “I lost my episodes.”
- Apps do not call unlock themselves; show-open does.
- Moving AI → PGC must not reset progress (migration copies the count).
- Novels / books are this same unlock product (chapters). Do not
  build a second novel paywall.
- A novel’s open-count is not the associated audio title’s
  open-count. Do not copy one onto the other.
- Some novels (and some audiobooks) also offer a full-title coin
  price. That is still this unlock, not a new store.

## Client Behavior

Needs network. Locked episodes fail visibly and should open paywall, not
play silently.

## Gaps

Which experiment currently changes lock points is live state — not here.

## Related labels and promos

Unlocking byline may label *how* an episode unlocks without changing counts
([unlocking-byline](unlocking-byline.md)). Episode Zero (LiveOps sibling) may
prepend promo assets for eligible low-playtime listeners
([liveops-tentpole](liveops-tentpole.md)).
