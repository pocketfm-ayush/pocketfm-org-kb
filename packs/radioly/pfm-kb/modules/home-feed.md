# Home feed

Aliases: home feed, get feed, For You, homepage, home rails

## What It Is

The first screen after launch: a stack of rails (continue, popular, editorial,
and experiment rows). The app asks the server; it does not assemble Home
from a local catalog.

v2 and v3 home URLs are the same product. Do not treat them as two homes.

## Actors

Listener (guest or logged-in). CMS/editorial for default rails. Experiments
may add or replace rails for already-enrolled users.

## Journey

1. App opens Home (or For You).
2. Server builds personalized rails, then shared editorial rails, then
   visibility rules (disabled, campaign-only, AI/PGC, device art).
3. Some locales get a UGC-row home and return that stack instead.
4. A genre-chip tap is a different stack — only if the listener is already
   in that test. Everyone else stays on For You. Home does not newly enroll
   launch-only tests.

## User-Visible Invariants

- Home is not one private snapshot per user. Editorial rails are shared
  among listeners in the same language/locale/app vintage.
- A title the user must not see (disabled, campaign-only, losing AI/PGC
  side) must not remain on a rail after assembly.
- Genre Home is not the default For You.

## Client Behavior

Needs network. Feels instant when shared rails are already warm. Logout
does not keep another person’s personalized rails.

## Gaps

Exact rail order and which experiment is live now are not recorded here.

## Related campaign injects

LiveOps tentpole may inject billboards/modules/banners on home for enrolled
devices. Start Writer module may CTA into Stage/Studio write navigation.
See [liveops-tentpole](liveops-tentpole.md) and [stage](stage.md).
