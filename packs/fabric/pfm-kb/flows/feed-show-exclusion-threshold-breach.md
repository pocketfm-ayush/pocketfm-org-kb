# Feed show exclusion threshold breach

## Journey
1. Listening playtime events reach the feed-show-exclusion consumer.
2. Service compares accumulated playtime to configured thresholds.
3. On breach, Content client applies show exclusion for the user.
4. Subsequent feed assemblies hide or demote that show.

## Modules
- [playtime-tracking](../modules/playtime-tracking.md)
- [feed-show-exclusion](../modules/feed-show-exclusion.md)
- [playtime-content-client](../modules/playtime-content-client.md)

## Failure modes
- Threshold misconfig excludes too aggressively.
- Content API failure leaves user still seeing the show.
