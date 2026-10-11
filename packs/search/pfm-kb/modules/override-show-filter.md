# Override show filter

Aliases: CS override, manual override, hide alternate, preferred version

## What It Is

If CS (or the user path that writes overrides) pins one member of a pair,
search hides the other member.

## User-Visible Invariants

- Override is stronger than algorithmic AI/PGC pick, except when routing
  is fully killed.
- Wrong pair map → user sees the version they were told they would not.
