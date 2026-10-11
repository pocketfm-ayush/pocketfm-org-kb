# Writer notes

Aliases: note from the writer, UGC notes, show note, episode note

## What It Is

A **writer note on an originals title** (series and/or episode).
Label: “NOTE FROM THE WRITER.” Starts collapsed. Listeners can
react. Not a review, not a Community post, not the creator note
that leads a review thread (comments-and-reviews).

## Actors

Anyone can read when the note is on. Logged-in listeners react.
Writers publish or hide from Studio — not from the listener show
page.

## Journey

1. Open an originals title. If notes are on for this app and this
   listener, the series note and per-episode notes load with the
   page.
2. Expand / collapse. React (thumbs, heart, 100, fire).
3. No note, or notes off → omit the block. Do not invent a blank
   “notes failed” state.

## User-Visible Invariants

- One note per series or episode. A second publish does not stack.
- Only originals titles. Studio / PGC titles must not grow a note.
- Not every originals title or vintage shows notes. Off is silent.
- Reactions belong to the login. Guests read; they do not react.
- Do not mix this with the review-thread creator note.

## Client Behavior

Needs network. Logout must not keep another person’s selected
reaction.

## Gaps

Which originals titles and vintages have notes on is live / test
state — not here.
