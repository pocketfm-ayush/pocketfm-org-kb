# Radioly Scylla / Cassandra catalog (generated)

Source: CQL + `KEYSPACE`/`TABLE_NAME` + `RadiolyKeyspacesEnum` in `radioly_client_api`.

**81** qualified tables referenced in application code.

These are **not** in Argus `fm_product_analytics` — use CODE SEARCH for columns.


Enum keyspaces: `audio_playtime`, `pocketlabs`, `advertisements`, `show_unlocks`,
`character_sheets`, `user_surveys`, `feed`, `content`, `subscriptions`, `payments`, `fm_iam`.

Also observed: `experience`, `loyalty_program`, `nexus`.


**Gap:** tables that exist in Scylla but are never referenced in this checkout
will not appear here.


## `advertisements` (9)

| table | example path |
|---|---|
| `advertisements.active_ad_streaks_status` | `v3/ads/models/ad_streak_status.py` |
| `advertisements.ads_device_ecpm_last_7days` | `v3/ads/models/ads_device_ecpm_last_7days.py` |
| `advertisements.ads_device_pam_thresholds` | `v3/ads/models/ads_device_pam_thresholds.py` |
| `advertisements.ads_dynamic_bidding_thresholds` | `v3/ads/models/ads_dynamic_bidding_thresholds.py` |
| `advertisements.ads_playtime` | `v2/content_api/ads/models/playtime_impressions_model.py` |
| `advertisements.user_ads_limits` | `v3/ads/models/ads_limit_model.py` |
| `advertisements.user_ads_rewards` | `v3/ads/models/rewards_updation.py` |
| `advertisements.user_ads_streaks` | `v3/ads/models/ads_streak_model.py` |
| `advertisements.user_rv_sale_category` | `v3/ads/experiments/rv_sale/rv_sale_experiment.py` |

## `audio_playtime` (14)

| table | example path |
|---|---|
| `audio_playtime.device_autoplay_removed_show` | `v2/feed_api/services/removed_show/autoplay_scylla_manager.py` |
| `audio_playtime.device_continue_playing_removed_shows` | `v2/feed_api/modules/continue_listening.py` |
| `audio_playtime.device_last_listened_story` | `v3/playtime/story_playtime/repositories.py` |
| `audio_playtime.device_recent_shows` | `v3/playtime/show_playtime/repositories.py` |
| `audio_playtime.device_show_playtime` | `v3/playtime/show_playtime/repositories.py` |
| `audio_playtime.device_story_playtime` | `v2/user_api/playtime_helpers.py` |
| `audio_playtime.feed_show_exclusion_threshold` | `v3/ppv/feed_show_exclusion_writer.py` |
| `audio_playtime.user_autoplay_removed_show` | `v2/feed_api/services/removed_show/autoplay_scylla_manager.py` |
| `audio_playtime.user_continue_playing_removed_shows` | `v2/feed_api/modules/continue_listening.py` |
| `audio_playtime.user_last_listened_story` | `v3/playtime/story_playtime/repositories.py` |
| `audio_playtime.user_login_device` | `v2/user_api/models.py` |
| `audio_playtime.user_recent_shows` | `v3/playtime/show_playtime/repositories.py` |
| `audio_playtime.user_show_playtime` | `v3/playtime/show_playtime/repositories.py` |
| `audio_playtime.user_story_playtime` | `v2/payments/services/check_renewal_eligibility_service.py` |

## `character_sheets` (2)

| table | example path |
|---|---|
| `character_sheets.character_list_stats` | `v2/content_api/show_character_sheet/show_character_sheet_helpers.py` |
| `character_sheets.likes` | `v2/content_api/show_character_sheet/show_character_sheet_helpers.py` |

## `content` (7)

| table | example path |
|---|---|
| `content.character_discovery_user_state` | `v3/content/character_discovery/constants.py` |
| `content.cw_ds_ranked_shows` | `v3/crosswalk_ds/ranked_shows/scylla_reader.py` |
| `content.device_first_dau` | `v2/content_api/repository/device_first_dau.py` |
| `content.device_kt_rotation_epoch` | `v3/experience/key_tropes/constants.py` |
| `content.discover_eligibility` | `v3/experience/discover_tab/services/discover_eligibility_service.py` |
| `content.ds_show_thumbnail` | `v2/content/ds_show_thumbnail/repository.py` |
| `content.user_qmau_tags` | `v2/experiments/feed/audiobook/services/nqmau_cohort_service.py` |

## `experience` (16)

