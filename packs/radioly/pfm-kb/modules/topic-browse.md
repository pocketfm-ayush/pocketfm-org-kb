# Topic and tag browse

Aliases: topic page, tag page, explore topics, see all, collection

## What It Is

A **one-topic (or one-tag) list of titles**. Tap a rail, theme,
or collection and land here. Not For You. Not Discover shorts.
Not Stage.

The old Hindi “explore topics” directory is this same browse, not
a fourth tab.

## Actors

Listener (guest or logged-in). Editorial fills topics. Adult
topics on the Hindi directory stay hidden unless the login is
marked adult.

## Journey

1. Tap a topic, tag, or “see all.”
2. Server returns that list (and may remap a “new / trending”
   cluster). Disabled / hidden titles are stripped.
3. Empty or unknown topic is a miss, not an empty Home.

## User-Visible Invariants

- Do not assemble this page from Home rails.
- Do not treat it as Discover.
- Hindi explore directory: do not assume other languages.
- Explicit topics on that directory: adults only.

## Client Behavior

Needs network. Logout must not keep another person’s adult gate.

## Gaps

Whether a dedicated Explore tab still ships (vs Home / tropes /
Stage “see all”) is not recorded here.
