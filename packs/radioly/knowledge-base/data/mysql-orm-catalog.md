# Radioly MySQL ORM catalog (generated)

Source: `radioly_client_api` Django `Meta.db_table` (+ a few raw-SQL tables).

**271 unique tables**. Not Argus warehouse — prefer this + CODE SEARCH for app schema.


**Gap:** tables that exist only in RDS and are never referenced in this checkout will not appear.


## ads

| table | ORM model | path |
|---|---|---|
| `user_primary_show_map` | `UserPrimaryShowMap` | `v3/ads/models/user_show_models.py` |
| `user_show_coin_spent_map` | `UserShowCoinSpentMap` | `v3/ads/models/user_show_models.py` |

## campaigns

| table | ORM model | path |
|---|---|---|
| `absolute_cashback_campaigns` | `AbsoluteCashbackCampaign` | `v2/campaigns/absolute_cashback/models/absolute_cashback_campaign.py` |
| `affiliate_campaign_transaction` | `AffiliateCampaignTransaction` | `v2/campaigns/affiliate_program/models/affiliate_campaign_transaction.py` |
| `battlepass_campaigns` | `BattlePassCampaign` | `v2/campaigns/battle_pass/models/battlepass_campaign.py` |
| `battlepass_plans` | `BattlePassPlan` | `v2/campaigns/battle_pass/models/battlepass_plan.py` |
| `campaign_assets` | `CampaignAsset` | `v2/campaigns/models.py` |
| `campaign_coin_plans` | `CampaignCoinPlanMapping` | `v2/campaigns/generic_services/models.py` |
| `campaign_meta` | `CampaignMeta` | `v2/campaigns/meta/models.py` |
| `campaigns` | `Campaigns` | `v2/campaigns/models.py` |
| `faq` | `Faq` | `v2/campaigns/faqs/models.py` |
| `faq_categories` | `FaqCategory` | `v2/campaigns/faqs/models.py` |
| `faq_feedback` | `FaqFeedback` | `v2/campaigns/faqs/models.py` |
| `faq_top_searches` | `FaqTopSearches` | `v2/campaigns/faqs/models.py` |
| `gift_inventory` | `GiftInventory` | `v2/campaigns/lucky_draw/model_class/gift_inventory.py` |
| `giveaway_campaigns` | `GiveawayCampaign` | `v3/giveaway/models/giveaway_campaign.py` |
| `incent_client_asset` | `ClientAsset` | `v2/campaigns/incent_campaign/models.py` |
| `incent_client_asset_action` | `ClientAssetAction` | `v2/campaigns/incent_campaign/models.py` |
| `incent_client_asset_client_asset_action_map` | `ClientAssetClientActionMap` | `v2/campaigns/incent_campaign/models.py` |
| `incent_client_asset_meta` | `ClientAssetMeta` | `v2/campaigns/incent_campaign/models.py` |
| `loyalty_program_campaign` | `LoyaltyProgramCampaign` | `v2/campaigns/loyalty_program/models/loyalty_program_campaign.py` |
| `loyalty_program_tier_info` | `LoyaltyProgramTierInfo` | `v2/campaigns/loyalty_program/models/loyalty_program_tier_info.py` |
| `loyalty_program_transactions` | `LoyaltyProgramTransaction` | `v2/campaigns/loyalty_program/models/loyalty_program_transaction.py` |
| `merchandise_user_address` | `MerchandiseUserAddress` | `v3/giveaway/models/merchandise_user_address.py` |
| `partnership_transactions` | `PartnershipTransactions` | `v2/campaigns/generic_services/models.py` |
| `terms_and_conditions` | `TermsAndConditions` | `v2/campaigns/terms_and_conditions/models/terms_and_conditions.py` |
| `user_battlepass_subscriptions` | `UserBattlePassSubscription` | `v2/campaigns/battle_pass/models/user_battlepass_subscription.py` |
| `user_campaigns_address` | `UserCampaignsAddress` | `v2/campaigns/lucky_draw/model_class/user_address.py` |
| `user_incent_asset_action_reward` | `UserAssetActionRewards` | `v2/campaigns/incent_campaign/models.py` |
| `user_incent_purchased_plan_details` | `UserIncentPurchasedPlanDetails` | `v2/campaigns/incent_campaign/models.py` |

