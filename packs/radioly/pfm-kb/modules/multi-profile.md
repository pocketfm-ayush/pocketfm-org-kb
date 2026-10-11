# Multi-profile

Aliases: family profile, extra profile, share profile, add profile

## What It Is

Extra **slots on one login** so family or friends can listen with
shared unlocks and coins. Not a second account, not account-transfer,
not the public profile page (listener-profile / community-updates).

## Actors

Primary listener on the login (creates and invites). Invitee joins
with a code the primary shares. Age on a new slot must be 13 or above.

## Journey

1. Primary opens add-profile (library, episode list, after a coin
   buy, or an app prompt). Cap is **five** slots.
2. They name the slot and give the primary phone or email. A code is
   created (valid **48 hours**).
3. They share the code / link. Invitee enters it and joins **this**
   login’s slot — or they can start / keep their own account instead.
4. Switching: the device is bound to one slot. Library and progress
   follow that slot (same rule those modules already use).
5. Primary can remove a slot (soft). A deleted slot cannot be joined;
   invitee is told to contact the inviter.

## User-Visible Invariants

- Five slots including the primary. At the cap, do not offer add.
- Shared: unlocks, coins, saved pay methods. Per slot: name, photo,
  language, list, and listen history (product FAQ).
- Listen / download on **five devices** at once is the stated benefit.
- The 48-hour invite code is not the account-login code.
- You cannot edit or delete another login’s slot.
- Create / edit rejects age under 13 (“13 or above”).
- Invited-profile verify can be refused as “limited users” (seen on
  US Android). Do not invent iOS availability — FAQ copy has said
  Android-only.

## Client Behavior

Needs network and the primary login to create. Invitee needs the
shared code. Device bind is what makes a switch stick.

## Security / PII / Compliance

**Sensitive.** Primary phone or email, invite code, slot name, age /
date of birth, gender, photo.

- Shared wallet and pay methods across slots is account takeover if
  the invite is leaked.
- Do not invent COPPA / legal meaning beyond the 13+ gate and the
  policy checkbox the create screen is given.
- Do not log invite codes.

## Event Meaning

Purchase-success “add profile” is an offer to create a slot, not a
completed invite.

## Gaps

- Whether iOS can create or join now (FAQ vs later work).
- Whether coins spent by an invitee debit the primary in every market.
