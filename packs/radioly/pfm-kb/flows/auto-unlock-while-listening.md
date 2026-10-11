# Auto-unlock while listening

Participating modules: auto-debit, show-details-and-unlock,
coins-wallet, paywall, rewarded-ads.

## Journey

1. Listener has auto-unlock on for this series (player, show
   page, or manage). Some audiobook-path titles stay on even if
   they turned it off.
2. They listen into a locked episode. If the toggle is on and
   the wallet can cover it, coins spend and the pack opens
   **without a fresh paywall tap**. Same durable unlock as
   show-open.
3. Coin history can label that spend Auto-unlocked.
4. Daily unlock still runs for the day. Auto-unlock must not
   skip it.
5. If the toggle is off, or coins are short: stop and show the
   lock sheet (pay and, if offered, watch-to-unlock). Do not
   play the locked episode.
6. After a successful coin pay, a prompt to turn this on is not
   the unlock-confirmation sheet.
7. Next-up / autoplay can stop if they cannot keep unlocking
   (off, or not enough coins). That is not a playlist bug.

## User-Visible Invariants

- This is not subscription auto-renew.
- On/off is account-wide for that series, not per profile.
- This experience does not flip the toggle off each day.
- Empty manage list is “none / not in this experience,” not an
  error.

## Failure modes

- Spend / unlock miss → episode stays locked; show the sheet.
  Do not play through.
- Not enough coins → “add coins” / paywall, not a silent skip.
- Guest / ineligible manage → empty list, not a broken settings
  page.
