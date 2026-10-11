---
id: capability.radioly-feed-variants
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/experiments/feed/audiobook/android_exp.py#AudiobookAndroidExperiment
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/experiments/feed/audiobook/audiobook_dollar_purchase_exp.py#AudiobookDollarPurchaseExp
---

**Aliases:** feed variants

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: AudiobookAndroidExperiment, AudiobookDollarPurchaseExp, CacheTTL, KeySchema, AudiobookSeriesCacheInvalidator, AudiobookSeriesCacheQuery, AudiobookSeriesDataFetcher, AudiobookSeriesDBHelper, AudiobookSeriesShowMapperDBHelper, SeriesType, Series, SeriesShowMapper, AudiobookSeriesAPIService, AudiobookSeriesService, AudiobookSeriesView, AudiobookV1Utils, AudiobookV1FeedBannerUtils, AudiobookV1EligibilityConstants, AudiobookSeriesConstants, AudiobookCrosswalkExperiment, AudiobookRevampExperiment, GermanAudiobookAutoplayExperiment, GermanAudiobookExperiment, GermanShortStoriesExperiment, _track_and_get_visit_count, _get_daily_impression_count, _increment_daily_impression_count, is_eligible, _get_pick_for_data, get_gtm_asset_data, AudiobookCrosswalkPopupGTM, IndiaAudiobookAutoplayExperiment, IndiaAudiobookExperiment, IndiaGenrePositionAudiobookExperiment, IndiaShortStoriesPositionExperiment, AudiobookModuleEntities, AudiobookMetadata, AudiobookAutoplayShowWeights, AudiobookAudioseriesGenreMapping, UsAudiobookPurchased, fetch_audiobook_show_detail, AudioBookContextDTO, AudioBookService, _extract_narrator_name, build_writer_credit, build_narrator_credit_from_metadata, build_narrator_credit, build_publisher_credit, AudiobookDollarPurchaseService, AudiobookFeedService, AudiobookV1ImpressionServiceDTO, AudiobookImpressionPublisher, AudiobookImpressionService, get_ldau_show_ids, _seed_from_playtime, AudiobookV1AppTabService, AudiobookModuleService, _normalize_scylla_row, _process_scylla_row, fetch_audiobook_feed_from_scylla. Plus 136 more classes in the same package.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