## cashback_rewards

| table | ORM model | path |
|---|---|---|
| `cashback_campaign_offers` | `CashbackCampaignOffer` | `v3/cashback_and_rewards/models/cashback_campaign_offer.py` |
| `cashback_campaign_offers_mapping` | `CashbackCampaignOfferMapping` | `v3/cashback_and_rewards/models/cashback_campaign_offer_mapping.py` |
| `cashback_campaign_usages` | `CashbackCampaignUsages` | `v3/cashback_and_rewards/models/cashback_campaign_usages.py` |
| `cashback_campaigns` | `CashbackCampaign` | `v3/cashback_and_rewards/models/cashback_campaign.py` |
| `user_cashback_offers` | `UserCashbackOffer` | `v3/cashback_and_rewards/models/user_cashback_offer.py` |
| `user_reward_wallet_transactions` | `UserRewardWalletTransaction` | `v3/cashback_and_rewards/models/user_reward_wallet_transactions.py` |
| `user_reward_wallets` | `UserRewardWallet` | `v3/cashback_and_rewards/models/user_reward_wallet.py` |

## content

| table | ORM model | path |
|---|---|---|
| `ads` | `Ads` | `v2/content_api/models.py` |
| `ai_pgc_show_mapping` | `AiPgcShowMapping` | `v2/content_api/services/show_exclusion/models.py` |
| `assets` | `AssetModel` | `v2/content_api/assets/models.py` |
| `banners` | `Banners` | `v2/content_api/models.py` |
| `bgms` | `BackGroundMusic` | `v2/content_api/models.py` |
| `billboards` | `BillBoard` | `v2/content_api/assets/billboard_models.py` |
| `book_auditions` | `BookAudition` | `v2/content_api/models_new/book_audition.py` |
| `book_show_association` | `BookShowAssociation` | `v2/content_api/models.py` |
| `books` | `Book` | `v2/content_api/book_models.py` |
| `chapters` | `Chapter` | `v2/content_api/book_models.py` |
| `character_discovery_asset` | `CharacterDiscoveryAsset` | `v3/content/character_discovery/models.py` |
| `character_sheet_show_details` | `CharacterSheetShowDetails` | `v2/content_api/show_character_sheet/models.py` |
| `comment_nudge_allocation` | `CommentNudgeAllocation` | `v2/content_api/models.py` |
| `community_posts` | `CommunityPosts` | `v2/content_api/models.py` |
| `contests` | `Contests` | `v2/content_api/models.py` |
| `contests_entity_mapping` | `ContestsEntityMapping` | `v2/content_api/models.py` |
| `creators` | `Creator` | `v2/content_api/models_new/creator.py` |
| `entity_associated_creators` | `EntityAssociatedCreators` | `v2/content_api/models.py` |
| `entity_coupons` | `EntityCoupon` | `v2/content_api/models_new/entity_coupon.py` |
| `entity_media_urls` | `EntityMediaUrls` | `v2/content_api/models.py` |
| `entity_notes` | `EntityNotes` | `v2/content_api/ugc_notes/models/entity_notes.py` |
| `entity_reactions` | `EntityReactions` | `v2/content_api/ugc_notes/models/entity_reactions.py` |
| `entity_stats` | `EntityStats` | `content_api/models.py` |
| `entity_stats_new` | `EntityStatsNew` | `v2/content_api/models.py` |
| `episode_recaps` | `EpisodeRecap` | `v3/content_api/models/episode_recap.py` |
| `explore_topics` | `ExploreTopics` | `v2/content_api/models.py` |
| `genre_module_entities` | `GenreModuleEntity` | `v3/content/home_page_redesign/genre_chip/models.py` |
| `module_entity_mapping` | `ModuleEntityMapping` | `content_api/models.py` |
| `module_thumbnail_config` | `ModuleThumbnailConfig` | `v2/content_api/models_new/module_thumbnail_config.py` |
| `modules` | `Modules` | `content_api/models.py` |
| `no_ad_pack_users` | `NoAdPackUser` | `v2/content_api/ads/models/no_ad_pack_users.py` |
| `original_book_credits` | `OriginalBookCredits` | `v2/content_api/models_new/original_book_credits.py` |
| `parallel_listener` | `ParallelListenerModel` | `v2/content_api/models_new/parallel_listener.py` |
| `scripts` | `Scripts` | `content_api/models.py` |
| `seo_details_web` | `SeoDetailsWeb` | `v2/content_api/services/seo/models.py` |
| `show_analytics` | `ShowAnalytics` | `v2/content_api/models.py` |
| `show_assets` | `ShowAsset` | `v2/content_api/models_new/show_assets.py` |
| `show_characters` | `ShowCharacter` | `v2/content_api/show_character_sheet/models.py` |
| `show_exclusion_group` | `ShowExclusionGroup` | `v2/content_api/services/show_exclusion/models.py` |
| `show_locale` | `ShowLocale` | `v2/content_api/models_new/show_locale.py` |
| `show_meta` | `ShowMeta` | `v2/content_api/models.py` |
| `show_replica_map` | `ShowReplicaMap` | `v2/content_api/models_new/show_replica_map.py` |
| `show_stories_sub_stats` | `ShowStoriesSubStats` | `v2/content_api/models_new/show_stories_sub_stats.py` |
| `show_tier` | `ShowTier` | `v2/content_api/models.py` |
| `show_variant_unlocks` | `ShowVariantUnlock` | `v2/content_api/models_new/show_variant_unlock.py` |
| `shows` | `Shows` | `content_api/models.py` |
| `shows_thumbnail_mapping` | `ShowThumbnailMapping` | `v2/content_api/models_new/show_thumbnail_map.py` |
| `stories` | `Stories` | `content_api/models.py` |
| `stories_meta` | `StoriesMeta` | `v2/content_api/ads/services/disclaimer_ad/models.py` |
| `story_keys` | `StoryClearKeys` | `v2/content_api/models.py` |
| `story_subs` | `StorySub` | `v2/content_api/models_new/story_subs.py` |
| `tag_entity_mapping` | `TagEntityMapping` | `v2/content_api/models.py` |
| `tags` | `Tags` | `v2/content_api/models.py` |
| `text_to_speech_eligible_shows` | `TextToSpeechEligibleShows` | `v2/content_api/models_new/text_to_speech_eligible_shows.py` |
| `top_shows` | `TopShows` | `v2/content_api/models.py` |
| `topic_entity_mapping` | `TopicEntityMapping` | `v2/content_api/models.py` |
| `topic_tags_mapping` | `TopicTagMapping` | `v2/content_api/models.py` |
| `topics` | `Topics` | `content_api/models.py` |
| `unlock_plan` | `UnlockPlans` | `v2/content_api/models_v2.py` |
| `user_community_links` | `UserCommunityLinks` | `v2/content_api/models_new/user_community_links.py` |
| `user_friction_controls` | `UserFrictionControl` | `v2/content_api/models_new/user_friction_control.py` |
| `user_show_meta` | `UserShowMeta` | `v2/content_api/models_new/user_show_meta.py` |
| `user_show_spents_new` | `UserShowSpentNew` | `v2/content_api/episode_return/models.py` |
| `user_show_unlocks` | `UserShowUnlock` | `v2/content_api/models_v2.py` |

