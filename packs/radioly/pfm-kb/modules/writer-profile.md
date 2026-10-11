# Writer profile

Aliases: author profile, my creations, author reviews, community links,
profile revamp, Studio profile

## What It Is

The **writer’s person page**: live titles, reviews those titles got,
and (when they are a writer) social links and a completion bar.

Not the listener person page (listener-profile). Not Stage. Not
“my reviews” (that is comments-and-reviews — reviews **this login**
wrote).

## Actors

Anyone can open a writer. Only that writer can edit links, bio, or
photo. A login is a writer here only if they have at least one
originals title.

## Journey

1. Open the person. Writer card only if they have a live original.
2. Viewer: name, photo, bio, social links, achievements, titles,
   reviews on those titles.
3. Owner: same, plus a completion bar (name, photo, links, bio)
   and edit.
4. Titles: live originals, plays, rating. Reviews: received on
   those titles, not the owner’s own reviews of other series.

## User-Visible Invariants

- You cannot edit another writer’s links or bio by sending their id.
- Allowed link types are server-listed (Instagram, Facebook, Discord,
  WhatsApp, YouTube, LinkedIn, X, custom). Do not invent a type.
- Empty titles / reviews is a quiet writer, not a failed Home.
- This is not Stage and not the listener profile.

## Client Behavior

Needs network. Logout must not keep another person’s completion bar
or link editor.

## Security / PII / Compliance

**Sensitive.** Name, photo, bio, social handles. Treat as a public
writer card, not a private library.

## Gaps

- Live achievement list and which vintages show the completion bar.
- Whether a listener with no originals can still see a stub card.
