# Experience API ↔ app screen map

Source of truth (screenshots live in Confluence — do **not** paste curls/tokens
from that page into answers):

https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/930251078/Content+API+Mapping+to+screens

Purpose: when a Slack ask includes a **screenshot / UI description / screen
name**, map it to the Radioly (or Search) path, then open the matching
`features/*/overview.md` + `pfm-kb` module. Never invent endpoints missing here
or from CODE SEARCH.

**Security:** Confluence curls contain live JWTs / uids / device ids. This pack
stores **paths + query shape only**. Never echo auth headers, tokens, or real
uids from that page.

## How to use (Groot)

1. Identify the screen from the image or words (bottom tabs, Explore/Home,
   show page, library history, profile, onboarding, login, multi-profile,
   search results).
2. Pick the primary API row below.
3. Load the linked feature / product module.
4. CODE SEARCH that path / dotted name in `radioly_client_api` (or
   `pocket_search` for universal search).
5. For debug/implement: cite screen → API → symbol. If the screenshot is
   ambiguous, ask which tab/surface before coding.

## Screen → API

| Screen (UI cue) | Primary API | Notable query / body | Pack feature | Product module | Service |
|---|---|---|---|---|---|
| App shell / bottom tabs | `GET /v2/user_api/user.get_app_tabs` | — | (tabs shell; see Discover/home) | `discover-tab`, `home-feed` | radioly |
| Explore / Home feed | `GET /v2/feed_api/get_feed_data` | `api_type=explore_v2`, `selected_language`, `onb_selected` | `home-feed`, `default-feed-cache`, `discover-tab` | `home-feed`, `default-feed-freshness` | radioly |
| Show details | `GET /v2/content_api/show.get_details` | `show_id`, `resolution` | `show-details-unlock` | `show-details-and-unlock` | radioly |
| Show episode list | `GET /v2/content_api/show.get_episodes` | `show_id`, `curr_ptr` | `show-details-unlock` | `show-details-and-unlock` | radioly |
| Subscribe / library action | `POST /v2/user_api/user_action.update` | body: `action`, `entity_id`, `action_on` (e.g. subscribe show) | `library` | `library` | radioly |
| Library (History tab) | `GET /v2/feed_api/get_library_feed` | `tab_id=history`, `sort_id=recent_activity`, `curr_ptr` | `library`, `user-show-history` | `library`, `user-show-history` | radioly |
| Profile details | `GET /v2/user_api/user.get_profile_details` | `profile_uid`, `info_level=max` | `listener-profile` | `listener-profile` | radioly |
| Profile update | `POST /v2/user_api/user.update` | profile fields | `listener-profile` | `listener-profile` | radioly |
| Show-page reco modules | `GET /v2/feed_api/get_show_feed` | `show_id`, `entity_type=show`, `required_module=reco`, `currPtr` | `home-feed`, `show-details-unlock` | `home-feed`, `show-details-and-unlock` | radioly |
| Onboarding states | `GET /v2/user_api/user.onb_states` | `skip_ad_group_onb`, `variant_id` | `onboarding-first-run` | `onboarding-first-run` | radioly |
| Onboarding show pick | `GET /v2/feed_api/get_onb_show_selection_feed` | — | `onboarding-show-pick` | `onboarding-show-pick` | radioly |
| Login states / auth gate | `GET /v2/user_api/user.login_states` | `locale` | `otp-login` | `otp-login` | radioly |
| Login | `POST /v2/user_api/user.login` | phone / OTP style body | `otp-login` | `otp-login` | radioly |
| Auth token mint | `GET /v2/user_api/user.get_authentication_token` | device / app version headers | `otp-login` | `otp-login` | radioly |
| Multi-profile benefits | `GET /v2/user_api/profile_benefits` | `source=create_profile` or `profile_selection` | `multi-profile` | `multi-profile` | radioly |
| Universal search results | `GET /v2/search/universal.search` | `query` | `universal-search` (search pack) | search `pfm-kb` | **pocket_search** |

## Visual recognition hints

Use these when the user pastes a screenshot without naming the screen:

- Bottom nav only / tab bar chips → `user.get_app_tabs`
- Vertical show rails / Explore language chips → `get_feed_data` (`explore_v2`)
- Single show hero + Play / episodes → `show.get_details` + `show.get_episodes`
- Subscribe / Follow control on show → often `user_action.update`
- Library History list → `get_library_feed` (`tab_id=history`)
- Avatar / edit profile fields → `user.get_profile_details` / `user.update`
- Reco carousels under a show → `get_show_feed` (`required_module=reco`)
- First-run language / show grid → `user.onb_states` + `get_onb_show_selection_feed`
- Phone / OTP / login chrome → `user.login_states` / `user.login` / `get_authentication_token`
- Create / switch profile benefits → `profile_benefits`
- Search results for a typed query → `universal.search` → switch pack to **search**

## Related Confluence

- Content POD hub: https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/851869741/FM+-+Content+POD+Wiki
- Onboarding links: https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/930152842/Onboarding+to+Pocket
- Pack pointer: `architecture/content-pod.md`