## crosswalk

| table | ORM model | path |
|---|---|---|
| `bigger_thumbnail_assets` | `BiggerThumbnailAsset` | `v3/crosswalk_ds/bigger_thumbnail/models.py` |
| `splash_assets` | `SplashAsset` | `v3/crosswalk_ds/splash/models.py` |

## experience

| table | ORM model | path |
|---|---|---|
| `account_transfer_logs` | `AccountTransferLog` | `v3/experience/account_transfer/models.py` |
| `bigger_thumbnails_editorial_campaigns` | `BiggerThumbnailsEditorialCampaign` | `v3/experience/bigger_thumbnails/models.py` |
| `bigger_thumbnails_editorial_shows` | `BiggerThumbnailsEditorialShows` | `v3/experience/bigger_thumbnails/models.py` |
| `bigger_thumbnails_user_state` | `BiggerThumbnailsUserState` | `v3/experience/bigger_thumbnails/models.py` |
| `chat_characters` | `ChatCharacter` | `v3/experience/character_chat/models.py` |
| `discovery_show_metadata` | `DiscoveryShowMetadata` | `v3/experience/pocket_pick/models.py` |
| `episode_subtitle_assets` | `EpisodeSubtitleAssets` | `v3/experience/readers_mode/models.py` |
| `genre_based_tropes` | `GenreBasedTropes` | `v3/experience/key_tropes/models.py` |
| `interactive_choice` | `InteractiveChoice` | `v3/experience/interactive/models.py` |
| `interactive_frame` | `InteractiveFrame` | `v3/experience/interactive/models.py` |
| `interactive_question` | `InteractiveQuestion` | `v3/experience/interactive/models.py` |
| `interactive_story` | `InteractiveStory` | `v3/experience/interactive/models.py` |
| `interactive_story_node` | `InteractiveStoryNode` | `v3/experience/interactive/models.py` |
| `key_tropes_show_metrics` | `KeyTropesShowMetrics` | `v3/experience/key_tropes/models.py` |
| `onboarding_genre_show` | `OnboardingGenreShow` | `v3/experience/onboarding/models.py` |
| `player_page_must_listen` | `PlayerPageMustListen` | `v3/experience/player_page_sampling/models.py` |
| `player_page_rising_hits` | `PlayerPageRisingHits` | `v3/experience/player_page_sampling/models.py` |
| `pocket_pick_user_impressions` | `PocketPickUserImpression` | `v3/experience/pocket_pick/models.py` |
| `shorts` | `Shorts` | `v3/experience/discover_tab/models.py` |
| `show_affinity_rank` | `(raw SQL)` | `v3/experience/show_affinity_engine/constants.py` |
| `show_promotion_assets_device_states` | `ShowPromotionDeviceState` | `v3/experience/show_promotion/models.py` |
| `show_promotion_assets_user_states` | `ShowPromotionUserState` | `v3/experience/show_promotion/models.py` |
| `show_recap` | `ShowRecap` | `v3/experience/show_ai_recap/models.py` |
| `show_referral_redemptions` | `ShowReferralRedemption` | `v3/experience/show_referral/models.py` |
| `show_referral_reward_transactions` | `ShowReferralRewardTransaction` | `v3/experience/show_referral/models.py` |
| `show_referrals` | `ShowReferral` | `v3/experience/show_referral/models.py` |
| `show_seo_summaries` | `ShowSeoSummary` | `v3/experience/show_seo_summary/models.py` |
| `show_trailer_codes` | `ShowTrailerCode` | `v3/experience/trailer_code/models.py` |
| `show_trope_mapping` | `ShowTropeMapping` | `v3/experience/key_tropes/models.py` |
| `sleep_stories` | `SleepStories` | `v3/experience/sleep_mode/models.py` |
| `story_evolution_cards` | `StoryEvolutionCard` | `v3/experience/story_evolution/models.py` |
| `story_evolutions` | `StoryEvolution` | `v3/experience/story_evolution/models.py` |
| `story_media_assets` | `StoryMediaAssets` | `v3/experience/pocket_pick/models.py` |
| `trope_language_ranking` | `TropeLanguageRanking` | `v3/experience/key_tropes/models.py` |
| `trope_show` | `TropeShow` | `v3/experience/key_tropes/models.py` |
| `tropes` | `Tropes` | `v3/experience/key_tropes/models.py` |
| `user_experimental_shorts` | `UserExperimentalShorts` | `v3/experience/discover_tab/models.py` |
| `video_playback_episode` | `VideoPlaybackEpisode` | `v3/experience/experiments/video_playback/models/video_playback_episode.py` |

