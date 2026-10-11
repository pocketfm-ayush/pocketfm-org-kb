# Comments and reviews

Aliases: show reviews, episode comments, comment thread, my reviews

## What It Is

Talk on a **series** (review + optional 1–5 stars) or an **episode**
(comment and replies). Not Community posts. Shorts comments are
Discover. The show-page “NOTE FROM THE WRITER” is writer-notes, not
a review. The creator note that can lead the review list is this
product.

## Actors

Logged-in listener to post, edit, delete, or report. Anyone can read.
Creators can pin. Novels use the same product (book review / chapter
comment).

## Journey

1. Show page: a few reviews. Full list: Top or Recent.
2. First page can lead with creator note, pinned, top, and **your**
   review — those must not repeat further down.
3. Post or reply. A second series review **updates** the first; it
   does not add another.
4. Delete is hide, not erase. Report: enough reports hide it.

## User-Visible Invariants

- Comments belong to the login, not an id the app stuffed in.
- “My reviews” is this login only. An author’s “reviews received”
  on their profile is writer-profile, not “my reviews.”
- Replies are not extra series reviews.
- Links / spam text are rejected before save.
- Shorts must not use this list.

## Client Behavior

Read needs network. Post / delete need a login. Logout must not keep
another person’s draft or “my reviews.”

## Security / PII / Compliance

Threads are public. Display name and avatar show. Treat reports as
moderation, not a private inbox.

## Gaps

Which titles get hashtag filters, live Top vs relevance order, and
the exact report count to hide are not recorded here.
