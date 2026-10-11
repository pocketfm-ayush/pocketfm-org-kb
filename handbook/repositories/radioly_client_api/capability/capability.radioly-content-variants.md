---
id: capability.radioly-content-variants
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/experiments/content/ai_rj_v1/exp.py#AiRjExperimentV1
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/experiments/content/ai_rj_v1/models.py#AiRjLastPlayed
---

**Aliases:** content variants

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: AiRjExperimentV1, AiRjLastPlayed, AutoplayReEngagementV1, AutoplayStitchingIndiaExp, AutoplayStitchingExp, AutoplayStitchingFeedExp, AutoplayStitchingIndiaFeedExp, M0StitchingBiggerThumbnailService, M0StitchingBiggerThumbnailsFeatureFlags, AutoplayStitchingModuleService, RankingService, AutoplayStitchingDeviceShowPlaytime, AutoplayStitchingLdauShow, ColdStartUserConfig, ColdStartModuleEntities, ColdStartModuleEntitiesSerializer, ContentRequest, ColdStartContentService, ColdStartDsService, ColdStartDsFallback, ColdStartModuleEntityService, SourceShowService, CollectionCacheHelper, is_seasons_collection, get_aspect_ratio_float, _batch_cache_aside, CollectionDataFetcher, CollectionDBHelper, ShowCollection, ShowCollectionMapping, serialize_collections, _build_module, _build_entities, _build_season_entity, _build_show_entity, _build_plays_badge, CollectionFacade, CollectionImpressionService, _resolve_image, CollectionService, SeasonCollectionService, get_show_collection_module, _try_genre, _try_candidate, _sanitize_uid, _resolve_entity, ShowCollectionService, get_playtime_map, sort_and_filter_shows, has_any_playtime, _round_robin, _sort_by_playtime, hours_delta, future_expiry_base, CollectionStateService, ShowCollectionExperiment, ContentLiveLengthUpdate, ContentLiveLengthUpdateGenric, DEAudiobookDailyUnlockExperiment, DSRestrictionExp. Plus 73 more classes in the same package.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
