<!-- Radioly overlay. Merges over global/skills/explain-flow.skill.md -->
# Skill: Explain / debug Radioly (Experience)

Follow `global/skills/explain-flow.skill.md`. This overlay names Radioly +
screenshot grounding.

## Screen / screenshot asks (required)

When the ask includes a screenshot, image URL, or UI description:

1. Read `# API TO SCREEN` / `architecture/api-to-screen.md` if attached.
2. Name the **screen** and the **primary API path** before deep diving.
3. Attach reasoning to `features/*/overview.md` + `pfm-kb` modules listed in
   that map.
4. If the image could be two surfaces (e.g. Home vs Discover vs Library), ask
   which tab — do not guess the wrong feed API.
5. Never paste JWTs, uids, or full Confluence curls. Paths + query keys only.
6. `universal.search` → pocket_search pack, not Radioly handlers.

## Canonical Experience paths (from api-to-screen)

- Tabs shell: `/v2/user_api/user.get_app_tabs`
- Explore/Home: `/v2/feed_api/get_feed_data` (`api_type=explore_v2`)
- Show page: `/v2/content_api/show.get_details` + `show.get_episodes`
- Library history: `/v2/feed_api/get_library_feed` (`tab_id=history`)
- Profile: `/v2/user_api/user.get_profile_details` / `user.update`
- Show reco modules: `/v2/feed_api/get_show_feed` (`required_module=reco`)
- Onboarding: `/v2/user_api/user.onb_states` + `/v2/feed_api/get_onb_show_selection_feed`
- Auth: `/v2/user_api/user.login_states` / `user.login` / `user.get_authentication_token`
- Multi-profile: `/v2/user_api/profile_benefits`

POD / onboarding pointers: `architecture/content-pod.md`.

## Clarify before concluding

Same as global: env, path, and which screen/API when ambiguous. Mark guesses
as Assumption. Prefer partial evidence + questions over a confident wrong RCA.

## Slack format

Same as the global skill: `*bold*`, no `**`, no `---`, no markdown tables,
no mermaid/ASCII diagrams. Lead with *Verdict* → *Details* (bullets) →
*Flow* as `A → B → C` or numbered steps if asked → Questions if needed.
Keep it ≤15 short lines. No operator Steps unless `raw_metadata=true`.
