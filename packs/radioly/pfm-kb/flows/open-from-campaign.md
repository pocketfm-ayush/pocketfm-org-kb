# Open from a campaign

Participating modules: campaign-deeplinks, onboarding-first-run,
onboarding-show-pick, show-details-and-unlock.

## Journey

1. Ad / install link resolves to a show or episode, or misses.
2. If first-run screens are still due, language / name / ATT still
   run. The picker does not.
3. Show-open decides visible id, unlock, and unavailable.
4. Hit + available → start playback. Hidden / suppressed →
   unavailable on the show page, not a silent Home.

## User-Visible Invariants

- Resolve success is not “this title is allowed on Home.”
- Picker skip is not first-run skip.

## Failure modes

- Unmapped campaign → no destination. Do not invent a title.
- Show-open miss / unavailable → deleted-style or lock UX. Do not
  replay the campaign resolver.
- Attribution miss on first-run → normal picker / Home. Do not
  block launch.
