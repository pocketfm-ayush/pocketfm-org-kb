# PPV testing (catalog)

Aliases: PPV test, pay-per-view test, LDAU cap, feed exclusion

## What It Is

How CMS decides whether a title should become paid / PPV — **not** the
listener checkout. A title in test can disappear from Home after enough
unique listeners.

Do not confuse this with a PPV subscription pass (unproven here).

## Actors

CMS / catalog ops start or pause a test. Listeners only see the title
appear or vanish. Home assembly then hides a breached title.

## Journey

1. A title is put into a test phase (UGC steps or PGC length buckets).
2. Unique listeners are counted toward a cap the test already set.
3. When the cap is hit, the title is pulled from Home modules that
   honor the exclusion. That is not a Home cache bug.
4. Starting a new test pauses the old one. Re-testing the same title
   is capped and cooled down.

## User-Visible Invariants

- This is not “the listener bought PPV.”
- A vanished test title must stay off Home; do not stitch it back
  from a local catalog.
- Complements visibility-filters (disabled / campaign-only). This
  hide is “this test hit its listener cap.”

## Client Behavior

Server-side. The app should not re-add a stripped id.

## Gaps

Listener-facing meaning of a PPV *pass* (versus this catalog test) is
not proven in this scan.
