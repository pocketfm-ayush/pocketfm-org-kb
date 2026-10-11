# Experience Search API ↔ app screen

Cross-link from Radioly’s Experience map (screenshots live in Confluence):

https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/930251078/Content+API+Mapping+to+screens

Full multi-screen table (Radioly + Search): `radioly/knowledge-base/architecture/api-to-screen.md`.

| Screen (UI cue) | Primary API | Pack feature | Service |
|---|---|---|---|
| Universal search results (typed query) | `GET /v2/search/universal.search` | `universal-search` | pocket_search |
| Search v3 entry (same product family) | `UniversalSearchV3View` / v3 search | `universal-search` | pocket_search |

**Security:** Never copy JWTs / uids from Confluence curls into answers.

When a screenshot shows a search results list / search chrome, prefer this pack
over Radioly feed APIs.
