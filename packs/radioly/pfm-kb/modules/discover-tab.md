# Discover tab

Aliases: Discover, shorts, reels, discover feed

## What It Is

A tab of short video promos for series — not Home. The server builds
the stack. English, Hindi, and German only.

## Actors

Listener (guest or logged-in). Editorial / LiveOps can inject a brand
clip. A shared short can pin to the top.

## Journey

1. App opens Discover, or the server sets Discover as the first tab.
2. First session today: default-land only if the campaign primary title
   is far enough along, or the listener has no heavily listened title.
3. A new or reinstalled device in the first 7 days can still open
   Discover, but must not default-land there.
4. At most one default-land per day across every nudge. Each nudge also
   has a 7-day cap.
5. Client nudges (priority order): scroll past next-series on the
   player, “discover more” in Library, expand a Home module, tap Search.
6. Feed: personalized recs (when present) own the top and suppress
   share-pin / onboarding seed / LiveOps. Else onboarding genres, then
   LiveOps, then a shared short can pin first.
7. Disabled, campaign-only, and losing AI/PGC titles are stripped.

## User-Visible Invariants

- Discover is not For You. Do not assemble it from Home rails.
- First week on a new or reinstalled device: tab visible, default-land
  forced to Home.
- A shared promo the listener must not see (disabled / hidden type)
  must not pin.
- Comments belong to the login, not an id the app stuffed in. Deletes
  are soft. Spam is rejected before save.

## Client Behavior

Needs network. Logout must not keep another person’s stack or likes.

## Gaps

Which personalized-rec test is live, rail/nudge order beyond the
client-nudge list, and social on/off by vintage are not recorded here.
