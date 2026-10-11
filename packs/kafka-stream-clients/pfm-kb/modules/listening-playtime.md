# Listening Playtime

## What It Is
Durable listening progress used for continue-listening and progress-gated product.

## Actors
Players/clients; critical playtime workers; MySQL/Redis progress stores.

## Client Behavior
App may ACK play events before this worker finishes; UI can briefly lag.

## Gaps
Fabric `consumer-playtime` is separate and may be incomplete — do not merge ownership.
