# Shared home rails (freshness)

Aliases: default feed cache, default home feed, shared rails, editorial feed

## What It Is

Popular / Top Picks / genre rails are built for a **cohort** (language,
locale, app vintage, replica generation) and reused. They are not a
per-user Home blob.

## User-Visible Invariants

- Two listeners in the same cohort can share those rails and still see
  different continue/personalized rows.
- Changing what a shared rail contains will show up for the whole cohort
  after the freshness window — not for one uid.
- Do not debug “wrong show on Home” as a per-user cache until personalized
  rails and visibility filters are ruled out.

## Client Behavior

Warm shared rails make Home feel faster. Stale shared rails mean many
users see the same outdated editorial row.

## Gaps

Exact freshness window length is operational and not recorded here.
