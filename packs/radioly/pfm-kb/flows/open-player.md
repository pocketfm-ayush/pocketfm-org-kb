# Open the player

Participating modules: show-details-and-unlock, player-chrome,
character-cards, show-ai-recap, episode-recap, in-player-ads,
banners, launch-overlays, auto-debit.

## Journey

1. Show-open (open-show) has already picked the visible title and
   open-episode count. This flow is chrome and what plays around
   the episode — not a second unlock compute.
2. Player asks for chrome: speeds, sleep timer, tabs, comments,
   background-play. Some reel titles restrict background play.
3. If the title has a published character sheet, icons can show.
   That is not the show-page chat bubble.
4. Separate asks, do not fold them:
   - Show AI recap (skippable daily / saga) before the next
     episode, if they are in that test.
   - Per-episode recap card, only if they ask for that episode’s
     recap.
   - In-player ad at the episode boundary (first-party clip, else
     network mid-roll).
5. Player promo strip is banners (server-picked for the player
   screen). Not chrome.
6. Player-open may show one overlay (often auto-unlock
   onboarding). Minimise may show one (often the survey). Same
   overlay picker as launch — one winner per surface; which
   campaign is a gap.

## User-Visible Invariants

- Show AI recap ≠ episode recap card ≠ first-party player clip.
- Missing recap audio is not an error sheet — continue into the
  episode. Missing episode-recap card is a visible miss if they
  asked for that card.
- First-party player clip wins over network mid-roll on one ask.
  Virtual Voice Ahead and explicit disclaimer still play for
  subscribers and ad-free.
- Do not invent whether recap or the player clip plays first.
  Those are separate asks.
- Empty character icons are normal when CMS has no sheet.

## Failure modes

- Chrome miss → do not invent tabs, speeds, or “background play
  is fine.”
- Ad miss → play the episode; do not invent a mid-roll.
- Overlay miss on player-open / minimise → no popup. Do not
  reuse a Home overlay.