## experiments

| table | ORM model | path |
|---|---|---|
| `ai_rj_last_played` | `AiRjLastPlayed` | `v2/experiments/content/ai_rj_v1/models.py` |
| `ap_stich_device_show_playtime` | `AutoplayStitchingDeviceShowPlaytime` | `v2/experiments/content/autoplay_stitching/models.py` |
| `ap_stiching_ldau_show` | `AutoplayStitchingLdauShow` | `v2/experiments/content/autoplay_stitching/models.py` |
| `audiobook_audioseries_genre_mapping` | `AudiobookAudioseriesGenreMapping` | `v2/experiments/feed/audiobook/models.py` |
| `audiobook_autoplay_show_weights` | `AudiobookAutoplayShowWeights` | `v2/experiments/feed/audiobook/models.py` |
| `audiobook_metadata` | `AudiobookMetadata` | `v2/experiments/feed/audiobook/models.py` |
| `audiobook_module_entities` | `AudiobookModuleEntities` | `v2/experiments/feed/audiobook/models.py` |
| `codec_blacklisted_device_models` | `CodecBlacklistedDeviceModels` | `v2/experiments/feed/codec_blacklist/models.py` |
| `coin_pack_discount_allocations` | `CoinPackDiscountAllocation` | `v2/experiments/payments/models/coin_pack_discount_allocation.py` |
| `cold_start_module_entities` | `ColdStartModuleEntities` | `v2/experiments/content/cold_start/models.py` |
| `content_throttling_german_mvs_excluded_users` | `ContentThrottlingGermanMvsExcludedUsers` | `v2/experiments/payments/content_throttling_german_mvs/models.py` |
| `content_throttling_v2_primary_show_v1` | `ContentThrottlingV2PrimaryShow` | `v2/experiments/payments/content_throttling_v2/models.py` |
| `content_throttling_v2_show_info` | `ContentThrottlingV2ShowInfo` | `v2/experiments/payments/content_throttling_v2/models.py` |
| `entity_experiment_mapping` | `EntityExperimentMapping` | `v2/experiments/models_data/entity_mapping_experiment.py` |
| `experiment_variants` | `ExperimentVariant` | `v2/experiments/models.py` |
| `experiments` | `Experiment` | `v2/experiments/models.py` |
| `external_account_reward` | `ExternalAccountRewards` | `v2/experiments/user_experience/external_account_signup/models.py` |
| `homefeed_ugc_discovery_new_row_playlist` | `HomefeedUGCDiscoveryNewROWPlaylist` | `v2/experiments/content/ugc/models/row_new.py` |
| `homefeed_ugc_discovery_row_shows` | `HomefeedUGCDiscoveryROWShows` | `v2/experiments/content/ugc/models/row.py` |
| `homefeed_ugc_discovery_usa_shows` | `HomefeedUGCDiscoveryUSAShows` | `v2/experiments/content/ugc/models/usa.py` |
| `placements` | `Placement` | `v2/experiments/models_new/placement.py` |
| `placements_experiments` | `PlacementExperiment` | `v2/experiments/models_new/placement_experiment.py` |
| `series` | `Series` | `v2/experiments/feed/audiobook/audiobook_series/models.py` |
| `series_show_mapper` | `SeriesShowMapper` | `v2/experiments/feed/audiobook/audiobook_series/models.py` |
| `show_collection_mapping` | `ShowCollectionMapping` | `v2/experiments/content/collections/models.py` |
| `show_seasons` | `ShowSeason` | `v2/experiments/content/seasons/models.py` |
| `shows_collection` | `ShowCollection` | `v2/experiments/content/collections/models.py` |
| `shows_schedule` | `DailyShowSchedule` | `v2/experiments/feed/daily_show/models.py` |
| `us_audiobook_purchased` | `UsAudiobookPurchased` | `v2/experiments/feed/audiobook/models.py` |