| table | example path |
|---|---|
| `experience.character_chat_bubble_text_impressions` | `v3/experience/character_chat/services/bubble_text_service.py` |
| `experience.character_chat_state` | `v3/experience/character_chat/services/bubble_text_service.py` |
| `experience.character_state` | `v3/experience/character_chat/services/milestone_service.py` |
| `experience.chat_messages` | `v3/experience/character_chat/services/chat_service.py` |
| `experience.device_stories_impressions` | `v3/experience/discover_tab/services/shorts_service.py` |
| `experience.device_trope_show_stats` | `v3/experience/key_tropes/services/user_shows_viewed_service.py` |
| `experience.device_trope_stats_v2` | `v3/experience/key_tropes/services/user_trope_viewed_service.py` |
| `experience.discover_device_preferences` | `v3/experience/discover_tab/services/user_preferences_service.py` |
| `experience.discover_device_viewed_content` | `v3/experience/discover_tab/services/viewed_shorts_service.py` |
| `experience.discover_user_preferences` | `v3/experience/discover_tab/services/user_preferences_service.py` |
| `experience.discover_user_viewed_content` | `v3/experience/discover_tab/services/viewed_shorts_service.py` |
| `experience.experience_device_meta` | `v3/experience/onboarding/services/genre_onboarding_service.py` |
| `experience.experience_user_meta` | `v3/experience/onboarding/services/genre_onboarding_service.py` |
| `experience.user_stories_impressions` | `v3/experience/discover_tab/services/shorts_service.py` |
| `experience.user_trope_show_stats` | `v3/experience/key_tropes/services/user_shows_viewed_service.py` |
| `experience.user_trope_stats_v2` | `v3/experience/key_tropes/services/user_trope_viewed_service.py` |

## `feed` (4)

| table | example path |
|---|---|
| `feed.autoplay` | `v2/feed_api/packaged_deployment.py` |
| `feed.discover` | `v3/experience/discover_tab/services/ds_recommendations_service.py` |
| `feed.personalised_feed` | `v2/experiments/feed/audiobook/services/audiobook_personalized_service.py` |
| `feed.result` | `v2/feed_api/views.py` |

## `fm_iam` (1)

| table | example path |
|---|---|
| `fm_iam.gdpr_consents` | `v3/ads/experiments/gdpr_sourcepoint_homepage_nudge/experiment.py` |

## `loyalty_program` (4)

| table | example path |
|---|---|
| `loyalty_program.loyalty_notification_history` | `v3/gamification/loyalty/models/user_notification.py` |
| `loyalty_program.loyalty_tier_user` | `v3/gamification/loyalty/models/user_tier.py` |
| `loyalty_program.user_benefits` | `v3/gamification/loyalty/models/user_benefits.py` |
| `loyalty_program.user_last_weeks_spent` | `v3/gamification/loyalty/models/user_last_week_data.py` |

## `nexus` (1)

| table | example path |
|---|---|
| `nexus.user_profiles` | `external_services/nexus/user_profile_repository.py` |

## `payments` (9)

| table | example path |
|---|---|
| `payments.budget_booster` | `v3/budget_booster/db/models.py` |
| `payments.daily_target` | `v2/miscellaneous/gamified_engagement/models.py` |
| `payments.ds_user_pack_recommendations` | `v3/payments/experiments/ds_pavo/fetcher.py` |
| `payments.merchandise_users` | `v3/giveaway/models/merchandise_users.py` |
| `payments.no_mandate_user_cohort` | `v3/subscriptions/biz_models/super_saver_pass/experiments/no_mandate_exp.py` |
| `payments.slot_machine_session_count` | `v3/gamification/slot_machine/models/user_sessions.py` |
| `payments.temp_users` | `v3/payments/sbm/services/unlocking.py` |
| `payments.user_promoted_pack_candidates` | `v3/payments/trial_pack_education_ux/pack_recommendations/service.py` |
| `payments.user_recommended_pack` | `v3/payments/payments_journey/repositories/payment_journey_android_in.py` |

## `pocketlabs` (3)

| table | example path |
|---|---|
| `pocketlabs.device_experiments_by_device_id` | `v2/experiments/repository/scylla/scylla_device_experiment_repository.py` |
| `pocketlabs.device_tentpole_eligibility` | `v3/liveops/repository/device_tentpole_eligibility_repository.py` |
| `pocketlabs.user_experiments_by_uid` | `v2/experiments/repository/scylla/scylla_user_experiment_repository.py` |

## `show_unlocks` (5)

| table | example path |
|---|---|
| `show_unlocks.device_latest_unlocks` | `v2/content_api/models_v2.py` |
| `show_unlocks.device_show_unlocks` | `v2/content_api/models_v2.py` |
| `show_unlocks.user_latest_unlocks` | `v2/content_api/models_v2.py` |
| `show_unlocks.user_show_unlocks` | `v2/content_api/models_v2.py` |
| `show_unlocks.user_show_unlocks_today` | `v2/miscellaneous/gamified_engagement/models.py` |

## `subscriptions` (4)

| table | example path |
|---|---|
| `subscriptions.impressions` | `v3/subscriptions/biz_models/services/impressions.py` |
| `subscriptions.savings_data` | `v2/experiments/repository/scylla/scylla_savings_data.py` |
| `subscriptions.subscription_id` | `v2/user_api/services/freshchat_helper/freshchat_request_helper.py` |
| `subscriptions.subscription_offer_engine` | `v3/subscriptions/biz_models/services/offer_engine.py` |

## `user_surveys` (2)

| table | example path |
|---|---|
| `user_surveys.survey_submissions` | `v3/user_survey/models.py` |
| `user_surveys.survey_submission_answers` | `v3/user_survey/models.py` |
