# In-player ads

Aliases: mid-roll, instream, player audio ad, first-party player clip, boundary audio, virtual voice ahead, disclaimer ad

## What It Is

Audio or video that interrupts the episode. One player ask, two kinds of fill:

1. **First-party clips** — Pocket’s own audio: AI-voice warning, explicit-content disclaimer, show-to-show bridge, paywall/trial nudge, ad-free expiry reminder, and similar.
2. **Network mid-roll** — only if no first-party clip won. Video while the app is in the foreground; audio while it is in the background.

Listeners never see an “internal ad manager.” They hear whichever clip won.

## Actors

Listener in the player. The server picks at most one clip per ask.

## Journey

1. Player asks what should play on this episode (foreground/background included).
2. A first-party clip is chosen if one is eligible.
3. Otherwise a network mid-roll is considered.
4. The app reports that the clip actually played. That report starts the quiet period.

## User-Visible Invariants

- First-party wins over network. Do not play both on one ask.
- **AI-voice warning (“Virtual Voice Ahead”)** plays on the last human-voice episode before an AI episode. Not skippable. Uses the current show’s art, not a generic ad still. Hindi listeners get Hindi then English; everyone else English. A second warning can play three episodes earlier. This is a content warning, not a sale. Subscribers and ad-free still hear it.
- **Explicit-content disclaimer** plays when that episode is flagged. Legal — subscribers and ad-free still hear it.
- Show-to-show bridge audio and the ad-free expiry reminder can still play for subscribers and ad-free. Other promotional first-party clips do not.
- Disney titles and subscription-exclusive titles do not get regular player ads; they have their own catalog clips.
- Episode 1: no promotional first-party clip (bridge onto a chain title is the exception).
- Network mid-roll is off for subscribers, ad-free, first-week accounts, GDPR-new accounts, and episodes already opened by watch-to-unlock or coins. Video is not for background listen; audio is not for foreground.
- Some free-app tests return no player ad at all.

## Client Behavior

Needs network at the episode boundary. Must send whether the app is in the foreground — that switches video vs audio. Must report a play; offering a clip without a play report does not start the quiet period.

## Event Meaning

The play report is what counts toward frequency and cooldown. “We were eligible” is not a play.

## Gaps

Which first-party nudge is live (paywall vs trial vs recap vs daily-show “come back tomorrow”) is campaign/test state — not here.