## feed

| table | ORM model | path |
|---|---|---|
| `billboard_user_mapping` | `BillboardUserMapping` | `v2/feed_api/billboards/models/billboard_users.py` |
| `campaign_day_tracking` | `CampaignDayTracking` | `v2/feed_api/festives/repository/models/campaign_day_tracking.py` |
| `collections_topic_modules` | `CollectionsTopic` | `v2/feed_api/models_new/collections_topics.py` |
| `default_home_feed_data_large` | `DefaultHomeFeedData` | `feed_api/models.py` |
| `feed_assets` | `FeedAsset` | `v2/feed_api/models_new/feed_config.py` |
| `latam_module_entities` | `LatamModuleEntities` | `v2/feed_api/models_new/latam_module_entities.py` |
| `module_entities` | `ModuleEntity` | `v3/feed/models/module_entities.py` |
| `personalised_home_feed_data` | `PersonalisedHomeFeedData` | `feed_api/models.py` |
| `show_impression` | `ShowImpression` | `v2/feed_api/models.py` |
| `trending_items_test` | `Trending` | `v2/trending/models.py` |

## gamification

| table | ORM model | path |
|---|---|---|
| `loyalty_benefits_user_info` | `LoyaltyBenefitsUserInfo` | `v3/gamification/loyalty/models/user_benefit.py` |
| `user_spin_state` | `UserSpinState` | `v3/gamification/slot_machine/models/user_spin_state.py` |
| `user_week_coin_spent` | `UserWeekCoinSpent` | `v3/gamification/loyalty/models/user_week_spent.py` |

