---
id: service.litefm-backend
type: service
repository: litefm-backend
status: established
evidence:
  - litefm-backend@a7c87f0e5259b4a08c395322b4a88d6d02d11852:radioly_api/urls.py#urlpatterns
  - litefm-backend@a7c87f0e5259b4a08c395322b4a88d6d02d11852:v2/feed_api/views.py#get_player_feed
---

LiteFM Django backend (feed, payments, experiments). Parallel product surface
to radioly_client_api — confirm which app traffic you are debugging. First stop
for LiteFM autoplay screen bugs (0 plays / 0.0 rating on autoplay) via
`get_player_feed`.
