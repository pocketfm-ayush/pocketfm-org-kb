# Switch profile

Participating modules: multi-profile, library, listening-progress,
listener-profile.

## Journey

1. Logged-in listener opens the slot list on this login (max five).
2. They pick a slot. The **device binds** to that slot.
3. Library and continue-listening reload for **that** slot.
4. In India, the profile page can show that slot’s name / photo.

## User-Visible Invariants

- This is not a new login and not account-transfer.
- Primary vs extra slot still share coins and unlocks.
- Guest cannot switch slots.

## Failure modes

- Slot deleted after invite → cannot join; contact the inviter.
- At five slots → no add, switch among existing only.
- Missing bind (no slot on the device) → do not invent another
  login’s library.