## geo

| table | ORM model | path |
|---|---|---|
| `cities` | `City` | `v2/cities/models.py` |
| `countries` | `Country` | `v2/countries/models.py` |
| `states` | `State` | `v2/states/models.py` |

## misc

| table | ORM model | path |
|---|---|---|
| `streak_campaign` | `StreakCampaign` | `v2/miscellaneous/continuous_streak/models/streak_campaign.py` |
| `streak_campaign_variant` | `StreakCampaignVariant` | `v2/miscellaneous/continuous_streak/models/streak_variant.py` |
| `streak_ledger` | `StreakLedger` | `v2/miscellaneous/continuous_streak/models/streak_ledger.py` |
| `streak_reward` | `StreakReward` | `v2/miscellaneous/continuous_streak/models/streak_reward.py` |
| `streak_user_meta_info` | `StreakUserMetaInfo` | `v2/miscellaneous/continuous_streak/models/streak_user_meta_info.py` |
| `tool_tips` | `ToolTip` | `v2/miscellaneous/model_data/tooltip.py` |

## notifications

| table | ORM model | path |
|---|---|---|
| `notifications` | `Notifications` | `v2/notification/user_wise_rate_limiter.py` |

## payments

| table | ORM model | path |
|---|---|---|
| `coin_coupons_plans` | `CoinCouponPlan` | `v2/payments/plans/models.py` |
| `coin_plans` | `CoinPlans` | `v2/payments/plans/models.py` |
| `coupons` | `Coupons` | `v2/payments/models.py` |
| `dead_letter_queue` | `DeadLetterQueue` | `v2/payments/models.py` |
| `ext_order_mapping` | `ExtOrderMapping` | `v3/payments/models/ext_order_mapping_model.py` |
| `gamified_unclaimed_reward` | `GamifiedUnclaimedReward` | `v3/payments/models/gamified_unclaimed_reward.py` |
| `novel_transactions` | `NovelTransactions` | `v3/payments/models/novels_transaction_model.py` |
| `novels_transaction_logs` | `NovelTransactionStateLog` | `v3/payments/models/transactions_state_log_model.py` |
| `offers` | `Offer` | `v2/payments/models.py` |
| `payment_gateways` | `PaymentGateways` | `v3/payments/models/payment_gateway_model.py` |
| `payment_gateways_logs` | `PaymentGatewaysLogs` | `v3/payments/models/payment_gateway_model.py` |
| `paypal_subscriptions` | `PaypalSubscriptions` | `v2/payments/models.py` |
| `playtime_credits_ledger` | `PlaytimeCreditsLedger` | `v3/payments/services/mhp/models/playtime_credits_ledger.py` |
| `refund_transactions` | `RefundTransactions` | `v3/payments/models/refund_transactions_model.py` |
| `secondary_show_pack_purchases` | `SecondaryShowPackPurchases` | `v3/payments/models/secondary_show_pack_model.py` |
| `stripe_customer` | `StripeCustomerModel` | `v2/payments/gateways/stripe/models/stripe_customer_model.py` |
| `stripe_web_payment_counts` | `StripeWebPaymentCount` | `v3/payments/models/stripe_web_payment_count_model.py` |
| `transaction_logs` | `TransactionStateLog` | `v3/payments/models/transactions_state_log_model.py` |
| `transactions` | `Transactions` | `v3/payments/models/transactions_model.py` |
| `transactions_meta` | `TransactionsMeta` | `v3/payments/models/transactions_meta_model.py` |
| `user_playtime_credits` | `UserPlaytimeCredits` | `v3/payments/services/mhp/models/user_playtime_credits.py` |
| `user_spending_segment` | `UserSpendingSegment` | `v2/payments/models_v2/user_spending_segment.py` |
| `user_vip_offers` | `UserVipOffer` | `v2/payments/models.py` |
| `user_web_commissions_meta` | `UserWebCommissionMeta` | `v3/payments/web_commissions/models.py` |
| `vip_plans` | `PaymentPlans` | `v2/payments/models.py` |

