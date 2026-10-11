# Show to player

## Journey
1. Listener opens show details and picks an episode.
2. Unlock/paywall may interrupt via payments/orchestrator.
3. Player service starts; mini/expanded UI and media session update.

## Modules
- [show-details](../modules/show-details.md)
- [payments-and-premium](../modules/payments-and-premium.md)
- [orchestrator](../modules/orchestrator.md)
- [player](../modules/player.md)

## Failure modes
- Unlock succeeds server-side but UI not refreshed.
- Background playback fails if media session/service miswired.
