# Home visibility filters

Aliases: disabled shows, hidden shows, campaign-only, campaign PGC

## What It Is

After Home (or UGC-row Home) is assembled, titles the listener must not
see are stripped: system/user-disabled, and campaign-only titles for
people not in that campaign.

## User-Visible Invariants

- These run **after** rails are built. Filtering only the candidate pool
  is not enough if a later stitch puts the title back.
- Campaign-only is “not in the campaign → invisible,” not a ranking tweak.
- Device-specific cover art is a stamp after this, not a visibility rule.

## Client Behavior

Server-side. The app should not re-add stripped ids from a local cache.
