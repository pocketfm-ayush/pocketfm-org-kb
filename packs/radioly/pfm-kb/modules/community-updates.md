# Community and profile updates

Aliases: community feed, updates feed, profile feed, community posts

## What It Is

A **posts** feed: follows, titles, and episodes people share. Not Home
and not Library.

Community is this listener’s updates (with some trending mixed in).
Profile is **that person’s** posts.

## Actors

Listener. Profile view can be another account’s public posts.

## Journey

1. App opens Community or a profile.
2. Server pages that person’s posts.
3. Community may mix a few trending posts into the middle.

## User-Visible Invariants

- This is not For You and not “my shows.”
- Profile is the viewed account’s posts, not the viewer’s Home.
- Phone numbers must not appear on people cards.

## Security / PII / Compliance

Strip phone numbers from people shown on a post. Treat profile as
public activity, not a private library.

## Client Behavior

Needs network. Empty is a quiet community, not a failed Home.