## ppv

| table | ORM model | path |
|---|---|---|
| `ppv_batch_queue` | `PPVBatchQueue` | `v3/ppv/models/ppv_batch_queue.py` |
| `ppv_check_shows` | `PPVCheckShow` | `v3/ppv/models/ppv_check_shows.py` |
| `show_stagger_runs` | `ShowStaggerRun` | `v3/ppv/models/show_stagger_runs.py` |

## rule_engine

| table | ORM model | path |
|---|---|---|
| `apps` | `App` | `v2/rule_engine/model_data/apps.py` |
| `rule_engine_users` | `RuleEngineUser` | `v2/rule_engine/model_data/users.py` |
| `rules` | `Rules` | `v2/rule_engine/model_data/rules.py` |
| `rulesets` | `Ruleset` | `v2/rule_engine/model_data/ruleset.py` |

## segmentation

| table | ORM model | path |
|---|---|---|
| `Segment_logs` | `SegmentLogs` | `v2/segmentation_engine/models.py` |
| `segments` | `Segments` | `v2/segmentation_engine/models.py` |
| `user_id_mapping` | `UseridMapping` | `v2/segmentation_engine/models.py` |

## social

| table | ORM model | path |
|---|---|---|
| `comment_ds_score_eligibility` | `CommentDSScoreEligibility` | `v2/social/models.py` |

## subscriptions

| table | ORM model | path |
|---|---|---|
| `pocket_subs_free_show` | `PocketSubsFreeShow` | `v3/subscriptions/biz_models/services/models.py` |
| `subscription_logs` | `SubscriptionLog` | `v3/subscriptions/core/models/subscription_logs.py` |
| `subscription_offer_types` | `SubscriptionOfferTypes` | `v3/subscriptions/core/models/subscription_type.py` |
| `subscription_payments` | `SubscriptionPayment` | `v3/subscriptions/core/models/subscription_payments.py` |
| `subscriptions` | `Subscription` | `v3/subscriptions/core/models/subscription.py` |
| `user_spend_segment_tracker` | `UserSpendSegmentTracker` | `v3/subscriptions/core/models/user_spend_segment_tracker.py` |

