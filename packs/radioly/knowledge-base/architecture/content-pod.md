# Content / Experience POD — pack pointers

Hub (team, repos, APIs, SOPs):

https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/851869741/FM+-+Content+POD+Wiki

## Repos (Experience / Content POD)

| Product surface | GitHub | Groot pack / repo id |
|---|---|---|
| Radioly (FM consumer monolith) | https://github.com/Pocket-Fm/radioly_client_api | pack `radioly` · `radioly_client_api` |
| Search | https://github.com/Pocket-Fm/pocket_search | pack `search` · `pocket_search` |

Screen ↔ API map (Experience APIs + UI cues): `architecture/api-to-screen.md`
(Confluence: Content API Mapping to screens).

## Onboarding (new joiners)

https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/930152842/Onboarding+to+Pocket

Linked from that page (open in Confluence — do not invent VPN/SSH details):

- New joiner onboarding (POCKETFM space)
- High-level Radioly repository overview
- OpenVPN setup
- SSH to QA machines
- Docker for Radioly

## How Groot should use this

- Repo ambiguity between Radioly vs Search: prefer API path from
  `api-to-screen.md` (feed/content/user_api → radioly; `/v2/search/` → search).
- Screenshot / UI asks: map screen → API → feature overview, then CODE SEARCH.
- Access / VPN / Docker questions: point at the Onboarding Confluence page;
  do not invent hostnames, keys, or credentials.