## survey

| table | ORM model | path |
|---|---|---|
| `survey_next_question_navigations` | `SurveyNextQuestionNavigation` | `v3/user_survey/models.py` |
| `survey_question_options` | `SurveyQuestionOption` | `v3/user_survey/models.py` |
| `survey_questions` | `SurveyQuestion` | `v3/user_survey/models.py` |
| `surveys` | `Survey` | `v3/user_survey/models.py` |

## ugc

| table | ORM model | path |
|---|---|---|
| `writer_activity_type` | `WriterActivityType` | `v2/ugc_originals_feed/models/writer_activity_type.py` |

## users

| table | ORM model | path |
|---|---|---|
| `creator_info` | `CreatorInfo` | `v2/user_api/models.py` |
| `default_tab_override` | `DefaultTabOverride` | `v2/user_api/models.py` |
| `device_ab` | `DeviceAB` | `v2/user_api/models.py` |
| `device_install_analytics` | `DeviceInstallAnalytics` | `v2/user_api/models.py` |
| `device_installs` | `DeviceInstall` | `v2/user_api/models.py` |
| `device_primary_show` | `DevicePrimaryShow` | `v2/user_api/models.py` |
| `device_promo_logs` | `DevicePromoLog` | `v2/user_api/models.py` |
| `deviceprofiles` | `DeviceProfile` | `v2/profiles/models_data/device_profile.py` |
| `devices` | `Devices` | `v2/user_api/models.py` |
| `devices_meta` | `DeviceMeta` | `v2/user_api/models.py` |
| `employee_users` | `EmployeeUser` | `v2/user_api/models.py` |
| `feedback_popup` | `FeedbackPopup` | `v2/user_api/models.py` |
| `follows` | `Follows` | `user_api/models.py` |
| `profile_link_invite` | `ProfileLinkInvite` | `v2/profiles/models_data/profile.py` |
| `profiles` | `Profile` | `v2/profiles/models_data/profile.py` |
| `user_actions` | `UserActions` | `user_api/models.py` |
| `user_activated_show` | `ActivatedShow` | `v2/user_api/models_new/invites.py` |
| `user_activity` | `UserActivity` | `user_api/models.py` |
| `user_block_report_activity` | `UserBlockReportActivity` | `v2/user_api/models_new/UserBlockReport/UserBlockReportActivity.py` |
| `user_deactivate_request` | `UserDeactivateRequest` | `v2/user_api/models.py` |
| `user_delete` | `UserDelete` | `v2/user_api/models.py` |
| `user_delete_request` | `UserDeleteRequest` | `v2/user_api/models.py` |
| `user_uploaded_contents` | `UserUploadedContents` | `user_api/models.py` |
| `users` | `Users` | `user_api/models.py` |
| `users_meta` | `UsersMeta` | `v2/user_api/models.py` |
| `writer_tab_visits` | `WriterTabVisit` | `v2/user_api/models.py` |

## wallet

| table | ORM model | path |
|---|---|---|
| `user_coin_credit_logger` | `UserCoinCreditLogger` | `v2/wallet/models.py` |
| `user_coin_wallet` | `UserCoinWallet` | `v2/wallet/models.py` |
| `user_coin_wallet_credit_type` | `UserCoinWalletCreditType` | `v2/wallet/models.py` |
| `user_coin_wallet_item_offers` | `UserCoinWalletItemOffers` | `v2/wallet/models.py` |
| `user_coin_wallet_txns_partitioned` | `UserCoinWalletTxnPartitioned` | `v2/wallet/models.py` |
